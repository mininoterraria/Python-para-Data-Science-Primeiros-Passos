#4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
flag = False
while(flag == False):
  celsius = float(input("Insira uma temperatura em celsius: "))
  print(f"{celsius}C")
  if(celsius == -273):
    flag = True
