
print("--- BIENVENIDO A LA ARENA ---")

# Nombre del Gladiador
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

# Ciclo de combate
while vida_jugador > 0 and vida_enemigo > 0:

    if turno_gladiador == True:

        print("\n", nombre, "(HP:", vida_jugador, ")")
        print("Enemigo (HP:", vida_enemigo, ")")
        print("Pociones:", pociones)

        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        # Ataque Pesado
        if opcion == "1":

            if vida_enemigo < 20:
                dano = ataque_pesado * 1.5
                print("¡Golpe Crítico!")

            else:
                dano = float(ataque_pesado)

            vida_enemigo -= dano

            print("¡Atacaste al enemigo por", dano, "puntos de daño!")

        # Ráfaga Veloz
        elif opcion == "2":

            print(">> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # Curar
        elif opcion == "3":

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te curaste 30 puntos de vida!")

            else:
                print("¡No quedan pociones!")

        # Cambiar turno
        turno_gladiador = False

    # Turno del enemigo
    else:

        vida_jugador -= danio_enemigo

        print("¡El enemigo te atacó por 12 puntos de daño!")

        turno_gladiador = True


# Fin del juego
if vida_jugador > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla.")

else:
    print("DERROTA. Has caído en combate.")

