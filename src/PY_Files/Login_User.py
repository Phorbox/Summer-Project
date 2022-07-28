# from PY_Files
from PY_Files.SQL_Queries import Get_Login


def Login(Credentials):
    Login_Info = Get_Login(Credentials)
    if Login_Info == []:
        return None

    return Login_Info[0]

