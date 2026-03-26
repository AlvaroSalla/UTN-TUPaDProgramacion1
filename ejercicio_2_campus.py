# Trabajo Practico Estructuras Repetitivas
# Alvaro Salla

# # # EJERCICIO 2 # # # 
# # # Acceso al Campus y Menú Seguro # # # 
# # # Login con intentos + menú de acciones con validación estricta # # #

usuario_correcto = "alumno"
contraseña_correcta = "python123"
acceso_permitido = False
intentos = 3

while intentos >= 1:
    print(f"Intento {intentos}/3")
    usuario_ingresado = input("Ingrese su usuario: ")
    contraseña_ingresada = input("Ingrese su contraseña: ")
    
    if usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_correcta:
        print("Acceso Permitido!")
        acceso_permitido = True
        break
    elif usuario_ingresado != usuario_correcto or contraseña_ingresada != contraseña_correcta:
        intentos -= 1
        if intentos == 0:
            print("Cuenta Bloqueada")
        else:
            print("Credenciales incorrectas, intete nuevamente")

while acceso_permitido:
    print("----------------------------")
    print("MENU PRINCIPAL")
    print("----------------------------")
    print("1) Ver estado de inscripcion \n" \
    "2) Cambiar clave \n" \
    "3) Mensaje motivacional \n" \
    "4) Salir")

    opcion = input("Ingrese una opcion: ")

    while not opcion.isdigit():
        print("Error! Debe ingresar un numero entero positivo")
        opcion = input("Ingrese una opcion: ")
    
    opcion = int(opcion)

    match opcion:
        case 1: 
            print("Estado: Inscripto")
        case 2:
            contraseña_nueva = input("Ingrese su nueva contraseña (Minimo 6 caracteres): ")
            if len(contraseña_nueva) < 6:
                print("Error! La contraseña debe tener como minimo 6 caracteres")
                continue

            confirmar_contraseña = input("Repita su nueva contraseña: ")

            if contraseña_nueva != confirmar_contraseña:
                print("Error! La contraseña no coiciden")
            else:
                print("Contraseña cambiada correctamente!")
                contraseña_correcta = contraseña_nueva
        case 3: 
            print("El éxito es la suma de pequeños esfuerzos repetidos día tras día")
        case 4:
            print("Saliendo...")
            acceso_permitido = False
        case _:
            print("Opcion invalida")