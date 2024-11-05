#12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:
'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
'''
#Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
designs = {
    'Design 1': 1334,
    'Design 2': 982,
    'Design 3': 1751,
    'Design 4': 210,
    'Design 5': 1811
}
maior_valor = 0
maior_chave = ''
total_votos = 0
for chave, valor in designs.items():
  total_votos += valor
  if(valor > maior_valor):
    maior_valor = valor
    maior_chave = chave
for i,j in designs.items():
  calculo = (j / total_votos) * 100
  print(f"Porcentagem do {i}: {calculo:.2f}%")
print(f"Design mais votado: {maior_chave}")
print(f"Total de votos: {total_votos}")
