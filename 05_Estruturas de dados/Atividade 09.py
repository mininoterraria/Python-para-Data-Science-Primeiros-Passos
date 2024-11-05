#9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
gabarito = ['D','A','C','B','A','D','C','C','A','B']
nota = 0
questao = 0
for i in gabarito:
  questao += 1
  resposta_aluno = input(f"Insira a resposta da questão {questao}: ").upper()
  if(resposta_aluno == i):
    nota += 1
print(f"Nota do aluno: {nota}")
