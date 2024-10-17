#2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
percentual_crescimento = float(input("Informe o percentual de crescimento da produção: "))
if(percentual_crescimento < 0):
  print("Houve decrescimento!")
elif(percentual_crescimento > 0):
  print("Houve crescimento!")
else:
  print("Não houve crescimento ou decrescimento!")
