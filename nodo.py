# =============================================================================
# Clase Nodo: Representa la unidad básica de la estructura.
# Contiene el valor almacenado, una prioridad opcional y el puntero al siguiente nodo.
# =============================================================================
class Nodo:
    def __init__(self, valor: str, prioridad: int = None):
        self.valor = valor
        self.prioridad = prioridad
        self.siguiente = None
