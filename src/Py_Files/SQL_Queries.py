import mysql.connector
import CONSTANTS


U_TABLE = CONSTANTS.USER_TABLE
A_TABLE = CONSTANTS.ADDRESS_TABLE
D_TABLE = CONSTANTS.DISCOUNT_TABLE
S_TABLE = CONSTANTS.SALE_TABLE
I_TABLE = CONSTANTS.ITEM_TABLE


def DB():
    return mysql.connector.connect(host=CONSTANTS.HOST, user=CONSTANTS.USER,
                                   password=CONSTANTS.PASSWORD, database=CONSTANTS.DATABASE)


def Push_To_Any(Table, Attributes, Values_List):
    My_Cursor = DB()
    My_Cursor = My_Cursor.cursor()
    Values_String = Value_List_To_String(Values_List)
    sql = f"insert into {Table} ({Attributes}) values ({Values_String})"
    print(sql)
    My_Cursor.execute(sql)
    My_Cursor.commit()
    My_Cursor.close()


def Push_To_User_Table(Values_List):
    Push_To_Any(U_TABLE, CONSTANTS.USER_ATTRIBUTES, Values_List)


def Push_To_ADDRESS_Table(Values_List):
    Push_To_Any(A_TABLE, CONSTANTS.ADDRESS_ATTRIBUTES, Values_List)


def Push_To_DISCOUNT_Table(Values_List):
    Push_To_Any(D_TABLE, CONSTANTS.DISCOUNT_ATTRIBUTES, Values_List)


def Push_To_SALE_Table(Values_List):
    Push_To_Any(S_TABLE, CONSTANTS.SALE_ATTRIBUTES, Values_List)


def Push_To_ITEM_Table(Values_List):
    Push_To_Any(I_TABLE, CONSTANTS.ITEM_ATTRIBUTES, Values_List)


def Value_List_To_String(Value_List):
    Returner = ""
    Delimiter = ", "
    for each in Value_List:
        Temp = f"'{each}'"
        Returner = Returner + Delimiter + Temp
    return Returner[2:]


def Get_Login(UserInfo):
    return Select_Any(U_TABLE, ["ID", "ADMINISTRATOR"], ["(USER)", "(PASS)"], UserInfo)


def Select_Any(Table, Select_List, Attribute_List, Value_List):
    My_Cursor = DB()
    My_Cursor = My_Cursor.cursor()
    Where = Format_Zip_List(Attribute_List, Value_List, "And")
    Selector = Format_Single_List(Select_List, ",")
    sql = f"Select {Selector} From {Table} Where {Where}"
    print(sql)
    My_Cursor.execute(sql)
    returner = My_Cursor.fetchone()
    My_Cursor.close()
    return returner


def Select_Where(Table, Where):
    My_Cursor = DB()
    My_Cursor = My_Cursor.cursor()
    Selector = "*"
    sql = f"Select {Selector} From {Table} Where {Where}"
    print(sql)
    My_Cursor.execute(sql)
    returner = My_Cursor.fetchone()
    My_Cursor.close()
    return returner


def Select_Item_Where(Where):
    return Select_Where(I_TABLE, Where)


def Select_All(Table):
    My_Cursor = DB()
    My_Cursor = My_Cursor.cursor()
    sql = f"Select * From {Table}"
    print(sql)
    My_Cursor.execute(sql)
    returner = My_Cursor.fetchall()
    My_Cursor.close()
    return returner


def Select_All_Items():
    Select_All(I_TABLE)


# where cat like thing or cat like thing
def Select_Like_Items(a):
    My_Cursor = DB()
    My_Cursor = My_Cursor.cursor()
    sql = f"Select * From {I_TABLE} Where Name like %{a}% or Description like %{a}%"
    print(sql)
    My_Cursor.execute(sql)
    returner = My_Cursor.fetchall()
    My_Cursor.close()
    return returner


def Description_Where(Descript):
    return f"Name like %{Descript}% or Description like %{Descript}%"


def Quantity_Where(Quanty):
    return f"QUANTITY BETWEEN {Quanty[0]} AND {Quanty[1]}"


def Price_Where(Price):
    return f"PRICE BETWEEN {Price[0]} AND {Price[1]}"

# def Select_Like(Table, Select_List, Attribute_List, Value_List):
#     My_Cursor = DB()
#     My_Cursor = My_Cursor.cursor()
#     Where = Format_Zip_List(Attribute_List, Value_List, "And")
#     Selector = Format_Single_List(Select_List, ",")
#     sql = f"Select {Selector} From {Table} Where {Category} like"
#     print(sql)
#     My_Cursor.execute(sql)
#     returner = My_Cursor.fetchall()
#     My_Cursor.close()
#     return returner


def Clean_Result(dirty):
    if(dirty == None):
        return "none"
    return dirty[0]


def Format_Zip_List(Attribute_List, Value_List, Delimiter):
    returner = ""

    for x, y in zip(Attribute_List, Value_List):
        returner += f"{x} = '{y}'"
        returner += f" {Delimiter} "

    returner = returner[:-len(f" {Delimiter} ")]
    return (returner)


def Format_Single_List(List, Delimiter):
    Returner = ""

    for x in List:
        Returner += f"{x}"
        Returner += f" {Delimiter} "

    Returner = Returner[:-len(f" {Delimiter} ")]
    return (Returner)

# Push_To_User_Table(["daboxmasta",	"matthew",	"henderson",	"daboxmasta@gmail.com",	123123,	123456790,	"100,200,300",	1])
