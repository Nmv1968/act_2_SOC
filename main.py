# =============================================================================
# MODULO PRINCIPAL: Centro de Operaciones de Seguridad (SOC)
# Coordina el uso de ColaSimple y ColaPrioridad para gestionar alertas.
# =============================================================================
from cola_simple import ColaSimple
from cola_prioridad import ColaPrioridad

# =============================================================================
# socMenu: Menu interactivo por consola para el usuario.
# Permite registrar diferentes tipos de alertas y visualizarlas, ademas de atenderlas.
# =============================================================================
def socMenu():
    # Inicializa las colas de alertas normales y críticas.
    cola_simple = ColaSimple()
    cola_prioridad = ColaPrioridad()
    # Bucle principal del menú de operaciones
    while True:
        print("\n=== 🚨 Centro de Operaciones de Seguridad (SOC) 🚨 ===")
        print("1. Registrar alerta normal 🔈")
        print("2. Registrar alerta crítica 🚨")
        print("3. Atender siguiente alerta 📡")
        print("4. Mostrar estado de colas 📊")
        print("5. Salir 🚪")
        print("\n ========================================")
        opcion = validar_input("Seleccione una opción: ")

        # Estructura de control para manejar las opciones del menú
        match opcion:
            case "1":
                print("\n=== Registrar alerta normal ===")
                print(registrar_alerta("normal", cola_simple, cola_prioridad))
            case "2":
                print("\n=== Registrar alerta crítica ===")
                print(registrar_alerta("critica", cola_simple, cola_prioridad))
            case "3":
                print("\n=== Atender siguiente alerta ===")
                print(atender_siguiente_alerta(cola_simple, cola_prioridad))
            case "4":
                print("\n=== Estado de las colas ===")
                print(
                    f"Cola de alertas normales 🔈 ({cola_simple.size()}): {[valor for valor in cola_simple]}"
                )
                print(
                    f"Cola de alertas críticas 🚨 ({cola_prioridad.size()}): {[f'{valor} (P{prioridad})' for valor, prioridad in cola_prioridad]}"
                )
            case "5":
                print("Saliendo...🚪")
                break
            case _:
                print("Opción no válida. Intente nuevamente. ⛔")

# Valida que la entrada de texto no esté vacía
def validar_input(texto: str) -> str:
    # Bucle que solicita entrada hasta que sea válida
    while True:
        valor = input(texto)
        if valor.strip():
            return valor
        print("Entrada no válida. Por favor, ingrese un valor no vacío. ⛔")

# Orquestador para el registro de alertas por tipo
def registrar_alerta(
    tipo: str, cola_simple: ColaSimple, cola_prioridad: ColaPrioridad
) -> str:
    # Estructura de control para manejar las opciones del menú de registro de alertas
    match tipo:
        case "normal":
            return registrar_alerta_normal(cola_simple)
        case "critica":
            return registrar_alerta_critica(cola_prioridad)

    return "Tipo de alerta no reconocido. ⛔"

# Encola alertas con lógica FIFO (Cola Simple)
def registrar_alerta_normal(cola_simple: ColaSimple) -> str:
    # Solicita la descripción de la alerta y la encola
    alerta = validar_input("Ingrese la descripción de la alerta 🔈: ")
    cola_simple.enqueue(alerta)
    return "↳ ENQUEUE alerta normal: " + alerta + " 🔈"

# Encola alertas con lógica de prioridad
def registrar_alerta_critica(cola_prioridad: ColaPrioridad) -> str:
    # Solicita la descripción de la alerta y la encola
    alerta = validar_input("Ingrese la descripción de la alerta 🚨: ")
    prioridad = validar_rango_prioridad("Ingrese la prioridad de la alerta (1-5): ")
    cola_prioridad.enqueue(alerta, prioridad)
    return "↳ ENQUEUE alerta crítica: " + alerta + " 🚨"

# Lógica de atención: Prioriza siempre la cola de alertas críticas
def atender_siguiente_alerta(
    cola_simple: ColaSimple, cola_prioridad: ColaPrioridad
) -> str:
    # Primero se revisa si hay algo urgente (Cola de Prioridad)
    if not cola_prioridad.is_empty():
        valor, prioridad = cola_prioridad.dequeue()
        return f"Atendiendo alerta crítica: {valor} (P{prioridad}) 🚨"
    # Si no hay urgencias, se atiende la cola normal (FIFO)
    elif not cola_simple.is_empty():
        return f"Atendiendo alerta normal: {cola_simple.dequeue()} 🔈"
    else:
        return "No hay alertas para atender. ⛔"

# Asegura que la prioridad esté dentro de los parámetros permitidos
def validar_rango_prioridad(prioridad: str) -> int:
    # Bucle que solicita prioridad hasta que sea válida
    while True:
        try:
            valor_prioridad = int(validar_input(prioridad))
            # Valida que la prioridad esté dentro del rango permitido
            if 1 <= valor_prioridad <= 5:
                break
            print("Prioridad no válida ⛔. Ingrese un valor entre 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número entero. ⛔")
    return valor_prioridad

# Función principal que inicia el menú de operaciones
def main():
    socMenu()

# Punto de entrada del programa
if __name__ == "__main__":
    main()

