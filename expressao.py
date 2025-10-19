class Expressão():
    def __init__(self, A:int,B: int,C:int):
        self.A = A
        self.B = B
        self.C = C

    def expressao(self):
        if self.B > 0: 
            return f'{self.A}x^2+{self.B}x+{self.C}'
        elif self.B < 0:
            return f'{self.A}x^2-{abs(self.B)}x+{self.C}'

    def calcular_delta(self):
        delta  = (self.B**2) -(4 * self.A * self.C)
        return delta 