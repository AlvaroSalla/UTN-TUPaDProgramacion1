# Trabajo Practico Estructuras Repetitivas
# Alvaro Salla

# # # EJERCICIO 3 # # #
# # # Agenda de Turnos con Nombres (Sin Listas) # # #
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

nombre_operador = input("Ingrese su nombre: ")
nombre_operador = nombre_operador.title()
cerrar_sist = 0

while not nombre_operador.replace(" ", "").isalpha():
    nombre_operador = input("Porfavor, ingrese un nombre valido: ")
    nombre_operador = nombre_operador.title()

while cerrar_sist != 5:
    print("---------------------")
    print("MENU PRINCIPAL")
    print("---------------------")
    print("1) Reservar turno \n" \
    "2) Cancelar turno \n" \
    "3) Ver agenda del dia \n" \
    "4) Ver resumen semanal \n" \
    "5) Cerrar sistema")

    opcion = input("Ingrese una opcion: ")

    while not opcion.isdigit():
        print("Error! Debe ingresar un numero entero positivo")
        opcion = input("Ingrese una opcion: ")
    
    opcion = int(opcion)

    match opcion:
        case 1:
            while True:
                dia_turno = input("1) Lunes\n2) Martes\n")

                if not dia_turno.isdigit():
                    print("Error! Debe ingresar un número entero positivo")
                    continue

                dia_turno = int(dia_turno)

                if dia_turno == 1 or dia_turno == 2:
                    break
                else:
                    print("Por favor, seleccione una opción válida")

            nombre_paciente = input("Por favor ingrese el nombre del paciente a registrar: ")
            while not nombre_paciente.replace(" ", "").isalpha():
                nombre_paciente = input("Porfavor, ingrese un nombre valido: ")
                nombre_paciente = nombre_paciente.title()

            if dia_turno == 1:

                if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                    print("Ese paciente ya tiene un turno en este día")
                else:
                    if lunes1 == "":
                        lunes1 = nombre_paciente
                        print("Paciente registrado correctamente!")
                    elif lunes2 == "":
                        lunes2 = nombre_paciente
                        print("Paciente registrado correctamente!")
                    elif lunes3 == "":
                        lunes3 = nombre_paciente
                        print("Paciente registrado correctamente!")
                    elif lunes4 == "":
                        lunes4 = nombre_paciente
                        print("Paciente registrado correctamente!")
                    else:
                        print("Todos los turnos para este día están ocupados")
                
            elif dia_turno == 2:

                if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                    print("Ese paciente ya tiene un turno en este día")
                else:
                    if martes1 == "":
                        martes1 = nombre_paciente
                        print("Paciente registrado correctamente!")
                    elif martes2 == "":
                        martes2 = nombre_paciente
                        print("Paciente registrado correctamente!")
                    elif martes3 == "":
                        martes3 = nombre_paciente
                        print("Paciente registrado correctamente!")

        case 2:
            while True:
                dia_cancelar = input("Elija el dia \n1) Lunes\n2) Martes\n")

                if not dia_cancelar.isdigit():
                    print("Error! Debe ingresar un número entero positivo")
                    continue

                dia_cancelar = int(dia_cancelar)

                if dia_cancelar == 1 or dia_cancelar == 2:
                    break
                else:
                    print("Por favor, seleccione una opción válida")

            nombre_paciente = input("Por favor ingrese el nombre del paciente: ")

            while not nombre_paciente.replace(" ", "").isalpha():
                nombre_paciente = input("Porfavor, ingrese un nombre valido: ")
                nombre_paciente = nombre_paciente.title()

            if dia_cancelar == 1:

                if lunes1 != nombre_paciente and lunes2 != nombre_paciente and lunes3 != nombre_paciente and lunes4 != nombre_paciente:
                    print("El paciente no se encuentra registrado para este dia.")
                else:
                    if lunes1 == nombre_paciente:
                        lunes1 = ""
                    elif lunes2 == nombre_paciente:
                        lunes2 = ""
                    elif lunes3 == nombre_paciente:
                        lunes3 = ""
                    elif lunes4 == nombre_paciente:
                        lunes4 = ""

                    print("Turno cancelado!")      

            
            elif dia_cancelar == 2:

                if martes1 != nombre_paciente and martes2 != nombre_paciente and martes3 != nombre_paciente:
                    print("El paciente no se encuentra registrado para este dia.")
                else:
                    if martes1 == nombre_paciente:
                        martes1 = ""
                    elif martes2 == nombre_paciente:
                        martes2 = ""
                    elif martes3 == nombre_paciente:
                        martes3 = ""

                    print("Turno cancelado!")                
        
        case 3:
            if lunes1 == "":
                print("Lunes 1: Libre")
            else:
                print("Lunes 1: Ocupado")
            
            if lunes2 == "":
                print("Lunes 2: Libre")
            else:
                print("Lunes 2: Ocupado")

            if lunes3 == "":
                print("Lunes 3: Libre")
            else:
                print("Lunes 3: Ocupado")
            
            if lunes4 == "":
                print("Lunes 4: Libre")
            else:
                print("Lunes 4: Ocupado")

            if martes1 == "":
                print("Martes 1: Libre")
            else:
                print("Martes 1: Ocupado")
            if martes2 == "":
                print("Martes 2: Libre")
            else:
                print("Martes 2: Ocupado")
            if martes3 == "":
                print("Martes 3: Libre")
            else:
                print("Martes 3: Ocupado")

        case 4:
            turnos_lunes_libres = 0
            turnos_lunes_ocupados = 0
            turnos_martes_libres = 0
            turnos_martes_ocupados = 0
            if lunes1 != "":
                turnos_lunes_ocupados += 1
            else:
                turnos_lunes_libres += 1
            if lunes2 != "":
                turnos_lunes_ocupados += 1
            else:
                turnos_lunes_libres += 1
            if lunes3 != "":
                turnos_lunes_ocupados += 1
            else:
                turnos_lunes_libres += 1
            if lunes4 != "":
                turnos_lunes_ocupados += 1
            else:
                turnos_lunes_libres += 1
            
            if martes1 != "":
                turnos_martes_ocupados += 1
            else:
                turnos_martes_libres += 1
            if martes2 != "":
                turnos_martes_ocupados += 1
            else:
                turnos_martes_libres += 1
            if martes3 != "":
                turnos_martes_ocupados += 1
            else:
                turnos_martes_libres += 1
            
            print(f"El lunes hay {turnos_lunes_libres} turnos libres, y hay {turnos_lunes_ocupados} turnos ocupados")
            print(f"El martes hay {turnos_martes_libres} turnos libres, y hay {turnos_martes_ocupados} turnos ocupados")

            if turnos_lunes_ocupados > turnos_martes_ocupados:
                print("El dia con mas turnos es el lunes")
            elif turnos_lunes_ocupados < turnos_martes_ocupados:
                print("El dia con mas turnos es el martes")
            else:
                print("Los dos dias tienen la misma cantidad de turnos")

        case 5:
            cerrar_sist = 5
            print("Saliendo...")
        case _:
            print("Ingrese una opcion dentro del rango (1-5)")