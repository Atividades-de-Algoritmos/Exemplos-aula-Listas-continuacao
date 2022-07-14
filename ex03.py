#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 13/07/2022
#
# 3 – ler uma lista de 4 notas e em seguida mostra
# as notas e a média.

# -- Entrada de dados --

listaNotas = [] # Criando uma lista vazia -> list()

for i in range(4): # for para adicionar 4 números inteiros a lista criada anteriormente
    nota = int(input(f"Informe a nota[{i+1}]: ")) # Solicitando um valor inteiro para atribuir a nota
    listaNotas.append(nota) # Adicionando nota a lista criada anteriormente

# -- Processamento e saída de dados --

print("\nnotas: ") # Imprimindo as notas

for i in range(4): # for para imprimir as notas e a média
    print(f"nota {i+1} = {listaNotas[i]}") # Imprimindo as nota da lista

media = sum(listaNotas) / len(listaNotas) # Calculando a média da lista
print(f"\nmédia = {media}") # Imprimindo a média das notas

print("\nfim do programa") # Informando ao usuário que o programa terminou
