# Trabajo Practico Estructuras Repetitivas
# Alvaro Salla

# # # EJERCICIO 5 # # #
# # # Escape Room: La Arena del Gladiador # # #

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_base_ataque_pesado = 15
daño_base_enemigo = 12
turno_gladiador = True

nombre_gladiador = input("Ingrese el nombre del gladiador: ")
nombre_gladiador = nombre_gladiador.title()

while not nombre_gladiador.replace(" ","").isalpha():
    print("ERROR! solo se permiten letras")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")
    nombre_gladiador = nombre_gladiador.title()

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    turno_gladiador = True
    print("=== NUEVO TURNO ===")
    print(f"{nombre_gladiador} ({vida_gladiador} HP) vs Enemigo ({vida_enemigo} HP) -- Pociones: {pociones_vida}")
    print("Elige acción")
    print("1) Ataque Pesado \n"
        "2) Rafaga Veloz \n" \
        "3) Curar")
    
    opcion = input("Opcion: ")

    while not opcion.isdigit():
        print("Error!, debe ingresar una de la acciones posibles")
        opcion = input("Opcion: ")
    
    opcion = int(opcion)

    match opcion:
        case 1:
            if vida_enemigo >= 20:
                vida_enemigo -= daño_base_ataque_pesado
                print("Haces un ataque pesado!")
                print(f"Atacaste al enemigo por {daño_base_ataque_pesado} puntos de daño!")
            elif vida_enemigo < 20:
                daño_critico_ataque_pesado = daño_base_ataque_pesado * 1.5
                daño_critico_ataque_pesado = float(daño_critico_ataque_pesado)
                vida_enemigo -= daño_critico_ataque_pesado
                print("Haces un ataque pesado!")
                print("GOLPE CRITICO!!!")
                print(f"Atacaste a tu enemigo por {daño_critico_ataque_pesado} punto de daño!")

            turno_gladiador = False

            if turno_gladiador == False and vida_enemigo > 0:
                print("El enemigo contraataca con 12 puntos de daño!")
                vida_gladiador -= 12
        case 2:
            
            print("Haces una rafaga de golpes!")
            for i in range(3):
                print("Golpe conectado por 5 puntos de daño!")
                vida_enemigo -= 5

            turno_gladiador = False

            if turno_gladiador == False and vida_enemigo > 0:
                print("El enemigo contraataca con 12 puntos de daño!")
                vida_gladiador -= 12
            
        case 3:
            
            if pociones_vida > 0:
                print("Tomando pocion...")
                print("Recuperaste 30 HP!")
                pociones_vida -= 1
                vida_gladiador += 30
            else:
                print("No quedan mas pociones!")
                turno_gladiador = False

                if turno_gladiador == False and vida_enemigo > 0:
                    print("El enemigo contraataca con 12 puntos de daño!")
                    vida_gladiador -= 12
        case _:
            print("Opcion fuera de rango!")

if vida_gladiador > 0:
    print(f"VICTORIA! {nombre_gladiador} ha ganado el combate!")
elif vida_gladiador <= 0:
    print(f"DERROTA! Has caido en combate")