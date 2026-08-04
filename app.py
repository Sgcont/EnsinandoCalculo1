import html
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
 
 
# Caixa 2 - Textos de cada aba (mesmo conteúdo do guia original)
 
texto_inicio = """
BEM-VINDO AO CÁLCULO I!
 
Este programa foi pensado como uma introdução completa aos principais
conceitos normalmente encontrados em uma disciplina de Cálculo I.
 
A ideia principal é:
 
        LIMITE
           ↓
     CONTINUIDADE
           ↓
       DERIVADA
           ↓
    APLICAÇÕES
           ↓
       INTEGRAL
           ↓
    TEOREMA FUNDAMENTAL
           ↓
    APLICAÇÕES DA INTEGRAL
 
 
POR QUE COMEÇAMOS PELO LIMITE?
 
Porque o Cálculo inteiro gira em torno da ideia de "aproximação".
 
A derivada pergunta:
 
    "O que acontece com a variação quando o intervalo fica
     infinitamente pequeno?"
 
A integral pergunta:
 
    "O que acontece quando somamos infinitas pequenas contribuições?"
 
Essas duas ideias parecem diferentes, mas estão profundamente conectadas.
 
 
COMO ESTUDAR
 
1. Leia a explicação.
2. Observe as fórmulas.
3. Execute os gráficos.
4. Tente explicar o conceito com suas próprias palavras.
5. Resolva exercícios depois.
 
 
IMPORTANTE
 
Este programa é um guia didático.
 
A matéria exata de Cálculo I varia de universidade para universidade.
Alguns tópicos podem aparecer em Cálculo II ou em disciplinas posteriores.
 
A intenção aqui é criar uma base ampla e intuitiva.
"""
 
texto_funcoes = """
1 — FUNÇÕES
 
Uma função associa cada valor de entrada a um valor de saída.
 
Podemos escrever:
 
    y = f(x)
 
Por exemplo:
 
    f(x) = x²
 
Se x = 2:
 
    f(2) = 4
 
 
DOMÍNIO
 
É o conjunto dos valores que podemos colocar em x.
 
Exemplo:
 
    f(x) = 1/x
 
Aqui:
 
    x ≠ 0
 
Portanto, o domínio é:
 
    R - {0}
 
 
IMAGEM
 
É o conjunto dos valores que a função pode produzir.
 
 
FUNÇÕES IMPORTANTES
 
Polinomial:
 
    f(x) = x² + 3x - 1
 
Exponencial:
 
    f(x) = eˣ
 
Logarítmica:
 
    f(x) = ln(x)
 
Trigonométricas:
 
    sen(x)
    cos(x)
    tan(x)
 
 
POR QUE FUNÇÕES SÃO IMPORTANTES?
 
Porque praticamente todo o Cálculo pode ser interpretado como o estudo
do comportamento de funções.
 
Queremos descobrir:
 
    • para onde a função vai;
    • se ela é contínua;
    • quão rapidamente ela muda;
    • onde cresce;
    • onde decresce;
    • onde possui máximos e mínimos;
    • quanto ela acumula.
"""
 
texto_limites = """
2 — LIMITES
 
O limite descreve para qual valor uma função está se aproximando.
 
Escrevemos:
 
        lim f(x)
        x→a
 
 
EXEMPLO
 
Considere:
 
    f(x) = x²
 
Quando x se aproxima de 2:
 
    x → 2
 
temos:
 
    x² → 4
 
Portanto:
 
    lim x² = 4
    x→2
 
 
A IDEIA MAIS IMPORTANTE
 
O limite não está necessariamente interessado no valor da função
exatamente em x = a.
 
Ele quer saber:
 
    "O que acontece com f(x) quando x fica cada vez mais próximo
     de a?"
 
 
LIMITES LATERAIS
 
Podemos nos aproximar pela esquerda:
 
    lim f(x)
    x→a⁻
 
ou pela direita:
 
    lim f(x)
    x→a⁺
 
 
Para o limite existir:
 
    limite pela esquerda = limite pela direita
 
 
INFINITO
 
Podemos estudar também:
 
    lim f(x)
    x→∞
 
Isso pergunta o comportamento da função quando x cresce
indefinidamente.
 
 
INDETERMINAÇÕES
 
Algumas expressões produzem formas indeterminadas:
 
    0/0
    ∞/∞
    ∞ - ∞
    0 · ∞
    1^∞
    0^0
    ∞^0
 
IMPORTANTE:
 
Uma indeterminação NÃO significa que o limite não existe.
 
Significa apenas:
 
    "Ainda não temos informação suficiente."
 
 
TÉCNICAS
 
Podemos usar:
 
    • fatoração
    • racionalização
    • simplificação algébrica
    • limites fundamentais
    • substituições
    • regra de L'Hôpital (quando aplicável)
 
 
LIMITES FUNDAMENTAIS
 
Um dos mais importantes:
 
        sen(x)
lim     ────── = 1
x→0      x
 
 
Outro:
 
        eˣ - 1
lim     ────── = 1
x→0       x
"""
 
