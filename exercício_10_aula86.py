"""
Exercício
Exibir os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
contador = 0
lista.append('Joao')
for indice in lista:
    print(contador, indice)
    contador += 1
