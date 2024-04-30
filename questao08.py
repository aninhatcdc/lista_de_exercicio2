atual = int(input("Digite a quantidade atual em estoque: "))
maxima = int(input("Digite a quantidade máxima em estoque: "))
minima = int(input("Digite a quantidade mínima em estoque: "))
media = (maxima + minima)/2
if atual >= media:
   print("Não efetuar compra")
else:
   print("Efetuar compra")