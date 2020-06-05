# coding=utf-8
#usuario = "Alfredo"
#password = "Rodrigo"
from passwords import encryptacion
from users import UsersEncriptation

def main(Usuario, Password):
    accept = False
    userContra = ""
    if(len(Usuario) >= 8):
        if(len(Password) >= 8):
            match = 0
            accept = True
            for x in Password:
                if(x == "@" or x == "-" or x == "_" or x == "?" or x == "." or x == "."):
                    if(x == ":"):
                        accept = False
                    match+= 1
            if(match >= 2 and accept == True):
                Pass = ""
                User = ""
                Pass = encryptacion(Usuario, Password)
                User = UsersEncriptation(Usuario, Pass)
                userContra = userContra + User + ":" + Pass

    return userContra