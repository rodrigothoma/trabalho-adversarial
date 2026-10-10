# Roteiro Oficial de Apresentação em Slides e Gravação em Vídeo

> **Trabalho 1 — Análise de um Sistema Adversarial: Flash Sale de Black Friday**  
> **Disciplina:** Engenharia de Software Adversarial — UNIPAMPA (Campus Alegrete)  
> **Duração Total Oficial:** Limite estrito de **10 minutos** (600 segundos)  
> **Integrantes e Ordem de Fala:** Rodrigo Thoma da Silva, Fade Hassan Husein Kanaan, Gabriel Camargo Ortiz e Artur Wahlbrink Kraemer  
> **Formato:** Apresentação em slides gravada em vídeo  
> 🎥 **Vídeo:** https://www.youtube.com/watch?v=ChZ1d21_zDU  
> 📄 **Slides (PDF):** https://drive.google.com/file/d/1EjfK8Uhjp4YEU_AqnSblfvfQnJEQJuIi/view?usp=sharing  
> 🌐 **Slides Interativos:** [Branch `slides`](../../tree/slides)

---

## 1. Visão Geral da Linha do Tempo (10 Minutos)

### Matriz de Alinhamento com a Divisão Oficial da Disciplina

| Bloco | Tempo | Duração | Conteúdo Exigido na Rubrica | Slide | Apresentador Responsável |
| :---: | :---: | :---: | :--- | :---: | :--- |
| **1** | 0:00–0:40 | 40 s | **Interação específica e delimitada:** qual sistema, qual interação e por que ela importa. | **Slide 2** | **Rodrigo Thoma da Silva** |
| **2** | 0:40–2:00 | 1 min 20 s | **Atores e contexto:** objetivos, ativos, capacidades, informações e pressupostos. | **Slide 3** | **Rodrigo Thoma da Silva** |
| **3** | 2:00–3:30 | 1 min 30 s | **Matriz de payoffs:** estratégias, significado dos valores e incentivos dos atores. | **Slides 4 e 5** | **Fade Hassan Husein Kanaan** |
| **4** | 3:30–6:30 | 3 min 00 s | **Três rodadas:** ação, resposta, observação e adaptação. O que muda de uma para outra. | **Slides 6 e 7** | **Gabriel Camargo Ortiz** |
| **5** | 6:30–8:00 | 1 min 30 s | **Pelo menos três ameaças:** probabilidade, impacto, risco e justificativa da prioritária. | **Slides 8 e 9** | **Artur Wahlbrink Kraemer** |
| **6** | 8:00–9:20 | 1 min 20 s | **Síntese do resultado:** o que revelou sobre a interação e como os 3 diagramas ajudam. | **Slide 10 (P1)** | **Artur Wahlbrink Kraemer** |
| **7** | 9:20–9:50 | 30 s | **Resposta à ameaça prioritária:** próxima adaptação do atacante e risco residual. | **Slide 10 (P2)** | **Artur Wahlbrink Kraemer** |
| **8** | 9:50–10:00 | 10 s | **Slide final:** referências, declaração de uso de IA e contribuições individuais. | **Slide 11** | **Artur Kraemer / Todos** |

---

## 2. Detalhamento Slide a Slide e Roteiro de Fala

### 🎙️ Bloco 1: Abertura, Delimitação e Atores (Rodrigo Thoma da Silva)
* **Tempo Total:** 0:00 a 2:00 min (Duração: 2m00s)

#### Slide 1: Capa e Identificação do Trabalho
* **Conteúdo:** Título oficial (*Análise de um Sistema Adversarial: Flash Sale de Black Friday — Scalper Bots vs. Fair Checkout*), identificação da disciplina (*Engenharia de Software Adversarial*), logotipo institucional da UNIPAMPA e nome dos 4 integrantes.
* **Fala Chave (~10s):** Cumprimentar a banca/professor, apresentar brevemente o grupo e introduzir o tema: a análise rigorosa do conflito entre cambistas automatizados e plataformas de e-commerce durante vendas de alta concorrência.

