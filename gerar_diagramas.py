#!/usr/bin/env python3
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('diagramas', exist_ok=True)

# -------------------------------------------------------------
# 1. DIAGRAMA DE CONTEXTO
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

# Título
plt.suptitle("Diagrama de Contexto: Sistema de Flash Sale sob Ameaça Adversarial", fontsize=18, fontweight='bold', y=0.96, color='#0f172a')
plt.title("Interação Concorrente de Compra de Itens Escassos (Scalper Bots vs. E-commerce Fair Allocation)", fontsize=11, color='#475569', pad=15)

# Bounding box Plataforma
rect_plat = patches.FancyBboxPatch((4.2, 0.8), 7.6, 6.4, boxstyle="round,pad=0.2", ec="#2563eb", fc="#eff6ff", lw=2, linestyle='--')
ax.add_patch(rect_plat)
ax.text(8.0, 7.0, "Plataforma de E-Commerce (Perímetro Defensivo)", fontsize=13, fontweight='bold', color='#1e40af', ha='center')

# Atores Externos
# 1. Consumidor Legítimo
box_leg = patches.FancyBboxPatch((0.4, 4.6), 3.2, 1.8, boxstyle="round,pad=0.15", ec="#16a34a", fc="#f0fdf4", lw=2)
ax.add_patch(box_leg)
ax.text(2.0, 5.8, "Consumidor Legítimo\n(Cliente Real)", fontsize=11, fontweight='bold', color='#166534', ha='center', va='center')
ax.text(2.0, 5.0, "• Interface Web / App Mobile\n• Digitação Humana (latência 2-4s)\n• Compra para uso próprio (1 un.)", fontsize=8.5, color='#14532d', ha='center', va='center')

# 2. Scalper Botnet
box_sc = patches.FancyBboxPatch((0.4, 1.4), 3.2, 2.0, boxstyle="round,pad=0.15", ec="#dc2626", fc="#fef2f2", lw=2)
ax.add_patch(box_sc)
ax.text(2.0, 2.7, "Operador de Scalper Bots\n(Atacante Estratégico)", fontsize=11, fontweight='bold', color='#991b1b', ha='center', va='center')
ax.text(2.0, 1.9, "• Requisições HTTP concorrentes\n• Pool de Proxies Residenciais\n• Latência de rede < 30ms\n• Múltiplas contas laranjas (Sybil)", fontsize=8.5, color='#7f1d1d', ha='center', va='center')

# Componentes Internos
# WAF / API Gateway
box_waf = patches.FancyBboxPatch((4.6, 4.4), 3.0, 1.6, boxstyle="round,pad=0.15", ec="#3b82f6", fc="#ffffff", lw=1.5)
ax.add_patch(box_waf)
ax.text(6.1, 5.4, "Borda & API Gateway", fontsize=11, fontweight='bold', color='#1e3a8a', ha='center', va='center')
ax.text(6.1, 4.8, "• Rate Limiting por IP\n• Fingerprinting TLS/JA3\n• Filtro de GeoIP e Reputação", fontsize=8.5, color='#334155', ha='center', va='center')

# Fila Virtual / PoW
box_q = patches.FancyBboxPatch((8.4, 4.4), 3.0, 1.6, boxstyle="round,pad=0.15", ec="#3b82f6", fc="#ffffff", lw=1.5)
ax.add_patch(box_q)
ax.text(9.9, 5.4, "Fila Virtual & Desafio", fontsize=11, fontweight='bold', color='#1e3a8a', ha='center', va='center')
ax.text(9.9, 4.8, "• Waiting Room (Queue-it)\n• Desafio PoW e CAPTCHA\n• Emissão de Token Assinado", fontsize=8.5, color='#334155', ha='center', va='center')

