#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 1 – 2 – ler uma lista de 5 número reais e imprimir a lista na ordem inversa.
#
# criar uma lista vazia e adicionar 5 números inteiros a ela.
lista = [] # criar uma lista vazia
# entrada: 5 números reais
for i in range(5): # for para adicionar 5 números reais a lista criada anteriormente
    num = float(input(f"informe um número[{i+1}]: ")) # entrada de número real para adicionar a lista
    lista.append(num) # adicionar número real a lista criada anteriormente

# saida:
print("lista inversa:") # imprimir a lista inversa
print(f" usando [::-1] = {lista[::-1]}") # imprimir a lista inversa com o comando [::-1]
lista.reverse() # inverter a lista
# o método reverse() inverte a ordem da lista mas sem ordena-la
print(f"usando o método .reverse = {lista}")

print("fim do programa")