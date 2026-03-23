# Ejercicio 1 - "Caja del Kiosco"

print(f"Ejercicio 1")

# Validación del nombre
nombre = ""
while not nombre.isalpha():
    nombre = input("Cliente: ")

# Validación de cantidad
cantidad = 0
while True:
    cant_str = input("Cantidad de productos a comprar: ")
    if cant_str.isdigit() and int(cant_str) > 0:
        cantidad = int(cant_str)
        break
    else:
        print ("Error: Por favor ingrese un número positivo.")

total_sin_desc = 0
total_con_desc = 0

# Iteración por producto
for i in range(1, cantidad + 1):
    print(f"\nProducto {i}")

    precio_str = ""
    while not precio_str.isdigit():
        precio_str = input("Precio: ")
    precio = int(precio_str)

    desc_str = ""
    while desc_str not in ["s", "n"]:
        desc_str = input("Descuento (S/N): ").lower()

    total_sin_desc += precio
    if desc_str == "s":
        total_con_desc += precio * 0.90
    else:
        total_con_desc += precio

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print("\n--- TICKET ---")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2  — “Acceso al Campus y Menú Seguro” 

print(f"Ejercicio 2")

intentos = 0
ingreso_exitoso = False

# Login
while intentos < 3:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == "alumno" and clave == "python123":
        print("Acceso concedido.\n")
        ingreso_exitoso = True
        break
    else:
        print("Error: credenciales inválidas.\n")

if not ingreso_exitoso:
    print("Cuenta bloqueada.")
else:
    # Menú principal
    while True:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            continue
    
        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: Opción fuera de rango.")
        elif opcion == 1:
            print("Estado: Inscripto.")
        elif opcion == 2:
            nueva_clave = input("Nueva Clave: ")
        elif opcion == 3:
            print("¡Sigue programando, vas por buen camino!")
        elif opcion == 4:
            print("Saliendo del sistema...")
            break


# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

print(f"Ejercicio 3")

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

operador = ""
while not operador.isalpha():
    operador = input("Nombre del operador: ")

while True:
    print("\n--- MENÚ AGENDA ---")
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen\n5. Salir")
    opcion = input("Opción: ")
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Opción inválida.")
        continue
    opcion = int(opcion)
    
    if opcion == 5:
        break
        
    elif opcion == 1 or opcion == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia not in ["1", "2"]:
            print("Día inválido.")
            continue
            
        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")
            
        if opcion == 1: # Reservar
            if dia == "1":
                if paciente in [lunes1, lunes2, lunes3, lunes4]:
                    print("Paciente ya tiene turno el Lunes.")
                elif lunes1 == "": lunes1 = paciente; print("Turno Lunes 1 asignado.")
                elif lunes2 == "": lunes2 = paciente; print("Turno Lunes 2 asignado.")
                elif lunes3 == "": lunes3 = paciente; print("Turno Lunes 3 asignado.")
                elif lunes4 == "": lunes4 = paciente; print("Turno Lunes 4 asignado.")
                else: print("No hay cupos el Lunes.")
            elif dia == "2":
                if paciente in [martes1, martes2, martes3]:
                    print("Paciente ya tiene turno el Martes.")
                elif martes1 == "": martes1 = paciente; print("Turno Martes 1 asignado.")
                elif martes2 == "": martes2 = paciente; print("Turno Martes 2 asignado.")
                elif martes3 == "": martes3 = paciente; print("Turno Martes 3 asignado.")
                else: print("No hay cupos el Martes.")
                
        elif opcion == 2: # Cancelar
            cancelado = False
            if dia == "1":
                if lunes1 == paciente: lunes1 = ""; cancelado = True
                elif lunes2 == paciente: lunes2 = ""; cancelado = True
                elif lunes3 == paciente: lunes3 = ""; cancelado = True
                elif lunes4 == paciente: lunes4 = ""; cancelado = True
            elif dia == "2":
                if martes1 == paciente: martes1 = ""; cancelado = True
                elif martes2 == paciente: martes2 = ""; cancelado = True
                elif martes3 == paciente: martes3 = ""; cancelado = True
            print("Turno cancelado." if cancelado else "Paciente no encontrado.")
            
    elif opcion == 3: # Ver agenda
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Lunes - T1: {lunes1 or '(libre)'}, T2: {lunes2 or '(libre)'}, T3: {lunes3 or '(libre)'}, T4: {lunes4 or '(libre)'}")
        elif dia == "2":
            print(f"Martes - T1: {martes1 or '(libre)'}, T2: {martes2 or '(libre)'}, T3: {martes3 or '(libre)'}")
            
    elif opcion == 4: # Resumen
        ocup_lunes = sum(1 for t in [lunes1, lunes2, lunes3, lunes4] if t != "")
        ocup_martes = sum(1 for t in [martes1, martes2, martes3] if t != "")
        print(f"Lunes: {ocup_lunes} ocupados, {4-ocup_lunes} libres.")
        print(f"Martes: {ocup_martes} ocupados, {3-ocup_martes} libres.")
        if ocup_lunes > ocup_martes: print("El Lunes tiene más turnos.")
        elif ocup_martes > ocup_lunes: print("El Martes tiene más turnos.")
        else: print("Ambos días tienen la misma cantidad de turnos.")


# Ejercicio 4  — “Escape Room: La Bóveda”

print(f"Ejercicio 4")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
spam_forzar = 0

agente = ""
while not agente.isalpha():
    agente = input("Nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\nEstado - Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("1. Forzar cerradura\n2. Hackear panel\n3. Descansar")
    
    opcion = input("Opción: ")
    if not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Opción inválida.")
        continue
    opcion = int(opcion)
    
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        spam_forzar += 1
        
        if spam_forzar == 3:
            print("¡La cerradura se trabó! Alarma activada.")
            alarma = True
        else:
            if energia < 40 and not alarma:
                azar = input("Riesgo de alarma. Ingrese número 1-3: ")
                if azar == "3":
                    print("¡Alarma activada!")
                    alarma = True
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")
                
    elif opcion == 2:
        spam_forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for _ in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado! Cerradura abierta.")
            codigo_parcial = "" # Reinicia para la próxima
            
    elif opcion == 3:
        spam_forzar = 0
        tiempo -= 1
        energia += 15
        if energia > 100: energia = 100
        if alarma: energia -= 10
        print("Descansaste.")

if cerraduras_abiertas == 3:
    print(f"\n¡VICTORIA! {agente} ha escapado con la bóveda abierta.")
else:
    print(f"\nDERROTA. {agente} ha fallado la misión.")


# Ejercicio 5  — “Escape Room:"La Arena del Gladiador"

print(f"Ejercicio 5")

# Estadísticas iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_jugador = True

print("=== BIENVENIDO A LA ARENA ===")
nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = input("Opción: ")
    if not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido.")
        continue
    opcion = int(opcion)
    
    if opcion == 1:
        dano_final = float(ataque_pesado)
        if vida_enemigo < 20:
            dano_final *= 1.5
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {int(dano_final)} puntos de daño!")
        
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("¡Te curaste 30 puntos de vida!")
        else:
            print("¡No quedan pociones! Pierdes el turno.")
            
    # Contraataque del enemigo (si sigue vivo)
    if vida_enemigo > 0:
        print("\n>> ¡El enemigo contraataca!")
        vida_jugador -= ataque_enemigo
        print(f"¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")

# Fin del juego
print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")