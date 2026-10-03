# Fontes e Referências Bibliográficas

Este documento reúne o referencial teórico, as normas de segurança em aplicações, os materiais didáticos da disciplina e a documentação técnica consultadas para a elaboração da análise adversarial do sistema de **Flash Sale de Black Friday (*Scalper Bots vs. Fair Checkout Engine*)**.

---

## 1. Material Didático e Aulas da Disciplina (UNIPAMPA)

1. **QUINCOZES, Silvio Ereno.** *Aulas, Notas de Estudo e Videoaulas da Disciplina de Engenharia de Software Seguro e Engenharia de Software Adversarial*. Universidade Federal do Pampa (UNIPAMPA), Campus Alegrete. Programa de Pós-Graduação em Engenharia de Software (PPGES) e Bacharelado em Engenharia de Software.
   * *Contribuição Principal:* Conceituação basilar de Engenharia de Software Adversarial versus Engenharia de Software Tradicional (o paradoxo da suposição cooperativa); formulação do ciclo adaptativo (*ação $\rightarrow$ resposta $\rightarrow$ observação $\rightarrow$ adaptação*); modelagem de incentivos e payoffs; armadilhas do Equilíbrio de Nash em sistemas de segurança; taxonomia de superfícies de ataque e avaliação de impacto e probabilidade.
   * *Aulas e Vídeos Consultados:* Videoaulas expositivas e seminários da disciplina sobre modelagem de jogos simultâneos e dinâmicos, ameaças automatizadas e mitigação arquitetural de abusos em sistemas distribuídos.

---

## 2. Referências Teóricas (Teoria dos Jogos e Engenharia Adversarial)

1. **NASH, John.** *Equilibrium Points in N-Person Games*. Proceedings of the National Academy of Sciences, v. 36, n. 1, p. 48-49, 1950.
   * *Contribuição:* Fundamentação teórica do conceito de Equilíbrio de Nash e modelagem de estratégias estáticas sob interdependência de escolhas.

2. **GIBBONS, Robert.** *Game Theory for Applied Economists*. Princeton University Press, 1992.
   * *Contribuição:* Metodologia para cálculo de matrizes de payoff normais (2x2), eliminação de estratégias estritamente dominadas e análise de jogos repetidos e dinâmicos.

3. **AXELROD, Robert.** *The Evolution of Cooperation*. Basic Books, 1984.
   * *Contribuição:* Análise da corrida armamentista e dinâmica iterada do Dilema do Prisioneiro em ambientes com agentes egoístas e racionais.

4. **ANDERSON, Ross.** *Security Engineering: A Guide to Building Dependable Distributed Systems*. 3. ed. Indianapolis: John Wiley & Sons, 2020.
   * *Contribuição:* Capítulo sobre economia da segurança da informação, incentivos assimétricos de atacantes e falhas decorrentes do desalinhamento entre quem assume o custo e quem aufere o benefício.

---

## 3. Padrões de Segurança da Informação e Modelagem de Ameaças

1. **OWASP (Open Web Application Security Project).** *OWASP Automated Threats to Web Applications*. Versão 2.0, 2020.
   * **OAT-005 (Scalping):** Aquisição massiva e automatizada de bens e serviços escassos antes de usuários humanos.
   * **OAT-009 (Denial of Inventory):** Esgotamento ou bloqueio temporário de estoque via reservas artificiais no carrinho.
   * **OAT-013 (Sniping):** Monitoramento contínuo e submissão automatizada de lances ou requisições de compra no último instante disponível.
   * **OAT-019 (Account Creation):** Criação automatizada de múltiplas contas sintéticas para contornar limites por usuário (ataque Sybil).

2. **SHOSTACK, Adam.** *Threat Modeling: Designing for Security*. Indianapolis: John Wiley & Sons, 2014.
   * *Contribuição:* Aplicação da metodologia de mapeamento de superfícies de ataque, identificação de fraquezas arquiteturais e matriz de probabilidade versus impacto.

---

## 4. Documentação Técnica da Indústria e Estudos de Caso

1. **CLOUDFLARE.** *Stopping Scalpers: Architectural Approaches to Defend Limited Inventory Drops*. Cloudflare Learning Center & Technical Reports, 2023. Disponível em: <https://www.cloudflare.com/learning/bots/what-is-ticket-scalping/>.
   * *Contribuição:* Análise de detecção de bots por fingerprinting de TLS (JA3/JA4), desafios gerenciados de Proof-of-Work (PoW) e mitigação de redes de proxies residenciais.

2. **QUEUE-IT.** *The Anatomy of Fair Queue Systems for High-Demand E-Commerce Drops*. Technical Whitepaper, 2022. Disponível em: <https://queue-it.com/white-papers/>.
   * *Contribuição:* Desenho arquitetural de salas de espera virtuais (*virtual waiting rooms*), emissão de tokens criptografados e transição de filas cronológicas (FIFO) para sorteios aleatórios ponderados (*fair ballot*).

3. **AKAMAI TECHNOLOGIES.** *The Scourge of Scalper Bots: Analyzing Traffic Spikes and Automated Abuse during Global E-Commerce Events*. Akamai State of the Internet / Security Report, 2023.
   * *Contribuição:* Dados empíricos sobre volume de requisições maliciosas em picos promocionais de Black Friday e comportamento de navegadores *headless* emulando telemetria humana.
