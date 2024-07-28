# cada mês/variavél vai ganhar uma posição dentro do vetor, indo de 0 a 11, já que são 12 váriaveis
vetor = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(input("Digite um número de um mês: "))

# Aqui nós estamos corrigindo a contagem humana para a contagem computacional
mes = mes - 1

if mes >= 0 and mes <= 11:
    # Criamos um laço de repetição para varrer o vetor
    for jordy in range(12):
        
        # Estamos verificando número por número que o contador assume, até chegarmos no número correspondente que o usuário inseriu como entrada
        if jordy == mes:
            print(vetor[jordy])
            
else:
    print("o número não corresponde a qualquer mês do ano")