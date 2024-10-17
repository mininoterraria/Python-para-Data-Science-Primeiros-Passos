#4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
preco_ano1 = float(input("Informe o preço médio no primeiro ano: "))
preco_ano2 = float(input("Informe o preço médio no segundo ano: "))
preco_ano3 = float(input("Informe o preço médio no terceiro ano: "))

maior_preco = preco_ano1
if (preco_ano2 > maior_preco):
  maior_preco = preco_ano2
if(preco_ano3 > maior_preco):
  maior_preco = preco_ano3

menor_preco = preco_ano1
if (preco_ano2 < menor_preco):
  menor_preco = preco_ano2
if(preco_ano3 < menor_preco):
  menor_preco = preco_ano3

print(f"Maior Preço: {maior_preco}\n Menor Preço: {menor_preco}")
