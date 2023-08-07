nome = "Carla Joaquina" # tipo str
idade = 27 # tipo int
altura = 1.759 # tipo float

print(f"Tipo da var nome: (type (nome))" % type(nome))
print(f"Tipo da var idade: (type (Idade)]" % type(idade))
print(f"Tipo da var altura: (type(altura)|" % type(altura))

print("Nome: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)
print("% possui %d anos e tem %.2fm de altura" % (nome, idade, altura))