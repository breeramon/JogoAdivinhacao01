from random import randint

numero_adivinhado = randint(0, 10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas + 1):
  numero_escolhido = int(input("Escolha um número entre 0 e 10: "))
  if numero_escolhido == numero_adivinhado:
    print(
        f"Parabéns, você acertou em {tentativa} tentativas, o número era {numero_adivinhado}"
    )
    break
  else:
    print("Você errou!")
print(f"O número era {numero_adivinhado}")
