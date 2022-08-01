from re import findall, sub
from numpy import concatenate

USER_ATTRIBUTES = ['ID', 'USER', 'FIRST', 'LAST',
                   'EMAIL', 'PHONE', 'CART', 'ADMINISTRATOR']
ADDRESS_ATTRIBUTES = ['ID', 'UID', 'NUMBER', 'STREET', 'STATE', 'ZIP']
DISCOUNT_ATTRIBUTES = ['ID', 'PID_LIST',
                       'FLAT', 'PERCENT', 'START', 'END', 'CODE']
SALE_ATTRIBUTES = ['ID', 'UID', 'PID_LIST', 'DID_LIST', 'TOTAL']
ITEM_ATTRIBUTES = ['ID', 'NAME', 'QUANTITY',
                   'PRICE', 'DESCRIPTION']


def Search(Table,Key):
    pass


def Parse_key(Key):
    returner = str(Key.split(" "))[1:-1]
    return f"({returner})"


print(Parse_key(f"Hello 1 2 thign"))
