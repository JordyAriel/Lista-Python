quan_numeros = int(input("Quantos números vão ser inseridos: "))

print()

vetor = [None] * quan_numeros
num_colunas = len(vetor)

for colunas in range(num_colunas):
    print("Digite o", (colunas + 1), "º número do Array: ")
    numero = int(input())
    vetor[colunas] = numero


quan_unicos = 0

for coluna in range(num_colunas):
    PosEsc = coluna
    numEsc = vetor[coluna]
    unico = True
    
    for varrer in range(num_colunas):

        if varrer == PosEsc:
             unico = True
                 
        elif numEsc == vetor[varrer]:
            unico = False
            break
            
        else:
            unico = True
        
    if unico:
        quan_unicos = quan_unicos + 1
        

print("\nArray com", quan_numeros, ", números: ", vetor, "\nQuantidade de número únicos:", quan_unicos)