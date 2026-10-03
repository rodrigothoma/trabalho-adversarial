# Rascunho Completo das Seções para os Integrantes do Grupo

> **Instruções para o Grupo:**  
> Este documento contém os textos base completos e validados tecnicamente para as seções atribuídas a cada integrante. Cada membro deve copiar o conteúdo de sua seção, revisar/personalizar e realizar o commit em sua própria branch no GitHub, garantindo o equilíbrio individual de contribuições exigido na rubrica.

---

# 👤 Seções do Rodrigo Thoma da Silva
* **Responsabilidade:** Seção 1 (Proposta), Seção 2 (Escolha do Sistema) e Seção 3.1 (Descrição do Sistema Adversarial e Diagrama de Contexto).

### Texto da Seção 1: Proposta
```markdown
## 1. Proposta

> **Questão central:** *O que torna esse sistema adversarial, como os participantes tomam decisões e como a interação evolui ao longo das rodadas?*

Este trabalho analisa a interação crítica de **checkout concorrente de produtos com estoque escasso em promoções relâmpago de Black Friday (*Flash Sales*)**, na qual 500 unidades de um item de altíssima demanda são disponibilizadas com 80% de desconto.

### Por que o sistema é adversarial?
O conflito de interesses entre os participantes é estrutural e puramente econômico:
* **Operadores de Scalper Bots (Cambistas Digitais):** Têm como meta monopolizar o maior percentual possível do inventário escasso no instante exato da abertura das vendas, utilizando automação para superar as limitações biológicas humanas. Seu objetivo é revender esses produtos no mercado secundário (redes sociais e marketplaces não oficiais) com ágio de 200% a 400%, extraindo para si o excedente econômico que o marketplace pretendia oferecer aos clientes.
* **A Plataforma de E-Commerce (Defensora):** Tem como objetivo maximizar a **justiça distributiva (*fair allocation*)**, garantindo que as 500 unidades cheguem a 500 consumidores humanos distintos. Essa pulverização é essencial para adquirir novos clientes, aumentar o *Customer Lifetime Value* (LTV), gerar engajamento de marca e preservar a reputação contra acusações de propaganda enganosa ou fraude promocional.

Não se trata de tráfego orgânico acidental ou mero erro operacional: o scalper calcula ativamente sua margem de lucro contra o custo operacional de proxies e infraestrutura de bots, contornando conscientemente as barreiras erguidas pela plataforma.

### Como os participantes tomam decisões?
Ambos os lados agem estrategicamente, calculando utilidades e payoffs sob incerteza e interdependência de escolhas:
* **O Atacante (Scalper):** Decide a tecnologia de automação (scripts HTTP assíncronos, navegadores *headless*, solvers de CAPTCHA), o volume de requisições concorrentes, o investimento em pools de proxies residenciais e a compra de identidades sintéticas (contas laranjas), ponderando o custo financeiro do ataque contra o lucro esperado na revenda.
* **O Defensor (Plataforma):** Calibra a sensibilidade de seus filtros defensivos (*Rate Limit*, filas virtuais, provas de trabalho criptográficas e sorteios ponderados), buscando neutralizar os robôs sem impor atrito excessivo, lentidão ou falsos positivos sobre consumidores legítimos que tentam comprar de forma autêntica.

### Como a interação evolui ao longo das rodadas?
A disputa não é estática; ela se desenvolve como uma clássica corrida armamentista iterada em camadas de rede, aplicação e identidade:
1. **Ação Inicial:** O atacante dispara um flood massivo de requisições de compra a partir de servidores virtuais (VPS) de alta velocidade.
2. **Resposta da Defesa:** A plataforma detecta picos volumétricos de tráfego e ativa bloqueios de taxa (*Rate Limiting*) por endereço IP.
3. **Observação e Adaptação:** O atacante observa o recebimento de códigos `HTTP 429 Too Many Requests`, identifica que a barreira é baseada em IP e adapta seu vetor de ataque, roteando as conexões através de redes de proxies residenciais rotativos com milhares de endereços válidos.
4. **Escalação Defensiva:** A plataforma percebe que a filtragem por IP tornou-se ineficaz e responde transferindo a disputa para a camada de integridade e identidade (implementando filas virtuais com desafios criptográficos e sorteios ponderados). Isso força o adversário a recorrer a fazendas de identidades reais e emulação de navegadores completos, elevando drasticamente o custo financeiro do ataque até que ele atinja o ponto de inviabilidade econômica.

> 💡 **Nota de continuidade com o Trabalho 2:** Esta etapa de planejamento e desenho arquitetural servirá de especificação direta para o código funcional a ser implementado no Trabalho 2, no qual desenvolveremos uma API concorrente, um pipeline de defesas adaptativas e um simulador de agentes (humanos vs. bots).
```

