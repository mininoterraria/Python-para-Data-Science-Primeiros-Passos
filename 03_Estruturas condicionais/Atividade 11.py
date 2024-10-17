#11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.
lado_1 = float(input("Insira o primeiro lado: "))
lado_2 = float(input("Insira o segundo lado: "))
lado_3 = float(input("Insira o terceiro lado: "))
if(lado_1 > 0 and lado_2 > 0 and lado_3 > 0):
  if(lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_2 + lado_3) > lado_1:
    if(lado_1 == lado_2 == lado_3):
      print("Esse triângulo é equilátero.")
    elif(lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
      print("Esse triângulo é isósceles.")
    elif(lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3):
      print("Esse triângulo é escaleno.")
  else:
    print("Os lados fornecidos não formam um triângulo válido!")
else:
  print("Um ou mais valores inválidos!")
