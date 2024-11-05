#11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
 #Escreva um código que calcule o total de vendas e o produto mais vendido.
soma_produtos = 0
maior_valor = 0
chave_maior = ''
for chave, valor in produtos.items():
  soma_produtos += valor
  if(valor > maior_valor):
    maior_valor = valor
    chave_maior = chave
print(f"Valor total de vendas: {soma_produtos}")
print(f"Produto mais vendido: {chave_maior}")
