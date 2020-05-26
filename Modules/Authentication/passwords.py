# coding=utf-8
from users import UsersEncriptation
def encryptacion(_usuario, _password):
    #Tamaño del arreglo / 2 y le sumamos el tamaño del arreglo
    #Encriptación principal
    for x in _password:
        _password = _password.replace(x, chr(ord(x) + 5), 1)

    #Mitad
    position = len(_password) / 2
    _password = _password.replace(_password[position],chr(ord(_password[position]) + len(_password)), 1)
    temp_number = 0

    #Primera
    for x in _usuario:
        temp_number += ord(x)
    _password = _password.replace(_password[0], chr(temp_number % 256), 1)

    #Ultima
    for x in _usuario:
        if(x == _usuario[len(_usuario) / 2]):
            temp_number = ord(x)
    temp_number += len(_usuario) + len(_password)
    _password = _password.replace(_password[len(_password) - 1], chr(temp_number % 256), 1)

    #codigoSecreto
    temp_number = ord(_password[len(_password) - 1]) + ord(_password[len(_password) - 2])
    _password + chr(temp_number % 128) + chr(temp_number % 224) + chr(temp_number % 256)
    #Imprimir resultado
    print (_password)
    UsersEncriptation(_usuario, _password)