# Checkout Service
box_chk = patches.FancyBboxPatch((4.6, 1.4), 3.0, 1.8, boxstyle="round,pad=0.15", ec="#3b82f6", fc="#ffffff", lw=1.5)
ax.add_patch(box_chk)
ax.text(6.1, 2.5, "Motor de Checkout", fontsize=11, fontweight='bold', color='#1e3a8a', ha='center', va='center')
ax.text(6.1, 1.8, "• Validação de Token de Fila\n• Validação de CPF e 2FA\n• Sorteio Ponderado / Ballot\n• Processamento de Pagamento", fontsize=8.5, color='#334155', ha='center', va='center')

# Estoque Atômico
box_est = patches.FancyBboxPatch((8.4, 1.4), 3.0, 1.8, boxstyle="round,pad=0.15", ec="#3b82f6", fc="#ffffff", lw=1.5)
ax.add_patch(box_est)
ax.text(9.9, 2.5, "Inventário de Estoque", fontsize=11, fontweight='bold', color='#1e3a8a', ha='center', va='center')
ax.text(9.9, 1.8, "• Estoque Escasso (500 un.)\n• Controle Atômico (Redis/Locks)\n• Expiração Curta de Holding\n• Registro de Auditoria", fontsize=8.5, color='#334155', ha='center', va='center')

# Mercado Secundário
box_mkt = patches.FancyBboxPatch((12.4, 2.2), 2.8, 2.6, boxstyle="round,pad=0.15", ec="#d97706", fc="#fffbeb", lw=2)
ax.add_patch(box_mkt)
ax.text(13.8, 3.8, "Mercado Secundário\n(Revenda Externa)", fontsize=11, fontweight='bold', color='#92400e', ha='center', va='center')
ax.text(13.8, 2.8, "• Marketplaces paralelos\n• Venda com ágio de 200-400%\n• Extração do excedente\n  econômico do consumidor", fontsize=8.5, color='#78350f', ha='center', va='center')

# Setas e Conexões
arrowprops = dict(arrowstyle="->", lw=1.8, color="#0f172a", shrinkA=4, shrinkB=4)

ax.annotate("Requisição de Compra", xy=(4.6, 5.3), xytext=(3.6, 5.3), arrowprops=arrowprops, fontsize=8, color="#166534", fontweight="bold")
ax.annotate("Flood Massivo", xy=(4.6, 4.6), xytext=(3.6, 2.8), arrowprops=dict(arrowstyle="->", lw=1.8, color="#dc2626"), fontsize=8, color="#dc2626", fontweight="bold")
ax.annotate("Triagem / Redirecionamento", xy=(8.4, 5.2), xytext=(7.6, 5.2), arrowprops=arrowprops, fontsize=8, color="#1e3a8a")
ax.annotate("Liberação com Token", xy=(6.1, 3.2), xytext=(8.4, 4.5), arrowprops=dict(arrowstyle="->", lw=1.8, color="#1e3a8a"), fontsize=8, color="#1e3a8a")
ax.annotate("Decremento Atômico", xy=(8.4, 2.3), xytext=(7.6, 2.3), arrowprops=arrowprops, fontsize=8, color="#1e3a8a")

# Seta de scalper para mercado secundário e consumidor
ax.annotate("Monopolização e Especulação", xy=(13.8, 4.8), xytext=(2.0, 3.4),
            arrowprops=dict(arrowstyle="->", lw=1.5, color="#d97706", linestyle=":", connectionstyle="arc3,rad=-0.4"),
            fontsize=8.5, color="#b45309", fontweight="bold")
ax.annotate("Preço Inflacionado", xy=(2.0, 4.6), xytext=(12.4, 3.6),
            arrowprops=dict(arrowstyle="->", lw=1.5, color="#d97706", linestyle=":", connectionstyle="arc3,rad=0.35"),
            fontsize=8.5, color="#b45309", fontweight="bold")

ax.set_xlim(0, 15.6)
ax.set_ylim(0.4, 7.6)
ax.axis('off')

plt.tight_layout()
plt.savefig('diagramas/contexto.png', dpi=300, bbox_inches='tight')
plt.close()
print("Contexto gerado com sucesso!")

