#5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
numeros = []
numeros_divisiveis = 0
numero = int(input("Insira um número qualquer: "))
print(f"Números Primos do intervalo de {numero}:")
for valores in range(1,numero + 1):
  numeros_divisiveis = 0
  for j in range(1,numero + 1):
      if(valores % j == 0):
          numeros_divisiveis += 1
  if(numeros_divisiveis == 2):
    if(valores == numero):
      continue
    else:
      numeros.append(valores)
print(numeros)
