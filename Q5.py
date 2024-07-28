num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

print("")

if num1 > num2:
    print("O número", num1, "é maior que o", num2)
elif num1 == num2:
    print("O número", num1, "é igual ao número", num2)
else:
    print("O número", num1, "é menor que o", num2)