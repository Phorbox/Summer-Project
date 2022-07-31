from cgi import print_form
from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash
from PY_Files.Login_User import Login
from PY_Files.Items import Get_Items
from PY_Files.SQL_Queries import Push_To_User_Table


app = Flask(__name__)
app.secret_key = 'super secret key'

## Home Page ##


@app.route("/", methods=['GET', 'POST'])
def login():

    if 'user' in session:
        return redirect(url_for('main_menu'))

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        Credentials = [request.form['username'], request.form['password']]
        account = Login(Credentials)

        if account == None:
            flash('Incorrect User information')
            return render_template('administration_interface/foc_admin_interface_login.html')

        if account[1] == 1:
            session["user"] = account[0]
            session["admin"] = account[1]
            return redirect(url_for('main_menu'))

    return render_template('administration_interface/foc_admin_interface_login.html')


@app.route("/main_menu", methods=['GET', 'POST'])
def main_menu():
    if not("user" in session):
        return redirect(url_for('login'))

    if session.get("admin"):
        pass

    if request.method == "POST" and 'username' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form:

        new_user = [request.form['username'], request.form['firstname'], request.form['lastname'],
                    request.form['email'], request.form['password'], 1234567890, "", 0]
        print(request.form['username'])
        print(new_user)

        if request.form['username'] == "":
            print("nothing there")

        if request.form['username'] != "":
            print("something there")
            Push_To_User_Table(new_user)

        print("add user request recieved")

    if request.method == "POST" and request.form.get("search_button") == "SEARCH E-MAILS":
        me = 0

    if request.method == "POST" and request.form.get("search_button") == "SEARCH ITEMS":
        me = 0

    if request.method == "POST" and request.form.get("search_button") == "SEARCH ORDERS":
        me = 0

    if request.method == "POST" and request.form.get("search_button") == "SEARCH USERS":
        me = 0

    return render_template('administration_interface/foc_admin_interface_menu.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.run(debug=True)
