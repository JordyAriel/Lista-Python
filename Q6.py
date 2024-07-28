dia = int(input("Insira um dia do mês: "))

if dia > 0 and dia <= 10:
    print("o número escolhido está no início do mês")
    
elif dia >= 11 and dia <= 20:
    print("o número escolhido está no meio do mês")
    
elif dia >= 21 and dia <= 31:
    print("o número escolhido está no fim do mês")

else: 
    print("o número escolhido é inválido")