class Nodo:
    def __init__(self, valor: str, prioridad: int):
        self.valor = valor
        self.prioridad = prioridad
        self.siguiente = None


class ColaPrioridad:
    def __init__(self):
        self.frente = None
        self.length = 0

    def enqueue(self, valor: str, prioridad: int):
        nuevo = Nodo(valor, prioridad)
        if self.is_empty() or prioridad > self.frente.prioridad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente and actual.siguiente.prioridad >= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self.length += 1
        return nuevo

    def dequeue(self):
        if self.is_empty():
            print("⚠️ Cola vacía")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        self.length -= 1
        return valor

    def is_empty(self):
        return self.frente is None

    def size(self):
        return self.length

    def __iter__(self):
        actual = self.frente
        while actual:
            yield actual.valor, actual.prioridad
            actual = actual.siguiente
