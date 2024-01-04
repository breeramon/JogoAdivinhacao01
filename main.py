from random import randint

adivinhar = int(input("Escolha um número entre 0 e 10: "))

numero_aleatorio = randint(0, 10)

if (adivinhar == numero_aleatorio):
  print(f"Número sorteado: {numero_aleatorio}")
  print(adivinhar)
  print("ACERTOU!")
else:
  print(adivinhar)
  print("ERROU!")
  print("")

while (adivinhar != numero_aleatorio):
  adivinhar = int(input("Escolha um número entre 0 e 10: "))
  if (adivinhar == numero_aleatorio):
    print(f"Número sorteado: {numero_aleatorio}")
    print(f"Seu número {adivinhar}")
    print("ACERTOU!")
    break
  else:
    print(adivinhar)
    print("ERROU!")
    print("")