# -------------------------------------------------------------
# 2. DIAGRAMA DO CICLO ADAPTATIVO (3 RODADAS)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

plt.suptitle("Diagrama do Ciclo Adaptativo: A Corrida Armamentista em 3 Rodadas", fontsize=18, fontweight='bold', y=0.96, color='#0f172a')
plt.title("Ação → Resposta → Observabilidade → Adaptação (Scalper Bots vs. E-Commerce)", fontsize=11, color='#475569', pad=15)

rounds = [
    {
        "rodada": "RODADA 1: Força Bruta vs. Rate Limit Estático",
        "cor": "#ef4444",
        "bg": "#fef2f2",
        "acao": "Scalper dispara flood de 1.000 req/s\na partir de único IP em VPS em nuvem.",
        "resposta": "API Gateway detecta volume anômalo\ne aplica Rate Limiting estático por IP.",
        "obs": "Status HTTP 429 (Too Many Requests),\nRetry-After header e corte de conexão.",
        "adapt": "Scalper contrata rede de proxies residenciais\nrotativos (pulverização em milhares de IPs)."
    },
    {
        "rodada": "RODADA 2: Pulverização de IPs vs. Fila com Desafio de Integridade",
        "cor": "#f59e0b",
        "bg": "#fffbeb",
        "acao": "Requisições simultâneas via 1.000 IPs residenciais\ncom cadastros sintéticos (contornando rate limit de IP).",
        "resposta": "Plataforma ativa Fila Virtual (Waiting Room)\ncom desafio PoW e CAPTCHA antes do checkout.",
        "obs": "Redirecionamento HTTP 302 para fila;\nHTTP 403 se tentar checkout sem token assinado.",
        "adapt": "Scalper adota automação de navegadores headless\n(Puppeteer) + serviços de IA para resolver CAPTCHAs."
    },
    {
        "rodada": "RODADA 3: Guerra de Latência vs. Sorteio Ponderado (Quebra do FIFO)",
        "cor": "#3b82f6",
        "bg": "#eff6ff",
        "acao": "Bots resolvem desafios em ~1s e tomam\nas primeiras posições da fila por latência superior.",
        "resposta": "Plataforma quebra regra FIFO: janela de 3 min,\nSorteio Ponderado por Reputação, CPF e 2FA.",
        "obs": "Ordem de chegada perde valor; compras exigem 2FA\ne auditoria de documento na Receita.",
        "adapt": "Ataques Sybil com CPFs e chips SIM reais comprados.\nCusto operacional extremo: ataque torna-se inviável."
    }
]

y_pos = [6.2, 3.5, 0.8]

for i, r in enumerate(rounds):
    y = y_pos[i]
    
    # Header da rodada
    header_box = patches.FancyBboxPatch((0.5, y + 1.8), 13.0, 0.45, boxstyle="round,pad=0.08", ec=r["cor"], fc=r["cor"])
    ax.add_patch(header_box)
    ax.text(7.0, y + 2.02, r["rodada"], fontsize=11, fontweight='bold', color="#ffffff", ha='center', va='center')
    
    # 4 Etapas
    etapas = [
        ("1. Ação do Atacante", r["acao"], 0.5, "#dc2626", "#fee2e2"),
        ("2. Resposta do Defensor", r["resposta"], 3.8, "#2563eb", "#dbeafe"),
        ("3. O que é Observável?", r["obs"], 7.1, "#d97706", "#fef3c7"),
        ("4. Adaptação Próxima Rodada", r["adapt"], 10.4, "#16a34a", "#dcfce7")
    ]
    
    for titulo, desc, x, c_borda, c_fundo in etapas:
        box = patches.FancyBboxPatch((x, y), 3.1, 1.7, boxstyle="round,pad=0.1", ec=c_borda, fc=c_fundo, lw=1.5)
        ax.add_patch(box)
        ax.text(x + 1.55, y + 1.4, titulo, fontsize=9.5, fontweight='bold', color=c_borda, ha='center', va='center')
        ax.text(x + 1.55, y + 0.65, desc, fontsize=8, color="#1e293b", ha='center', va='center', multialignment='center')
        
        # Seta entre passos
        if x < 10.4:
            ax.annotate("", xy=(x + 3.75, y + 0.85), xytext=(x + 3.15, y + 0.85),
                        arrowprops=dict(arrowstyle="->", lw=1.8, color="#64748b"))

    # Seta de transição entre rodadas
    if i < 2:
        ax.annotate("Escalação Adversarial", xy=(7.0, y - 0.15), xytext=(7.0, y - 0.55),
                    arrowprops=dict(arrowstyle="->", lw=2, color="#475569", linestyle="--"),
                    fontsize=8.5, fontweight="bold", color="#475569", ha='center', va='center')

