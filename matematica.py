vetor = [2, 2, 3, 3, 4]
num_colunas = len(vetor)
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
            
print("Temos", quan_unicos, "Número únicos")