valor = 10.0

print("Mercadoria:")
print("Creatina:\t", valor, "R$\n")

saldo = float(input("Quanto você tem para gastar? "))

if saldo >= valor:
    decisao = int(input("Você quer comprar?\n(Digite 1 para sim, e 2 para não): "))
    
    if decisao == 1:
        print("Restou-lhe apenas", (saldo - valor), "R$")
        
    elif decisao == 2:
        print("Ok, fica pra próxima!!")
        
    else:
        print("Não é uma escolha válida!!")
        
else:
    print("Quer vir trabalhar comigo?")