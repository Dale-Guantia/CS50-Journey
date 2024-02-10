import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, jsonify, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])

    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])[0]["cash"]

    total_value = cash
    grand_total = cash

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["price"] = quote["price"]
        stock["value"] = quote["price"] * stock["total_shares"]
        total_value += stock["value"]
        grand_total += stock["value"]

    return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares.isdigit():
            return apology("You cannot purchase partial shares.")

        if not symbol:
            return apology("Enter Symbol")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol does not exist")

        if int(shares) < 0:
            return apology("Shares must be positive number")

        transact_value = int(shares) * stock["price"]

        user_id = session["user_id"]
        user_balance = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_balance[0]["cash"]

        if user_cash < transact_value:
            return apology("Not Enough Balance")

        update_cash = user_cash - transact_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)

        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions(user_id, symbol, shares, price, date) VALUES(?, ?, ?, ?, ?)",
                   user_id, stock["symbol"], shares, stock["price"], date)

        flash(f"Transaction Completed! You bought {shares} shares of {symbol.upper()} for {usd(transact_value)}")

        return redirect("/")

# personal_touch
@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Allows users to add cash"""
    if request.method == "GET":
        return render_template("add_cash.html")
    else:
        new_cash = int(request.form.get("new_cash"))

        if not new_cash:
            return apology("Enter Cash Amount")

        user_id = session["user_id"]

        user_balance = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_balance[0]["cash"]

        update_cash = user_cash + new_cash
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)

        cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])[0]["cash"]

        flash(f"Transaction Completed! Just added {usd(new_cash)} your account. Current balance is {usd(cash)}")

        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = :user_id ORDER BY date DESC", user_id=session["user_id"])

    return render_template("history.html", transactions=transactions)


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
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Enter Symbol")

        stock = lookup(symbol.upper())

        if not stock:
            return apology("Symbol does not exist")

        return render_template("quoted.html", price=stock["price"], symbol=stock["symbol"])


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


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        user_id = session["user_id"]
        user_symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = :id GROUP BY symbol HAVING SUM(shares) > 0", id=user_id)

        return render_template("sell.html", symbols=[row["symbol"] for row in user_symbols])

    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares.isdigit():
            return apology("You cannot sell partial shares.")

        if not symbol:
            return apology("Enter Symbol")

        stock = lookup(symbol.upper())

        if stock == None:
            return apology("Symbol does not exist")

        if int(shares) < 0:
            return apology("Shares must be positive number")

        transact_value = int(shares) * stock["price"]

        user_id = session["user_id"]
        user_balance = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        user_cash = user_balance[0]["cash"]

        user_shares = db.execute("SELECT SUM(shares) AS shares FROM transactions WHERE user_id=:id AND symbol = :symbol", id=user_id, symbol=symbol)

        user_shares_real = user_shares[0]["shares"]

        if int(shares) > user_shares_real:
            return apology("Not Enough Shares To Sell")

        update_cash = user_cash + transact_value
        db.execute("UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id)

        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions(user_id, symbol, shares, price, date) VALUES(?, ?, ?, ?, ?)",
                   user_id, stock["symbol"], (-1) * int(shares), stock["price"], date)

        flash(f"Transaction Completed! You sold {shares} shares of {symbol} for {usd(transact_value)}")

        return redirect("/")
