# Exercicio 028 - Aula 010
# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 a 5.
# Peça para o usuário tentar descobrir qual foi o número escolhido.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice  # Importa a função choice() da biblioteca .random()
from time import sleep  # Importa a função sleep() da biblioteca Time
print('Bem vindo ao =-=-=INTUITION TEST=-=-=\n\nVamos jogar?')  # Introdução
sleep(1)  # Peço para o computador esperar 1 segundo
x1 = True  # Crio a variável x1 como True para dar inicio ao loop

while x1 == True:  # Enquanto x1 for igual a True, exeuta o loop
    x = [0, 1, 2, 3, 4, 5]  # Cria um grupo de 0 a 5
    xx = choice(x)  # Sorteia de 0 a 5
    print('\nVou sortear um número de 0 a 5 e você deve adivinhar qual é!')
    print('\n...Carregando...')
    sleep(1)  # Peço para o computador esperar 2 segundos
    n = str(input('\nPor favor, digite um número válido de 0 a 5:\n')).strip().upper()
    if n.isnumeric() == False:  # Filtro caso o usuário insira uma frase ou letra ou caractere no lugar de número
        continue  # Retorna ao inicio
    else:  # Se for número, verifica outro filtro:
        nn = int(n)  # Transforma a string N em inteiros NN
    if nn < 0 or nn > 5:  # Filtra se o número é valido de 0 a 5...
        continue  # Se for menor que 0 ou maior que 5, retorna ao inicio
    else:  # Se estiver ok, segue o jogo...
        print('\nVocê escolheu o número {}...'.format(nn))

    print('\n...Carregando...\n')
    sleep(1)  # Peço para o computador esperar 2 segundos
    if nn == xx:  # Verifica se o usuário ganhou ou perdeu
        print('#'*30)
        print('Parabéns, você acertou!')
        print('#'*30)
        new = str(input('\n\nDeseja jogar novamente?\n')).strip().upper()
        if new == 'SIM' or new == 'S':  # Caso o usuário queira jogar novamente, retorna ao inicio
            x1 = True  # Determina x1 como True e retorna o loop
        else:  # Caso o contrário, determina x1 como False e encerra o jogo
            x1 = False

    else:  # Caso o usuário tenha perdido, imprime em tela o número sorteado e informa que perdeu.
        print('\n\n-=-=-=-=-=-Você errou!=-=-=-=-=-\n\n>>>O número sorteado foi (({}))<<<'.format(xx))
        # Requisita se quer jogar novamente
        new = str(input('\n\nDeseja jogar novamente?\n')).strip().upper()
        if new == 'SIM' or new == 'S':  # caso queira jogar, retorna ao inicio como True
            x1 = True
        else:  # Caso não queira, encerra o loop como False e encerra o jogo
            x1 = False

print('\n\nObrigado por jogar!\nAté a próxima')
# Fim
