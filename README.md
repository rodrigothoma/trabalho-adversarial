<div align="center">

# Análise de um Sistema Adversarial
### Trabalho 1 — Modelo Estático, Modelo Dinâmico, Ameaças e Riscos

<p align="center">
  <b>Etapa de Planejamento e Desenho Arquitetural</b><br>
  <i>Especificação conceitual e estratégica para a implementação funcional no Trabalho 2</i>
</p>

[![Fase](https://img.shields.io/badge/Fase-Planejamento%20e%20Arquitetura-0969da?style=flat-square)](#)
[![Segurança](https://img.shields.io/badge/Foco-Segurança%20Adversarial-d73a49?style=flat-square)](#)

</div>

---

### 📌 Materiais de Apresentação

| Recurso | Formato / Plataforma | Link de Acesso |
| :--- | :---: | :--- |
| 📄 **Slides da Apresentação** | PDF (Google Drive) | [Inserir link do Google Drive aqui] |
| 🎥 **Vídeo de Apresentação** | YouTube (Gravação Canva) | [Inserir link do YouTube aqui] |

---

### 👥 Integrantes do Grupo

| 👤 Nome Completo |
| :--- |
| Artur Wahlbrink Kraemer |
| Fade Hassan Husein Kanaan |
| Gabriel Camargo Ortiz |
| Rodrigo Thoma da Silva |

---

## 1. Proposta

> **Questão central:** *O que torna esse sistema adversarial, como os participantes tomam decisões e como a interação evolui ao longo das rodadas?*

Este trabalho analisa a interação de **publicar e calcular avaliações de estabelecimentos** (nota de 1 a 5 estrelas e comentário) em plataformas digitais, como marketplaces e aplicativos de delivery.

### Por que o sistema é adversarial?

Existe um conflito de interesse direto entre os participantes:

* **Estabelecimentos comerciais maliciosos:** Dependem de uma nota alta para obter visibilidade orgânica e faturar mais. Por isso, têm forte incentivo para fraudar o sistema comprando avaliações falsas positivas para si (*astroturfing*) ou negativas contra concorrentes (*review bombing*).
* **A plataforma:** Precisa que as notas reflitam com fidelidade a realidade para preservar a confiança dos consumidores. Se estabelecimentos ruins exibirem notas altas, os clientes perdem a confiança e abandonam o serviço.

### Como os participantes tomam decisões?

Ambos os lados agem estrategicamente, ponderando custos operacionais contra ganhos esperados:

* **O atacante (fraudador):** Avalia o custo de criar/comprar contas e forjar avaliações contra o benefício financeiro de elevar sua nota média sem sofrer banimento.
* **O defensor (plataforma):** Calibra o rigor dos filtros de bloqueio e dos algoritmos de média, buscando barrar fraudes sem gerar atrito excessivo nem punir clientes autênticos (minimizando falsos positivos).

###  Como a interação evolui ao longo das rodadas?

A disputa se desenvolve em ciclos contínuos de ação, resposta, observação e adaptação:

1. **Ação inicial:** O fraudador publica um lote de avaliações falsas em massa para inflar rapidamente sua média.
2. **Resposta da defesa:** O sistema detecta o padrão anômalo, descarta as avaliações suspeitas e aplica restrições às contas.
3. **Observação e adaptação:** O fraudador percebe a remoção e adapta sua tática (ex.: recorre a IA generativa para variar vocabulário, espaça os envios no tempo ou utiliza contas antigas com histórico).
4. **Escalação:** O sistema aprimora suas defesas com checagens mais profundas (reputação histórica, correlação temporal e grafos), estabelecendo uma corrida armamentista contínua.

>  **Nota de continuidade:** Esta etapa de planejamento e desenho arquitetural servirá de especificação direta para a implementação funcional do mecanismo no Trabalho 2.

---

## 2. Escolha do Sistema

###  Ficha Técnica da Interação

| Atributo | Definição no Projeto |
| :--- | :--- |
| **Sistema Escolhido** | Plataforma de Reputação e Avaliação de Estabelecimentos (presente em apps de delivery, e-commerce e serviços locais). |
| **Interação Específica** | Submissão de avaliação pós-consumo (nota de 1 a 5 estrelas e comentário textual) e o processamento dessa entrada para o recálculo da nota pública do estabelecimento. |

###  Conformidade com os Critérios do Enunciado

| # | Critério Obrigatório | Atendimento no Sistema Analisado |
| :-: | :--- | :--- |
| **1** | **Dois participantes com tomada de decisão** | • **Estabelecimento malicioso (ou operador):** decide a frequência de envio, notas atribuídas, perfis textuais e quais contas utilizar.<br>• **Mecanismo de moderação da plataforma:** decide se publica imediatamente, se descarta por suspeita de fraude ou se reduz o peso da nota com base na reputação do perfil. |
| **2** | **Objetivos total ou parcialmente conflitantes** | • **Estabelecimento:** quer inflar artificialmente a nota média para atrair clientes e faturar mais, sem ser punido.<br>• **Plataforma:** quer garantir que a nota pública reflita a experiência real de consumo, protegendo a credibilidade do marketplace sem barrar avaliações legítimas. |
| **3** | **Regra, métrica ou decisão explorável** | A fórmula de cálculo da nota média (ex.: média aritmética ou média ponderada simples) e a influência imediata de notas extremas (1 e 5 estrelas), aproveitando a impossibilidade prática de o sistema verificar presencialmente se cada consumo foi autêntico. |
| **4** | **Resposta observável e adaptação** | O atacante observa publicamente se a nota média do estabelecimento aumentou, se o comentário foi publicado ou se o perfil foi sinalizado. A partir dessa observação, adapta sua estratégia (variando textos com IA, reduzindo a cadência ou adquirindo contas mais antigas). |
| **5** | **Escopo viável para o Trabalho 2** | Fluxo de dados enxuto: envio de payload (`estabelecimento_id`, `usuario_id`, `nota`, `texto`, `timestamp`) $\rightarrow$ passagem por regras/filtros de moderação $\rightarrow$ recálculo da nota média. Escopo modular e plenamente viável de ser simulado e implementado em poucas classes ou endpoints (Python ou Node.js). |

---

## 3. Desenvolvimento

### 3.1 Descrição do Sistema Adversarial

* **Qual é o sistema e qual interação será analisada:**
* **Quais são os principais atores:**
* **Qual é o objetivo de cada ator:**
* **Qual ativo ou propriedade precisa ser preservado (justiça, confiança, privacidade, disponibilidade, distribuição correta de um recurso, etc.):**
* **Quais ações ou capacidades cada ator possui:**
* **Quais informações cada ator consegue observar:**
* **Quais custos ou restrições limitam suas ações:**
* **Pelo menos dois pressupostos dos quais o sistema depende:**
  1. *Pressuposto 1:*
  2. *Pressuposto 2:*
* **Como esses pressupostos podem falhar:**
  1. *Falha do Pressuposto 1:*
  2. *Falha do Pressuposto 2:*

#### Tabela de Atores

| Ator | Objetivo | Ações ou capacidades | Informações observáveis | Restrições ou custos |
|---|---|---|---|---|
| Ator 1 | | | | |
| Ator 2 | | | | |

#### Diagrama de Contexto

![Diagrama de Contexto](diagramas/contexto.png)

#### Natureza Adversarial do Caso

*[Explicar por que o caso representa uma situação adversarial, e não apenas um erro ou acidente.]*

---

### 3.2 Modelo Estratégico Estático

#### Matriz de Decisão (Jogo 2x2)

> Ordem dos payoffs no par: `(payoff do Jogador A, payoff do Jogador B)`  
> Valores utilizados: escala de preferência simples (ex.: 0, 1, 2, 3)

| Jogador A \ Jogador B | Ação B1: *[Nome da Ação]* | Ação B2: *[Nome da Ação]* |
|---|:---:|:---:|
| **Ação A1: *[Nome da Ação]*** | ( , ) | ( , ) |
| **Ação A2: *[Nome da Ação]*** | ( , ) | ( , ) |

#### Análise do Modelo Estático

* **O que representa cada ação:**
  * *Ação A1:*
  * *Ação A2:*
  * *Ação B1:*
  * *Ação B2:*
* **Por que cada resultado recebeu aqueles payoffs:**
  * *(A1, B1):*
  * *(A1, B2):*
  * *(A2, B1):*
  * *(A2, B2):*
* **Quais são as melhores respostas dos jogadores:**
  * *Melhores respostas do Jogador A:*
  * *Melhores respostas do Jogador B:*
* **Existe estratégia dominante?**
* **Existe um resultado no qual nenhum jogador melhora mudando sozinho (Equilíbrio de Nash)?**
* **Esse resultado é bom para o sistema e para os usuários legítimos?**

---

### 3.3 Modelo Estratégico Dinâmico

#### Ciclo de Rodadas Adversariais

| Rodada | Ação do participante | Resposta do sistema ou defensor | O que se torna observável? | Adaptação para a rodada seguinte |
|:---:|---|---|---|---|
| **1** | | | | |
| **2** | | | | |
| **3** | | | | |

#### Diagrama do Ciclo Adaptativo

![Diagrama do Ciclo Adaptativo](diagramas/ciclo-adaptativo.png)

#### Perguntas de Análise Dinâmica

* **Quem observa quem?**
* **O que cada lado consegue mudar?**
* **O que dispara uma adaptação?**
* **Qual é o custo da adaptação para cada lado?**
* **Em que ponto pode surgir uma corrida armamentista?**

---

### 3.4 Ameaças e Riscos

#### Diagrama de Superfície de Ataque

![Diagrama de Superfície de Ataque](diagramas/superficie-de-ataque.png)

#### Pontos de Exploração Identificados
1. *Ponto de Exploração 1:*
2. *Ponto de Exploração 2:*
3. *Ponto de Exploração 3:*

#### Cenários de Ameaça

> **Formato padrão:**  
> *Um [ator] pode realizar [ação] por meio de [ponto de exploração], aproveitando [fraqueza ou pressuposto], causando [impacto] sobre [ativo ou propriedade].*

* **A1:** Um `[ator]` pode realizar `[ação]` por meio de `[ponto de exploração]`, aproveitando `[fraqueza ou pressuposto]`, causando `[impacto]` sobre `[ativo ou propriedade]`.
* **A2:** Um `[ator]` pode realizar `[ação]` por meio de `[ponto de exploração]`, aproveitando `[fraqueza ou pressuposto]`, causando `[impacto]` sobre `[ativo ou propriedade]`.
* **A3:** Um `[ator]` pode realizar `[ação]` por meio de `[ponto de exploração]`, aproveitando `[fraqueza ou pressuposto]`, causando `[impacto]` sobre `[ativo ou propriedade]`.

#### Avaliação de Riscos

> **Escala (1 a 3):**  
> * Probabilidade: 1 = baixa, 2 = média, 3 = alta  
> * Impacto: 1 = baixo, 2 = médio, 3 = alto  
> * Risco: $\text{Probabilidade} \times \text{Impacto}$

| ID | Cenário de ameaça | Ponto de exploração | Pressuposto ou fraqueza | Ativo afetado | Probabilidade (1-3) | Impacto (1-3) | Risco (1-9) |
|:---:|---|---|---|---|:---:|:---:|:---:|
| **A1** | | | | | | | |
| **A2** | | | | | | | |
| **A3** | | | | | | | |

#### Detalhamento da Ameaça de Maior Prioridade

* **Ameaça selecionada:**
* **Como o sistema poderia responder:**
* **Que informação essa resposta revelaria:**
* **Como o adversário poderia se adaptar na rodada seguinte:**
* **Quais efeitos colaterais poderiam atingir usuários legítimos:**
* **Qual risco continuaria existindo após a resposta (risco residual):**
* **O que o sistema precisa continuar preservando apesar das adaptações:**

---

## 4. Continuidade com o Trabalho 2

*[Descrever as decisões arquiteturais e o planejamento para transformar a especificação deste Trabalho 1 em uma implementação funcional de código no Trabalho 2.]*

---

## 5. Referências e Fontes Consultadas

*[Listar as principais referências bibliográficas e documentações técnicas utilizadas. O detalhamento completo pode ser mantido em [fontes/referencias.md](fontes/referencias.md).]*

---

## 6. Declaração sobre Uso de IA Generativa

*[Declarar para quais tarefas a IA generativa foi utilizada e descrever como o grupo verificou e validou o conteúdo produzido, conforme exigido na Seção 6 do enunciado.]*

---

## 7. Contribuições Individuais dos Integrantes

*[Descrever a divisão de trabalho e a contribuição de cada membro no repositório e na apresentação.]*

| Integrante | Papel / Responsabilidades | Seções Desenvolvidas |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

---

## 8. Pergunta Final

> **"Depois que o sistema responder, o que o outro lado aprenderá e tentará fazer em seguida?"**

*[Inserir a resposta reflexiva do grupo à questão final do enunciado.]*

