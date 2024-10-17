#5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto_1 = float(input("Insira o preço do primeiro produto: "))
produto_2 = float(input("Insira o preço do segundo produto: "))
produto_3 = float(input("Insira o preço do terceiro produto: "))

mais_barato = produto_1
if(produto_2 < mais_barato):
  mais_barato = produto_2
if(produto_3 < mais_barato):
  mais_barato = produto_3

if(mais_barato == produto_1):
  print("O primeiro produto é o mais barato.")
elif(mais_barato == produto_2):
  print("O segundo produto é o mais barato.")
elif(mais_barato == produto_3):
  print("O terceiro produto é o mais barato.")
