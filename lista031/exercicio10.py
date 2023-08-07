'''Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula
prestação =
valor + (valor x (taxa : 100) x tempo em dias).

Perguntar ao usuario
- valor normal da prestaçao
- taxa de juros
- tempo em dias

resposta:
-valor da prestaçao em atraso
'''

valor = float(input("Qual é o valor normal da prestaçao?"))
taxa = float(input("Qual é a taxa de juros?"))
tempo = float(input("Quantos dias de atraso?"))

#valor + (valor x (taxa : 100) x tempo em dias).
prestacao = valor + (valor * (taxa/100) * tempo)

print("O valor da prestaçao em atraso é R$", prestacao)