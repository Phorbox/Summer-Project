HOST = "summer.cgikrpj2erfe.us-east-1.rds.amazonaws.com"
USER = "summersingle"
PASSWORD = "4kqE{`7Yz.FS;$Cf"
DATABASE = "summer"

USER_TABLE = f"{DATABASE}.USER_TABLE"
ADDRESS_TABLE = f"{DATABASE}.ADDRESS_TABLE"
DISCOUNT_TABLE = f"{DATABASE}.DISCOUNT_TABLE"
SALE_TABLE = f"{DATABASE}.SALE_TABLE"
ITEM_TABLE = f"{DATABASE}.ITEM_TABLE"

USER_ATTRIBUTES = 'USER, FIRST, LAST, EMAIL, PASS, PHONE, CART, ADMINISTRATOR'
ADDRESS_ATTRIBUTES = 'UID, NUMBER, STREET, STATE, ZIP'
DISCOUNT_ATTRIBUTES = 'PID_LIST, FLAT, PERCENT, START, END, CODE'
SALE_ATTRIBUTES = 'UID, PID_LIST, DID_LIST, TOTAL'
ITEM_ATTRIBUTES = 'NAME, QUANTITY, PRICE, DESCRIPTION, IMAGE_NAME'