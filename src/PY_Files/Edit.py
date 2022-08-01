from PY_Files.SQL_Queries import Search_Item_Where,Search_User_Where,Search_Order_Where
from PY_Files.SQL_Queries import Update_Item,Update_User,Update_Order

USER_LIST = ['ID','USER', 'FIRST', 'LAST', 'EMAIL',
    'PASS', 'PHONE', 'CART', 'ADMINISTRATOR']
ADDRESS_LIST = ['ID','UID', 'NUMBER', 'STREET', 'STATE', 'ZIP']
DISCOUNT_LIST = ['ID','PID_LIST', 'FLAT', 'PERCENT', 'START', 'END', 'CODE']
SALE_LIST = ['ID','UID', 'PID_LIST', 'DID_LIST', 'TOTAL']
ITEM_LIST = ['ID','NAME', 'QUANTITY', 'PRICE', 'DESCRIPTION']


def Edit_Format(Edit_type, ID):
    # edit type to list
    ID = Value_Switch(Edit_type,ID)
    
    Edit_type = Attribute_Switch(Edit_type)
    return (Edit_type,ID)

def Attribute_Switch(Edit_type):
    match Edit_type:
        case 'SEARCH ITEMS':
            return ITEM_LIST

        case 'SEARCH USERS'|'SEARCH E-MAILS':
            return USER_LIST

        case 'SEARCH ORDERS':
            return SALE_LIST

def Value_Switch(Edit_type,ID):
    
    match Edit_type:
        case 'SEARCH ITEMS':
            return Search_Item_Where(f"ID = {ID}")[0][:-1]

        case 'SEARCH USERS'|'SEARCH E-MAILS':
            return Search_User_Where(f"ID = {ID}")[0]

        case 'SEARCH ORDERS':
            return Search_Order_Where(f"ID = {ID}")[0]

def Update_Switch(Edit_type,Field, New, ID):
        match Edit_type:
            case 'SEARCH ITEMS':
                Update_Item(Field, New, ID)

            case 'SEARCH USERS'|'SEARCH E-MAILS':
                Update_User(Field, New, ID)

            case 'SEARCH ORDERS':
                Update_Order(Field, New, ID)