#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
contador_elementos = 0
preco_elementos = 0
for valores in valores_gastos:
  if(valores > 3000):
    preco_elementos += valores
    contador_elementos += 1
print(f"Compras realizadas: {contador_elementos}")
print(f"Porcentagem quanto ao total de compras acima de 3000: {(contador_elementos / len(valores_gastos)) * 100:.2f}%")
