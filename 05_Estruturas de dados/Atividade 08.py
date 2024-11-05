#8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
id_par = 0
id_impar = 0
for i in range(1,11):
  id = int(input("Insira um id inteiro: "))
  if(id % 2 == 0):
    id_par += 1
  else:
    id_impar += 1
print(f"Quantidade de produtos doces: {id_par}")
print(f"Quantidade de produtos amargos: {id_impar}")
