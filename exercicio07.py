'''Fazer um algoritmo que pergunte 3 números e apresente a média aritmética entre estes 3 número'''
# entrada de dados
num1 = float(input("Digite a primeiro numero:  "))
num2 = float(input("Digite a segundo numero:  "))
num3 = float(input("Digite a terceiro numero:  "))

# Calculando a média
media = (num1 + num2+ num3) / 3

# Exibindo a média
print(f"A média dos numeros é: {media:.2f}")