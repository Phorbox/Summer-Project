import SQL_Queries


def ICreate(Item_Info):
    SQL_Queries.Push_To_ITEM_Table(Item_Info)


def Get_Items(Description="", Quantity_Range="", Price_Range=""):
    Where_Statement = Format_Search_Statement(
        Description, Quantity_Range, Price_Range)
    return SQL_Queries.Select_Item_Where(Where_Statement)


def Format_Search_Statement(Description, Quantity_Range, Price_Range):
    Where_Statement = ""
    Delimiter = " and "
    if Description != "":
        Where_Statement += SQL_Queries.Description_Where(Description)
        Where_Statement += Delimiter
    if Quantity_Range != "":
        Quantity_Range = SQL_Queries.Quantity_Where(Quantity_Range)
        Where_Statement += Delimiter
    if Price_Range != "":
        Price_Range = SQL_Queries.Price_Where(Price_Range)
        Where_Statement += Delimiter
    print(Where_Statement[:-len(Delimiter)])
    return Where_Statement[:-len(Delimiter)]

def Sell(Product_ID, Quantity):
    Updater = SQL_Queries.Select_Item_Where(f"ID = {Product_ID}")
    Updater -= Quantity
    SQL_Queries.Update_Field()
    

def Restock():
    pass


def Adjust():
    pass
