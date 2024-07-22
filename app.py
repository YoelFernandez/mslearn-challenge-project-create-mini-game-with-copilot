import random
print("Bienvenido al juego de Piedra, Papel o Tijera")
opciones = ["piedra", "papel", "tijera"]
while True:
    generado_maquina = random.randint(0, 2)
    eleccion_maquina = opciones[generado_maquina]

    # Solicitar la entrada del usuario y convertirla a minúsculas
    eleccion_usuario = input("Ingrese una opción (piedra, papel, tijera) o 'salir' para terminar: ").lower()

    # Verificar si el usuario quiere salir del juego
    if eleccion_usuario == "salir":
        print("Gracias por jugar. ¡Hasta luego!")
        break

    # Verificar si la opción ingresada es válida
    if eleccion_usuario not in opciones:
        print("Opción no válida. Inténtelo de nuevo.")
        continue

    print(f"Tú elegiste: {eleccion_usuario}")
    print(f"La máquina eligió: {eleccion_maquina}")

    # Determinar el ganador
    if eleccion_usuario == eleccion_maquina:
        print("¡Es un empate!")
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_maquina == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

    print()