ax.set_xlim(0, 14.0)
ax.set_ylim(0.2, 9.2)
ax.axis('off')

plt.tight_layout()
plt.savefig('diagramas/ciclo-adaptativo.png', dpi=300, bbox_inches='tight')
plt.close()
print("Ciclo adaptativo gerado com sucesso!")

# -------------------------------------------------------------
# 3. DIAGRAMA DE SUPERFÍCIE DE ATAQUE
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
ax.set_facecolor('#f8fafc')
fig.patch.set_facecolor('#ffffff')

plt.suptitle("Diagrama de Superfície de Ataque e Pontos de Exploração", fontsize=18, fontweight='bold', y=0.96, color='#0f172a')
plt.title("Mapeamento de Interfaces Expostas, Fraquezas Exploradas, Controles e Impactos", fontsize=11, color='#475569', pad=15)

colunas = [
    ("Vetores de Ameaça (Atacante)", 0.6, 2.8, "#fee2e2", "#dc2626"),
    ("Pontos de Exploração (Interfaces)", 3.9, 3.4, "#fef3c7", "#d97706"),
    ("Controles de Mitigação", 7.8, 3.2, "#dbeafe", "#2563eb"),
    ("Ativos Impactados", 11.5, 2.5, "#dcfce7", "#16a34a")
]

for col_titulo, x, w, bg, cor in colunas:
    c_box = patches.FancyBboxPatch((x, 6.7), w, 0.45, boxstyle="round,pad=0.08", ec=cor, fc=cor)
    ax.add_patch(c_box)
    ax.text(x + w/2, 6.92, col_titulo, fontsize=10, fontweight='bold', color="#ffffff", ha='center', va='center')

# Itens da Coluna 1: Vetores
v1 = patches.FancyBboxPatch((0.6, 4.6), 2.8, 1.8, boxstyle="round,pad=0.1", ec="#dc2626", fc="#ffffff", lw=1.5)
ax.add_patch(v1)
ax.text(2.0, 5.8, "Vetor 1: Botnet Distribuída", fontsize=9.5, fontweight='bold', color="#991b1b", ha='center')
ax.text(2.0, 5.0, "• Scripts HTTP assíncronos\n• Proxies residenciais rotativos\n• Requisições paralelas maciças", fontsize=8, color="#334155", ha='center')

v2 = patches.FancyBboxPatch((0.6, 2.5), 2.8, 1.8, boxstyle="round,pad=0.1", ec="#dc2626", fc="#ffffff", lw=1.5)
ax.add_patch(v2)
ax.text(2.0, 3.7, "Vetor 2: Automação Sybil", fontsize=9.5, fontweight='bold', color="#991b1b", ha='center')
ax.text(2.0, 2.9, "• Centenas de contas falsas\n• Geração de dados sintéticos\n• Fazendas de chips/SMS", fontsize=8, color="#334155", ha='center')

