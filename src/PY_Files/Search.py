from PY_Files.SQL_Queries import Select_Item_Where, Select_Order_Where, Select_User_Where

USER_ATTRIBUTES = ['ID', 'USER', 'FIRST',
                   'LAST', 'PHONE', 'CART', 'ADMINISTRATOR']
EMAIL_ATTRIBUTES = ['EMAIL']
ADDRESS_ATTRIBUTES = ['ID', 'UID', 'NUMBER', 'STREET', 'STATE', 'ZIP']
DISCOUNT_ATTRIBUTES = ['ID', 'PID_LIST',
                       'FLAT', 'PERCENT', 'START', 'END', 'CODE']
SALE_ATTRIBUTES = ['ID', 'UID', 'PID_LIST', 'DID_LIST', 'TOTAL']
ITEM_ATTRIBUTES = ['ID', 'NAME', 'QUANTITY',
                   'PRICE', 'DESCRIPTION']


def Select_Item(Where):
    Where = Where_Construction(ITEM_ATTRIBUTES, Where)
    return Select_Item_Where(Where)


def Select_Order(Where):
    Where = Where_Construction(SALE_ATTRIBUTES, Where)
    return Select_Order_Where(Where)


def Select_User(Where):
    Where = Where_Construction(USER_ATTRIBUTES, Where)
    return Select_User_Where(Where)

def Select_Email(Where):
    Where = Where_Construction(EMAIL_ATTRIBUTES, Where)
    return Select_User_Where(Where)


def Where_Construction(Attribute, Key):
    Returner = f""
    Key = Parse_key(Key)
    for each in Attribute:
        Returner += f"{each} in {Key} or "
    return Returner[:-len(f" or ")]


def Parse_key(Key):
    returner = str(Key.split(" "))[1:-1]
    return f"({returner})"
