#9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

#Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
#Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
#Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
branco = 0
nulo = 0
votos_totais = 0
print("Candidato1 - 1")
print("Candidato2 - 2")
print("Candidato3 - 3")
print("Candidato4 - 4")
print("Branco - 5\nNulo - 6")
for eleitores in range(1,21):
  voto = int(input("Insira seu voto: "))
  if(voto == 1):
    candidato1 += 1
    votos_totais += 1
  elif(voto == 2):
    candidato2 += 1
    votos_totais += 1
  elif(voto == 3):
    candidato3 += 1
    votos_totais += 1
  elif(voto == 4):
    candidato4 += 1 
    votos_totais += 1
  elif(voto == 5):
    branco += 1
    votos_totais += 1
  else:
    nulo += 1
    votos_totais += 1
print(f"Votos do candidato 1: {candidato1}")
print(f"Votos do candidato 2: {candidato2}")
print(f"Votos do candidato 3: {candidato3}")
print(f"Votos do candidato 4: {candidato4}")
print(f"Quantidade branco: {branco}")
print(f"Quantidade nulo: {nulo}")
print(f"Percentual votos brancos: {(branco / votos_totais) * 100:.2f}%")
print(f"Percentual votos nulos: {(nulo / votos_totais) * 100:.2f}%")
