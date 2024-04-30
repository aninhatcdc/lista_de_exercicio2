quantidade = int(input("Qual a quantidade de maçãs a serem compradas? "))
maca = 1.30
maca2 = 1.00
valor1 = maca * quantidade
valor2 = maca2 * quantidade
if quantidade < 12:
    print(valor1,"reais")
elif quantidade >= 12:
    print(valor2,"reais")