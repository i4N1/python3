from typing import BinaryIO
from unicodedata import decimal

def separarPalabra():
    palabra = input("Introduce la palabra: ")
    separada = [str(a) for a in str(palabra)]
    print(separada)
    return separada

def palabraDecimal():
    separada = separarPalabra()
    decimalSeparado = []
    x=0
    for x in separada:
        decimalSeparado.append(ord(x))
        x=+1
    print(decimalSeparado)
    return decimalSeparado


def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def toBinary():
    decimalSeparado = palabraDecimal()
    binarioSeparado = []
    x=0
    for x in decimalSeparado:
        binarioSeparado.extend(binarizar(x) + "n")
    print(binarioSeparado)

x=0 
binarioSeparado = toBinary()
for x in binarioSeparado:
    print("a")
