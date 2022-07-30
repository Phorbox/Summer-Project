from cgi import print_form
from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash
from PY_Files.Login_User import Login
from PY_Files.Items import Get_Items


app = Flask(__name__)
app.secret_key = 'super secret key'

## Home Page ##


@app.route("/", methods=['GET', 'POST'])
def login():

    if 'user' in session:
        return redirect(url_for('main_menu'))

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        Credentials=[request.form['username'],request.form['password']]
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

    # lookup item
    if request.method == "POST":
        print("here")
        print(request.form["search_button"])
    # if request.method == ["POST"] and 'Item_Search' in request.form:
    #     Get_Items
    #     pass


    return render_template('administration_interface/foc_admin_interface_menu.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.run(debug = True)
