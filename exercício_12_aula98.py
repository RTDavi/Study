"""OBJETIVO DESTE EXERCÍCIO, FAZER O CÁLCULO DO PRIMEIRO DÍGITO DE UM CPF
CPF: 746.824.890-70
COLETE A SOMA DOS 9 DIGITOS E MULTIPLIQUE OS VALORES UM POR UM POR UMA CONTAGEM REGRESSIVA COMEÇANDO POR 10

10 9 8 7 6 5 4 3 2 
 7 4 6 8 2 4 8 9 0
"""
import random 

for _ in range(100):

    cpf_str = ''
    for i in range(9):
       cpf_str += str(random.randint(0, 9)) 

    digito1_cpf = cpf_str[:9]
    contador = 10
    digito1 = 0
    digito2 = 0

    for multi in range(0, 9):

        multiplicado = int(digito1_cpf[multi]) * contador
        contador += -1
        digito1 += multiplicado

    digito1 *= 10
    digito1 %= 11

    if digito1 > 9:
        digito1 = 0

    digito2_cpf = cpf_str[:10]
    digito2 = 0
    contador_digito2 = 11

    for multidigito2 in range(0, 9):

        multiplicador = int(digito2_cpf[multidigito2]) * contador_digito2
        contador_digito2 += -1
        digito2 += multiplicador

    digito2 *= 10
    digito2 %= 11

    if digito2 > 9:
        digito2 = 0

    cpf_gerado_calculo = f'{cpf_str}{digito1}{digito2}'
    print(cpf_gerado_calculo)