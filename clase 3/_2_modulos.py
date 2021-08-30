# 1º modulos de la propia biblioteca de py
# 2º modulos creados por nosotros
# 3º modulos descargados de internet

""" Modulo de Python """
# Modulo propio de Python
from colorama import Fore, Style
from _3_funciones import holaUsuario
import datetime

# print(datetime.date.today())
# print(datetime.timedelta(minutes=70))


""" Modulos creados por nosotros """

# holaUsuario()


""" Modulo descargado de internet """
# fuente: https://pypi.org/project/colorama/
# una vez descargado e instalado el modulo
# Podemos verlo con pip3 list
# pip3 install colorama

print(Fore.RED + "Este es un texto en rojo")
print(Style.RESET_ALL)
print('Este es otro mensaje en blanco')
