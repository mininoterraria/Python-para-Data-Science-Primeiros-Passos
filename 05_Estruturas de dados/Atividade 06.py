#6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
#31 dias: Janeiro, março, maio, julho, agosto, outubro, dezembro.
#30 dias: Abril, Junho, Setembro, Novembro.
#28 dias quando não bissexto: Fevereiro.
#29 dias quando bissexto: Fevereiro.
dia = int(input("Insira um dia: "))
mes = int(input("Insira um mês: "))
ano = int(input("Insira um ano: "))
meses_30_dias = [4,6,9,11]
meses_31_dias = [1,3,5,7,8,10,12]
if(dia <= 0):
  print('Data Inválida1') #Erro 1 : Caso dia seja menor igual a 0.
elif(mes <= 0 or mes > 12):
  print("Data Inválida2") #Erro 2 : Caso mes seja menor igual a 0 ou superior a 12.
elif(ano <= 0 ):
  print("Data Inválida3") #Erro 3 : Caso ano seja menor igual a 0.
elif(mes in meses_30_dias and dia > 30):
  print("Data Inválida4") #Erro 4 : Caso no mes de 30 dias seja digitado dia superior à 30.
elif(mes in meses_31_dias and dia > 31):
  print("Data Inválida5") #Erro 5 : Caso no mes de 31 dias seja digitado dia superior à 31.
else:
  if(ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)): #Caso ano seja bissexto.
    if(mes == 2 and dia > 29): #No ano bissexto, o mês de fevereiro não pode ter mais de 29 dias.
      print("Data Inválida6") #Erro 6 : Caso seja digitado dia superior a 29 dias no mês de fevereiro quando é ano bissexto.
    else:
      print(f"{dia:02}/{mes:02}/{ano}")
  else:
    if(mes == 2 and dia > 28):
      print("Data Inválida7") #Erro 7 : Caso seja digitado superior a 28 dias no mês de fevereiro quando não é bissexto.
    else:
      print(f"{dia:02}/{mes:02}/{ano}")
