from cola_simple import ColaSimple
from cola_prioridad import ColaPrioridad


def socMenu():
    cola_simple = ColaSimple()
    cola_prioridad = ColaPrioridad()
    while True:
        print("\n--- Centro de Operaciones de Seguridad (SOC) ---")
        print("1. Registrar alerta normal")
        print("2. Registrar alerta crítica")
        print("3. Atender siguiente alerta")
        print("4. Mostrar estado de colas")
        print("5. Salir")
        print("\n --------------------")
        opcion = validar_input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("\n--- Registrar alerta normal ---")
                print(registrar_alerta("normal", cola_simple, cola_prioridad))
            case "2":
                print("\n--- Registrar alerta crítica ---")
                print(registrar_alerta("critica", cola_simple, cola_prioridad))
            case "3":
                print("\n--- Atender siguiente alerta ---")
                print(atender_siguiente_alerta(cola_simple, cola_prioridad))
            case "4":
                print("\n--- Estado de las colas ---")
                print(
                    f"Cola de alertas normales ({cola_simple.size()}): {[valor for valor in cola_simple]}"
                )
                print(
                    f"Cola de alertas críticas ({cola_prioridad.size()}): {[f'{valor} (P{prioridad})' for valor, prioridad in cola_prioridad]}"
                )
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


def validar_input(texto: str) -> str:
    while True:
        valor = input(texto)
        if valor.strip():
            return valor
        print("Entrada no válida. Por favor, ingrese un valor no vacío.")


def registrar_alerta(
    tipo: str, cola_simple: ColaSimple, cola_prioridad: ColaPrioridad
) -> str:
    match tipo:
        case "normal":
            return registrar_alerta_normal(cola_simple)
        case "critica":
            return registrar_alerta_critica(cola_prioridad)

    return "Tipo de alerta no reconocido."


def registrar_alerta_normal(cola_simple: ColaSimple) -> str:
    alerta = validar_input("Ingrese la descripción de la alerta 🔈: ")
    cola_simple.enqueue(alerta)
    return "↳ ENQUEUE alerta normal: " + alerta


def registrar_alerta_critica(cola_prioridad: ColaPrioridad) -> str:
    alerta = validar_input("Ingrese la descripción de la alerta 🔈: ")
    prioridad = validar_rango_prioridad("Ingrese la prioridad de la alerta (1-5): ")
    cola_prioridad.enqueue(alerta, prioridad)
    return "↳ ENQUEUE alerta crítica: " + alerta


def atender_siguiente_alerta(
    cola_simple: ColaSimple, cola_prioridad: ColaPrioridad
) -> str:
    if not cola_prioridad.is_empty():
        return f"Atendiendo alerta crítica: {cola_prioridad.dequeue()}"
    elif not cola_simple.is_empty():
        return f"Atendiendo alerta normal: {cola_simple.dequeue()}"
    else:
        return "No hay alertas para atender."


def validar_rango_prioridad(prioridad: str) -> int:
    while True:
        valor_prioridad = int(validar_input(prioridad))
        if 1 <= valor_prioridad <= 5:
            break
        print("Prioridad no válida. Ingrese un valor entre 1 y 5.")
    return valor_prioridad


def main():
    socMenu()


if __name__ == "__main__":
    main()
