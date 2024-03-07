"""
Exercício, criar uma função que duplica, triplica e quadriplica um número.
"""


def double(num):
    contador = 1
    lista = []
    
    for i in range(0, 4):
        resultado = contador * num
        print(resultado)
        contador += 1
        lista.append(resultado)
        
    return print(lista)

double(4)