#6) Escreva um programa que leia três números e os exiba em ordem decrescente.
numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
numero3 = float(input("Insira o terceiro número: "))

maior_numero = 0
if(numero3 < numero1 > numero2):
  print(f"{numero1}\n")
  if(numero3 > numero2):
    print(f"{numero3}\n")
    print(f"{numero2}")
  else:
    print(f"{numero2}\n")
    print(f"{numero3}")

elif(numero1 < numero2 > numero3):
  print(f"{numero2}\n")
  if(numero3 > numero1):
    print(f"{numero3}\n")
    print(f"{numero1}")
  else:
    print(f"{numero1}\n")
    print(f"{numero3}")

elif(numero1 < numero3 > numero2):
  print(f"{numero3}\n")
  if(numero1 > numero2):
    print(f"{numero1}\n")
    print(f"{numero2}")
  else:
    print(f"{numero2}\n")
    print(f"{numero1}")