#### Slide 2: Delimitação da Interação e Conflito Adversarial
* **Tempo Alvo:** 0:10 a 0:40 min (30s)
* **Conteúdo:** 
  * **Recorte Específico:** Endpoint crítico `POST /api/v1/checkout/orders` durante a abertura da Flash Sale (500 ingressos promocionais com 80% de desconto; cota de 1 unidade por CPF).
  * **Natureza Adversarial:** Não se trata de falha acidental ou pico inocente de tráfego, mas de um agente racional e intencional cujo objetivo econômico é o lucro com ágio de revenda no mercado paralelo.
  * **Ativos em Disputa:** Justiça Distributiva (*Fair Allocation*), Disponibilidade da API e Confiança da Marca.
* **Fala Chave:** Enfatizar que a análise não abrange a loja inteira, mas especificamente a janela de segundos da submissão do pedido, demonstrando a racionalidade econômica do cambista.

#### Slide 3: Atores, Capacidades e Pressupostos Críticos
* **Tempo Alvo:** 0:40 a 2:00 min (1m20s)
* **Conteúdo:**
  * **Tabela de Atores:** Comparativo entre o Operador de Scalper Bots (Atacante) e a Plataforma de E-Commerce (Defensor), confrontando objetivos, capacidades, sinais observáveis e restrições/custos.
  * **Pressupostos Críticos e Modos de Falha:**
    1. *Identidade Única (1 conta = 1 pessoa):* Quebra pelo **Ataque Sybil** (criação em massa de contas com CPFs sintéticos ou vazados).
    2. *Latência Justa (FIFO é equitativo):* Quebra pela **Vantagem da Máquina** (scripts fecham conexão em 50 ms vs. 2 a 3 segundos de leitura e clique de um humano).
* **Fala Chave:** Conectar o objetivo de lucro do cambista com a fragilidade dos dois pressupostos clássicos da computação tradicional, passando a palavra para o Fade demonstrar a modelagem em Teoria dos Jogos.

---

### 🎙️ Bloco 2: Teoria dos Jogos e Simulação de Concorrência (Fade Hassan Husein Kanaan)
* **Tempo Total:** 2:00 a 3:30 min (Duração: 1m30s)

#### Slide 4: Modelo Estratégico Estático: Teoria dos Jogos (2x2)
* **Tempo Alvo:** 2:00 a 3:00 min (1m00s)
* **Conteúdo:**
  * Matriz formal 2x2 com payoffs ordinais de 0 a 3:
    * Linhas (Scalper): $A_1$ (Flood de Bots) vs. $A_2$ (Compra Manual).
    * Colunas (Plataforma): $B_1$ (Checkout Direto FIFO) vs. $B_2$ (Fila Justa com Desafio).
  * **Estratégia Dominante:** $A_1$ domina estritamente $A_2$ ($3 > 2$ se $B_1$; $1 > 0$ se $B_2$). Automatizar é sempre a decisão racional do atacante.
  * **Equilíbrio de Nash em $(A_1, B_2)$ com payoff $(1, 2)$:** Ponto de estabilidade mútua onde nenhum agente melhora mudando de escolha unilateralmente.
  * **Ineficiência de Pareto:** O ótimo cooperativo seria $(A_2, B_1)$ com soma 5 $(2 + 3)$. A tentação da trapaça arrasta o sistema para o equilíbrio custoso em $(1, 2)$ com soma 3.
* **Fala Chave:** Explicar de forma intuitiva que o payoff é o grau de ganho de cada participante e por que o cambista é incentivado a usar robôs, forçando a plataforma a investir em segurança.

#### Slide 5: Simulação de Concorrência: Disputa dos 500 Ingressos
* **Tempo Alvo:** 3:00 a 3:30 min (30s)
* **Conteúdo:** Motor visual interativo em JavaScript simulando a disputa pelos 500 ingressos promocionais.
* **Dinâmica dos Cliques:**
  1. *Clica em "Cenário 1: FIFO Puro":* Os 500 pontos preenchem-se rapidamente em vermelho. Demonstra como os robôs monopolizam 100% do estoque por vantagem de velocidade, deixando os clientes reais com erro de esgotado.
  2. *Clica em "Cenário 2: Fila Adaptativa + Sorteio":* O gateway retém requisições na sala de espera (PoW), ativa o sorteio ponderado e valida 2FA. O painel atinge **87% de alocação para humanos (verde)** e apenas 13% de resíduo para bots.
