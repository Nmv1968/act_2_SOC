class Nodo:
    def __init__(self, valor: str):
        self.valor = valor
        self.siguiente = None


class ColaSimple:
    def __init__(self):
        self.frente = None
        self.final = None
        self.length = 0

    def is_empty(self):
        return self.frente is None

    def enqueue(self, valor: str):
        nuevo = Nodo(valor)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if self.frente is None:
            self.frente = nuevo
        self.length += 1
        return valor

    def dequeue(self):
        if self.is_empty():
            print("⚠️ Underflow: cola vacía.")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.length -= 1
        return valor

    def front(self):
        return None if self.is_empty() else self.frente.valor

    def size(self):
        return self.length

    def __iter__(self):
        actual = self.frente
        while actual:
            yield actual.valor
            actual = actual.siguiente