texto_derivadas = """
3 — DERIVADAS
 
A derivada mede uma taxa de variação instantânea.
 
Imagine um carro.
 
A velocidade média é:
 
        Δposição
        ────────
        Δtempo
 
Mas queremos saber a velocidade exatamente em um instante.
 
Então fazemos:
 
        Δposição
lim     ────────
Δt→0    Δtempo
 
 
DEFINIÇÃO DA DERIVADA
 
        f(x+h) - f(x)
f'(x)= lim ───────────
       h→0      h
 
 
INTERPRETAÇÃO GEOMÉTRICA
 
A derivada é a inclinação da reta tangente ao gráfico.
 
 
SE:
 
    f'(x) > 0
 
a função está crescendo.
 
 
SE:
 
    f'(x) < 0
 
a função está decrescendo.
 
 
SE:
 
    f'(x) = 0
 
podemos estar diante de um máximo, mínimo ou outro ponto crítico.
 
 
REGRAS BÁSICAS
 
Constante:
 
    d/dx(c) = 0
 
 
Potência:
 
    d/dx(xⁿ) = n·xⁿ⁻¹
 
 
Soma:
 
    (f + g)' = f' + g'
 
 
Produto:
 
    (fg)' = f'g + fg'
 
 
Quociente:
 
    (f/g)' = (f'g - fg') / g²
 
 
REGRA DA CADEIA
 
Se:
 
    y = f(g(x))
 
então:
 
    y' = f'(g(x)) · g'(x)
 
 
DERIVADAS IMPORTANTES
 
    d/dx(sen x) = cos x
 
    d/dx(cos x) = -sen x
 
    d/dx(tan x) = sec² x
 
    d/dx(eˣ) = eˣ
 
    d/dx(ln x) = 1/x
 
 
A DERIVADA É UMA DAS GRANDES IDEIAS DO CÁLCULO.
 
Ela permite estudar:
 
    • velocidade
    • crescimento
    • máximos
    • mínimos
    • otimização
    • comportamento de gráficos
    • taxas relacionadas
"""
 
texto_aplicacoes_derivadas = """
4 — APLICAÇÕES DAS DERIVADAS
 
 
CRESCIMENTO E DECRESCIMENTO
 
Se:
 
    f'(x) > 0
 
a função cresce.
 
Se:
 
    f'(x) < 0
 
a função decresce.
 
 
PONTOS CRÍTICOS
 
Um ponto crítico ocorre quando:
 
    f'(x) = 0
 
ou quando a derivada não existe.
 
 
MÁXIMO LOCAL
 
A função passa de crescente para decrescente.
 
 
MÍNIMO LOCAL
 
A função passa de decrescente para crescente.
 
 
TESTE DA PRIMEIRA DERIVADA
 
Observe o sinal de f'(x).
 
    + → -
 
indica máximo.
 
    - → +
 
indica mínimo.
 
 
SEGUNDA DERIVADA
 
A segunda derivada:
 
    f''(x)
 
ajuda a estudar a concavidade.
 
 
SE:
 
    f''(x) > 0
 
a função é côncava para cima.
 
 
SE:
 
    f''(x) < 0
 
a função é côncava para baixo.
 
 
PONTO DE INFLEXÃO
 
É um ponto onde a concavidade muda.
 
 
OTIMIZAÇÃO
 
Problemas de otimização procuram:
 
    máximo possível
 
ou
 
    mínimo possível
 
 
Exemplo:
 
Queremos construir um retângulo com determinada quantidade
de material e maximizar sua área.
 
Criamos uma função:
 
    A(x)
 
Depois calculamos:
 
    A'(x)
 
e procuramos os pontos críticos.
 
 
TAXAS RELACIONADAS
 
Imagine duas grandezas variando ao mesmo tempo:
 
    volume
    raio
    altura
 
Podemos relacioná-las através de derivadas.
 
Por exemplo:
 
    V = πr²h
 
Se r e h mudam com o tempo:
 
    dV/dt
 
pode ser relacionado com:
 
    dr/dt
 
e
 
    dh/dt.
"""
 
