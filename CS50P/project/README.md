# Project Title: RICE50

---

#### Video Demo: [Click hear!](https://youtu.be/dQNWml8M-n0)

#### Description:
Many people in Western countries are not familiar with how to cook rice, perhaps because they don't eat rice regularly, unlike other countries, especially in Asia. However, with this program, it will teach you how to cook rice with ease. This program will display instructions on how to cook rice perfectly and also require users to input the measurements and cooking time. The result of the program (cooked rice) will depend on the user's input.

# Libraries used:

---

> #### **In project.py**

* [**Pyfiglet**](http://www.figlet.org/)
* [**Time**](https://docs.python.org/3/library/time.html#time.sleep)
* [**Sys**](https://docs.python.org/3/library/sys.html#sys.stdout)

> #### **In test_project.py**

* [**Unittest.mock**](https://docs.python.org/3/library/unittest.mock.html?highlight=mock#module-unittest.mock)
* [**Pytest**](https://docs.pytest.org/en/7.1.x/how-to/assert.html)

# How the RICE50 works?

---

The idea of this program is simple and straightforward. When the program is run, it will display the perfect rice formula. Then, the user will be required to input the following data:

* Number of rice in cups
* Number of water in cups
* Heat levels of cooking (e.g., Low, Medium, High)
* Cooking time (in minutes)

By following the given formula, the outcome should display 'Perfect rice.' If the user changes the data shown above, the outcome of the rice will differ.

# Contents of the project

---

The project folder contains the following files:

> #### **project.py**

This is the main file where all of the code has been written. It consist libraries that have been used and has multiple functions, which will be explained as follows:

* **_main()_** - it is responsible for all program printing and contains some while loops and conditional statements.

* **_add_rice()_** - this function accepts 1 positional argument, which should be an integer, and returns it as a formatted string. It also includes loops, conditional statements, and exceptions.

* **_add_water()_** - this function accepts 1 positional argument, which should be an integer, and returns it as a formatted string. It also includes loops, conditional statements, and exceptions.

* **_heat_and_time()_** - this function accepts 1 positional argument in string format, prompts the user for an integer input, and returns a tuple containing two values. It also includes loops, conditional statements, and exceptions.

* **_result()_** - this function accepts 2 positional arguments, one in string format and the other in integer format. It consists of multiple 'if' and 'elif' statements that trigger based on user input, and it returns the result as a string.

* **_loading()_** - this function accepts 1 or 2 optional positional arguments, both in string and integer format. It consists of 'if-else' statements and a 'for' loop responsible for creating a delay effect during the rice rinsing and cooking process.

> #### **test_project.py**

This file are used to write and execute test codes. Each of the functions from the main file (project.py) are imported through this file. The libraries that I have been used for testing are unit test and pytest.

> #### **requirements.txt**

All of the pip-installable libraries in my project are listed in this file.

> #### **README.md**

This is a text file that introduces and explains my project. It contains information that is commonly required to understand what the project is about.

# How to run the program?

---

1. Make sure your python version is up-to-date.
2. Clone the code. [Click here](https://github.com/code50/142967173/blob/main/project/project.py)
3. Make sure to import and install all pip-installable libraries in "requirements.txt" file. [Click here](https://github.com/code50/142967173/blob/main/project/requirements.txt)
4. With all of the above completed, you're all set to go!