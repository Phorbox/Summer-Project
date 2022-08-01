from PY_Files.SQL_Queries import Push_To_ITEM_Table, Search_Item_Where, Description_Where, Price_Where, Update_Field, Quantity_Where


def ICreate(Item_Info):
    Push_To_ITEM_Table(Item_Info)


def Get_Items(Description="", Quantity_Range="", Price_Range=""):
    Where_Statement = Format_Search_Statement(
        Description, Quantity_Range, Price_Range)
    return Search_Item_Where(Where_Statement)


def Format_Search_Statement(Description, Quantity_Range, Price_Range):
    Where_Statement = ""
    Delimiter = " and "
    if Description != "":
        Where_Statement += Description_Where(Description)
        Where_Statement += Delimiter
    if Quantity_Range != "":
        Quantity_Range = Quantity_Where(Quantity_Range)
        Where_Statement += Delimiter
    if Price_Range != "":
        Price_Range = Price_Where(Price_Range)
        Where_Statement += Delimiter
    print(Where_Statement[:-len(Delimiter)])
    return Where_Statement[:-len(Delimiter)]


def Sell(Product_ID, Quantity):
    Updater = Search_Item_Where(f"ID = {Product_ID}")
    Updater -= Quantity
    Update_Field()


def Restock():
    pass


def Adjust():
    pass
