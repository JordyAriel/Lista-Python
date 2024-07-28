mes = int(input("Digite um número de um mês: "))

if mes >= 1 and mes <= 6:
    print("Esse mês está no primeiro semestre do ano!")
    
elif mes >= 7 and mes <= 12:
    print("Esse mês está no segundo semestre do ano!")
    
else:
    print("Esse número não corresponde a nenhum mês do ano!")