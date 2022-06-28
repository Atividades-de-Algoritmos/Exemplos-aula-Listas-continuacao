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
for i in range(5):
    num = int(input(f"informe um número[{i+1}]: "))
    lista.append(num)
# saida: 5 números inteiros e suas posições
for i in range(5):
    print(f"lista[{lista[i]}] -> {i+1}")

# ou
print("ou")
for i in range(5):
    print(f"O número {num} está na posição {i}")

print("fim do programa")