from cgi import print_form
from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash
from PY_Files.Login_User import Login
from PY_Files.Items import Get_Items
from PY_Files.SQL_Queries import Push_To_User_Table
from PY_Files.SQL_Queries import Push_To_DISCOUNT_Table
from PY_Files.SQL_Queries import Push_To_ITEM_Table


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
        #print(request.form["search_button"])
    # if request.method == ["POST"] and 'Item_Search' in request.form:
    #     Get_Items
    #     pass

    if request.method == "POST" and 'username' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form and 'phone' in request.form:
        
        new_user=[request.form['username'], request.form['firstname'], request.form['lastname'], request.form['email'], request.form['password'], request.form['phone'], "", 0]
        Push_To_User_Table(new_user)
        print("add user request recieved")
        
    if request.method == "POST" and 'code' in request.form and 'percent-off' in request.form and 'discount-id' in request.form and 'start-date' in request.form and 'end-date' in request.form and 'flat' in request.form:
        
        new_discount=[request.form['discount-id'], request.form['flat'], request.form['percent-off'], request.form['start-date'], request.form['end-date'], request.form['code'] ]
        Push_To_DISCOUNT_Table(new_discount)
        print("add discount request recieved")
        
    if request.method == "POST" and 'item-name' in request.form and 'quantity' in request.form and 'item-description' in request.form and 'item-id' in request.form and image-name in request.form:
        
        new_item=[request.form['item-name'], request.form['item-id'], request.form['quantity'], request.form['item-description'], request.form['image-name']]
        Push_To_ITEM_Table(new_item)
        print("add item request recieved")
    

    return render_template('administration_interface/foc_admin_interface_menu.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


app.run(debug = True)