texto_integrais = """
5 — INTEGRAIS
 
Agora chegamos a uma das ideias mais importantes do Cálculo.
 
 
A PERGUNTA
 
Imagine a região abaixo de uma curva:
 
        y = f(x)
 
Queremos descobrir sua área.
 
Para algumas figuras é fácil.
 
Retângulo:
 
    A = base × altura
 
Mas e se a curva for complicada?
 
 
A IDEIA DE RIEMANN
 
Dividimos a região em muitos retângulos pequenos.
 
A área aproximada é:
 
    A ≈ Σ f(xᵢ) Δx
 
 
Quanto mais retângulos usamos:
 
    Δx → 0
 
e o número de retângulos cresce.
 
 
A INTEGRAL DEFINIDA
 
Escrevemos:
 
        b
    ∫   f(x) dx
        a
 
 
Ela representa o limite dessas somas.
 
 
INTERPRETAÇÃO
 
A integral pode representar:
 
    • área
    • distância acumulada
    • massa
    • volume
    • trabalho
    • quantidade acumulada
 
 
INTEGRAL INDEFINIDA
 
Também podemos procurar uma função cuja derivada seja f(x).
 
Por exemplo:
 
    ∫ x² dx
 
queremos uma função F tal que:
 
    F'(x) = x²
 
Como:
 
    d/dx(x³/3) = x²
 
temos:
 
    ∫ x² dx = x³/3 + C
 
 
REGRA DA POTÊNCIA
 
        xⁿ⁺¹
∫ xⁿ dx = ──── + C
         n+1
 
 
para n ≠ -1.
 
 
EXEMPLO
 
    ∫ 2x dx = x² + C
 
 
INTEGRAIS TRIGONOMÉTRICAS
 
    ∫ cos(x) dx = sen(x) + C
 
    ∫ sen(x) dx = -cos(x) + C
 
 
INTEGRAIS EXPONENCIAIS
 
    ∫ eˣ dx = eˣ + C
 
 
INTEGRAL DE 1/x
 
    ∫ 1/x dx = ln|x| + C
"""
 
texto_aplicacoes_integrais = """
6 — APLICAÇÕES DAS INTEGRAIS
 
 
ÁREA SOB UMA CURVA
 
Se:
 
    f(x) ≥ 0
 
então:
 
        b
    A = ∫ f(x) dx
        a
 
 
ÁREA ENTRE DUAS CURVAS
 
Se f(x) está acima de g(x):
 
        b
    A = ∫ [f(x) - g(x)] dx
        a
 
 
VOLUME POR DISCOS
 
Se giramos uma função ao redor de um eixo:
 
        b
    V = π ∫ [f(x)]² dx
        a
 
 
VOLUME POR ANÉIS
 
Quando existe um raio externo e um interno:
 
        b
    V = π ∫ [R(x)² - r(x)²] dx
        a
 
 
MÉTODO DAS CASCAS CILÍNDRICAS
 
Outra maneira de calcular volumes de sólidos de revolução.
 
A ideia básica é somar muitas cascas cilíndricas pequenas.
 
 
DISTÂNCIA
 
Se v(t) é velocidade:
 
    deslocamento = ∫ v(t) dt
 
 
Se queremos distância total e a velocidade muda de sinal,
precisamos tomar cuidado com o valor absoluto.
 
 
VALOR MÉDIO DE UMA FUNÇÃO
 
        1
    f̄ = ───── ∫ f(x) dx
        b-a   a
 
 
Isso representa a altura constante que produziria a mesma
área acumulada no intervalo.
 
 
TRABALHO
 
Em Física:
 
    W = ∫ F(x) dx
 
A integral permite somar pequenas quantidades de trabalho
produzidas ao longo do deslocamento.
"""
 
