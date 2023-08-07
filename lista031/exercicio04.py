''' Fazer um programa que pergunte um número inteiro e apresente o seu antecessor e seu sucessor'''

# Solicitar o número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Calcular o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Exibir o resultado
print(f"O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.")