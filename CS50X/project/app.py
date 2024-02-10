import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from PIL import Image, ImageOps
import datetime
import numpy as np
import json

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")
# Get only 5 highest values of colors
TOP_5 = 5

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        color_code = request.form['color_code']
        colors_list = find_hex(f.stream, color_code)
        file_name = f.filename
        date = datetime.datetime.now()

        if session.get("user_id") is None:
            return render_template('index.html', colors_list=colors_list, code=color_code)
        else:
            if color_code == 'hex':
                user_id = session["user_id"]
                j_list = json.dumps(colors_list)
                db.execute("INSERT INTO history(user_id, file_name, hex_code, date) VALUES(?, ?, ?, ?)", user_id, str(file_name), j_list, date)
                return render_template('index.html', colors_list=colors_list, code=color_code)
            else:
                list_hex = []
                for key in colors_list:
                    hex = rgb_to_hex(key)
                    list_hex.append(hex)

            converted_list = list_hex
            user_id = session["user_id"]
            j_list = json.dumps(converted_list)
            db.execute("INSERT INTO history(user_id, file_name, hex_code, date) VALUES(?, ?, ?, ?)", user_id, str(file_name), j_list, date)
            return render_template('index.html', colors_list=colors_list, code=color_code)

    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Account doesn't exist", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Enter Valid Username")
        if not password:
            return apology("Enter Password")
        if not password:
            return apology("Enter Confirmation Password")
        if password != confirmation:
            return apology("Password do not match")

        hash = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash)
        except:
            return apology("Username Already Exist")

        session["user_id"] = new_user

        return redirect("/")



@app.route("/history", methods=['GET', 'POST'])
@login_required
def history():
    """Show history of color palettes"""
    if request.method == 'POST':
        color_code = request.form['color_code']
        history_db = db.execute("SELECT hex_code FROM history WHERE user_id = :user_id ORDER BY date DESC", user_id=session["user_id"])
        hex_list = []
        temp_list = []

        #Create hex list from history DB
        for item in history_db:
            for key in item:
                hex_list.append(json.loads(item[key]))

        #Convert hex value to rgb values
        for item in history_db:
            for key in item:
                each_list = json.loads(item[key])
                for i in range(len(each_list)):
                    t_rgb = hex_to_rgb(each_list[i])
                    temp_list.append(t_rgb)

        rgb_list = [x for x in zip(*[iter(temp_list)]*5)]

        return render_template("history.html", hex_list = hex_list, rgb_list=rgb_list, code=color_code)

    return render_template('history.html')


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def find_hex(file_path, code):
    uploaded_image = Image.open(file_path).convert('RGB')
    image_size = uploaded_image.size
    if image_size[0] >= 400 or image_size[1] >= 400:
        uploaded_image = ImageOps.scale(image = uploaded_image, factor=0.2)
    elif image_size[0] >= 600 or image_size[1] >= 600:
        uploaded_image = ImageOps.scale(image = uploaded_image, factor=0.4)
    elif image_size[0] >= 800 or image_size[1] >= 800:
        uploaded_image = ImageOps.scale(image = uploaded_image, factor=0.5)
    elif image_size[0] >= 1200 or image_size[1] >= 1200:
        uploaded_image = ImageOps.scale(image = uploaded_image, factor=0.6)
    uploaded_image = ImageOps.posterize(uploaded_image, 2)
    image_array = np.array(uploaded_image)

    # Make a dictionary of distinct colors by setting the count of each color to 0.
    # if it is present in the dictionary, increment by 1.
    new_colors = {}  # (r, g, b): count
    for column in image_array:
        for rgb in column:
            t_rgb = tuple(rgb)
            if t_rgb not in new_colors:
                new_colors[t_rgb] = 0
            if t_rgb in new_colors:
                new_colors[t_rgb] += 1

    # obtain a list of the top five instances or counts of each color
    # from unique colors dictionary
    sorted_new_colors = sorted(new_colors.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_new_colors)

    # get only 5 highest values
    values = list(converted_dict.keys())
    # print(values)
    top_5 = values[0:TOP_5]
    # print(top_5)
    print(top_5)

    # code to convert rgb to hex
    if code == 'hex':
        list_hex = []
        for key in top_5:
            hex = rgb_to_hex(key)
            list_hex.append(hex)
        return list_hex
    else:
        return top_5


if __name__ == '__main__':
    app.run(debug=True)
