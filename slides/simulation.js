/* ==========================================================================
   Simulação Visual de Concorrência Adversarial
   Sistema: IngressosFlash (500 Ingressos Promocionais com 80% de desconto)
   Cenários:
     1. FIFO Monolítico sem Defesa (Monopólio do Scalper)
     2. Fila Virtual Adaptativa + Sorteio Ponderado por Reputação + 2FA
   ========================================================================== */

(function () {
  const TOTAL_STOCK = 500;
  let animationTimer = null;
  let isRunning = false;

  // Elementos do DOM
  let gridContainer = null;
  let timeDisplay = null;
  let botCountDisplay = null;
  let humanCountDisplay = null;
  let stockRemainingDisplay = null;
  let fairnessDisplay = null;
  let gatewayStatusDisplay = null;
  let scenarioTitleEl = null;
  let step1El = null;
  let step2El = null;
  let step3El = null;
  let botBar = null;
  let humanBar = null;
  let dots = [];

  function initSimulation() {
    gridContainer = document.getElementById("stock-grid");
    timeDisplay = document.getElementById("sim-time");
    botCountDisplay = document.getElementById("sim-bots");
    humanCountDisplay = document.getElementById("sim-humans");
    stockRemainingDisplay = document.getElementById("sim-remaining");
    fairnessDisplay = document.getElementById("sim-fairness");
    gatewayStatusDisplay = document.getElementById("sim-gateway-status");
    scenarioTitleEl = document.getElementById("sim-scenario-title");
    step1El = document.getElementById("sim-step-1");
    step2El = document.getElementById("sim-step-2");
    step3El = document.getElementById("sim-step-3");
    botBar = document.getElementById("sim-bar-bots");
    humanBar = document.getElementById("sim-bar-humans");

    if (!gridContainer) return;

    // Renderizar os 500 pontos visuais de estoque (25 colunas x 20 linhas)
    gridContainer.innerHTML = "";
    dots = [];
    for (let i = 0; i < TOTAL_STOCK; i++) {
      const dot = document.createElement("div");
      dot.className = "stock-dot";
      dot.title = `Ingresso #${i + 1}`;
      gridContainer.appendChild(dot);
      dots.push(dot);
    }

    resetSimulation();
  }

  function resetSimulation() {
    if (animationTimer) {
      clearInterval(animationTimer);
      animationTimer = null;
    }
    isRunning = false;

    dots.forEach((dot) => {
      dot.className = "stock-dot";
    });

    if (timeDisplay) timeDisplay.textContent = "0 ms";
    if (botCountDisplay) botCountDisplay.textContent = "0 (0%)";
    if (humanCountDisplay) humanCountDisplay.textContent = "0 (0%)";
    if (stockRemainingDisplay) stockRemainingDisplay.textContent = "500 / 500";
    if (fairnessDisplay) {
      fairnessDisplay.className = "badge badge-blue";
      fairnessDisplay.textContent = "Aguardando Início da Promoção";
    }
    if (gatewayStatusDisplay) {
      gatewayStatusDisplay.className = "badge badge-blue";
      gatewayStatusDisplay.textContent = "Gateway Ocioso";
    }
    if (scenarioTitleEl) {
      scenarioTitleEl.textContent = "Fases da Interação Adversarial:";
    }
    if (step1El) {
      step1El.className = "sim-step";
      step1El.innerHTML = "<strong>1. Selecione um cenário</strong> nos botões acima para iniciar.";
    }
    if (step2El) {
      step2El.className = "sim-step";
      step2El.innerHTML = "<strong>2. Três fases explicativas</strong> serão apresentadas sequencialmente.";
    }
    if (step3El) {
      step3El.className = "sim-step";
      step3El.innerHTML = "<strong>3. Acompanhe a ocupação</strong> dos 500 ingressos no painel.";
    }
    if (botBar) botBar.style.width = "0%";
    if (humanBar) humanBar.style.width = "0%";
  }

  // CENÁRIO 1: FIFO Desprotegido
  // Cadência mais lenta e controlada com 3 fases permanentes
  function runScenario1() {
    if (isRunning) resetSimulation();
    isRunning = true;

    if (gatewayStatusDisplay) {
      gatewayStatusDisplay.className = "badge badge-red";
      gatewayStatusDisplay.textContent = "FIFO Direto: Concorrência por ordem de chegada";
    }
    if (fairnessDisplay) {
      fairnessDisplay.className = "badge badge-amber";
      fairnessDisplay.textContent = "Processando requisições em alta concorrência...";
    }

    if (scenarioTitleEl) {
      scenarioTitleEl.textContent = "Cenário 1: FIFO Puro (Sem Defesas)";
    }
    if (step1El) {
      step1El.className = "sim-step active";
      step1El.innerHTML = "<strong>1. Disparo Concorrente:</strong> Scripts automatizados chegam a 1.000 req/s a partir de servidores em nuvem, disputando o endpoint de checkout.";
    }
    if (step2El) {
      step2El.className = "sim-step";
      step2El.innerHTML = "<strong>2. Absorção por Latência:</strong> Conexões de bots fecham em ~50 ms. O lote de 500 ingressos é completamente absorvido antes do primeiro segundo.";
    }
    if (step3El) {
      step3El.className = "sim-step";
      step3El.innerHTML = "<strong>3. Falha Distributiva:</strong> Usuários humanos chegam com latência de 2 a 3 segundos e encontram HTTP 409 (Esgotado). Monopólio de 100% pelos bots.";
    }

    let elapsed = 0;
    let allocated = 0;
    const stepDuration = 50; // 50ms por tick
    const batchSize = 7;     // ~7 ingressos por tick -> ~3.5 segundos total de simulação

    animationTimer = setInterval(() => {
      elapsed += stepDuration;
      const currentBatch = Math.min(batchSize, TOTAL_STOCK - allocated);

      for (let i = 0; i < currentBatch; i++) {
        dots[allocated + i].className = "stock-dot dot-bot";
      }
      allocated += currentBatch;

      const remaining = TOTAL_STOCK - allocated;
      const botPct = ((allocated / TOTAL_STOCK) * 100).toFixed(0);

      timeDisplay.textContent = `${elapsed} ms`;
      botCountDisplay.textContent = `${allocated} (${botPct}%)`;
      humanCountDisplay.textContent = "0 (0%)";
      stockRemainingDisplay.textContent = `${remaining} / 500`;
      if (botBar) botBar.style.width = `${botPct}%`;

      if (allocated >= TOTAL_STOCK * 0.45 && step2El && !step2El.classList.contains("active")) {
        step1El.className = "sim-step";
        step2El.className = "sim-step active";
      }

      if (allocated >= TOTAL_STOCK) {
        clearInterval(animationTimer);
        animationTimer = null;
        isRunning = false;

        if (fairnessDisplay) {
          fairnessDisplay.className = "badge badge-red";
          fairnessDisplay.textContent = "Falha Distributiva: 100% monopolizado por bots";
        }
        if (gatewayStatusDisplay) {
          gatewayStatusDisplay.className = "badge badge-red";
          gatewayStatusDisplay.textContent = "Estoque Esgotado: Humanos receberam HTTP 409 Conflict";
        }
        if (step2El) step2El.className = "sim-step";
        if (step3El) step3El.className = "sim-step danger";
      }
    }, stepDuration);
  }

  // CENÁRIO 2: Fila Adaptativa + Sorteio Ponderado por Reputação + 2FA
  // Distribuição estocástica uniforme de 435 humanos (87%) e 65 bots residuais (13%)
  function runScenario2() {
    if (isRunning) resetSimulation();
    isRunning = true;

    // Gerar e embaralhar aleatoriamente os 500 bilhetes com Fisher-Yates
    const targetHumans = 435;
    const targetBots = 65;
    const ticketTypes = [];

    for (let i = 0; i < targetHumans; i++) ticketTypes.push("human");
    for (let i = 0; i < targetBots; i++) ticketTypes.push("bot");

    for (let i = ticketTypes.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      const temp = ticketTypes[i];
      ticketTypes[i] = ticketTypes[j];
      ticketTypes[j] = temp;
    }

    if (gatewayStatusDisplay) {
      gatewayStatusDisplay.className = "badge badge-amber";
      gatewayStatusDisplay.textContent = "Fila Virtual Ativa: Retendo conexões na Sala de Espera (PoW & Token)";
    }
    if (fairnessDisplay) {
      fairnessDisplay.className = "badge badge-blue";
      fairnessDisplay.textContent = "Janela de Espera (3 minutos)...";
    }

    if (scenarioTitleEl) {
      scenarioTitleEl.textContent = "Cenário 2: Fila Adaptativa + Sorteio + 2FA";
    }
    if (step1El) {
      step1El.className = "sim-step active";
      step1El.innerHTML = "<strong>1. Contenção na Sala de Espera:</strong> O tráfego não toca o banco diretamente. A borda retém requisições na fila, exige PoW e descarta chamadas sem token assinado.";
    }
    if (step2El) {
      step2El.className = "sim-step";
      step2El.innerHTML = "<strong>2. Quebra do FIFO (Sorteio Ponderado):</strong> A velocidade de rede deixa de garantir a compra. A plataforma sorteia vagas priorizando contas com histórico e reputação.";
    }
    if (step3El) {
      step3El.className = "sim-step";
      step3El.innerHTML = "<strong>3. Validação 2FA & Alocação Justa:</strong> Desafio SMS/Push barra automação barata. 87% (435 un.) vão para consumidores legítimos, restando apenas 13% (65 un.) para bots com identidades adquiridas.";
    }

    let elapsed = 0;
    let phase = 1; // 1 = Sala de espera, 2 = Sorteio Ponderado e 2FA
    let currentIndex = 0;
    let humansAllocated = 0;
    let botsAllocated = 0;

    animationTimer = setInterval(() => {
      elapsed += 50;
      timeDisplay.textContent = `${(elapsed / 1000).toFixed(1)} s`;

      if (phase === 1) {
        // Simulação da sala de espera por 1.8 segundos
        if (elapsed >= 1800) {
          phase = 2;
          if (gatewayStatusDisplay) {
            gatewayStatusDisplay.className = "badge badge-green";
            gatewayStatusDisplay.textContent = "Janela Aberta: Sorteio Ponderado e Validação 2FA via SMS";
          }
          if (step1El) step1El.className = "sim-step";
          if (step2El) step2El.className = "sim-step active";
        }
      } else if (phase === 2) {
        // Alocar lote cadenciado de 6 bilhetes por tick (~4.2 segundos total)
        const batch = Math.min(6, TOTAL_STOCK - currentIndex);

        for (let b = 0; b < batch; b++) {
          const type = ticketTypes[currentIndex + b];
          if (type === "human") {
            dots[currentIndex + b].className = "stock-dot dot-human";
            humansAllocated++;
          } else {
            dots[currentIndex + b].className = "stock-dot dot-bot";
            botsAllocated++;
          }
        }

        currentIndex += batch;
        const remaining = TOTAL_STOCK - currentIndex;
        const humanPct = ((humansAllocated / TOTAL_STOCK) * 100).toFixed(0);
        const botPct = ((botsAllocated / TOTAL_STOCK) * 100).toFixed(0);

        botCountDisplay.textContent = `${botsAllocated} (${botPct}%)`;
        humanCountDisplay.textContent = `${humansAllocated} (${humanPct}%)`;
        stockRemainingDisplay.textContent = `${remaining} / 500`;

        if (botBar) botBar.style.width = `${botPct}%`;
        if (humanBar) humanBar.style.width = `${humanPct}%`;

        if (currentIndex >= TOTAL_STOCK * 0.7 && step3El && !step3El.classList.contains("active")) {
          if (step2El) step2El.className = "sim-step";
          if (step3El) step3El.className = "sim-step active";
        }

        if (currentIndex >= TOTAL_STOCK) {
          clearInterval(animationTimer);
          animationTimer = null;
          isRunning = false;

          if (fairnessDisplay) {
            fairnessDisplay.className = "badge badge-green";
            fairnessDisplay.textContent = "Justiça Preservada: 87% alocado para consumidores reais";
          }
          if (gatewayStatusDisplay) {
            gatewayStatusDisplay.className = "badge badge-green";
            gatewayStatusDisplay.textContent = "Alocação Concluída: 435 legítimos vs 65 residuais";
          }
          if (step2El) step2El.className = "sim-step";
          if (step3El) step3El.className = "sim-step success";
        }
      }
    }, 50);
  }

  // Exportar funções globais para os botões do slide
  window.runSimulationScenario1 = runScenario1;
  window.runSimulationScenario2 = runScenario2;
  window.resetSimulation = resetSimulation;

  document.addEventListener("DOMContentLoaded", () => {
    initSimulation();
  });

  if (window.Reveal) {
    window.Reveal.on("slidechanged", (event) => {
      if (event.currentSlide && event.currentSlide.querySelector("#stock-grid")) {
        if (dots.length === 0) initSimulation();
      }
    });
  }
})();
