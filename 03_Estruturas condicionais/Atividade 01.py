#1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
numero_1 = float(input("Insira um número:"))
numero_2 = float(input("Insira outro número:"))

if(numero_1 > numero_2):
  print(f"Maior número é {numero_1}")
elif(numero_1 < numero_2):
  print(f"Maior número é: {numero_2}")
else:
  print(f"Números são iguais.")