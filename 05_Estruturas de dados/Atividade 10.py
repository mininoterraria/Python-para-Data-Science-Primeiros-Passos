#10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
lista_temperaturas = []
soma_temperaturas = 0
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
for i in range(1,13):
  temperatura = float(input(f"Insira a temperatura do mes {i}: "))
  lista_temperaturas.append(temperatura)
  soma_temperaturas += temperatura

media_anual = soma_temperaturas / len(lista_temperaturas)
print(f"Média anual das temperaturas mensais: {media_anual:.2f}°C")
print("Temperaturas acima da média geral:")
for j in range (len(lista_temperaturas)): #Isso fará com que a variavel j armazene os indices da lista temperatura.
    if(lista_temperaturas[j] > media_anual):
      print(f"{meses[j]}")
