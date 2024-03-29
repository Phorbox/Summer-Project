import sys
from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session, flash
from PY_Files.Login_User import Login
from PY_Files.SQL_Queries import Push_To_User_Table, Push_To_ITEM_Table, Push_To_DISCOUNT_Table, Push_To_ORDER_Table
from PY_Files.Search import Select_Item, Select_Order, Select_User, Select_Email
from PY_Files.Edit import Edit_Format, Update_Switch



app = Flask(__name__)
app.secret_key = 'super secret key'



@app.route("/", methods=['GET', 'POST'])
def login():

    if 'user' in session:
        return redirect(url_for('main_menu'))

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        Credentials = [request.form['username'], request.form['password']]
        account = Login(Credentials)

        if account == None:
            # flash('Incorrect User information')
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

    if request.method == "POST" and 'username' in request.form and 'password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form and 'phone' in request.form:

        new_user = [request.form['username'], request.form['firstname'], request.form['lastname'],
                    request.form['email'], request.form['password'], request.form['phone'], "", 0]
        Push_To_User_Table(new_user)
        

    if request.method == "POST" and 'code' in request.form and 'percent-off' in request.form and 'discount-id' in request.form and 'start-date' in request.form and 'end-date' in request.form and 'flat' in request.form:

        new_discount = [request.form['discount-id'], request.form['flat'], request.form['percent-off'],
                        request.form['start-date'], request.form['end-date'], request.form['code']]
        Push_To_DISCOUNT_Table(new_discount)
        

    if request.method == "POST" and 'item-name' in request.form and 'quantity' in request.form and 'item-description' in request.form and 'item-id' in request.form and 'image-name' in request.form:

        new_item = [request.form['item-name'], request.form['item-id'],
                    request.form['quantity'], request.form['item-description'], request.form['image-name']]
        Push_To_ITEM_Table(new_item)
       

    if request.method == "POST" and "search_button" in request.form:
        session["search"] = request.form.get("search_button")
        print(request.form['search-key'])

        session["Key"] = request.form['search-key']


        return redirect(url_for('results'))

    return render_template('administration_interface/foc_admin_interface_menu.html')


@app.route("/results", methods=['GET', 'POST'])
def results():
    temp = session.get('Key')
    print(temp)
    match session.get("search"):
        case 'SEARCH ITEMS':
            result = Select_Item(temp)
            Columns = 7

        case 'SEARCH USERS':
            result = Select_User(temp)
            Columns = 10

        case 'SEARCH E-MAILS':
            result = Select_Email(temp)
            Columns = 10

        case 'SEARCH ORDERS':
            result = Select_Order(temp)
            Columns = 4
    

    if result == None:
        # flash(f'No results for {temp}')
        return redirect(url_for('main_menu'))

    if request.method == "POST":
        session["Edit_ID"] = request.form.get("Edit")
        return redirect(url_for('edit'))
    return render_template('administration_interface/foc_admin_interface_results.html', Tuple_List=result, Columns = Columns)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    Table_Type = session.get("search")
    Id = session.get("Edit_ID")
    Fields = Edit_Format(Table_Type, Id)

    if request.method == "POST":
        Attribute = []
        Value = []
        for Each in request.form:
            Attribute.append(Each)
            Value.append(request.form.get(Each))

        Update_Switch(Table_Type, Attribute, Value, Id)
        return redirect(url_for('main_menu'))

    return render_template('administration_interface/foc_admin_interface_edit.html', Attribute_List=Fields[0], Value_List=Fields[1], Ranger=range(len(Fields[0])))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
    # app.run(debug=True) 
