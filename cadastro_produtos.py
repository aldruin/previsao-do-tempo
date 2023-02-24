'''
@author - aldruinn
exercicio 070 da aula 15 do mundo 02 de python.3 - curso em video
'''

# Variaveis
p_nome = []
p_valor = []
p_novo = ['S', 'N']
# Inicio da estrutura de repetição com teste lógico
while True:
    # Nome do produto
    p_n = str(input('Digite o nome do produto: ')).strip().upper()

    # Filtro 'nome do produto'
    while p_n.isnumeric() == True:
        p_n = str(
            input('Digite o nome do produto [Ex: Bicicleta]:\n ')).strip().upper()

    # Valor do produto
    p_v = float(
        input('Digite o valor do produto [Ex:R$1000.20 // R$100.20]:\nR$ '))

    # Filtro 'valor do produto'
    while p_v < 0:
        p_v = float(
            input('Digite o valor do produto [Ex:R$1000.20 // R$100.20]:\nR$ '))

    # Adição dos valores 'nome' e 'valor' em 'p_nome' e 'p_valor'
    p_nome.append(p_n)
    p_valor.append(p_v)

    # Informa o produto cadastrado
    print(f'O produto {p_n} foi cadastrado com o valor de R${p_v:.2f}')

    # Novo produto
    new = str(
        input('Deseja registrar um novo produto? [S/N]\n')).strip().upper()

    # Filtro 'novo produto'
    while new not in p_novo:
        new = str(
            input('Deseja registrar um novo produto? [S/N]\n')).strip().upper()

    # Novo cadastro
    if new == 'S':
        continue

    # Encerra o cadastramento
    elif new == 'N':
        break

    # Fim da estrutura de repetição com teste lógico

# Filtrando informações para gerar o resultado final
gasto_total = sum(p_valor)
p_1000 = [produto for produto in p_valor if produto > 1000.00]
p_0 = min(p_valor)
index_nome_p_0 = p_valor.index(p_0)
nome_p_0 = p_nome[index_nome_p_0]

# Resultado
print('##'*20)
print(f'Foi gasto um total de R${gasto_total:.2f} na compra')
print(f'No total {len(p_1000)} produtos custam mais de R$1.000,00')
print(f'O produto mais barato se chama {nome_p_0}')
print('##'*20)
