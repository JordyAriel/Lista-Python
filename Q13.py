vogais = ["A", "E", "I", "O", "U"]
consoantes = ["Q", "W", "R", "T", "Y", "P", "S", "D", "F", "G", "H", "J", "K", "L" "Z", "X", "C", "V", "B", "N", "M"]

ehVogal = False
ehConsoante = False
num_consoantes = len(consoantes)

letra = input("Digite uma letra: ").upper()

for jordy in range(num_consoantes):
    
    if jordy >= 0 and jordy < 5:
        if letra == vogais[jordy]:
            ehVogal = True
            break
        
    if letra == consoantes[jordy]:
        ehConsoante = True
        break

if ehVogal:        
    print("A letra \"" + letra + "\" é uma vogal")
    
elif ehConsoante:
    print("A letra \"" + letra + "\" é uma consoante")
    
else:
    print("O Caracter digitado não faz parte do alfabeto!!")