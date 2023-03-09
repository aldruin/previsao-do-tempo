'''
@author - aldruinn
Exercicio do curso em video, cujo precisei criar uma lista de palavras sem acento, e mostrar para cada palavra, quais sao suas vogais
'''

# Dados
palavras = ("abacaxi", "banana", "cenoura", "dente", "elefante", "futebol", "guitarra", "hotel", "igreja",
            "jogador", "ketchup", "limão", "melancia", "navio", "ouro", "pessoa", "queijo", "roda", "sapato", "tigre")
vogais = ("a", "e", "i", "o", "u")

# Laço de iteração 'palavra' em 'lista de palavras'
for palavra in palavras:

    # Variaveis de controle
    vogal = False

    # Lista temporaria de vogais encontradas na palavra
    vogais_na_palavra = []

    # Laço de iteração 'letra' em cada 'palavra'
    for letra in palavra:

        # Define vogal como verdadeira e acrescenta à lista de vogais encontradas caso ainda não esteja
        if letra in vogais and letra not in vogais_na_palavra:
            vogal = True
            vogais_na_palavra.append(letra)

        # Caso a vogal ja esteja na lista, remove e acrescenta novamente para manter o controle de não repetir a vogal
        elif letra in vogais_na_palavra:
            vogais_na_palavra.remove(letra)
            vogais_na_palavra.append(letra)

    # Resultado
    print(
        f"A palavra '{palavra}' contém as vogais '{','.join(vogais_na_palavra)}' ")
