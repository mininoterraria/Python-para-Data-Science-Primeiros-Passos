#3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
dados = 1
while(dados <= 15):
  avaliacoes = int(input("Insira uma nota entre 0 a 5: "))
  if(avaliacoes < 0 or avaliacoes > 5):
    print("Valor inválido, insira uma avaliação entre 0 e 5.")
  else:
    dados += 1
