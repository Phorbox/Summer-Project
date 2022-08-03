from PY_Files.SQL_Queries import Search_Item_Where, Search_Order_Where, Search_User_Where

USER_ATTRIBUTES = ['ID', 'USER', 'FIRST',
                   'LAST', 'PHONE', 'CART', 'ADMINISTRATOR']
EMAIL_ATTRIBUTES = ['EMAIL']
ADDRESS_ATTRIBUTES = ['ID', 'UID', 'NUMBER', 'STREET', 'STATE', 'ZIP']
DISCOUNT_ATTRIBUTES = ['ID', 'PID_LIST',
                       'FLAT', 'PERCENT', 'START', 'END', 'CODE']
SALE_ATTRIBUTES = ['ID', 'UID', 'PID_LIST', 'DID_LIST', 'TOTAL']
ITEM_ATTRIBUTES = ['ID', 'NAME', 'QUANTITY',
                   'PRICE', 'DESCRIPTION']
                   
ORDER_ATTRIBUTES = ['USER', 'NAME', 'QUANTITY']


def Select_Item(Where):
    if Where == "":
        Where = " ID > -1"
    else:
        Where = Where_Construction(ITEM_ATTRIBUTES, Where)
    return Search_Item_Where(Where)


def Select_Order(Where):
    if Where == "":
        Where = " QUANTITY > -1"
    else:
        Where = Where_Construction(ORDER_ATTRIBUTES, Where)
    return Search_Order_Where(Where)


def Select_User(Where):
    if Where == "":
        Where = " ID > -1"
    else:
        Where = Where_Construction(USER_ATTRIBUTES, Where)
    return Search_User_Where(Where)

def Select_Email(Where):
    if Where == "":
        Where = " ID > -1"
    else:
        Where = Where_Construction(EMAIL_ATTRIBUTES, Where)
    return Search_User_Where(Where)


def Where_Construction(Attribute, Key):
    Returner = f""
    Key = Parse_key(Key)
    for each in Attribute:
        Returner += f"{each} in {Key} or "
    return Returner[:-len(f" or ")]


def Parse_key(Key):
    returner = str(Key.split(" "))[1:-1]
    return f"({returner})"
