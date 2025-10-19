import random
from expressao import Expressão
from placar import Placar

def main():
    sair = "não"
    placar = Placar(0, 0, 0)

    print("\n--- Corrida das Raízes Reais ---\n")

    print("Objetivo do Jogo:\nSeu desafio é montar uma equação do 2º grau da forma Ax^2 + Bx + C = 0, escolhendo estrategicamente os coeficientes A e B. O coeficiente C será sorteado automaticamente pelo sistema, com um valor entre 1 e 1000.\n\nComo vencer:\nVocê vence a rodada se a equação gerada tiver duas raízes reais diferentes. Caso contrário, o ponto vai para o computador!\n\n")
    
    while sair != "sim":
        try:
            A = int(input("\nInsira o valor de A: "))
            B = int(input("Insira o valor de B: "))
            C = random.randint(1, 1000)

            if A == 0:
                print("O valor de A não pode ser zero! Tente novamente.")
                continue

        except ValueError:
            print("Os valores de A e B devem ser inteiros! Tente novamente.")
            continue
        
        exp = Expressão(A,B,C)

        exp_gerada = exp.expressao()
        print(f"\nExpressão Gerada: {exp_gerada}")

        delta = exp.calcular_delta()
        print(f"O valor calculado para o delta é: {delta}")

        placar.A = A
        placar.B = B
        placar.C = C

        resultado = placar.atribuir_ponto()
        print(resultado["mensagem"])

        print(placar.mostrar_placar())

        finalizar = input("\nDeseja terminar o jogo? (Sim ou Não): ")
        sair = finalizar.lower().strip()
    else:
        print("\n--- Jogo Finalizado ---")
        placar.mostrar_resultado_final()


main()