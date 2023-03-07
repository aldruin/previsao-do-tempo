'''
Exercicio (073) contido no 'Mundo 3' do curso de 'Python 3' do site CursoEmVideo.com
@author : aldruinn
'''

# Variaveis
times_20_colocados = ('PALMEIRAS', 'INTERNACIONAL', 'FLUMINENSE', 'CORINTHIANS', 'FLAMENGO', 'ATHLETICO PARANAENSE', 'ATLETICO MINEIRO', 'FORTALEZA',
                      'SAO PAULO', 'AMERICA FC SAF', 'BOTAFOGO', 'SANTOS', 'GOIAS', 'RED BULL BRAGANTINO', 'CORITIBA', 'CUIABA SAF', 'CEARA', 'ATLETICO', 'AVAI', 'JUVENTUDE')
cinco_primeiros = []
quatro_ultimos = []

# Laço de iteração para encontrar a posição e o nome do time na lista times_20_colocados
for posicao, times in enumerate(times_20_colocados, start=1):

    # Adiciona à lista 'cinco_primeiros' os 5 primeiros colocados
    if posicao <= 5:

        cinco_primeiros.append(f'{posicao}º {times}')

    # Adiciona à lista 'quatro_ultimos' os 4 ultimos colocados
    elif posicao > len(times_20_colocados) - 4:

        quatro_ultimos.append(f'{posicao}º {times}')

# Cinco primeiros colocados
print('#'*50)
print('Os cinco primeiros colocados foram:')
print('\n'.join(cinco_primeiros))
print('#'*50)

# Quatro ultimos colocados
print('\nOs quatro ultimos colocados foram:')
print('\n'.join(quatro_ultimos))
print('#'*50)

# Times participantes
print('\nOs times participantes foram (A-Z):\n')
print('\n'.join(sorted(times_20_colocados)))
print('#'*60)

# Filtra se há o time 'Chapecoense'
if 'Chapecoense' in times_20_colocados or 'CHAPECOENSE' in times_20_colocados:
    print('O time CHAPECOENSE está entre os 20 classificados')
    posicao_chapecoense = times_20_colocados.index('CHAPECOENSE')

    # Exibe a posição do time
    print(f'Sua posição é: {posicao_chapecoense+1}º CHAPECOENSE')
    print('#'*60)

# Time 'Chapecoense' não foi encontrado
elif 'Chapecoense' not in times_20_colocados or 'CHAPECOENSE' not in times_20_colocados:
    print('O time CHAPECOENSE não foi encontrado entre os 20 classificados')
    print('#'*60)