texto_mapa = """
🧠 O MAPA MENTAL DO CÁLCULO I
 
 
                    FUNÇÕES
                       │
                       ▼
                    LIMITES
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
        CONTINUIDADE        DERIVADA
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                    ▼           ▼           ▼
                CRESCIMENTO  MÁX/MÍN   CONCAVIDADE
                    │           │           │
                    └───────────┼───────────┘
                                │
                                ▼
                         APLICAÇÕES
                                │
                                ▼
                           INTEGRAL
                                │
                    ┌───────────┼───────────┐
                    │           │           │
                    ▼           ▼           ▼
                 ÁREA        VOLUME     ACUMULAÇÃO
                    │           │           │
                    └───────────┼───────────┘
                                │
                                ▼
                 TEOREMA FUNDAMENTAL
                      DO CÁLCULO
 
 
A GRANDE CONEXÃO
 
 
DERIVADA:
 
    "Quanto está mudando agora?"
 
 
INTEGRAL:
 
    "Quanto acumulou ao longo do caminho?"
 
 
E O TEOREMA FUNDAMENTAL DIZ, EM ESSÊNCIA:
 
    derivar e integrar são operações profundamente relacionadas.
 
 
Se:
 
    F'(x) = f(x)
 
então:
 
        b
    ∫ f(x) dx = F(b) - F(a)
        a
 
 
Essa conexão é uma das ideias centrais de todo o Cálculo.
 
 
=============================================================
 
O QUE VOCÊ DEVE CONSEGUIR FAZER AO FINAL DE CÁLCULO I?
 
✓ Interpretar funções
 
✓ Calcular e interpretar limites
 
✓ Identificar indeterminações
 
✓ Verificar continuidade
 
✓ Calcular derivadas
 
✓ Entender derivada geometricamente
 
✓ Aplicar regra da cadeia
 
✓ Encontrar máximos e mínimos
 
✓ Estudar crescimento e decrescimento
 
✓ Analisar concavidade
 
✓ Resolver problemas de otimização
 
✓ Interpretar taxas relacionadas
 
✓ Entender a integral como soma
 
✓ Calcular integrais
 
✓ Usar o Teorema Fundamental do Cálculo
 
✓ Calcular áreas
 
✓ Calcular volumes
 
✓ Interpretar quantidades acumuladas
 
 
=============================================================
 
UMA ÚLTIMA IDEIA
 
O Cálculo não é simplesmente um conjunto de fórmulas.
 
Ele é uma linguagem para descrever:
 
    MUDANÇA
 
e
 
    ACUMULAÇÃO.
 
 
A derivada descreve mudança.
 
A integral descreve acumulação.
 
O limite permite tornar essas ideias precisas.
"""
 
 
# Caixa 3 - Função auxiliar para exibir um texto formatado em uma aba
 
def caixa_texto(texto):
    texto_seguro = html.escape(texto)
    conteudo = (
        "<pre style='font-family: monospace; font-size: 13px; "
        "white-space: pre-wrap; line-height: 1.3;'>"
        + texto_seguro
        + "</pre>"
    )
    return widgets.HTML(
        value=conteudo,
        layout=widgets.Layout(width="100%", height="480px", overflow="auto",
                               border="1px solid #ccc", padding="10px")
    )
 
 
# Caixa 4 - Funções dos gráficos interativos (matplotlib, sem tkinter)
 