v3 = patches.FancyBboxPatch((0.6, 0.4), 2.8, 1.8, boxstyle="round,pad=0.1", ec="#dc2626", fc="#ffffff", lw=1.5)
ax.add_patch(v3)
ax.text(2.0, 1.6, "Vetor 3: Denial of Inventory", fontsize=9.5, fontweight='bold', color="#991b1b", ha='center')
ax.text(2.0, 0.8, "• Bloqueio temporário de estoque\n• Retenção sem finalização\n• Especulação e estresse de venda", fontsize=8, color="#334155", ha='center')

# Itens da Coluna 2: Pontos de Exploração
p1 = patches.FancyBboxPatch((3.9, 4.6), 3.4, 1.8, boxstyle="round,pad=0.1", ec="#d97706", fc="#ffffff", lw=1.5)
ax.add_patch(p1)
ax.text(5.6, 6.0, "[PONTO 1] Endpoint de Checkout", fontsize=9.5, fontweight='bold', color="#b45309", ha='center')
ax.text(5.6, 5.6, "POST /api/v1/checkout/orders", fontsize=8.5, family="monospace", color="#b45309", ha='center')
ax.text(5.6, 4.9, "Fraqueza: FIFO estrito e latência\ncomo critério único de alocação.", fontsize=8, color="#334155", ha='center')

p2 = patches.FancyBboxPatch((3.9, 2.5), 3.4, 1.8, boxstyle="round,pad=0.1", ec="#d97706", fc="#ffffff", lw=1.5)
ax.add_patch(p2)
ax.text(5.6, 3.9, "[PONTO 2] Serviço de Contas", fontsize=9.5, fontweight='bold', color="#b45309", ha='center')
ax.text(5.6, 3.5, "POST /api/v1/auth/register", fontsize=8.5, family="monospace", color="#b45309", ha='center')
ax.text(5.6, 2.8, "Fraqueza: Cadastro sem custo ou\nvalidação biométrica prévia.", fontsize=8, color="#334155", ha='center')

p3 = patches.FancyBboxPatch((3.9, 0.4), 3.4, 1.8, boxstyle="round,pad=0.1", ec="#d97706", fc="#ffffff", lw=1.5)
ax.add_patch(p3)
ax.text(5.6, 1.8, "[PONTO 3] Reserva de Carrinho", fontsize=9.5, fontweight='bold', color="#b45309", ha='center')
ax.text(5.6, 1.4, "PUT /api/v1/cart/reserve", fontsize=8.5, family="monospace", color="#b45309", ha='center')
ax.text(5.6, 0.7, "Fraqueza: Holding lock com tempo\nexcessivo sem penalidade.", fontsize=8, color="#334155", ha='center')

# Itens da Coluna 3: Controles
c1 = patches.FancyBboxPatch((7.8, 4.6), 3.2, 1.8, boxstyle="round,pad=0.1", ec="#2563eb", fc="#ffffff", lw=1.5)
ax.add_patch(c1)
ax.text(9.4, 5.8, "Controle 1: Fila & Sorteio", fontsize=9.5, fontweight='bold', color="#1e40af", ha='center')
ax.text(9.4, 5.0, "• Fila virtual com token assinado\n• Desafio PoW / Proof-of-Human\n• Sorteio ponderado (quebra do FIFO)", fontsize=8, color="#334155", ha='center')

c2 = patches.FancyBboxPatch((7.8, 2.5), 3.2, 1.8, boxstyle="round,pad=0.1", ec="#2563eb", fc="#ffffff", lw=1.5)
ax.add_patch(c2)
ax.text(9.4, 3.7, "Controle 2: Validação Forte", fontsize=9.5, fontweight='bold', color="#1e40af", ha='center')
ax.text(9.4, 2.9, "• Verificação 2FA (SMS/App)\n• Validação de CPF na Receita\n• Histórico de reputação da conta", fontsize=8, color="#334155", ha='center')

