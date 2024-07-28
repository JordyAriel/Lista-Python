inteiros = [None] * 6

num_linhas = len(inteiros)
somaPares = 0
somaImpares = 0

for coluna in range(num_linhas):
    print("Digite o", (coluna + 1), "º do array: ", end=" ")
    numero = int(input())
    inteiros[coluna] = numero


for coluna in range(num_linhas):
    
    if (inteiros[coluna] % 2) == 0:
        somaPares = somaPares + inteiros[coluna]
        
    else:
        somaImpares = somaImpares + inteiros[coluna]
        
print("A soma dos números pares é igual a:", somaPares)
print("A soma dos números impares é igual a:", somaImpares)