#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
numero1 = float(input("Insira um número:"))
numero2 = float(input("Insira outro número:"))
operacao = input("Insira a operação desejada: ")
operacoes = 'adicao,subtracao,multiplicacao,divisao'

if(operacao in operacoes):
  if(operacao == 'adicao'):
    resultado = (numero1 + numero2)
  elif(operacao == 'subtracao'):
    resultado = (numero1 - numero2)
  elif(operacao == 'multiplicacao'):
    resultado = (numero1 * numero2)
  elif(operacao == 'divisao'):
    resultado = (numero1 / numero2)

  print(resultado)
  if(resultado % 2 == 0):
    print("É par.")
  else:
    print("É impar.")
  if(resultado >= 0):
    print("É positivo.")
  else:
    print("É negativo.")
  if(resultado % 1 == 0):
    print("É inteiro.")
  else:
    print("É decimal.")
else:
  print("Operação inválida!")