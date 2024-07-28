dia = int(input("Digite um número de um dia da semana: "))

if dia > 1 and dia < 7:
    print("o número corresponde a um dia da semana")

elif dia == 1 or dia == 7:
    print("o número corresponde a um dia de fim semana") 
    
else:
    print("o número não corresponde a qualquer dia da semana")