* **Fala Chave:** Mostrar a quebra do FIFO na prática e transferir a palavra para o Gabriel explicar como essa defesa evolui através de três rodadas adaptativas.

---

### 🎙️ Bloco 3: Modelo Dinâmico e Ciclo Adaptativo (Gabriel Camargo Ortiz)
* **Tempo Total:** 3:30 a 6:30 min (Duração: 3m00s — cerca de 1 min por rodada + reflexão)

#### Slide 6: Modelo Dinâmico: A Corrida Armamentista em 3 Rodadas
* **Tempo Alvo:** 3:30 a 5:30 min (2m00s)
* **Conteúdo:** Tabela estruturada com o ciclo *Ação $\rightarrow$ Resposta $\rightarrow$ Observação $\rightarrow$ Adaptação*:
  * **Rodada 1 (Força Bruta Monolítica vs. Rate Limit):** Scalper faz flood de 1.000 req/s por único IP $\rightarrow$ Plataforma bloqueia com `HTTP 429` $\rightarrow$ Scalper observa `Retry-After` e deduz filtro por IP $\rightarrow$ Adapta para pool rotativo de *proxies residenciais*.
  * **Rodada 2 (Pulverização Distribuída vs. Fila com PoW):** Scalper ataca com 500 IPs residenciais e contas sintéticas $\rightarrow$ Plataforma redireciona para Waiting Room com PoW e token assinado (`HTTP 403` sem token) $\rightarrow$ Scalper descobre que chamadas diretas falham $\rightarrow$ Adapta para *navegadores headless* (Playwright) com solvers de desafio.
  * **Rodada 3 (Bots Avançados vs. Sorteio Ponderado e 2FA):** Bots headless resolvem desafios e simulam humanos $\rightarrow$ Plataforma quebra o FIFO com janela fechada, **sorteio ponderado por reputação da conta**, limite de 1 un/CPF e **2FA via SMS** $\rightarrow$ Velocidade pura deixa de garantir compra e contas novas têm utilidade mínima $\rightarrow$ Scalper precisa comprar contas antigas e chips reais, elevando o custo marginal a ponto de **inviabilizar o lucro da revenda**.
* **Fala Chave:** Conduzir a evolução rodada a rodada, demonstrando que toda defesa gera sinais observáveis que incentivam a escalada técnica do adversário.

#### Slide 7: Análise Dinâmica e Pergunta Reflexiva da Rubrica
* **Tempo Alvo:** 5:30 a 6:30 min (1m00s)
* **Conteúdo:**
  * **Quem Observa Quem & Custos:** Telemetria da plataforma (tráfego, TLS, comportamento) vs. sinais captados pelo atacante (status HTTP, latência, telas de fila). Efeitos colaterais em usuários legítimos (espera e atrito de SMS).
  * **Resposta à Pergunta Reflexiva:** *"Depois que o sistema responder com Sorteio e 2FA, o que o atacante aprende e tenta fazer em seguida?"*
    1. *Aprendizado:* A disputa deixou de ser por latência de rede e virou uma disputa por **reputação de identidade**.
    2. *Próxima Ação:* Migração para engenharia social, compra de contas antigas no mercado cinzento e aluguel de pessoas reais para receber SMS.
    3. *Ponto de Inviabilidade:* Quando o custo de adquirir identidades supera a margem de revenda, o modelo de negócios do scalper colapsa.
* **Fala Chave:** Responder frontalmente à questão reflexiva da rubrica e passar a palavra para o Artur apresentar a superfície de ataque e a matriz de riscos.

---

### 🎙️ Bloco 4: Ameaças, Síntese e Encerramento (Artur Wahlbrink Kraemer)
* **Tempo Total:** 6:30 a 10:00 min (Duração: 3m30s)

