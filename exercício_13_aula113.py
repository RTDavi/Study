"""
EXERCÍCIO COM FUNÇÕES

Crie uma função que multiplique os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Cria uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar

"""

def multi(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return print(total)


multi(8, 2, 2)

def parouimpar(x):

    if x % 2 == 0:
        return print(f'o número {x} é par!')
    else:
        return print(f'o número {x} é ímpar!')
    
parouimpar(6)

