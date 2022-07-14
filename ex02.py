#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 13/08/2022
#
# 2 – ler uma lista de 5 número reais e imprimir a lista na ordem inversa.

# -- Entrada de dados --

lista = [] # Criando uma lista vazia e adicionando 5 números inteiros a ela.

for i in range(5): # for para adicionar 5 números reais a lista criada anteriormente
    num = float(input(f"Informe um número[{i+1}]: ")) # Solicitando valores reais
    lista.append(num) # Adicionando número real a lista criada anteriormente

# -- Processamento e saída de dados --

print(f"\nLista na ordem inversa: {lista[::-1]}") # Imprimindo a lista inversa com o comando [::-1]

# lista.reverse() # Invertendo a lista usando o método .reverse(), ele inverte a ordem da lista mas sem ordena-la

print("\nfim do programa") # Informando ao usuário que o programa chegou ao fim
