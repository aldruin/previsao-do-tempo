'''
@author aldruinn 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

#Variaveis
extenso = ('zero','um','dois','três','quatro','cinco',
           'seis','sete','oito','nove','dez','onze',
           'doze','treze','quatorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte')

#Estrutura de repetição por teste lógico
while True:
    
    #Entrada do usuário
    n = str(input('Digite um número: ')).strip()

    #Validação da entrada do usuário
    while not n.replace('.','').isdigit() or n.count('.') >=1 or int(n) > 20:
        n = str(input('Digite um número válido entre 0 e 20: '))

    #Converte para inteiro
    n = int(n)
    
    #Resultado
    print (f'Você digitou o número {extenso[n].upper()}')
    
    #Fim
    break
