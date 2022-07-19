# from PY_Files
import SQL_Queries
import CONSTANTS


def Login_User(Username, Password):
    return SQL_Queries.Get_Login([Username, Password])


print(Login_User("daboxmasta", "123123"))
