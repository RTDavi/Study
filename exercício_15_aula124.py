"""
Fazer um sistema de perguntas com 4 alternativas, mínimo 3 perguntas
"""

perguntas = [
    { 
       'Pergunta': 'Quanto é 5*9?',
       'Opções': ['40', '45', '50', '55'],
       'resposta': '2' 
    },
    { 
       'Pergunta': 'Quanto é 8+7',
       'Opções': ['13', '16', '22', '15'],
       'resposta': '4' 
    },
    { 
       'Pergunta': 'Qual ave não voa?',
       'Opções': ['Gavião', 'Avestruz', 'Pato', 'Flamingo'],
       'resposta': '2' 
    }
]

escolhas = 0
acertos = 0
print('****************JOGO DAS PERGUNTAS****************')

print(f'\n************PRIMEIRA PERGUNTA************')
print(perguntas[0].get('Pergunta'))
for opção in perguntas[0].get("Opções"):
    escolhas += 1
    print(f'{escolhas}) {opção}')

resposta1 = input('Escolha uma opção:')

if resposta1 == perguntas[0].get('resposta'):
    print('Você acertou!!')
    acertos += 1
else:
    print('Você errou!')
escolhas = 0

print(f'\n************SEGUNDA PERGUNTA************')

print(perguntas[1].get('Pergunta'))
for opção in perguntas[1].get('Opções'):
    escolhas += 1
    print(f'{escolhas}) {opção}')

resposta2 = input('Escolha uma opção:')

if resposta2 == perguntas[1].get('resposta'):
    print('Você acertou!!!')
    acertos += 1
else:
    print('Você errou!')
escolhas = 0

print(f'\n************TERCEIRA PERGUNTA************')

print(perguntas[2].get('Pergunta'))
for opção in perguntas[2].get('Opções'):
    escolhas += 1
    print(f'{escolhas}) {opção}')

resposta2 = input('Escolha uma opção:')

if resposta2 == perguntas[2].get('resposta'):
    print('\nVocê acertou!!!')
    acertos += 1
else:
    print('\nVocê errou!')

print(f'\nFIM DE JOGO!!!!!!')
print(f'\nVOCÊ ACERTOU {acertos} DE {len(perguntas)} PERGUNTAS!')
