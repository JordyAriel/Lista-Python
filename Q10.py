semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

dia = int(input("Digite um número de um dia da semana: "))
dia = dia - 1

if dia >= 0 and dia <= 6:

    for jordy in range(7):
        
        if jordy == dia:
            
            if jordy > 0 and jordy < 6:
                print(semana[jordy] + "-Feira")
            
            else:
                print(semana[jordy])
            
else:
    print("o número não corresponde a qualquer dia da semana")