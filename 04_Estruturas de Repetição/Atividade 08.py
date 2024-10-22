#8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
intervalo5 = 0
flag = True
while(flag == True):
  idade = int(input("Insira uma idade: "))
  if(idade >= 0 and idade <= 25):
    intervalo1 += 1
  elif(idade >= 26 and idade <= 50):
    intervalo2 += 1
  elif(idade >= 51 and idade <= 75):
    intervalo3 += 1
  elif(idade >= 76 and idade <= 100):
    intervalo4 += 1
  elif(idade > 100):
    intervalo5 += 1
  if(idade < 0):
    flag = False

print(f"Distribuição [0-25]: {intervalo1}")
print(f"Distribuição [26-50]: {intervalo2}")
print(f"Distribuição [51-75]: {intervalo3}")
print(f"Distribuição [76-100]: {intervalo4}")
print(f"Distribuição [101+]: {intervalo5}")
