import random

numero_adivinar = random.randint(0, 99)
intentos = 0

while True:
    try:
        intento = int(input("Escribe un número entre 0 y 99: "))

        if intento >= 0 and intento <= 99:  
            intentos += 1  

        if intento == numero_adivinar:   
            if intentos == 1:
                print(f"Bien has acertado el número en {intentos} intento.")
            else:
                print(f"Bien has acertado el número en {intentos} intentos.")
            break
        elif intento < 0 or intento > 99:
            print("Por favor, escribe un número entre 0 y 99.")
        elif intento < numero_adivinar:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    except ValueError:
        print("Eso no es un numero, escribe un número entre 0 y 99.")