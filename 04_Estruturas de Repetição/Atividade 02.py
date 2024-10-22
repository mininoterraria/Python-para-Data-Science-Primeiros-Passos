#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
  #Colonia A:
    #Taxa de crescimento: 3%
    #Elementos: 4
  #Colonia B:
    #Taxa de crescimento: 1,5%
    #Elementos: 10
dias = 0
colonia_a = 4
colonia_b = 10
while(colonia_a <= colonia_b):
  colonia_a = colonia_a + (colonia_a * 0.03)
  colonia_b = colonia_b + (colonia_b * 0.015)
  dias+=1
print(f"Serão necessários {dias} dias para colônia A ultrapassar colônia B.")
