conta = (input("Digite o número da conta: "))
saldo = float(input("Digite o saldo desta conta: "))
debito = int(input("Digite o débito da conta: "))
credito = int(input("Digite o crédito da conta: "))
resultado = saldo - debito + credito
if resultado >= 0:
    print("Saldo positivo")
elif resultado < 0:
    print("Saldo negativo")