#### Slide 8: Superfície de Ataque e Pontos de Exploração
* **Tempo Alvo:** 6:30 a 7:15 min (45s)
* **Conteúdo:** Tabela arquitetural mapeando os três pontos críticos:
  * **P1 (Endpoint de Checkout - `POST /api/v1/checkout/orders`):** Motor de pedidos e concorrência direta pelo estoque.
  * **P2 (Serviço de Autenticação - `POST /api/v1/auth/register`):** Criação em lote de identidades sintéticas (Ataque Sybil) burlando o limite de 1 item por CPF.
  * **P3 (Reserva de Carrinho - `PUT /api/v1/cart/reserve`):** Retenção temporária abusiva (*Holding Lock*) causando negação de estoque (*Denial of Inventory*).
* **Fala Chave:** Relacionar as interfaces do software com as falhas dos pressupostos identificadas no início da apresentação.

#### Slide 9: Cenários de Ameaça e Matriz de Riscos ($P \times I$)
* **Tempo Alvo:** 7:15 a 8:00 min (45s)
* **Conteúdo:**
  * Tabela quantitativa de riscos ($P \times I$ de 1 a 3):
    * **A1 (Flood Concorrente no Checkout):** $P=3, I=3 \rightarrow$ **Risco 9 (Crítico) — Ameaça Prioritária**.
    * **A2 (Identidades Falsas / Sybil):** $P=3, I=2 \rightarrow$ **Risco 6 (Alto)**.
    * **A3 (Retenção Abusiva de Carrinho):** $P=2, I=2 \rightarrow$ **Risco 4 (Médio)**.
  * **Aprofundamento na Ameaça Prioritária (A1):** Resposta defensiva (Waiting Room + PoW + token HMAC), efeitos colaterais em legítimos (espera obrigatória), informação revelada (403/302) e risco residual.
* **Fala Chave:** Justificar tecnicamente por que o esgotamento por robôs (A1) é a ameaça de maior severidade sobre o negócio.

#### Slide 10: Síntese do Resultado e o Papel dos Três Diagramas
* **Tempo Alvo:** 8:00 a 9:50 min (1m50s)
* **Conteúdo:**
  * **Síntese da Interação e Papel dos 3 Diagramas:**
    * A segurança de vendas relâmpago não é falha de código, mas de **incentivos econômicos**.
    * *Diagrama de Contexto:* Mostrou onde os pressupostos foram violados (1 CPF ≠ 1 humano; 50ms vs 3s).
    * *Diagrama do Ciclo Adaptativo:* Evidenciou a corrida armamentista temporal em 3 rodadas.
    * *Diagrama de Superfície de Ataque:* Revelou o gargalo do acoplamento direto entre checkout e banco de dados.
  * **Resposta à Ameaça Prioritária (A1):** Desacoplamento via Fila Virtual assíncrona, Proof of Work (PoW) e quebra do FIFO com Sorteio Ponderado por 2FA.
  * **Próxima Adaptação & Risco Residual:** O atacante é empurrado para o mercado cinzento (aluguel de pessoas reais). O sistema tolera conscientemente um **risco residual de ~13% de bots**, garantindo 87%+ de ingressos distribuídos com equidade e mantendo a reputação da marca íntegra.
* **Fala Chave:** Fechar o ciclo conceitual conectando os três diagramas da documentação escrita ao redesenho resiliente da arquitetura.

#### Slide 11: Conclusão, Referências e Contribuições Individuais
* **Tempo Alvo:** 9:50 a 10:00 min (10s)
* **Conteúdo:**
  * **Referências:** Aulas do Prof. Silvio Quincozes (UNIPAMPA), OWASP Automated Threats (OAT-005, OAT-007), John Nash (1951) e Cloudflare/Queue-it.
  * **Declaração de Uso de IA:** Uso consultivo de LLM para estruturação de documentação e scaffolding de slides, sob total supervisão e validação técnica da equipe.
  * **Contribuições Individuais:**
    * *Rodrigo Thoma:* Delimitação, mapeamento de contexto e pressupostos críticos.
    * *Fade Kanaan:* Teoria dos Jogos 2x2, Equilíbrio de Nash e motor de simulação.
    * *Gabriel Ortiz:* Modelo dinâmico em 3 rodadas e observabilidade.
    * *Artur Kraemer:* Superfície de ataque, matriz de riscos, síntese e resiliência.
* **Fala Chave:** Concluir dentro dos 10 minutos cravados, agradecer a atenção dos professores e colegas e abrir para perguntas.

---