# coding=utf-8

def UsersEncriptation(_users, _password):
    match = 0
    usuarioBase = _users
    encriptation = 32
    while(not match >= 2 or encriptation > 256):
        _users = usuarioBase
        temp_number = 0

        for x in _password:
            temp_number += ord(x)

        for x in _users:
            modificador = 0
            if((temp_number + ord(x)) % encriptation == 10):
                modificador = 1
            _users = _users.replace(x, chr((temp_number + ord(x) + modificador) % encriptation), 1)
            #print ((temp_number + ord(x)) % encriptation)


        for x in _users:
            if(x == "$" or x == "/" or x == "!" or x == "-" or x == "K" or x == " " or x == "7"):
                match+= 1
        encriptation += 16
    return _users