'''
@author: aldruinn
exercicio 069 da aula 15 do mundo 02 de python.3 - curso em video
'''

# Variaveis
sexo = ['MASCULINO', 'M', 'FEMININO', 'F']
novo_cadastro = ['S', 'N', 'SIM', 'NAO']
idades = []
masc = ['M', 'MASCULINO']
masc_l = []
fem = ['F', 'FEMININO']
fem_l = []
fem_idade = []

# Estrutura de repetição com teste lógico
while True:

    print('Cadastramento - Digite o nome, idade e sexo \n')

    # Nome
    nome = str(input('Digite o nome: ')).strip().upper()

    # Filtro 'nome'
    while nome.isnumeric() == True:
        nome = str(input('Digite o nome [Aa Bb]: ')).strip().upper()

    # Idade
    idade = int(input('Digite a idade: '))

    # Filtro 'idade'
    while idade < 0:
        idade = int(input('Digite a idade [0+]: '))

    # Sexo
    sex = str(input('Digite o sexo: ')).strip().upper()

    # Filtro 'sexo'
    while sex not in sexo:
        sex = str(input('Digite o sexo [M/F]: ')).strip().upper()

    # Informações ao usuário
    print('=-='*20)
    print(f'Nome:{nome} Idade:{idade} Sexo:{sex}')
    print('=-='*20)

    # Cadastro do sexo masculino
    if sex in masc:
        masc_l.append(sex)
        idades.append(idade)

    # Cadastro do sexo feminino
    elif sex in fem:
        fem_l.append(sex)
        idades.append(idade)
        fem_idade.append(idade)

        # Novo Cadastramento
    novo = str(
        input('Deseja realizar um novo cadastro? [S/N]')).strip().upper()

    # Filtro 'novo cadastramento'
    while novo not in novo_cadastro:
        novo = str(
            input('Deseja realizar um novo cadastro? [S/N]')).strip().upper()

    # Continua o cadastramento
    if novo == 'S' or novo == 'SIM':
        continue

    # Interrompe o cadastramento
    elif novo == 'N' or novo == 'NAO':
        break

# Filtrando informações para exibir em resultado

# Mulheres com menos de 20 anos
fem_idade_menor_20 = [idade for idade in fem_idade if idade < 20]

# Pessoas com menos de 18 anos
idades_menor_18 = [idade for idade in idades if idade < 18]
pessoas_menor_18 = len(idades_menor_18)

# Quantos homens foram cadastrados
cad_masc = len(masc_l)

# Resultado do filtro de informações
print('=-='*20)
print(f'{pessoas_menor_18} pessoas tem mais de 18 anos')
print(f'{len(fem_idade_menor_20)} mulheres tem menos de 20 anos')
print(f'{cad_masc} homens foram cadastrados')
print('=-='*20)

# Fim
print('Até a próxima')
