#8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
numero = int(input("Insira um número inteiro: "))
if(numero % 2 == 0):
  print("É par.")
else:
  print("É impar.")