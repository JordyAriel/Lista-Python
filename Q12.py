produtos = [
    [1, "Creatina\t", 100],
    [2, "Whey Protein", 80],
    [3, "Beta Alanina", 50],
    [4, "Pré-Treino", 60]
]

num_linhas = len(produtos)
num_colunas = len(produtos[1])

print("*********************************")

for linha in range(num_linhas):
    
    for coluna in range(num_colunas):
        
        if coluna == 0:
            print("*", produtos[linha][coluna], ":", end=" ")
        
        elif coluna == 1:
            print(produtos[linha][coluna], "\tR$" , end=" ")
            
        else:
            print(produtos[linha][coluna], end=" ")
            
    print("\t*")
    
item = int(input("*****************| CÓDIGO: "))
item = item - 1

if item >= 0 and item < num_linhas:
    print("\no/a",produtos[item][1], "está por R$", produtos[item][2])

else:
    print("O código do item não corresponde a nenhum item!!")