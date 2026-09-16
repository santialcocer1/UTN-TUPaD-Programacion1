usuario_correcto = "alumno"
clave_correcta  = "python123"

intentos = 0
acceso = False

while intentos > 3:
    usuario = input(f"{intentos + 1}/3. Usuario:  ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso permitido.")
        acceso = True
        break
    else:
        print("Credenciales invalidas.")
        intentos += 1

if acceso == False:
    print("Cuenta bloqueada.")
else: 
    opcion = ""
    while opcion != "4":

        print("1) Estado   2) Cambiar clave    3) Mensaje   4) Salir")
        opcion = input("Opcion: ")
        if not opcion.isdigit():
            print("Error: ingrese un numero valido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opcion fuera de rango.")
        elif opcion == "1":
            print("Estado: Inscripto.")
        elif opcion == "2":
            nueva_clave = input("Ingresar nueva clave: ")
            if len(nueva_clave) < 6:
                print("Ingresar clave con minimo 6 caracteres: ")
            else: 
                confirmacion = input("Confirmar nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta == nueva_clave
                    print("Clave cambiada correctamente.")
                else: 
                    print("Claves no coinciden.")
        elif opcion == "3":
            print("Segui adelante, estas haciendo un gran trabajo.")
        elif opcion == "4":
            print("Sesion finalizada.")