import random

options = ["Piedra", "Papel", "Tijeras"]

computerWins = 0
userWins = 0

rounds = 1

while True:

  print('-' * 30)
  print("Que empiece el Juego")
  print('-' * 30)

  userOption = input("Elige Piedra, Papel, o Tijeras => ").capitalize()
  if not userOption in options:
    print("Esa opción no es válida")
    continue

  computerOption = random.choice(options)
  print("La opción del usuario fue:", userOption)
  print("La opción del Computador fue:", computerOption)

  if userOption == computerOption:
    print("Empate")
  elif userOption == "Piedra":
    if computerOption == "Tijeras":
      print("Piedra gana a tijeras")
      print("Usuario ganó!")
      userWins += 1
    else:
      print("Papel gana a piedra")
      print("Computador ganó!")
      computerWins += 1
  elif userOption == "Papel":
    if computerOption == "Piedra":
      print("papel gana a piedra")
      print("user ganó!")
      userWins += 1
    else:
      print("tijera gana a papel")
      print("computer ganó!")
      computerWins += 1
  elif userOption == "Tijeras":
    if computerOption == "Papel":
      print("tijera gana a papel")
      print("user ganó!")
      userWins += 1
    else:
      print("piedra gana a tijera")
      print("computer ganó!")
      computerWins += 1

  if computerWins == 2:
    print("El ganador es la computadora")
    break
  if userWins == 2:
    print("El ganador es el Usuario")
    break

  print("-" * 30)
  print("Punto para el computador", computerWins)
  print("Punto para el usuario", userWins)
  print("-" * 30)

  rounds +=1