### Texto da Seção 2: Escolha do Sistema
```markdown
## 2. Escolha do Sistema

### 📋 Ficha Técnica da Interação

| Atributo | Definição no Projeto |
| :--- | :--- |
| **Sistema Escolhido** | Plataforma de E-Commerce com Mecanismo de Flash Sale / Venda de Estoque Escasso. |
| **Interação Específica** | Submissão concorrente da requisição de finalização de compra (`POST /api/v1/checkout/orders`) para aquisição de item promocional limitado (500 unidades disponíveis) no instante exato da liberação de vendas. |
| **Contexto de Operação** | Evento de pico promocional (Black Friday) com estoque finito, alta assimetria temporal (abertura sincronizada) e forte incentivo financeiro para revenda secundária com lucro expressivo. |

### 🎯 Conformidade com os Critérios Obrigatórios do Enunciado

| # | Critério Obrigatório | Atendimento no Sistema Analisado |
| :-: | :--- | :--- |
| **1** | **Pelo menos dois participantes capazes de tomar decisões** | • **Operador de Scalper Bots:** Decide cadência de disparo, arquitetura de rede (proxies), tecnologia de cliente (HTTP direto vs. *headless*) e alocação de contas.<br>• **Motor de Fila e Checkout da Plataforma:** Decide roteamento de requisições, retenção em sala de espera, exigência de desafios de humanidade e critérios de alocação de estoque (FIFO vs. Sorteio Ponderado). |
| **2** | **Objetivos total ou parcialmente conflitantes** | • **Scalper:** Quer concentrar e monopolizar o inventário para revenda especulativa com ágio.<br>• **Plataforma:** Quer pulverizar o estoque entre o maior número de consumidores reais distintos (1 item por CPF) para fidelização e reputação, preservando a disponibilidade do serviço. |
| **3** | **Regra, métrica ou decisão explorável** | A métrica tradicional de **ordem de chegada por latência de rede (FIFO estrito)**. O atacante explora essa regra executando scripts automatizados próximos aos servidores da CDN/API, superando a velocidade de reação biológica humana em ordens de magnitude (milissegundos vs. segundos). |
| **4** | **Resposta observável que permita reação ou adaptação** | O atacante observa publicamente códigos de status HTTP (200, 403, 429, 503), cabeçalhos de resposta (`Retry-After`), latência da conexão, redirecionamentos de URL (telas de fila) e o decremento do contador público de estoque. Com base nesses dados, altera dinamicamente seus parâmetros de ataque. |
| **5** | **Escopo viável para implementação no Trabalho 2** | Interação pontual e altamente modular: endpoint de checkout (`/checkout`), repositório de estoque em memória com controle de concorrência (`asyncio.Lock` ou Redis), middlewares comutáveis de defesa (Rate Limit, Fila/Token, Sorteio) e um script gerador de carga concorrente simulando compradores legítimos vs. robôs. |
```

