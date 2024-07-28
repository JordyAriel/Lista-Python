ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(input("Digite um número de um mês: "))
mes = mes - 1

if mes >= 0 and mes <= 11:
    
    for jordy in range(12):
        
        if jordy == mes:
            print(ano[jordy])

else:
    print("O número não corresponde a qualquer mês do ano")