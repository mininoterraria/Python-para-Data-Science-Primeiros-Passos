#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
numeros_inteiros = []
for numeros in range(1,6):
  valores = int(input("Insira 5 números inteiros: "))
  numeros_inteiros.append(valores)
print(f"Lista de números inteiros: {numeros_inteiros}")
