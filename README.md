# Centro de Operaciones de Seguridad (SOC)

Mini proyecto en Python que gestiona alertas usando dos tipos de colas:

- `ColaSimple` para alertas normales (FIFO).
- `ColaPrioridad` para alertas críticas con prioridad de 1 a 5.

## Estructura del proyecto

- `main.py`: módulo principal con menú interactivo de consola.
- `cola_simple.py`: implementación de una cola simple basada en nodos.
- `cola_prioridad.py`: implementación de una cola de prioridad basada en nodos.

## Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto.

2. Ejecuta el programa:
   ```bash
   python main.py
   ```

## Funcionalidad

- Registrar alertas normales.
- Registrar alertas críticas con prioridad.
- Atender la siguiente alerta, dando preferencia a las alertas críticas.
- Ver el estado actual de las colas.

## Requisitos

- Python 3.x

## Notas

- Las alertas críticas se atienden antes que las alertas normales.
- La prioridad más alta es 5 y la más baja es 1.
