#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 28/06/2022
#
# 3 – ler uma lista de 4 notas e em seguida mostra
# as notas e a média.
#
# criar uma lista vazia e adicionar 4 números inteiros a ela.
listaNotas = [] # criar uma lista vazia
# entrada: 4 números inteiros
for i in range(4): # for para adicionar 4 números inteiros a lista criada anteriormente
    nota = int(input(f"informe a nota[{i+1}]: ")) # entrada da nota para adicionar a lista
    listaNotas.append(nota) # adicionar nota a lista criada anteriormente

# saida:
print("notas:") # imprimir as notas
for i in range(4): # for para imprimir as notas e a média
    print(f"nota {i+1} = {listaNotas[i]}") # imprimir nota da lista
media = sum(listaNotas) / len(listaNotas) # calcular a média  da lista
print(f"média = {media}") # imprimir a média
print("fim do programa") # imprimir fim do programa