c3 = patches.FancyBboxPatch((7.8, 0.4), 3.2, 1.8, boxstyle="round,pad=0.1", ec="#2563eb", fc="#ffffff", lw=1.5)
ax.add_patch(c3)
ax.text(9.4, 1.6, "Controle 3: Lock Agressivo", fontsize=9.5, fontweight='bold', color="#1e40af", ha='center')
ax.text(9.4, 0.8, "• Timeout de reserva curto (2 min)\n• Liberação atômica em Redis\n• Limite de 1 reserva por sessão", fontsize=8, color="#334155", ha='center')

# Itens da Coluna 4: Ativos
a1 = patches.FancyBboxPatch((11.5, 4.6), 2.5, 1.8, boxstyle="round,pad=0.1", ec="#16a34a", fc="#ffffff", lw=1.5)
ax.add_patch(a1)
ax.text(12.75, 5.8, "Justiça Distributiva\n(Fair Allocation)", fontsize=9.5, fontweight='bold', color="#15803d", ha='center')
ax.text(12.75, 4.9, "Risco: A1 (Crítico: 9)\nEstoque distribuído a\nclientes legítimos.", fontsize=8, color="#334155", ha='center')

a2 = patches.FancyBboxPatch((11.5, 2.5), 2.5, 1.8, boxstyle="round,pad=0.1", ec="#16a34a", fc="#ffffff", lw=1.5)
ax.add_patch(a2)
ax.text(12.75, 3.7, "Disponibilidade & API", fontsize=9.5, fontweight='bold', color="#15803d", ha='center')
ax.text(12.75, 2.9, "Risco: A2 (Alto: 6)\nServidores operando sem\ncolapso ou DoS.", fontsize=8, color="#334155", ha='center')

a3 = patches.FancyBboxPatch((11.5, 0.4), 2.5, 1.8, boxstyle="round,pad=0.1", ec="#16a34a", fc="#ffffff", lw=1.5)
ax.add_patch(a3)
ax.text(12.75, 1.6, "Confiança & Retenção", fontsize=9.5, fontweight='bold', color="#15803d", ha='center')
ax.text(12.75, 0.8, "Risco: A3 (Médio: 4)\nSatisfação do cliente e\nintegridade de marca.", fontsize=8, color="#334155", ha='center')

# Conexões
arr = dict(arrowstyle="->", lw=1.3, color="#64748b")
ax.annotate("", xy=(3.9, 5.5), xytext=(3.4, 5.5), arrowprops=arr)
ax.annotate("", xy=(3.9, 3.4), xytext=(3.4, 3.4), arrowprops=arr)
ax.annotate("", xy=(3.9, 1.3), xytext=(3.4, 1.3), arrowprops=arr)

ax.annotate("", xy=(7.8, 5.5), xytext=(7.3, 5.5), arrowprops=dict(arrowstyle="->", lw=1.3, color="#2563eb", linestyle=":"))
ax.annotate("", xy=(7.8, 3.4), xytext=(7.3, 3.4), arrowprops=dict(arrowstyle="->", lw=1.3, color="#2563eb", linestyle=":"))
ax.annotate("", xy=(7.8, 1.3), xytext=(7.3, 1.3), arrowprops=dict(arrowstyle="->", lw=1.3, color="#2563eb", linestyle=":"))

ax.annotate("", xy=(11.5, 5.5), xytext=(11.0, 5.5), arrowprops=dict(arrowstyle="->", lw=1.3, color="#16a34a"))
ax.annotate("", xy=(11.5, 3.4), xytext=(11.0, 3.4), arrowprops=dict(arrowstyle="->", lw=1.3, color="#16a34a"))
ax.annotate("", xy=(11.5, 1.3), xytext=(11.0, 1.3), arrowprops=dict(arrowstyle="->", lw=1.3, color="#16a34a"))

ax.set_xlim(0, 14.5)
ax.set_ylim(0.1, 7.5)
ax.axis('off')

plt.tight_layout()
plt.savefig('diagramas/superficie-de-ataque.png', dpi=300, bbox_inches='tight')
plt.close()
print("Superficie de ataque gerada com sucesso!")
