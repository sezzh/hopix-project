# -*- encoding: utf-8 -*-
import os

jwt_secret = os.environ['AUTHSERVICE_JWT_SECRET']
if os.getenv('AUTHSERVICE_PATTERN_PASSWORD_SECRET') is None:
    pattern_password = (
        '(?=.*[A-Z])(?=.*[!#$%&/()?¿¡@;*])(?=.*[0-9])(?=.*[a-z]).{8,15}'
    )
    """
    (?=.*[A-Z])     Algúna letra en mayúscula
    (?=.*[!#$%&/()?¿¡@;*]  Algún caracter especial de la lista
    (?=.*[0-9])     Algún número
    (?=.*[a-z])     Algúna letra en minúscula
    {8,15}          dominio de 8 a 15 letras
    """

else:
    pattern_password = os.environ['AUTHSERVICE_PATTERN_PASSWORD_SECRET']
