# coding=utf-8
from users import UsersEncriptation
def encryptacion(_usuario, _password):
    #Tamaño del arreglo / 2 y le sumamos el tamaño del arreglo
    #Encriptación principal
    for x in _password:
        _password = _password.replace(x, chr(ord(x) + 5), 1)
    modificador = 0
    #Mitad
    position = len(_password) / 2
    if(ord(_password[position]) + len(_password) == 58):
        modificador = 1
    _password = _password.replace(_password[position],chr(ord(_password[position]) + len(_password) + modificador), 1)
    temp_number = 0

    modificador = 0
    #Primera
    for x in _usuario:
        temp_number += ord(x)
    if(temp_number % 256 == 58):
        modificador = 1
    _password = _password.replace(_password[0], chr(temp_number % 256 + modificador), 1)

    modificador = 0
    #Ultima
    for x in _usuario:
        if(x == _usuario[len(_usuario) / 2]):
            temp_number = ord(x)
    temp_number += len(_usuario) + len(_password)
    if(temp_number % 256 == 58):
        modificador = 1
    _password = _password.replace(_password[len(_password) - 1], chr(temp_number % 256 + modificador), 1)

    modificador = 0
    modificador1 = 1
    modificador2 = 2

    #codigoSecreto
    temp_number = ord(_password[len(_password) - 1]) + ord(_password[len(_password) - 2])
    if(temp_number % 128 == 58):
        modificador = 1
    if(temp_number % 224 == 58):
        modificador1 = 1
    if(temp_number % 256 == 58):
        modificador2 = 1
    _password + chr(temp_number % 128 + modificador) + chr(temp_number % 224 + modificador1) + chr(temp_number % 256 + modificador2)
    #Imprimir resultado
    print (_password)
    return _password