### Texto da Seção 3.1: Descrição do Sistema Adversarial
```markdown
### 3.1 Descrição do Sistema Adversarial

* **Qual é o sistema e qual interação será analisada:**  
  Plataforma de E-Commerce de Grande Porte durante eventos de *Flash Sale*. A interação analisada é a **submissão e validação da requisição de compra** no endpoint `POST /api/v1/checkout/orders`, na qual múltiplos clientes competem simultaneamente por 500 unidades promocionais de um item de alta demanda.

* **Quais são os principais atores:**  
  * **Operador de Scalper Bots (Atacante Estratégico):** Agente motivado pelo lucro da revenda no mercado secundário, que opera softwares automatizados de disparo concorrente de compras.
  * **Motor de Defesa e Fila Justa da Plataforma (Defensor):** Sistema de controle de tráfego, mitigação de abusos e alocação de estoque responsável por proteger a infraestrutura e garantir a distribuição equitativa dos produtos.
  * *(Ator de Contexto) Consumidor Legítimo:* Indivíduo humano autêntico que navega pelo aplicativo ou site oficial, preenche formulários manualmente e deseja adquirir o produto para uso próprio pelo preço oficial anunciado.

* **Qual ativo ou propriedade precisa ser preservado:**  
  * **Justiça Distributiva (*Fair Allocation*):** Propriedade de que o recurso promocional escasso seja distribuído de forma pulverizada entre consumidores reais únicos, impedindo que um agente monopolize o benefício.
  * **Disponibilidade e Resiliência da Infraestrutura:** Manutenção dos serviços de catálogo, pagamento e checkout operacionais durante picos de tráfego extremo, evitando negação de serviço (DoS).
  * **Confiança e Reputação da Marca:** Preservação da percepção pública de idoneidade da promoção, evitando danos à imagem decorrentes da sensação de "fraude" ou "sorteio viciado".

* **Quais ações ou capacidades cada ator possui:**  
  * **Operador de Scalper Bots:** Disparar requisições HTTP paralelas em escala de milhares por segundo; alternar endereços IP utilizando proxies residenciais; executar navegadores automatizados (*headless* como Playwright e Puppeteer); resolver desafios de CAPTCHA via serviços terceirizados de IA; gerar cadastros com dados sintéticos ou credenciais laranjas.
  * **Plataforma (Defensora):** Inspecionar cabeçalhos de rede, assinaturas TLS (JA3/JA4) e metadados de requisição; aplicar limites de taxa (*Rate Limiting*); enfileirar requisições em salas de espera virtuais (*Waiting Rooms*); exigir provas criptográficas de trabalho (*Proof-of-Work*) e desafios de humanidade; auditar CPF em bases oficiais; cancelar pedidos suspeitos antes do despacho físico; alterar regras de alocação de estoque de FIFO para sorteio aleatório ponderado.

* **Quais informações cada ator consegue observar:**  
  * **O Scalper observa:** Códigos de resposta HTTP (200 OK, 403 Forbidden, 429 Too Many Requests, 503 Service Unavailable); cabeçalhos de resposta (como `Retry-After`); tempo de resposta (*Round-Trip Time*); redirecionamentos para telas de desafio/fila; mensagens de erro retornadas no payload JSON; disponibilidade ou esgotamento do estoque no catálogo público.
  * **A Plataforma observa:** Endereço IP de origem, ASN e geolocalização; taxa de requisições por segundo por IP, sessão e endpoint; fingerprints de navegador e propriedades de canvas/WebGL; tempos de interação na página (tempo de preenchimento de campos e movimentos de cursor); histórico de compras, idade da conta e dados de faturamento do cartão de crédito.

* **Quais custos ou restrições limitam suas ações:**  
  * **Restrições do Scalper:** Custo monetário de aluguel de proxies residenciais rotativos (cobrados por gigabyte trafegado); custo financeiro de APIs de resolução de CAPTCHA; custo de aquisição de contas/CPFs laranjas e cartões de crédito; risco de ter o capital financeiro retido caso a plataforma cancele os pedidos após a aprovação do pagamento; risco jurídico de apreensão de mercadorias.
  * **Restrições da Plataforma:** Limite de capacidade computacional e custos com infraestrutura de nuvem e serviços especializados de mitigação (como Cloudflare ou Queue-it); risco de **falsos positivos** (bloquear um cliente humano fiel por confundi-lo com um bot); risco de **atrito excessivo** (impor desafios tão demorados que consumidores humanos legítimos desistam da compra, aumentando a taxa de abandono de carrinho).

* **Pelo menos dois pressupostos dos quais o sistema depende:**  
  1. *Pressuposto da Identidade Única (1 Requisição = 1 Consumidor Humano):* O sistema assume que cada requisição de checkout associada a uma sessão autenticada representa a intenção de um indivíduo físico distinto e de boa-fé.
  2. *Pressuposto da Latência Justa (A Ordem de Chegada TCP/HTTP reflete o Esforço Humano):* O sistema assume que a ordem cronológica em que os pacotes de requisição atingem o servidor (política FIFO — *First-In, First-Served*) é um critério justo e imparcial de desempate para a entrega de recursos escassos.

* **Como esses pressupostos podem falhar:**  
  1. *Falha do Pressuposto 1 (Ataque Sybil e Contas Laranjas):* Um único operador de scalper pode criar automaticamente centenas de contas utilizando geradores de CPF ou dados vazados de terceiros, disparando compras simultâneas fingindo ser centenas de clientes diferentes.
  2. *Falha do Pressuposto 2 (Supremacia da Automação de Rede):* Scripts executados em instâncias de nuvem localizadas a poucos quilômetros dos *datacenters* da plataforma completam o handshake TLS e transmitem a ordem de compra em menos de 20 milissegundos. Um ser humano, operando por interfaces visuais, leva entre 2.000 e 4.000 milissegundos para reagir e clicar no botão, tornando o critério FIFO uma reserva de mercado monopolizada por robôs.

#### Tabela de Atores

| Ator | Objetivo | Ações ou capacidades | Informações observáveis | Restrições ou custos |
|---|---|---|---|---|
| **Operador de Scalper Bots (Atacante)** | Monopolizar o estoque promocional de 500 unidades para revenda lucrativa no mercado secundário com ágio. | Disparar requisições concorrentes massivas; alternar proxies residenciais; executar navegadores headless; burlar CAPTCHAs via IA; operar múltiplas contas laranjas. | Códigos de status HTTP (200, 403, 429); cabeçalhos de rede; tempo de latência; redirecionamentos para filas; status de estoque público. | Custo financeiro de proxies e solvers de CAPTCHA; custo de aquisição de contas/CPFs; risco de estorno e retenção financeira de capital. |
| **Motor de Defesa e Fila Justa (Defensor)** | Garantir a distribuição justa (1 un./CPF humano), manter a infraestrutura estável e maximizar a satisfação de clientes reais. | Aplicar Rate Limiting; rotear tráfego para salas de espera virtuais; exigir provas de trabalho (PoW) e CAPTCHA; validar CPFs; ordenar alocação por sorteio ponderado. | Volume e cadência de tráfego; fingerprints de rede/dispositivo; telemetria comportamental de navegação; histórico e dados de pagamento. | Custo computacional de servidores de defesa; risco de degradar a experiência do usuário autêntico com atrito; risco de falsos positivos (descartar clientes reais). |

#### Diagrama de Contexto

![Diagrama de Contexto](diagramas/contexto.png)

#### Natureza Adversarial do Caso
Este caso não constitui um problema de tráfego inesperado, bug acidental de concorrência ou falha fortuita de software. Trata-se de um **cenário estritamente adversarial** porque existe um agente consciente e racional cujos incentivos financeiros são potencializados pela quebra da equidade do sistema. O scalper estuda as regras de negócio da plataforma (como limites de carrinho e endpoints de API), mede a resposta do sistema a partir dos retornos de rede, projeta ferramentas específicas para explorar as premissas ingênuas de latência e adapta sua tecnologia ativamente sempre que uma nova defesa é implantada. O ganho privado do atacante decorre diretamente da perda de utilidade da plataforma e dos consumidores legítimos.
```

