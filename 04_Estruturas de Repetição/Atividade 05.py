#5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
numero = int(input("Insira um número inteiro qualquer: "))
fatorial = 1
numero_copia = numero
flag = False
while(numero > 1):
  if(numero < numero_copia):
    fatorial = fatorial * (numero - 1)
  else:
    fatorial = (numero * (numero - 1))
  numero -=1
print(f"Fatorial de {numero_copia}: {fatorial}")
