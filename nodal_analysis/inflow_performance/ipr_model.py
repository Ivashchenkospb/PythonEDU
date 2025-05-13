class IPR:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def production(self, q):
        return self.b - self.a * q