class VLP:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def production(self, q):
        return self.a * q ** 2 + self.b
