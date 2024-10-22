#Aquecendo na programação
#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
inicio = int(input("Insira um número inteiro: "))
fim = int(input("Insira outro número inteiro: "))
if(inicio < fim):
  for i in range(inicio,fim):
      print(i)
elif(inicio > fim):
  for i in range(fim,inicio):
    print(i)
else:
    print("Não há intervalo")