---

# 👤 Seções do Artur Wahlbrink Kraemer
* **Responsabilidade:** Seção 3.3 (Modelo Estratégico Dinâmico e Diagrama do Ciclo Adaptativo) e Seção 8 (Pergunta Final).

### Texto da Seção 3.3: Modelo Estratégico Dinâmico
```markdown
### 3.3 Modelo Estratégico Dinâmico

Expandindo a análise estática para um modelo iterado temporal, representamos a interação ao longo de **três rodadas consecutivas** guiadas pelo ciclo contínuo:
$$\text{Ação do Atacante} \longrightarrow \text{Resposta do Sistema} \longrightarrow \text{Observabilidade} \longrightarrow \text{Adaptação para a Próxima Rodada}$$

#### Ciclo de Rodadas Adversariais

| Rodada | Ação do participante (Scalper) | Resposta do sistema ou defensor (Plataforma) | O que se torna observável? | Adaptação para a rodada seguinte |
|:---:|---|---|---|---|
| **1** | **Força Bruta Monolítica:** Dispara flood de 1.000 requisições simultâneas por segundo contra o endpoint `/checkout` a partir de uma instância VPS em nuvem de alta largura de banda. | **Rate Limiting Estático por IP:** O API Gateway identifica o pico anômalo de conexões originadas do mesmo endereço IP e aplica bloqueio temporário retornando `HTTP 429 Too Many Requests`. | O código de status `HTTP 429`, o cabeçalho `Retry-After: 300` e a interrupção abrupta do handshake TCP. O atacante percebe que o bloqueio é estritamente baseado no endereço IP de origem. | **Pulverização de Infraestrutura:** O scalper abandona o servidor único e adquire acesso a um *pool* de proxies residenciais rotativos, distribuindo suas requisições por milhares de IPs de provedores de internet comerciais. |
| **2** | **Dispersão Geográfica e Cadência Furtiva:** Dispara requisições simultâneas distribuídas entre centenas de IPs residenciais distintos, contornando o *Rate Limiter* por IP e enviando dados cadastrais sintéticos. | **Fila Virtual (*Waiting Room*) com Desafio:** A plataforma redireciona o tráfego entrante para uma sala de espera que exige a execução de uma prova de trabalho criptográfica (PoW) e resolução de CAPTCHA interativo antes de conceder um token assinado temporário (`ticket_token`). | O redirecionamento `HTTP 302 Found` para a URL da fila virtual; requisições diretas de checkout recebem `HTTP 403 Forbidden` na ausência do token criptográfico assinado. O atacante descobre que requisições HTTP puras (*curl/requests*) não conseguem mais comprar. | **Automação Headless e Solvers de IA:** O scalper migra de scripts HTTP simples para frameworks de automação de navegadores completos (*headless* Playwright/Puppeteer), integrando serviços de resolução de CAPTCHA por visão computacional baseada em IA para emular um ambiente de navegador real. |
| **3** | **Bypass Automatizado de Desafios em Alta Velocidade:** Os navegadores automatizados executam o código JavaScript do desafio de PoW em ~800ms, resolvem o CAPTCHA via IA e submetem ordens de compra em massa logo no primeiro segundo de liberação da fila. | **Quebra da Política FIFO e Sorteio Ponderado:** A plataforma abandona o critério de ordem de chegada (FIFO). Estabelece uma janela de entrada de 3 minutos na qual todos os participantes recebem um bilhete com probabilidade uniforme; o estoque é alocado via **sorteio ponderado por reputação da conta**, exigindo validação de CPF na Receita e 2FA via SMS/App push. | A ordem de chegada na fila perde totalmente o valor; o tempo de confirmação da compra torna-se assíncrono e estocástico; o sistema passa a exigir digitação de código de validação em dois fatores enviado para o celular cadastrado. | **Ataques Sybil Físicos (Fazendas de SIM Cards e CPFs Reais):** O scalper passa a comprar identidades reais de terceiros e chips de telefonia física (fazendas de SMS) para validar as contas sorteadas. O custo operacional e de capital do ataque torna-se astronômico, forçando o atacante a abandonar o produto ou migrar para plataformas desprotegidas. |

#### Diagrama do Ciclo Adaptativo

![Diagrama do Ciclo Adaptativo](diagramas/ciclo-adaptativo.png)

#### Perguntas de Análise Dinâmica

* **Quem observa quem?**  
  O **Scalper observa a superfície externa da Plataforma** através de respostas da camada de aplicação e rede: códigos HTTP, cabeçalhos, tempos de resposta (*latency probing*), scripts clientes transmitidos e mensagens de sucesso/falha na interface.  
  A **Plataforma observa o comportamento agregado e singular dos Clientes**: telemetria de tráfego, concentração geográfica de IPs, assinaturas TLS/JA3, ordem de execução de eventos DOM no navegador e anomalias estatísticas de pedidos (como esgotamento de estoque em tempo incompatível com a cognição humana).

* **O que cada lado consegue mudar?**  
  O **Scalper consegue mudar:** a infraestrutura de origem (endereços IP, portas, provedores de tráfego), a tecnologia do cliente (scripts Python `requests` $\rightarrow$ navegadores `Chromium headless` $\rightarrow$ extensões injetadas), a cadência de requisições, o conteúdo dos formulários de cadastro e as contas de usuário utilizadas.  
  A **Plataforma consegue mudar:** as políticas de bloqueio de borda (limiares de *rate limit*), a arquitetura do fluxo de checkout (inserção de salas de espera virtuais e tokens dinâmicos), os mecanismos de prova de trabalho/humanidade (CAPTCHA, desafios matemáticos em JS), os fatores de autenticação exigidos (2FA) e as regras matemáticas de atribuição de estoque (de FIFO determinístico para sorteio probabilístico).

* **O que dispara uma adaptação?**  
  Do lado do **Scalper:** a perda de eficácia de seu ataque — receber códigos de erro (403, 429), constatar que suas requisições foram rejeitadas ou observar que o estoque esgotou para outros compradores antes de seus robôs concluírem o processo.  
  Do lado da **Plataforma:** a constatação empírica de violação de seus objetivos de negócio — esgotamento anômalo de 500 unidades em menos de 2 segundos, volume massivo de reclamações de consumidores legítimos nas redes sociais ou saturação dos recursos computacionais de banco de dados por requisições concorrentes não filtradas.

* **Qual é o custo da adaptação para cada lado?**  
  Para o **Scalper:** custo financeiro direto (pagamento por gigabyte em redes de proxies residenciais, assinatura de APIs de resolução de CAPTCHA, compra de contas e números de SMS descartáveis) e complexidade de desenvolvimento (manter scripts adaptados a cada alteração do site).  
  Para a **Plataforma:** custo financeiro de infraestrutura de nuvem e ferramentas corporativas de proteção contra bots; custo de engenharia de software para construir e calibrar fluxos complexos de checkout; e, criticamente, o **custo de atrito ao consumidor autêntico**, que é obrigado a esperar em filas, digitar códigos de SMS e resolver quebra-cabeças visuais.

* **Em que ponto pode surgir uma corrida armamentista?**  
  A corrida armamentista surge quando a defesa abandona regras determinísticas simples baseadas em atributos estáticos (como endereço IP ou User-Agent) e passa a adotar **análise comportamental e verificação de integridade de execução**. Nesse limiar, o atacante é forçado a desenvolver robôs que emulam com fidelidade quase perfeita a interação humana (movimentação estocástica do mouse com curvas de Bézier, variações no intervalo de digitação de teclas e renderização completa de canvas). Essa escalada atinge seu ápice quando a plataforma deixa de tentar distinguir tecnicamente humano de máquina na velocidade de rede e passa a impor **custos econômicos e de identidade física (sorteios com 2FA e CPF auditado)**, transformando uma batalha puramente computacional em uma disputa de viabilidade financeira.
```

