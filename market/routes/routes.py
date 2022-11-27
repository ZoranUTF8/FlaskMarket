from market import app
from flask_login import login_required
from market.controllers import UserController, itemController


@app.route("/")
@app.route("/home")
def homePage():
    return UserController.homePage()


@app.route("/publicMarket", methods=["GET", "POST"])
# Decorator that checks if the user is logged in
@login_required
def marketPage():
    return itemController.marketPage()


'''
RegisterForm
Register new user and add to db
'''


@app.route("/register", methods=["GET", "POST"])
def registerPage():
    return UserController.registerUser()


'''
Check if a user with he provided email is in the database
if true than compare the passwords
'''


@app.route("/login", methods=["GET", "POST"])
def loginPage():
    return UserController.loginUser()


@app.route("/logout",)
def logoutPage():
    return UserController.logoutUser()
