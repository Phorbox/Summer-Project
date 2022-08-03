# Summer Project


Admin Login: Theers 
Password: 123
http://ec2-52-87-179-156.compute-1.amazonaws.com:8080/



2
FOODS
OF
COLOR
internet commerce administration system official user manual


LOGGING IN
1   Visit foodsofcolor.com/admin in your web browser to gain access to the administrator login page. The web page will look similar to the diagram below.

2   Click above the line denoted as “USERNAME” to focus the input field. With the field focused, type your administrator username in correctly. 

3   Click above the line denoted as “PASSWORD” to focus the input field. With the field focused, type your administrator password in correctly. 

4   Now that both username and password fields are correctly populated, clicking the button below the fields labeled “SUBMIT” will grant you access to the system menu.

NAVIGATING THE MAIN MENU
1   After successfully logging in, you will be presented with a menu page which should look similar to the diagram below.

2   Click the button labeled “ADD” to gain access to the add menu. This menu will be covered in detail in the next page (page 3) of the user manual. 

3   Click the button labeled “LOOKUP” to gain access to the search tools. These tools will 
be coverd in detail in page 4.

3   If you step away from your computer or finish working with the system, please click the button labeled “LOGOUT” to log your adminstrator account out of the system and ensure only properly priviledged administrators make system changes.

USING THE ADD MENU
1   Clicking the “<” (back) button at any time will return the interface to the main menu.

2   Clicking any button in this button row will bring up it’s respective input form. As shown in the diagram above, the form will appear below the button row. In this case, the user form appears when the user button is clicked. To switch forms, simply click another button

3   The user add form functions exactly like the login page does. Focus each field, then input the correct data. Once the form is complete, clicking the button labeled “SUBMIT” will insert the data as a new row into the database.

USING THE LOOKUP MENU
1   Clicking the “<” (back) button at any time will return the interface to the main menu.

2   Clicking any button in this button row will bring up it’s respective search form, as shown in the diagram above, the form will appear b elow the button row. In this case, the e-mail form appears when the user button is clicked.

3   Once the “SEARCH KEY” field is populated with a valid search key, pressing the “SEARCH” button will send a request to the database and present the data matching the criteria in a different web page. This webpage will be detailed in page 5 of the user manual.

4   E-MAIL will search users based on e-mail address. ITEM will search items based on item name. ORDER will search orders based on order ID. USER will search users based on username.

VIEWING SEARCH RESULTS
1   These rectangles to the side of each result are buttons. Clicking one will load a web
page which allows you to edit the item which was beside the rectangle.

2   To return to the previous menu, you will need to use the back button of your browser.

EDITING SEARCH RESULTS
1   Enter the new value into the field corresponding field. The old value will be presented
next to the field name.

2   To return to the previous menu, you will need to use the back button of your browser.

3   Once all the necessary fields are full, press the submit button to update the information
in the database.

STARTING THE SERVER
1   Copy all src files.

2   download flask and mysql-connector

3   execute Server_Start.sh

Stopping the server
1   execute the following script:
        kill "$(ps -aux | grep "python3 app.py" | grep -v grep | awk '{print $2}')"