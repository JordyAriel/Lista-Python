numeros = [None] * 6

num_colunas = len(numeros)
maiorNumero = 0

for colunas in range(num_colunas):
    print("Digite o", (colunas + 1), "º número do array: ")
    numero = int(input())
    numeros[colunas] = numero


for jordy in range(num_colunas):
    
    if numeros[jordy] > maiorNumero:
        maiorNumero = numeros[jordy]


print("O maior número do array é o:", maiorNumero)