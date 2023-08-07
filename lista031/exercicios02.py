'''Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro'''

# Solicita os quatro valores inteiros
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))

# Calcula a adição dos valores
soma = valor1 + valor2 + valor3 + valor4

# Calcula a multiplicação dos valores
multiplicacao = valor1 * valor2 * valor3 * valor4

# Apresenta os resultados
print("Resultado da adição:", soma)
print("Resultado da multiplicação:", multiplicacao)