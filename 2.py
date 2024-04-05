numero = int(input("Digite um número: "))
fibonacci = 1
sequencia = [1]
while numero >= fibonacci:
  sequencia.append(fibonacci)
  fibonacci += sequencia[-2]

if numero in sequencia:
  print("O número pertence à sequência de Fibonacci.")
else:
  print("O número não pertence à sequência de Fibonacci.")