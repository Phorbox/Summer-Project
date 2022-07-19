from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash
import PY_Files 



app = Flask(__name__)
app.secret_key = 'super secret key'

# Connect to database

# DB = mysql.connector.connect(host=CONSTANTS.HOST, user=CONSTANTS.USER,
#                              password=CONSTANTS.PASSWORD, database=CONSTANTS.DATABASE)

## Home Page ##
@app.route("/")
def login():
    # print(session["UID"])

    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    #     # Create variables for easy access

    #     username = request.form['username']
    #     passw = request.form['password']

    #     account = Login_User.Login_User(username, passw)
    #     if account == None:
    #         flash('Incorrect User information')
    #         return render_template('login.html')

    #     else:
    #         session["UID"] = str(account)
    #         session["username"] = username
    #         flash('Login Sucessful. Welcome back ' + username + '!')
    #         # Redirect to home page
    #         return redirect(url_for('homepage'))

    # # Show the login form with message (if any)
    return render_template('login.html')

app.run(debug=True)