'''Fazer um programa que pergunte um valor em Dólares e apresente o equivalente em Reais. Considere U$1,00 =
R$3,80.'''

# Solicita o valor em Dólares para o usuário
valor_em_dolares = float(input("Digite o valor em Dólares: "))

# Realiza a conversão para Reais
valor_em_reais = valor_em_dolares * 3.80

# Exibe o resultado da conversão
print(f"{valor_em_dolares} Dólares equivalem a {valor_em_reais:.2f} Reais.")

