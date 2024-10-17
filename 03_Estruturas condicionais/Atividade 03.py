#3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
vogais = 'a,e,i,o,u'
consoantes = 'C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z'.lower()
letra = input("Insira uma letra: ")
if(letra in vogais):
  print("É vogal")
elif(letra in consoantes):
  print("É consoante")
else:
  print("Valor inválido!")
