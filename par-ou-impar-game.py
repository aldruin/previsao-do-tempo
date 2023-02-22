'''
@author: aldruinn

'''

from random import randint
from time import sleep

# Inicio
print('=-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*20)

# Variaveis
par = ['PAR', 'P']
impar = ['IMPAR', 'I']
jogadas = ['PAR', 'P', 'IMPAR', 'I']
vencedoras = 0

while True:
    # Maquina joga
    n_maquina = randint(1, 10)

    # Player joga
    j1 = int(input('DIGITE UM NÚMERO: '))

    # Filtro 'j1'
    while j1 < 0:
        j1 = int(input('DIGITE UM NÚMERO: '))

    # Player escolhe 'P' ou 'I'
    j2 = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()

    # Filtro 'j2'
    while j2 not in jogadas:
        j2 = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()

    # Pausa Dramática
    print('\nCARREGANDO...')
    sleep(1)

    # Impar vence
    if (n_maquina + j1) % 2 == 1:

        # Jogador venceu
        if j2 in impar:
            print('=-='*10)
            print(
                f'VOCÊ JOGOU {j1} E O COMPUTADOR JOGOU {n_maquina}. TOTAL DE {(j1+n_maquina)} DEU IMPAR')
            print('=-='*10)
            print('PARABÉNS, VOCÊ VENCEU!!')
            print('=-='*10)
            print('VAMOS JOGAR NOVAMENTE...')
            print('=-='*10)
            vencedoras += 1

        # Maquina venceu
        elif j2 in par:
            print('=-='*10)
            print(
                f'VOCÊ JOGOU {j1} E O COMPUTADOR JOGOU {n_maquina}. TOTAL DE {(j1+n_maquina)} DEU IMPAR')
            print('=-='*10)
            print('VOCÊ PERDEU!')
            print('=-='*10)
            print(f'GAME OVER, VOCÊ VENCEU {vencedoras} VEZES')
            break

    # Par vence
    elif (n_maquina + j1) % 2 == 0:

        # Jogador venceu
        if j2 in par:
            print('=-='*10)
            print(
                f'VOCÊ JOGOU {j1} E O COMPUTADOR JOGOU {n_maquina}. TOTAL DE {(j1+n_maquina)} DEU PAR')
            print('=-='*10)
            print('PARABÉNS, VOCÊ VENCEU!!')
            print('=-='*10)
            print('VAMOS JOGAR NOVAMENTE...')
            print('=-='*10)
            vencedoras += 1

        # Maquina venceu
        elif j2 in impar:
            print('=-='*10)
            print(
                f'VOCÊ JOGOU {j1} E O COMPUTADOR JOGOU {n_maquina}. TOTAL DE {(j1+n_maquina)} DEU PAR')
            print('=-='*10)
            print('VOCÊ PERDEU!')
            print('=-='*10)
            print(f'GAME OVER, VOCÊ VENCEU {vencedoras} VEZES')
            break
