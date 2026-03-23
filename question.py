import random
import string

words = {"programacion":[
                        "python",
                        "programa",
                        "variable",
                        "funcion",
                        "bucle",
                        "cadena",
                        "entero",
                        "lista",
                        ]
         , "matematicas":[
                         "suma",
                         "multiplicacion",
                         "derivada",
                         "integral"
                         ]
         , "facultades":[
                         "ingenieria",
                         "humanidades",
                         "informatica",
                         "medicina",
                         ]
}

#Le pido que elija la categoria
cat=input(f"Elija una categoria : {" - ".join(words)} : ")

while not(cat in words):
    cat=input(f"Elija una categoria dentro de las opciones: {" - ".join(words)} : ")

word = random.choice(words[cat])
guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        print(f"Puntaje: {puntaje}")
        break
  
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    # Si el caracter ingresado es mayuscula la paso a minuscula
    letter = (input("Ingresá una letra: ")).lower

    # Verifico si el caracter es valido o no
    if (letter in string.ascii_lowercase) and (letter!=""):
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
    else:
        print("entrada no valida")
        
    print()

else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje: {puntaje}")
