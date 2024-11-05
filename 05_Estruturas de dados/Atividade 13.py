#13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
total_gasto = 0
abono_minimo = 0
maior_abono = 0
for valor in salarios:
  abono = (0.10 * valor)
  abono = round(abono,2) #A função round serve para cortar casas decimais sem precisar transformar o valor numerico em string como era feito antes para cortar casas decimais.
  if(abono < 200):
    abono = 200
  total_gasto += abono
  colaboradores = {
    valor : abono
  }
  if(abono == 200):
    abono_minimo += 1
  if(abono > maior_abono):
    maior_abono = abono
  print(colaboradores)
print(f"Gasto total com o abono: R$ {total_gasto}")
print(f"Quantos receberam abono mínimo: {abono_minimo}")
print(f"Maior abono recebido: R${maior_abono}")
