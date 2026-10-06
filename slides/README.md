# 📽️ Apresentação em Slides — Trabalho 1 (Sistema Adversarial)

Este diretório contém a apresentação de slides interativa em **HTML moderno (Reveal.js)** para a gravação do vídeo do Trabalho 1 da disciplina de **Engenharia de Software Seguro (UNIPAMPA)**.
---

## 🚀 Como Executar e Apresentar

### Opção 1: Abrir diretamente no Navegador (Mais Rápido)
Basta dar duplo clique no arquivo [`index.html`](index.html) ou abrir o caminho absoluto no seu navegador:
```bash
google-chrome slides/index.html
# ou
firefox slides/index.html
```

### Opção 2: Servidor Local Rápido (Recomendado)
Para carregar sem restrições de CORS em qualquer navegador:
```bash
python3 -m http.server 8000 --directory slides
```
Acesse no navegador: **[http://localhost:8000](http://localhost:8000)**

---

## ⌨️ Teclas de Atalho para a Apresentação

| Tecla | Ação |
| :---: | :--- |
| `→` ou `Espaço` | Avançar para o próximo slide |
| `←` | Voltar para o slide anterior |
| `F` | Ativar modo **Tela Cheia** (*Fullscreen*) |
| `Esc` ou `O` | Visão geral dos slides em grade (*Overview*) |
| `Home` / `End` | Ir para o primeiro / último slide |
| `Ctrl + P` | Abrir diálogo para **Exportar em PDF** |

---

## 🎮 Simulação Visual Interativa (Slide 6)

No **Slide 6**, há um simulador interativo em tempo real com **500 ingressos promocionais**:
- Clique em **`▶ Cenário 1: FIFO Puro (Sem Defesa)`**: Demonstra a invasão de bots a 1.000 req/s, esgotando o estoque em ~150 ms e deixando os humanos a ver navios (100% Bots, 0% Humanos).
- Clique em **`▶ Cenário 2: Fila Adaptativa + Sorteio`**: Demonstra a retenção na sala de espera, desafio PoW, validação de token e sorteio ponderado com 2FA (87% Humanos, 13% Bots residuais).
- Clique em **`↺ Reset`**: Reinicia o lote para nova demonstração.

---

## 🖨️ Como Exportar para PDF (Google Drive)

Para gerar o arquivo PDF exigido pelo enunciado para envio no Google Drive:
1. Abra a apresentação no Chrome ou Edge.
2. Clique no botão **`🖨️ Exportar PDF (Ctrl+P)`** no canto superior direito (ou pressione `Ctrl + P`).
3. Nas opções de impressão:
   - **Destino:** Salvar como PDF
   - **Layout:** Paisagem (*Landscape*)
   - **Margens:** Nenhuma (*None*)
   - **Gráficos de segundo plano:** Ativado (*Background graphics*)
4. Salve como `Apresentacao_Trabalho_1_Sistema_Adversarial.pdf` e submeta o link do Google Drive no `README.md`.
