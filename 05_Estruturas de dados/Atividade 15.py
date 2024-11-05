#15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
rh = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}
#Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
soma_idades = 0
soma_idades_setores = 0
soma_listas_setores = 0
iteracao = 0
acima_media_geral = 0
for setores, idades in rh.items():
  soma_listas_setores += len(idades)
  for numeros in idades:
    if(iteracao == 10):
      iteracao = 0
      soma_idades += numeros
    else:
      iteracao += 1
      soma_idades += numeros
  print(f"Soma das idades do {setores}: {soma_idades / len(idades)}")
  soma_idades_setores += soma_idades
  soma_idades = 0
media_geral = soma_idades_setores / soma_listas_setores
print(f"Média das idades dos setores: {media_geral}")
for idades in rh.values():
  for idade in idades:
    if(idade > media_geral):
      acima_media_geral += 1
print(f"Pessoas acima da média geral dos setores: {acima_media_geral}")
