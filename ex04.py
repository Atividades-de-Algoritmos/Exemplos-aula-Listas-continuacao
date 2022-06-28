#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 4 – ler uma lista de 5 números e imprimir o menor e maior valor.
#
# criar uma lista vazia e adicionar 5 números inteiros a ela.
lista = []
# entrada: 5 números inteiros
for i in range(5): # for para adicionar 5 números inteiros a lista criada anteriormente
    num = int(input(f"informe um número[{i+1}]: ")) # entrada de número inteiro para adicionar a lista
    lista.append(num) # adicionar número inteiro a lista criada anteriormente

# saida:
print("lista:") # imprimir a lista
print(f"{lista}") # imprimir a lista
print("menor valor:") # imprimir o menor valor
print(f"{min(lista)}") # imprimir o menor valor da lista
print("maior valor:") # imprimir o maior valor
print(f"{max(lista)}") # imprimir o maior valor da lista
print("fim do programa") # imprimir fim do programa
