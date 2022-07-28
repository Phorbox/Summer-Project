import mysql.connector
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


def Drop_table(Table):
    DB = mysql.connector.connect(host=HOST, user=USER,
                                 password=PASSWORD, database=DATABASE)
    My_Cursor = DB.cursor()
    sql = f"DROP TABLE if exists {Table};"
    My_Cursor.execute(sql)


ID = "ID INT NOT NULL AUTO_INCREMENT"
USER = "USER VARCHAR(255) NOT NULL"
FIRST = "FIRST VARCHAR(255) NOT NULL"
LAST = "LAST VARCHAR(255) NOT NULL"
EMAIL = "EMAIL VARCHAR(255) NOT NULL"
PASS = "PASS VARCHAR(255) NOT NULL"
PHONE = "PHONE CHAR(10) NOT NULL"
CART = "CART VARCHAR(255)"
ADMINISTRATOR = "ADMINISTRATOR BOOL NOT NULL"
PRIMARY = "PRIMARY KEY (ID) "
USERFIELDS = [ID, USER, FIRST, LAST, EMAIL,
              PASS, PHONE, CART, ADMINISTRATOR, PRIMARY]

UID = "UID INT NOT NULL"
NUMBER = "NUMBER INT NOT NULL"
STREET = "STREET VARCHAR(255) NOT NULL"
STATE = "STATE CHAR(2) NOT NULL"
ZIP = "ZIP INT NOT NULL"
ADDRESSFIELDS = [ID, UID, NUMBER, STREET, STATE, ZIP, PRIMARY]

PID_LIST = "PID_LIST VARCHAR(255) NOT NULL"
FLAT = "FLAT INT NOT NULL"
PERCENT = "PERCENT INT NOT NULL"
START = "START int NOT NULL"
END = "END int NOT NULL"
CODE = "CODE VARCHAR(255) NOT NULL"
DISCOUNTFIELDS = [ID, PID_LIST, FLAT, PERCENT, START, END, CODE, PRIMARY]

DID_LIST = "DID_LIST VARCHAR(255) NOT NULL"
TOTAL = "TOTAL INT NOT NULL"
SALEFIELDS = [ID, UID, PID_LIST, DID_LIST, TOTAL, PRIMARY]

ITEM_NAME = "NAME VARCHAR(255) NOT NULL"
QUANTITY = "QUANTITY INT NOT NULL"
PRICE = "PRICE INT NOT NULL"
DESCRIPTION = "DESCRIPTION VARCHAR(255)"
IMAGE_NAME = "IMAGE_NAME VARCHAR(255) NOT NULL"
ITEMFIELDS = [ID, ITEM_NAME, QUANTITY, PRICE, DESCRIPTION, IMAGE_NAME, PRIMARY]

START_ID = "ALTER TABLE {} AUTO_INCREMENT=100"

TABLES = [USER_TABLE, ADDRESS_TABLE,
          DISCOUNT_TABLE, SALE_TABLE, ITEM_TABLE]

FELDS = [USERFIELDS, ADDRESSFIELDS, DISCOUNTFIELDS, SALEFIELDS, ITEMFIELDS]


def Make_Table(userTable, newfields):
    DB = mysql.connector.connect(host=HOST, user=USER,
                                 password=PASSWORD, database=DATABASE)

    My_Cursor = DB.cursor()
    fields = Format_Statement(newfields)
    sql = f'CREATE TABLE {userTable} ({fields})'
    print(sql)
    My_Cursor.execute(sql)
    sql = f"ALTER TABLE {userTable} AUTO_INCREMENT=100"
    print(sql)
    My_Cursor.execute(sql)


def Format_Statement(list):
    print(list)
    sql = "{}"
    returner = ""

    for x in list:
        returner += sql.format(x)
        returner += " , "

    returner = returner[:-len(" , ")]
    return (returner)


def Drop_All():
    for each in TABLES:
        Drop_table(each)


def Make_All():
    for each, other in zip(TABLES, FELDS):
        Make_Table(each, other)


Drop_All()
Make_All()
