# Trabajo Practico Estructuras Repetitivas
# Alvaro Salla

# # # EJERCICIO 4 # # #
# # # Escape Room: La Bóveda # # #

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
alarma_bloqueo = False
codigo_parcial = ""
forzar_seguidas = 0

nombre_agente = input("Ingrese el nombre del agente: ")
nombre_agente = nombre_agente.title()

while not nombre_agente.replace(" ", "").isalpha():
    nombre_agente = input("Ingrese un nombre valido: ")
    nombre_agente = nombre_agente.title()

while (energia > 0 and tiempo > 0 and cerraduras_abiertas < 3) and alarma_bloqueo == False:
    if alarma == True and tiempo <= 3:
        alarma_bloqueo = True
        break
    print("----------------")
    print("INFO")
    print("----------------")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Veces cerradura forzada: {forzar_seguidas}, si la fuerzas 3 veces seguidas se activa la alarma")
    print(f"Codigo parcial: {codigo_parcial}")
    print("----------------")
    print("MENU")
    print("----------------")
    print("1) Forzar cerradura (-20 energia, -2 tiempo)\n" \
    "2) Hacker panel (-10 energia, -3 tiempo)\n" \
    "3) Descansar (+15 energia (100 max), -1 Tiempo, Si alarma ON: -10 Energia)")
    print("----------------")

    opcion = input("Ingrese una opcion: ")
    
    while not opcion.isdigit():
        print("Error! Debe ingresar un numero entero positivo")
        opcion = input("Ingrese una opcion: ")
    
    opcion = int(opcion)

    match opcion:
        case 1: 
            tiempo -= 2
            energia -= 20
            forzar_seguidas += 1
            if forzar_seguidas >= 3:
                alarma = True
                print("Activate la alarma!!!")
                continue
            if energia >= 40:
                cerraduras_abiertas += 1
                print("Se restaron 20 de energia!")
                print("Se resto 3 de tiempo!")
                print("Se abrio una cerradura con exito!")
            elif alarma:
                print("No se ha abierto la cerradura porque la alarma esta activada")
            elif energia < 40 and alarma == False: 
                print("Hay riesgo de activar la alarma!")
                opcion_alarma = input("Elije un numero entre 1 y 3: ")
                while not opcion_alarma.isdigit():
                    opcion_alarma = input("Elije un numero entre 1 y 3: ")
                opcion_alarma = int(opcion_alarma)
                match opcion_alarma:
                        case 1:
                            cerraduras_abiertas += 1
                            print("Se abrio una cerradura con exito")
                        case 2: 
                            cerraduras_abiertas += 1
                            print("Se abrio una cerradura con exito")
                        case 3:
                            alarma = True
                            print("Activate la alarma!!!")
                            continue
                        case _:
                            print("Elija un numero entre 1 y 3")
        case 2:
            energia -= 10
            tiempo -= 3
            forzar_seguidas = 0

            for i in range(4):
                codigo_parcial += "A"

            print("Hackeando panel...")
            print(f"Codigo actual: {codigo_parcial}")
            
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
                codigo_parcial = ""
                print("Cerradura abierta!")
            else: 
                print("La cerradura todavia no se abre!, prueba nuevamente")
        
        case 3:
            tiempo -= 1 
            forzar_seguidas = 0
            print("Descansando...")

            if alarma:
                print("Descansaste con la alarma activada, -10 de energia")
                energia -= 10
            else:
                print("Recuperaste 15 de energia!")
                energia += 15

            if energia >= 100:
                energia = 100 
                print("Llegaste al limite de energia! (100)")
        case _:
            print("ERROR! Opcion fuera de rango")

if cerraduras_abiertas == 3:
    print("GANASTE!!")
elif alarma_bloqueo:
    print("GAME OVER: La alarma bloqueo el sistema!")
elif energia <= 0:
    print("GAME OVER: Te quedaste sin energia!")
elif tiempo <= 0:
    print("GAME OVER: Te quedaste sin tiempo!")