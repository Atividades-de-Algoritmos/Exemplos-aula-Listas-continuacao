#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 13/07/2022
#
# 1 – ler uma lista de 5 número inteiros e imprimir cada número juntamente com a sua posição na lista.

# -- Entrada de dados --

lista = [] # Criando uma lista vazia e adicionar 5 números inteiros a ela.

for i in range(5): # for para adicionar 5 números inteiros a lista criada anteriormente
    num = int(input(f"Informe um número[{i+1}]: ")) # Entrada de número inteiro para adicionar a lista
    lista.append(num) # Adicionando número inteiro a lista criada anteriormente

# -- Processamento e Saída de dados --

print() # Print vazio funciona como um enter do teclado

for i in range(5):  # for para imprimir 5 números inteiros e suas posições na lista
    print(f"lista[{lista[i]}] -> {i+1}") # imprimir número inteiro e sua posição na lista

# Modo 2.0

# for i in range(5): # for para imprimir 5 números inteiros e suas posições na lista
#    print(f"O número {lista[i]} está na posição [{i}]") # imprimir número inteiro e sua posição na lista

# Modo 3.0

# for posicao, valor in enumerate(lista): # Enumerate cria um tupla com os valores e suas posições.
#    print(f'O número {valor} está na posição {posicao}')

print("\nfim do programa") # Informa ao usuário que o programa terminou