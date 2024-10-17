#9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
numero = float(input("Insira um número inteiro ou decimal:"))
if(numero % 1 == 0):
  print("É inteiro")
else:
  print("É decimal")
