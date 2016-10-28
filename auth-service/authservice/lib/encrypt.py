from passlib.hash import pbkdf2_sha512


def encrypt_sha512(password, rounds, salt):
    rounds = rounds if rounds is not None else 10000
    salt = salt if salt is not None else 10
    if password is None:
        password_encrypt = "Password field empty"
    else:
        password_encrypt = pbkdf2_sha512.encrypt(
            password, rounds=rounds, salt_size=salt
            )
    return password_encrypt


def check_sha512(unknown_password, valid_password):
    if unknown_password is None or valid_password is None:
        return "Sin parametros"
    else:
        return pbkdf2_sha512.verify(unknown_password, valid_password)
