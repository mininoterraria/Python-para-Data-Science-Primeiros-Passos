#7.Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input("Insira o numerador: "))
denominador = int(input("Insira o denominador (NÃO PODE SER IGUAL A 0): "))
divisao_inteira = numerador // denominador
divisao_inteira