### Texto da Seção 8: Pergunta Final
```markdown
## 8. Pergunta Final

> **"Depois que o sistema responder, o que o outro lado aprenderá e tentará fazer em seguida?"**

Ao término da terceira rodada, quando a plataforma implementa a defesa avançada de **Sorteio Ponderado por Reputação acoplado a Desafios Criptográficos e Verificação em Dois Fatores (2FA)**, o adversário aprende uma lição fundamental sobre a nova dinâmica do sistema:

1. **O que o atacante aprende:**
   * Ele aprende que a **vantagem de velocidade pura de rede e infraestrutura de servidores foi anulada**. Ter a menor latência em milissegundos não garante mais a captura dos produtos, pois a ordem cronológica de chegada (FIFO) deixou de ser o critério de atribuição de estoque;
   * Ele aprende que requisições automatizadas sem identidade humana comprovada (ou sem histórico transacional crível) são sumariamente descartadas ou recebem peso quase nulo no algoritmo de sorteio;
   * Ele aprende que o sistema agora correlaciona metadados de pagamento, documentos de CPF e números de telefone celular no momento da liquidação da compra.

2. **O que o atacante tentará fazer em seguida:**
   * O scalper profissional migrará seu vetor de ataque da **camada de concorrência de rede para a camada de engenharia social e economia de identidades físicas (*Human-in-the-Loop Sybil Farms*)**:
     * Em vez de rodar milhares de bots cegos, ele passará a recrutar e remunerar pessoas reais (redes de afiliados ou grupos fechados de revendedores em aplicativos de mensagens) que emprestam seus dados cadastrais, números de WhatsApp e cartões de crédito em troca de uma comissão fixa sobre o produto obtido;
     * Desenvolverá extensões de navegador personalizadas distribuídas para esses colaboradores humanos, onde o script automatiza apenas os cliques finais após o humano autenticar o 2FA e resolver o CAPTCHA de forma legítima (*assisted human checkout*);
     * Alternativamente, se o custo de manter essa rede de identidades humanas superar o lucro esperado na revenda dos 500 itens, o atacante racional **abandonará essa plataforma específica**, migrando seu arsenal de bots para concorrentes de menor maturidade técnica de segurança que ainda operam sob o modelo ingênuo de FIFO direto sem fila virtual.
```

