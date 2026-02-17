# PATP-Pole-Position

Um projeto desenvolvido no 1º semestre da faculdade por mim e por meu amigo Richarlison Ângelo Ávila, estagiário da Aurora.

---
## Tecnologias usadas:
- Python:
- Pygame

## Estrutura do Projeto

- PATP-Pole-Position/
- ├── dados/ ← Pasta onde ficam os dados usados pelo jogo
- ├── imagens/ ← Imagens utilizadas no jogo (sprites, backgrounds, etc.),todas elas feitas pelo meu colega Richarlison
- ├── model/ ← Modelos ou scripts relacionados à lógica do jogo(car.py,player.py)
- ├── som/ ← Arquivos de som e efeitos sonoros
- ├── game_stats.py ← Módulo para registrar e exibir estatísticas do jogo
- ├── main.py ← Arquivo principal que inicia o jogo
- ├── settings.py ← Configurações globais da aplicação (ex: telas, controles)
- └── README.md ← Documentação do projeto
  
### Detalhamento das pastas e arquivos

- **`.vscode/`**: Contém configurações específicas para o VS Code, como `settings.json`, `launch.json`, ou extensões recomendadas, facilitando o desenvolvimento consistente.

- **`dados/`**: Armazena dados persistentes ou interfases de dados que o jogo usa (pontuações salvas, configurações, etc.).

- **`imagens/`**: Guarda todos os recursos visuais — como gráficos, sprites de carros, pistas, telas de fundo, logos, etc.

- **`model/`**: Lugar para lógica mais complexa ou componentes de modelo que ajudam na computação dos comportamentos de jogo (como física ou inteligência artificial simplificada).

- **`som/`**: Reúne os arquivos de áudio — trilha sonora, efeitos de motor, colisões, etc.

- **`game_stats.py`**: Responsável por controlar e exibir estatísticas, como tempo de corrida, melhor volta, pontuação, etc.

- **`main.py`**: Ponto de entrada do jogo. Carrega configurações, inicializa a janela, gerencia o loop principal e invoca outras funções conforme o fluxo do jogo.

- **`settings.py`**: Define variáveis globais como tamanho da janela, frames por segundo (FPS), chaves de controle ou configurações padrões de jogo.

---

## Sobre o Projeto

Este projeto é um jogo de corrida com nome de *Pole Position*, desenvolvido com meu colega Richarlison Ângelo Ávila, durante o primeiro semestre da faculdade. Nosso objetivo foi aplicar conhecimentos de lógica de programação, manipulação de recursos multimídia (imagens, sons), além de estruturar um código organizado e funcional, completo com estatísticas de desempenho dentro do jogo.

---

## Instalacao de dependencias:

```bash
# clonar repositorio:
git clone https://github.com/ldm-code/PATP-Pole-Position.git
cd PATP-Pole-Position

# configurar ambiente:

# no linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

# No windows(powershell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalacao de frameworks:
pip install pygame

```

---

- ## Observacao:
- É preciso ter o python 3.13.2 instalado em sua maquina para que assim voce possa executar o arquivo main.py e jogar o jogo,
- Voce pode executar o main.py rodando ele na sua ide ou executando o seguinte comando


```bash

# no linux/macOS execute:
python3 main.py

# no windows execute:
python main.py


```


---

## Controles basicos
 
**Apos realizar o processo acima em sua maquina e execuatar o main.py,existem alguns controles basicos que devem ser destacados,cada um deles estao listados abaixo**

- Ao executar o arquivo main.py voce abre o menu de jogador ,e clicando iniciar entra na tela de selecao da partida.
- Ao acessar a tela de selecao de equipe ,selecione a equipe clicando na logo.
- Ao entrar na tela de piloto,selecione seu  piloto clicando no capacete.
- Para para sair de uma tela a outra onde nao tiver nada escrito  voltar ou sair aperte a tecla esc do teclado.
- O piloto king e equipe legend sao liberados ao apertar a tecla p do teclado com a loja aberta.
- Voce pode ativar/desativar o som nas configuracoes do jogo.
- Apos finalizar a selecao de equipes e pilotos um contador aparece,apos a contagem de 3 segundos a partida comeca.
- Use as setas para direita e esquerda para mover o jogador.

---

---

## 📄 Licença

Este projeto está licenciado sob a MIT License – veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
