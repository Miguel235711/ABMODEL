# coding=utf-8
#usuario = "Alfredo"
#password = "Rodrigo"
from passwords import encryptacion
from users import UsersEncriptation

def main():
    accept = False
    while(not accept):
        Usuario = raw_input("Ingresa tu usuario.")
        Password = raw_input("Ingresa tu contraseña")
        if(len(Usuario) >= 8):
            if(len(Password) >= 8):
                match = 0
                for x in Password:
                    if(x == "@" or x == "-" or x == "_" or x == "?" or x == "." or x == "."):
                        match+= 1
                if(match >= 2):
                    Pass = ""
                    User = ""
                    Pass = encryptacion(Usuario, Password)
                    User = UsersEncriptation(Usuario, Pass)
                    accept = True
                else:
                    print("Contraseña insegura. Combina caracteres especiales")
            else:
                print("Tu contraseña es muy pequeña")
        else:
            print("Nombre de usuario muy corto")
main()