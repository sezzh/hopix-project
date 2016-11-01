import re


def validate_email(email):
    """ Criterios de un correo
        letras || números || guión bajo || guión || punto
        simbolo @ arroba
        letras || números || guión bajo || guión || punto
        longitud minima >= 4
        longitu máxima <= 15
    """
    pattern = '^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.).{1,15}$]'
    if re.match(pattern, email.lower()):
        return True
    else:
        return False


def validate_password(password):
    """ Criterios de una contraseña
        Letra mayúscula >= 1.
        Caracter especial >= 1
        Número >= 1
        Letra minúscula >= 1
        Longitud mínima >= 8
        Longitud máxima <= 15
    """
    pattern = '^(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8,15}$'
    if re.match(pattern, password):
        return True
    else:
        return False
