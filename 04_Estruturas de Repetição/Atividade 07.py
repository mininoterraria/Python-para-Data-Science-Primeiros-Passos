#7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
numero = int(input("Insira um número inteiro: "))
numeros_divisiveis = 0
for i in range(1,numero + 1):
  if(numero % i == 0):
    print(i)
    numeros_divisiveis += 1
if(numeros_divisiveis == 2):
    print("É número primo.")
else:
    print("Não é número primo.") 
