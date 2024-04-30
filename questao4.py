nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
if media >= 6:
    print("APROVADO,sua média foi:",media)
elif media <6:
    print("NÃO APROVADO,sua média foi:",media)