
print("=== ESCAPE ROOM: LA BÓVEDA ===")

nombre = input("Nombre del agente: ")

while not nombre.isalpha():
    print("Error: solo se permiten letras.")
    nombre = input("Nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:

    print("Agente:", nombre)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese una opción válida.")
        opcion = input("Opción: ")

    if opcion == "1":

        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:
            print("La cerradura se trabó.")
            alarma = True

        else:

            if energia < 40:

                numero = input("Riesgo de alarma. Elija un número del 1 al 3: ")

                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    print("Error: ingrese un número del 1 al 3.")
                    numero = input("Riesgo de alarma. Elija un número del 1 al 3: ")

                if numero == "3":
                    alarma = True
                    print("¡Alarma activada!")

            if alarma == False:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    elif opcion == "2":

        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        print("Hackeando panel...")

        for paso in range(4):
            codigo_parcial += "A"
            print("Progreso:", codigo_parcial)

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta automáticamente!")

    elif opcion == "3":

        forzar_seguidas = 0

        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma == True:
            energia -= 10

        print("Descansaste.")

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("El sistema se bloqueó.")
        break


if cerraduras_abiertas == 3:
    print("¡VICTORIA!")

elif alarma == True:
    print("DERROTA. La bóveda quedó bloqueada.")

elif energia <= 0 or tiempo <= 0:
    print("DERROTA.")
