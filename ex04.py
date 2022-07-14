#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 13/07/2022
#
# 4 – ler uma lista de 5 números e imprimir o menor e maior valor.

# -- Processamento e entrada de dados --

lista = [] # Criando uma lista vazia e adicionar 5 números inteiros a ela.

for i in range(5): # for para adicionar 5 números inteiros a lista
    num = int(input(f"Informe um número[{i+1}]: ")) # Solicitando um valor int
    lista.append(num) # Adicionando número inteiro a lista criada anteriormente

# -- Saída de dados --

print("\nLista:", lista) # Imprimndo a lista
print("\nMenor valor:", min(lista)) # Imprimindo o menor valor
print("\nMaior valor:", max(lista)) # imprimindo o maior valor

print("\nfim do programa") # Informando ao usuário que o programa terminou
