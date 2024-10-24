#12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:
#O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
#O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
tipo_etanol = 'e,E,etanol,Etanol'
tipo_diesel = 'd,D,diesel,Diesel'
e_preco = 2
d_preco = 1.70
combustivel = input("Insira qual tipo de combustivel: ")
litros = float(input("Insira a quantidade de litros: "))

if(combustivel in tipo_etanol):
  preco_bruto_etanol = litros * 1.70
  if(litros > 0):
    if(litros <= 15):
      valor_desconto = 1.70 * litros * 0.02
      preco_liquido = preco_bruto_etanol - valor_desconto
      print(f"Preço que o cliente pagará: R${preco_liquido}")
    else:
      valor_desconto = 1.70 * litros * 0.04
      preco_liquido = preco_bruto_etanol - valor_desconto
      print(f"Preço que o cliente pagará: R${preco_liquido}")
  else:
    print("Quantidade inválida de litros!")
  
elif(combustivel in tipo_diesel):
  preco_bruto_diesel = litros * 2
  if(litros > 0):
    if(litros <= 15):
      valor_desconto = 2 * litros * 0.03
      preco_liquido = preco_bruto_diesel - valor_desconto
      print(f"Preço que o cliente pagará: R${preco_liquido}")
    else:
      valor_desconto = 2 * litros * 0.05
      preco_liquido = preco_bruto_diesel - valor_desconto
      print(f"Preço que o cliente pagará: R${preco_liquido}")
  else:
    print("Quantidade inválida de litros!")
  
else:
  print("Combustivel inválido!")
