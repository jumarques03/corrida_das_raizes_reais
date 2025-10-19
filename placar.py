from expressao import Expressão

class Placar(Expressão):
    def __init__(self, A, B, C):
        super().__init__(A, B, C)
        self.pontos_jogador = 0
        self.pontos_sistema = 0

    def atribuir_ponto(self):
        if self.calcular_delta() > 0:
            self.pontos_jogador += 1
            return {"mensagem": "Ponto atribuido à você"}
        else:
            self.pontos_sistema += 1
            return {"mensagem": "Ponto atribuido ao sistema"}

    def mostrar_placar(self):
        return f"Pontos Jogador: {self.pontos_jogador} | Pontos Sistema: {self.pontos_sistema}"
    
    def mostrar_resultado_final(self):
        print("\n--- RESULTADO FINAL ---")
        print(f"Você: {self.pontos_jogador} ponto(s)")
        print(f"Sistema: {self.pontos_sistema} ponto(s)")

        if self.pontos_jogador > self.pontos_sistema:
            print("Parabéns! Você venceu a Corrida das Raízes Reais!")
        elif self.pontos_jogador < self.pontos_sistema:
            print("\nO sistema venceu! Mais sorte na próxima!")
        else:
            print("\nEmpate! Foi uma disputa equilibrada!")
        print("--------------------------------------\n")