---

# 👤 Seções do Gabriel Camargo Ortiz
* **Responsabilidade:** Seção 3.4 (Ameaças e Riscos, Superfície de Ataque e Matriz de Riscos) e Seção 6 (Declaração sobre Uso de IA Generativa).

### Texto da Seção 3.4: Ameaças e Riscos
```markdown
### 3.4 Ameaças e Riscos

#### Diagrama de Superfície de Ataque

![Diagrama de Superfície de Ataque](diagramas/superficie-de-ataque.png)

#### Pontos de Exploração Identificados

1. **[Ponto de Exploração 1] Endpoint de Checkout de Alta Concorrência (`POST /api/v1/checkout/orders`):**  
   Interface pública de aplicação responsável por processar a intenção final de compra. A vulnerabilidade reside na dependência de políticas cronológicas de rede (FIFO estrito) e na ausência de acoplamento estrito entre autorização prévia em sala de espera e a submissão final da ordem.
2. **[Ponto de Exploração 2] Serviço de Cadastro e Autenticação de Usuários (`POST /api/v1/auth/register`):**  
   Interface de entrada de novas contas na plataforma. A vulnerabilidade reside no baixo custo de entrada e na ausência de validação de prova de humanidade ou verificação estrita de documentos no ato do cadastro, permitindo ataques Sybil (criação automatizada de milhares de perfis laranjas).
3. **[Ponto de Exploração 3] Mecanismo de Bloqueio e Reserva Temporária de Carrinho (`PUT /api/v1/cart/reserve`):**  
   Componente de controle de concorrência de inventário que reserva unidades para o usuário durante o fluxo de preenchimento de endereço e pagamento (*holding lock*). A vulnerabilidade reside no tempo excessivo de reserva (ex.: 15 minutos) sem garantia de pagamento ou cobrança de caução, permitindo ataques de negação de estoque (*Denial of Inventory*).

#### Cenários de Ameaça

> *Um [ator] pode realizar [ação] por meio de [ponto de exploração], aproveitando [fraqueza ou pressuposto], causando [impacto] sobre [ativo ou propriedade].*

* **A1 (Scalping Massivo via Flood Concorrente):**  
  Um `operador de scalper bots` pode realizar `a submissão massiva de centenas de requisições de compra por segundo utilizando proxies residenciais` por meio do `endpoint público de checkout (/api/v1/checkout/orders)`, aproveitando a `dependência do sistema de métricas simplistas de IP e latência FIFO como critério de desempate`, causando o `esgotamento total do estoque de 500 unidades em milissegundos para um único agente especulador` sobre a `justiça distributiva (fair allocation) e a integridade da infraestrutura`.
* **A2 (Manipulação de Fila e Sorteio via Ataque Sybil):**  
  Um `atacante especulador` pode realizar a `criação e operação simultânea de centenas de perfis de usuários com dados sintéticos` por meio do `serviço público de cadastro de contas (/api/v1/auth/register)`, aproveitando o `pressuposto de que cada conta cadastrada representa uma pessoa física real independente`, causando a `apropriação desproporcional de bilhetes de sorteio e posições na fila virtual` sobre a `equidade na distribuição de recursos promocionais aos clientes autênticos`.
* **A3 (Sequestro de Estoque por Negação de Inventário):**  
  Um `grupo de bots concorrentes` pode realizar a `reserva sistemática de todo o estoque promocional em carrinhos de compras abandonados propositalmente` por meio do `mecanismo de reserva temporária de inventário (/api/v1/cart/reserve)`, aproveitando a `janela de tolerância excessiva de holding lock (15 minutos) sem exigência de caução ou pagamento antecipado`, causando a `indisponibilidade artificial dos produtos para consumidores reais durante a janela de pico promocional (OWASP OAT-009)` sobre a `disponibilidade do serviço e a receita comercial do marketplace`.

#### Avaliação de Riscos

> **Critérios de pontuação (Escala de 1 a 3):**  
> * **Probabilidade:** 1 = Baixa, 2 = Média, 3 = Alta.  
> * **Impacto:** 1 = Baixo, 2 = Médio, 3 = Alto.  
> * **Risco:** $\text{Probabilidade} \times \text{Impacto}$ (1 a 2 = Baixo; 3 a 5 = Médio; 6 a 9 = Crítico).

| ID | Cenário de ameaça | Ponto de exploração | Pressuposto ou fraqueza | Ativo afetado | Probabilidade (1-3) | Impacto (1-3) | Risco (1-9) |
|:---:|---|---|---|---|:---:|:---:|:---:|
| **A1** | Scalping Massivo via Flood Concorrente de Requisições | Endpoint de Checkout (`POST /checkout`) | FIFO estrito de rede e validação simples de IP | Justiça Distributiva e Disponibilidade | 3 | 3 | **9 (Crítico)** |
| **A2** | Manipulação de Fila e Sorteio via Ataque Sybil | Serviço de Cadastro (`POST /auth/register`) | Presunção de unicidade da identidade digital | Equidade na Distribuição | 3 | 2 | **6 (Alto)** |
| **A3** | Sequestro de Estoque por Negação de Inventário (*Denial of Inventory*) | Mecanismo de Reserva (`PUT /cart/reserve`) | Tempo excessivo de *holding lock* sem penalidade | Disponibilidade e Confiança | 2 | 2 | **4 (Médio)** |

---

#### Detalhamento da Ameaça de Maior Prioridade (A1 — Risco 9)

* **Ameaça Selecionada:** **A1 — Scalping Massivo via Flood Concorrente de Requisições** (Risco Crítico = 9).
* **Como o sistema poderia responder:**  
  A plataforma adota uma defesa em profundidade com quatro camadas interdependentes:
  1. *Camada de Borda:* Redirecionamento de todo o tráfego que tenta acessar a URL da promoção para uma **Sala de Espera Virtual (*Waiting Room*)** gerenciada na CDN, blindando o endpoint de checkout contra concorrência direta não autorizada.
  2. *Camada de Integridade:* Exigência da resolução de um desafio criptográfico dinâmico de *Proof-of-Work* (PoW) executado no navegador do usuário e de um CAPTCHA interativo com análise de telemetria comportamental (movimento de ponteiro e eventos de teclado).
  3. *Camada de Alocação Justa:* Concessão de um token assinado criptograficamente (`HMAC-SHA256`) com tempo de vida curto (ex.: 90 segundos) vinculado exclusivamente ao CPF do usuário autenticado. Quebra-se o FIFO: todos os usuários que entraram nos primeiros 3 minutos concorrem em um **Sorteio Ponderado por Reputação**, desarmando a vantagem de velocidade dos robôs.
* **Que informação essa resposta revelaria:**  
  A resposta do sistema revela abertamente ao atacante:
  * A existência e a duração da janela de tolerância de entrada na fila virtual (os 3 minutos);
  * Os algoritmos e a complexidade matemática do desafio de PoW e o fornecedor do serviço de CAPTCHA utilizado;
  * A estrutura e os parâmetros do token criptográfico (`ticket_token`), bem como seu prazo de validade (`expiration_timestamp`);
  * A confirmação de que tentativas de requisição direta ao endpoint sem o token prévio são rejeitadas com código `HTTP 403 Forbidden`.
* **Como o adversário poderia se adaptar na rodada seguinte:**  
  De posse dessas informações, o scalper não tenta mais disparar requisições brutas via terminal; ele adapta sua engenharia para:
  * Distribuir a execução de instâncias completas de navegadores *headless* (Playwright) em clusters de contêineres na nuvem, capazes de resolver o código JS do PoW de forma autônoma;
  * Contratar fazendas humanas ou APIs especializadas em visão computacional para quebrar os desafios de CAPTCHA dentro da janela de 3 minutos;
  * Operar centenas de contas autênticas de "laranjas" com CPFs válidos previamente adquiridos para obter múltiplos bilhetes no sorteio ponderado, aumentando probabilisticamente suas chances de captura.
* **Quais efeitos colaterais poderiam atingir usuários legítimos:**  
  A defesa gera impactos colaterais inevitáveis sobre os compradores autênticos:
  * *Aumento substancial da fricção cognitiva:* Usuários humanos são submetidos a testes visuais desgastantes (selecionar imagens, arrastar peças) e tempos de espera em salas virtuais;
  * *Sensação de incerteza e frustração:* A eliminação da ordem de chegada (FIFO) em favor do sorteio aleatório remove a sensação de recompensa do usuário que foi ágil e chegou cedo, gerando descontentamento;
  * *Risco de falsos positivos:* Consumidores com computadores mais lentos (que demoram a processar o PoW) ou navegando em conexões móveis instáveis podem ter seus tokens expirados ou ser erroneamente classificados como robôs, perdendo a oportunidade de compra.
* **Qual risco continuaria existindo após a resposta (Risco Residual):**  
  Mesmo com o sorteio ponderado e os desafios criptográficos ativados, **o risco residual não é nulo**. Operadores de scalper bots altamente capitalizados ainda conseguem operar uma rede de 50 a 100 contas com dados de terceiros e chips telefônicos reais, participando do sorteio com múltiplos bilhetes. O risco residual consiste na captura de 5% a 15% do inventário por esses operadores profissionais. Contudo, o impacto sistêmico é reduzido dramaticamente (de 100% de monopolização instantânea para uma fração marginal que inviabiliza cambistas amadores).
* **O que o sistema precisa continuar preservando apesar das adaptações:**  
  A plataforma deve manter vigilância estrita sobre três pilares essenciais:
  1. *A Acessibilidade do Consumidor Humano:* O nível de dificuldade dos desafios e o tempo de fila não podem ultrapassar o limite que leva o cliente legítimo ao abandono da plataforma;
  2. *A Conversão de Vendas dentro do Prazo:* A plataforma precisa garantir que as 500 unidades sejam efetivamente vendidas e pagas durante a janela do evento de Black Friday, evitando que produtos fiquem "presos" em reservas não concretizadas;
  3. *A Estabilidade Operacional do Gateway de Pagamentos:* As defesas devem filtrar o tráfego espúrio antes que ele atinja as adquirentes e processadoras de cartão, prevenindo bloqueios por suspeita de fraude bancária ou custos inflacionados por transações rejeitadas.
```

