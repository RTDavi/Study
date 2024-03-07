# """
# Fazer uma lista de compras com listas
# o usuário deve poder apagar, inserir e listar os itens da lista
# Não permita erros de índices inexistentes
# """
# resposta = input('Bem vindo ao programa de listas para compras, deseja começar? [S] ou [N]:').upper()
# lista = []
# continuar = False

# if resposta == 'S':

#     continuar = True

#     while continuar == True:
#         escolha = input(f'Escolha uma opção\n [I]nserir [A]pagar [L]istar:').upper()

#         if escolha == 'I':
#             lista.append(input('Digite o nome do item:'))
#             resposta = input('Deseja continuar? [S] ou [N]:').upper()

#             if resposta == 'N':
#                 continuar = False
    
#         if escolha == 'A':
#             indices = int(input('Digite o índice da lista para apagar:'))

#             try:
#                 indice = int(indices)
#                 del lista[indice]
#             except IndexError:
#                 print('Índice não encontrado na lista.')
#             except ValueError:
#                 print('Digite um número inteiro.')
                    
#             resposta = input('Deseja continuar? [S] ou [N]:').upper()

#             if resposta == 'N':
#                 continuar = False
        
#         if escolha == 'L':
#             for indice, nome in enumerate(lista):
#                 print(indice, nome)

#             resposta = input('Deseja continuar? [S] ou [N]:').upper()

#             if resposta == 'N':
#                 continuar = False
# print(f'Obrigado por usar a lista, aqui está sua lista\n {lista}')

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

print(len(perguntas))