from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash
from PY_Files.SQL_Queries import Get_Login


app = Flask(__name__)
app.secret_key = 'super secret key'

## Home Page ##


@app.route("/", methods=['GET', 'POST'])
def login():

    if 'UID' in session:
        return redirect(url_for('administration_interface/foc_admin_interface_login.html'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        print(f"username:{request.form['username']} password:{request.form['password']}")
        Credentials=[]
        Credentials.append(request.form['username'])
        Credentials.append(request.form['password'])

        account=Get_Login(Credentials)
        print (account)

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
    return render_template('administration_interface/foc_admin_interface_login.html')

app.run(debug = True)