### Texto da Seção 6: Declaração sobre Uso de IA Generativa
```markdown
## 6. Declaração sobre Uso de IA Generativa

Em total conformidade com as diretrizes da Seção 6 do enunciado, o grupo declara a utilização de modelos de inteligência artificial generativa (Google Gemini / Antigravity Assistant) durante o desenvolvimento deste trabalho, nos seguintes termos:

### 1. Tarefas em que a IA Generativa foi Utilizada:
* Auxílio na formatação e padronização visual das tabelas e blocos em Markdown;
* Sugestão de roteiros e estruturas narrativas para o vídeo de apresentação com slides;
* Geração do esqueleto de scripts Python em `matplotlib` para renderização visual dos diagramas conceituais em formato PNG de alta resolução.

### 2. Metodologia de Verificação e Validação pelo Grupo:
* **Validação Conceitual dos Payoffs:** Todos os valores numéricos e deduções da matriz estática 2x2 foram revisados matematicamente pelos integrantes do grupo com base na bibliografia clássica de Teoria dos Jogos (Gibbons e Nash), assegurando que a dominância estrita e o Equilíbrio de Nash fossem demonstrados formalmente;
* **Conferência da Coerência das Rodadas Dinâmicas:** As transições entre as Rodadas 1, 2 e 3 foram confrontadas com arquiteturas reais de mitigação de tráfego de grandes provedores de segurança (Cloudflare e Akamai) para certificar a plausibilidade dos códigos de rede e vazamentos de informação;
* **Revisão Técnica das Ameaças:** Cada cenário de risco foi auditado contra a taxonomia oficial do projeto OWASP Automated Threats (OAT), garantindo que a distinção entre vulnerabilidade, ativo e impacto fosse estritamente preservada;
* **Autoria Intelectual e Domínio do Tema:** Todas as decisões arquiteturais, justificativas estratégicas e respostas às perguntas reflexivas foram amplamente discutidas, compreendidas e assumidas por todos os integrantes do grupo, que estão plenamente aptos a sustentá-las presencialmente e no vídeo de apresentação.
```
