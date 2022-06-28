#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 1 – ler uma lista de 5 número inteiros e imprimir cada número juntamente com a sua posição na lista.
#
# criar uma lista vazia e adicionar 5 números inteiros a ela.
lista = []
# entrada: 5 números inteiros
for i in range(5): # for para adicionar 5 números inteiros a lista criada anteriormente
    num = int(input(f"informe um número[{i+1}]: ")) # entrada de número inteiro para adicionar a lista
    lista.append(num) # adicionar número inteiro a lista criada anteriormente

# saida: 5 números inteiros e suas posições
for i in range(5):  # for para imprimir 5 números inteiros e suas posições na lista
    print(f"lista[{lista[i]}] -> {i+1}") # imprimir número inteiro e sua posição na lista

# ou
print("ou")
for i in range(5): # for para imprimir 5 números inteiros e suas posições na lista
    print(f"O número {lista[i]} está na posição [{i}]") # imprimir número inteiro e sua posição na lista

print("fim do programa")