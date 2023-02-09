#Exercicio 037 - Aula 12
#Escreva um programa que leia um número inteiro qualquer
#Peça para o usuário escolher qual será a base de conversão:
#/1. para binário /2. para octal /3. para hexadecimal


n = int(input('Digite um número: '))#Solicita um número para o usuário
conversão = str(input('\n1. Binário\n2. Octal\n3. Hexadecimal\nQual será a base de conversão?\n')).strip().upper()#Usuário escolhe a base de conversão, remove espaço e transforma em caixa maior

if conversão == ('1') or conversão == ('BINÁRIO'):#Define escolha como 1 ou BINÁRIO
    print ('\nVocê escolheu BINÁRIO')#Informa a escolha
    print ('Analisando...')#Informa analisando
    b = bin(n)#Transforma 'n' para binário utilizando a função bin()
    print (b[2:])#Informa o valor em binário
elif conversão == ('2') or conversão == ('OCTAL'):#Define escolha como 2 ou OCTAL
    print ('\nVocê escolheu OCTAL')#Informa a escolha
    print ('Analisando...')
    o = oct(n)#Transforma 'n' para octal utilizando a função 'oct()'
    print (o[2:])#Informa o valor em OCTAL
elif conversão == ('3') or conversão == ('HEXADECIMAL'):#Define escolha como 3 ou HEXADECIMAL
    print ('\nVocê escolheu HEXADECIMAL')#Informa a escolha
    print ('Analisando...')
    h = hex(n)#Transforma 'n' em hexadecimal usando a função hex()
    print (h[2:])#Informa o valor em Hexadecimal

else:#Caso contrário define como opção invalida
    print ('Opção inválida')
