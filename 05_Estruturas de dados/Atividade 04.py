#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
decremento = -1
numeros_inteiros = []
for numeros in range(1,4):
  valores = int(input("Insira 3 números inteiros: "))
  numeros_inteiros.append(valores)
for indices in numeros_inteiros:
  print(numeros_inteiros[decremento])
  decremento -= 1
