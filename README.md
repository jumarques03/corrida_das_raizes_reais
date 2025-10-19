# CP03 – A Corrida das Raízes Reais

**Aluno:** Júlia Souza Marques 
**Turma:** 1CCA  
**RM:** 565010  

---

## Descrição do Projeto

Este programa foi desenvolvido como parte da atividade **“A Corrida das Raízes Reais”**, cujo objetivo é aplicar conceitos de equações do 2º grau em um jogo interativo no terminal.

## Regras:
    - O jogador deve escolher os coeficientes **A** e **B** de uma equação do tipo **Ax² + Bx + C = 0**
    - O valor de **C** é sorteado automaticamente pelo sistema (entre 1 e 1000).

Com base nisso, o programa calcula o discriminante (Δ = B² - 4AC) para determinar o resultado da rodada:

    - Se **Δ > 0**, o jogador marca ponto (duas raízes reais diferentes).  
    - Se **Δ ≤ 0**, o ponto vai para o computador.

O jogo continua até o jogador decidir encerrar. Ao final, é exibido o placar e o vencedor.

---

## ⚙️ Arquivos incluídos

- `main.py` → arquivo principal do jogo  
- `expressao.py` → contém a classe **Expressão**, responsável por gerar a equação e calcular o delta  
- `placar.py` → contém a classe **Placar**, responsável por contabilizar e exibir os pontos  
- `print_execucao.png` → captura de tela mostrando o jogo em execução  

---

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado.  
2. Coloque todos os arquivos `.py` na mesma pasta.  
3. Abra o terminal nessa pasta e execute o comando:  **python main.py**