def grafico_limite(botao):
    with saida_limite:
        clear_output(wait=True)
 
        x = np.linspace(-3, 3, 1000)
        y = (x**2 - 4) / (x - 2)
        mascara = np.abs(x - 2) > 0.01
 
        plt.figure(figsize=(7, 4.5))
        plt.plot(x[mascara], y[mascara], label="f(x) = (x² - 4) / (x - 2)")
        plt.scatter([2], [4], s=80, facecolors="white", edgecolors="black", zorder=5)
        plt.axvline(2, linestyle="--", alpha=0.5)
        plt.axhline(4, linestyle="--", alpha=0.5)
        plt.title("Quando x se aproxima de 2, f(x) se aproxima de 4")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()
 
 
def grafico_derivada(botao):
    with saida_derivada:
        clear_output(wait=True)
 
        x = np.linspace(-3, 3, 500)
        y = x**2
 
        a = 1
        f_a = a**2
        derivada = 2 * a
        tangente = f_a + derivada * (x - a)
 
        plt.figure(figsize=(7, 4.5))
        plt.plot(x, y, label="f(x) = x²")
        plt.plot(x, tangente, linestyle="--", label="Reta tangente")
        plt.scatter([a], [f_a], s=80, zorder=5)
        plt.axhline(0, alpha=0.4)
        plt.axvline(0, alpha=0.4)
        plt.title("A derivada em x = 1 é a inclinação da reta tangente")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()
 
 
def grafico_riemann(botao):
    with saida_riemann:
        clear_output(wait=True)
 
        x = np.linspace(0, 4, 500)
        y = x**2
 
        plt.figure(figsize=(7.5, 5))
        plt.plot(x, y, linewidth=2, label="f(x) = x²")
 
        n = 12
        pontos = np.linspace(0, 4, n + 1)
        dx = 4 / n
        valor = 0
 
        for i in range(n):
            esquerda = pontos[i]
            altura = esquerda**2
            plt.bar(esquerda, altura, width=dx, align="edge", alpha=0.3, edgecolor="black")
            valor += altura * dx
 
        plt.title(f"Soma de Riemann com {n} retângulos\nÁrea aproximada = {valor:.3f}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()
 
 
# Caixa 5 - Montagem de cada aba (texto + botão + gráfico quando existir)
 
aba_inicio = caixa_texto(texto_inicio)
aba_funcoes = caixa_texto(texto_funcoes)
 
saida_limite = widgets.Output()
botao_limite = widgets.Button(description="📈 Visualizar aproximação de um limite")
botao_limite.on_click(grafico_limite)
aba_limites = widgets.VBox([caixa_texto(texto_limites), botao_limite, saida_limite])
 
saida_derivada = widgets.Output()
botao_derivada = widgets.Button(description="📐 Visualizar derivada como reta tangente")
botao_derivada.on_click(grafico_derivada)
aba_derivadas = widgets.VBox([caixa_texto(texto_derivadas), botao_derivada, saida_derivada])
 
aba_aplicacoes_derivadas = caixa_texto(texto_aplicacoes_derivadas)
 
saida_riemann = widgets.Output()
botao_riemann = widgets.Button(description="▥ Visualizar soma de Riemann")
botao_riemann.on_click(grafico_riemann)
aba_integrais = widgets.VBox([caixa_texto(texto_integrais), botao_riemann, saida_riemann])
 
aba_aplicacoes_integrais = caixa_texto(texto_aplicacoes_integrais)
aba_mapa = caixa_texto(texto_mapa)
 
 
# Caixa 6 - Montagem final em abas (equivalente ao ttk.Notebook do tkinter)
 
abas = widgets.Tab(children=[
    aba_inicio,
    aba_funcoes,
    aba_limites,
    aba_derivadas,
    aba_aplicacoes_derivadas,
    aba_integrais,
    aba_aplicacoes_integrais,
    aba_mapa,
])
 
titulos = [
    "🏠 Início",
    "1. Funções",
    "2. Limites",
    "3. Derivadas",
    "4. Aplicações",
    "5. Integrais",
    "6. Aplicações da Integral",
    "🧠 Mapa do Cálculo",
]
 
for i, t in enumerate(titulos):
    abas.set_title(i, t)
 
display(widgets.HTML(
    "<h2 style='text-align:center'>CÁLCULO I — GUIA INTERATIVO</h2>"
    "<p style='text-align:center'>Do conceito de limite até o Teorema "
    "Fundamental do Cálculo</p>"
))
display(abas)
