#7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
turno = input("Insira o turno em que você estuda: ")
turnos_validos = 'manhã,tarde,noite'
if(turno in turnos_validos):
  if(turno == 'manhã'):
    print("Bom dia!")
  elif(turno == 'tarde'):
    print("Boa tarde!")
  elif(turno == 'noite'):
    print("Boa noite!")
else:
  print("Valor inválido!")
