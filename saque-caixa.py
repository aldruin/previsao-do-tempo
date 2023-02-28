'''
@author - aldruinn
Simulação de saque no caixa eletrônico
Distribuição de cédulas
'''

# Entrada do usuário para saque
valor = str(input('Que valor você deseja sacar? R$ '))

#Validação da entrada do usuário
while not valor.replace('.', '').isdigit() or valor.count('.') >= 1:
    valor = str(
        input('Valor inválido. Digite um valor para saque (ex: R$100 / R$ 1500): R$ '))

# Variaveis
valor = int(valor)
cedulas_lista = [50, 20, 10, 1]
cedulas_total = 0

# Loop de iteração em lista
for cedulas in cedulas_lista:

    # Estrutura de repetição com reste lógico
    while True:

        # Define quantidade de notas
        if valor >= cedulas:
            valor -= cedulas
            cedulas_total += 1

        # Resultado da quantidade de 'cedulas' atual
        elif cedulas_total > 0:
            print(f'{cedulas_total} notas de {cedulas}')
            cedulas_total = 0
            break

        # Saque concluido com sucesso
        elif valor == 0:
            break
'''fim'''
