import random

import streamlit as st


st.set_page_config(page_title="Ensinando Cálculo 1", page_icon="📘", layout="wide")

st.title("📘 Ensinando Cálculo 1")
st.write("Plataforma de estudo para quem está entrando em Cálculo 1.")

pagina = st.sidebar.radio("Navegação", ["Conteúdo", "Simuladores", "Questões"])

CONTEUDOS = [
    {
        "titulo": "Funções e interpretação gráfica",
        "explicacao": "Uma função relaciona cada valor de x a um único valor de y. "
        "No gráfico, observe interceptos, domínio, imagem e tendência.",
        "formula": "y = f(x)",
        "exemplo": "f(x)=x² cresce para x>0 e decresce para x<0.",
    },
    {
        "titulo": "Limites",
        "explicacao": "Limite descreve o valor para o qual f(x) se aproxima quando x se aproxima de a.",
        "formula": "lim x→a f(x)",
        "exemplo": "lim x→2 (x²-4)/(x-2) = 4.",
    },
    {
        "titulo": "Indeterminações",
        "explicacao": "Formas como 0/0 e ∞/∞ pedem mais manipulação algébrica antes de concluir o limite.",
        "formula": "0/0, ∞/∞, ∞-∞, 0·∞, 1^∞",
        "exemplo": "(x²-4)/(x-2) vira (x+2) para x≠2.",
    },
    {
        "titulo": "Continuidade",
        "explicacao": "Uma função é contínua em a quando limite e valor da função no ponto coincidem.",
        "formula": "lim x→a f(x) = f(a)",
        "exemplo": "Polinômios são contínuos em todo número real.",
    },
    {
        "titulo": "Definição de derivada",
        "explicacao": "Derivada é taxa de variação instantânea.",
        "formula": "f'(a)=lim h→0 [f(a+h)-f(a)]/h",
        "exemplo": "Para f(x)=x², f'(x)=2x.",
    },
    {
        "titulo": "Derivada como inclinação da reta tangente",
        "explicacao": "f'(a) mede a inclinação da reta tangente ao gráfico em x=a.",
        "formula": "y - f(a) = f'(a)(x-a)",
        "exemplo": "Em f(x)=x² e a=1, inclinação = 2.",
    },
    {
        "titulo": "Regras de derivação",
        "explicacao": "Facilitam derivar sem usar o limite em toda conta.",
        "formula": "(f+g)'=f'+g' e (x^n)'=n·x^(n-1)",
        "exemplo": "(3x⁵ - 2x)' = 15x⁴ - 2.",
    },
    {
        "titulo": "Regra do produto",
        "explicacao": "Para derivar u(x)v(x), derive uma parte por vez.",
        "formula": "(uv)' = u'v + uv'",
        "exemplo": "(x²·sen x)' = 2x·sen x + x²·cos x.",
    },
    {
        "titulo": "Regra do quociente",
        "explicacao": "Usada para funções em fração.",
        "formula": "(u/v)' = (u'v - uv')/v²",
        "exemplo": "(x/(x+1))' = 1/(x+1)².",
    },
    {
        "titulo": "Regra da cadeia",
        "explicacao": "Para composição de funções: derivada da de fora vezes derivada da de dentro.",
        "formula": "(f(g(x)))' = f'(g(x))·g'(x)",
        "exemplo": "d/dx[(3x+1)^5] = 5(3x+1)^4·3.",
    },
    {
        "titulo": "Derivadas trigonométricas, exponenciais e logarítmicas",
        "explicacao": "Família-base muito usada em problemas reais.",
        "formula": "(sen x)'=cos x, (e^x)'=e^x, (ln x)'=1/x",
        "exemplo": "d/dx[e^x·ln x] = e^x·ln x + e^x/x.",
    },
    {
        "titulo": "Máximos e mínimos",
        "explicacao": "Ocorrem em pontos críticos onde f'(x)=0 ou f' não existe.",
        "formula": "Pontos críticos: f'(x)=0 ou indefinida",
        "exemplo": "f(x)=x² tem mínimo em x=0.",
    },
    {
        "titulo": "Crescimento e decrescimento",
        "explicacao": "Sinal da derivada indica comportamento da função.",
        "formula": "f'(x)>0 cresce | f'(x)<0 decresce",
        "exemplo": "f(x)=x³ cresce para todo x.",
    },
    {
        "titulo": "Concavidade",
        "explicacao": "Vem da segunda derivada.",
        "formula": "f''(x)>0 côncava para cima | f''(x)<0 para baixo",
        "exemplo": "f(x)=x² é côncava para cima em todo x.",
    },
    {
        "titulo": "Problemas de otimização",
        "explicacao": "Transforme o contexto em função objetivo e maximize/minimize com derivadas.",
        "formula": "Encontrar extremos de f(x) sob restrições",
        "exemplo": "Maximizar área de retângulo com perímetro fixo.",
    },
    {
        "titulo": "Integral definida",
        "explicacao": "Representa acumulação líquida no intervalo [a,b].",
        "formula": "∫[a,b] f(x)dx",
        "exemplo": "Se f≥0, interpreta-se como área sob a curva.",
    },
    {
        "titulo": "Soma de Riemann",
        "explicacao": "A integral aparece como limite de somas de retângulos.",
        "formula": "Σ f(xi*)Δx",
        "exemplo": "Quanto maior n, melhor a aproximação da área.",
    },
    {
        "titulo": "Integral como área acumulada",
        "explicacao": "A função área A(x)=∫[a,x] f(t)dt acumula variações de f.",
        "formula": "A(x)=∫[a,x] f(t)dt",
        "exemplo": "Se f é velocidade, A acumula deslocamento.",
    },
    {
        "titulo": "Teorema Fundamental do Cálculo",
        "explicacao": "Conecta derivada e integral.",
        "formula": "Se F'=f, então ∫[a,b] f(x)dx = F(b)-F(a)",
        "exemplo": "∫[0,2] x²dx = (x³/3)|0^2 = 8/3.",
    },
    {
        "titulo": "Integração por substituição",
        "explicacao": "Troca de variável para simplificar integrais compostas.",
        "formula": "u=g(x), du=g'(x)dx",
        "exemplo": "∫2x·cos(x²)dx = ∫cos(u)du = sen(u)+C.",
    },
    {
        "titulo": "Integração por partes",
        "explicacao": "Ideal para produto de funções.",
        "formula": "∫u dv = uv - ∫v du",
        "exemplo": "∫x·e^x dx = x·e^x - ∫e^x dx.",
    },
    {
        "titulo": "Área entre curvas",
        "explicacao": "Subtraia curva de baixo da curva de cima.",
        "formula": "A = ∫[a,b] (f(x)-g(x))dx",
        "exemplo": "Entre y=x e y=x² em [0,1], A=1/6.",
    },
    {
        "titulo": "Volume por discos",
        "explicacao": "Sólido de revolução sem furo.",
        "formula": "V = π∫[a,b] R(x)² dx",
        "exemplo": "Rotação de y=x em [0,1] gera V=π/3.",
    },
    {
        "titulo": "Volume por anéis",
        "explicacao": "Sólido com raio externo e interno.",
        "formula": "V = π∫[a,b] (R(x)²-r(x)²)dx",
        "exemplo": "Diferença entre dois volumes por discos.",
    },
    {
        "titulo": "Comprimento de arco",
        "explicacao": "Mede o tamanho da curva y=f(x) em [a,b].",
        "formula": "L = ∫[a,b] √(1+(f'(x))²)dx",
        "exemplo": "Exige derivada e integração na mesma expressão.",
    },
]

QUESTOES = [
    {
        "topico": "Funções",
        "pergunta": "A imagem de uma função representa:",
        "opcoes": ["Os valores possíveis de x", "Os valores produzidos de y", "Os pontos críticos", "A derivada da função"],
        "correta": 1,
    },
    {
        "topico": "Limites",
        "pergunta": "O valor de lim x→2 (x²-4)/(x-2) é:",
        "opcoes": ["0", "2", "4", "Não existe"],
        "correta": 2,
    },
    {
        "topico": "Indeterminações",
        "pergunta": "A forma 0/0 indica:",
        "opcoes": ["Limite igual a zero", "Limite inexistente", "Indeterminação que exige manipulação", "Erro de cálculo sem solução"],
        "correta": 2,
    },
    {
        "topico": "Continuidade",
        "pergunta": "Para f ser contínua em a, precisamos de:",
        "opcoes": ["f(a)=0", "lim x→a f(x)=f(a)", "f'(a)=0", "f''(a)>0"],
        "correta": 1,
    },
    {
        "topico": "Definição de derivada",
        "pergunta": "Qual expressão define f'(a)?",
        "opcoes": ["lim h→0 [f(a+h)-f(a)]/h", "lim h→∞ [f(a+h)-f(a)]/h", "f(a+h)/h", "[f(a)-f(h)]/a"],
        "correta": 0,
    },
    {
        "topico": "Reta tangente",
        "pergunta": "Geometricamente, a derivada em um ponto mede:",
        "opcoes": ["A área sob a curva", "A inclinação da tangente", "A concavidade", "O comprimento de arco"],
        "correta": 1,
    },
    {
        "topico": "Regras de derivação",
        "pergunta": "A derivada de x^7 é:",
        "opcoes": ["7x^6", "x^6", "6x^7", "7x"],
        "correta": 0,
    },
    {
        "topico": "Regra do produto",
        "pergunta": "Se y=u·v, então y' é:",
        "opcoes": ["u'v'", "u'v + uv'", "(u'+v')", "(u/v)'"],
        "correta": 1,
    },
    {
        "topico": "Regra do quociente",
        "pergunta": "A regra correta para (u/v)' é:",
        "opcoes": ["(u'v + uv')/v²", "(u'v - uv')/v²", "u'/v'", "(u-v)'"],
        "correta": 1,
    },
    {
        "topico": "Regra da cadeia",
        "pergunta": "Para y=(3x+1)^5, a derivada envolve:",
        "opcoes": ["Regra do produto", "Regra da cadeia", "Soma de Riemann", "L'Hôpital"],
        "correta": 1,
    },
    {
        "topico": "Trig/exp/log",
        "pergunta": "A derivada de ln(x), para x>0, é:",
        "opcoes": ["x", "1/x", "e^x", "ln(x)"],
        "correta": 1,
    },
    {
        "topico": "Máximos e mínimos",
        "pergunta": "Um ponto crítico ocorre quando:",
        "opcoes": ["f(x)=0", "f'(x)=0 ou não existe", "f''(x)=0 apenas", "f(a)=lim x→∞ f(x)"],
        "correta": 1,
    },
    {
        "topico": "Crescimento/decrescimento",
        "pergunta": "Se f'(x)<0 num intervalo, f é:",
        "opcoes": ["Crescente", "Constante", "Decrescente", "Periódica"],
        "correta": 2,
    },
    {
        "topico": "Concavidade",
        "pergunta": "Se f''(x)>0, então a função é:",
        "opcoes": ["Côncava para cima", "Côncava para baixo", "Constante", "Sem derivada"],
        "correta": 0,
    },
    {
        "topico": "Otimização",
        "pergunta": "Em otimização, após modelar a função objetivo, normalmente buscamos:",
        "opcoes": ["Limites laterais", "Pontos críticos", "Somas geométricas", "Séries de Fourier"],
        "correta": 1,
    },
    {
        "topico": "Integral definida",
        "pergunta": "A integral definida em [a,b] representa:",
        "opcoes": ["Taxa instantânea", "Acumulação líquida", "Apenas derivada", "Somente volume"],
        "correta": 1,
    },
    {
        "topico": "Soma de Riemann",
        "pergunta": "Ao aumentar o número de retângulos em uma soma de Riemann:",
        "opcoes": ["A aproximação piora", "A aproximação melhora", "Nada muda", "O limite deixa de existir"],
        "correta": 1,
    },
    {
        "topico": "Área acumulada",
        "pergunta": "Se f(x)≥0, então ∫[a,b] f(x)dx pode ser vista como:",
        "opcoes": ["Inclinação média", "Área sob a curva", "Concavidade média", "Raiz da função"],
        "correta": 1,
    },
    {
        "topico": "Teorema Fundamental",
        "pergunta": "Se F'=f, então ∫[a,b] f(x)dx é:",
        "opcoes": ["f(b)-f(a)", "F(b)-F(a)", "f'(b)-f'(a)", "F'(b)-F'(a)"],
        "correta": 1,
    },
    {
        "topico": "Substituição",
        "pergunta": "Integração por substituição é útil quando:",
        "opcoes": ["Há função composta", "Há fração simples", "Não há derivadas", "A função é constante"],
        "correta": 0,
    },
    {
        "topico": "Por partes",
        "pergunta": "A fórmula de integração por partes é:",
        "opcoes": ["∫u dv = uv - ∫v du", "∫u dv = du/dv", "∫u dv = u+v", "∫u dv = uv"],
        "correta": 0,
    },
    {
        "topico": "Área entre curvas",
        "pergunta": "A área entre curvas usa:",
        "opcoes": ["∫(curva de cima - curva de baixo)dx", "∫(curva de baixo - curva de cima)dx", "∫f'(x)dx", "∫(R²-r²)dx"],
        "correta": 0,
    },
    {
        "topico": "Volume por discos",
        "pergunta": "No método dos discos, a expressão típica é:",
        "opcoes": ["π∫R²dx", "2π∫Rdx", "π∫(R²-r²)dx", "∫√(1+f'²)dx"],
        "correta": 0,
    },
    {
        "topico": "Volume por anéis",
        "pergunta": "No método dos anéis, usamos:",
        "opcoes": ["π∫(R²-r²)dx", "π∫R²dx", "2π∫Rdx", "∫f(x)dx"],
        "correta": 0,
    },
    {
        "topico": "Comprimento de arco",
        "pergunta": "Para y=f(x), o comprimento de arco em [a,b] é:",
        "opcoes": ["∫[a,b] f(x)dx", "∫[a,b] √(1+(f'(x))²)dx", "π∫[a,b] f(x)²dx", "∫[a,b] f''(x)dx"],
        "correta": 1,
    },
]


def arredonda(valor: float) -> float:
    return float(f"{valor:.6f}")


def f_limite(x: float) -> float:
    return (x * x - 4) / (x - 2)


def f_exemplo(x: float) -> float:
    return x * x


def reta_tangente(a: float, x: float) -> float:
    return f_exemplo(a) + (2 * a) * (x - a)


def soma_riemann_esquerda(a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    acumulado = 0.0
    for i in range(n):
        xi = a + i * dx
        acumulado += f_exemplo(xi) * dx
    return acumulado


def integral_exata_x2(a: float, b: float) -> float:
    return (b**3 - a**3) / 3


if pagina == "Conteúdo":
    st.header("Página de conteúdo")
    st.write("Resumo dos tópicos-chave para sua base de Cálculo 1.")
    for item in CONTEUDOS:
        with st.expander(item["titulo"], expanded=False):
            st.write(item["explicacao"])
            st.caption(f"**Fórmula-base:** {item['formula']}")
            st.caption(f"**Exemplo rápido:** {item['exemplo']}")

    st.success(
        "Sequência recomendada de estudo: Funções → Limites → Continuidade → Derivadas "
        "→ Aplicações de Derivadas → Integrais → Aplicações de Integrais."
    )

if pagina == "Simuladores":
    st.header("Simuladores interativos")
    st.write("Use os controles para visualizar os conceitos na prática.")
    aba_limite, aba_derivada, aba_riemann = st.tabs(
        ["Limites", "Reta tangente", "Soma de Riemann"]
    )

    with aba_limite:
        st.subheader("Limite de (x²-4)/(x-2) quando x→2")
        distancias = [1, 0.5, 0.1, 0.01, 0.001]
        linhas = []
        for d in distancias:
            x_esq = 2 - d
            x_dir = 2 + d
            linhas.append({"x (esquerda)": arredonda(x_esq), "f(x)": arredonda(f_limite(x_esq))})
            linhas.append({"x (direita)": arredonda(x_dir), "f(x)": arredonda(f_limite(x_dir))})
        st.dataframe(linhas, hide_index=True, use_container_width=True)
        st.info("Os valores de f(x) se aproximam de 4 pelos dois lados, então o limite é 4.")

    with aba_derivada:
        st.subheader("Derivada como inclinação da reta tangente em f(x)=x²")
        a = st.slider("Escolha o ponto de tangência (a)", min_value=-3.0, max_value=3.0, value=1.0, step=0.5)
        xs = [(-3.0 + 0.1 * i) for i in range(61)]
        curva = [f_exemplo(x) for x in xs]
        tangente = [reta_tangente(a, x) for x in xs]
        st.line_chart({"f(x)=x²": curva, "reta tangente": tangente}, height=320)
        st.metric("Inclinação da tangente (f'(a))", arredonda(2 * a))
        st.caption("Para f(x)=x², a derivada é f'(x)=2x.")

    with aba_riemann:
        st.subheader("Aproximação de área por soma de Riemann para f(x)=x² em [0,b]")
        b = st.slider("Valor de b", min_value=1.0, max_value=6.0, value=4.0, step=0.5)
        n = st.slider("Número de retângulos", min_value=2, max_value=120, value=12, step=1)
        aproximada = soma_riemann_esquerda(0.0, b, n)
        exata = integral_exata_x2(0.0, b)
        erro = abs(exata - aproximada)

        c1, c2, c3 = st.columns(3)
        c1.metric("Área aproximada (Riemann)", arredonda(aproximada))
        c2.metric("Área exata", arredonda(exata))
        c3.metric("Erro absoluto", arredonda(erro))
        st.caption("Com mais retângulos, o erro tende a diminuir.")

if pagina == "Questões":
    st.header("Página de questões de marcar")
    st.write("Monte um simulado, marque as respostas e clique em **Corrigir**.")

    quantidade = st.slider("Quantidade de questões", min_value=5, max_value=len(QUESTOES), value=12, step=1)

    if "quiz_id" not in st.session_state:
        st.session_state.quiz_id = 0
    if "quiz_indices" not in st.session_state:
        st.session_state.quiz_indices = random.sample(range(len(QUESTOES)), quantidade)

    if st.button("Gerar novo simulado"):
        st.session_state.quiz_id += 1
        st.session_state.quiz_indices = random.sample(range(len(QUESTOES)), quantidade)

    if len(st.session_state.quiz_indices) != quantidade:
        st.session_state.quiz_indices = random.sample(range(len(QUESTOES)), quantidade)

    respostas = []
    quiz_id = st.session_state.quiz_id
    questoes_ativas = [QUESTOES[i] for i in st.session_state.quiz_indices]

    for i, q in enumerate(questoes_ativas):
        resposta = st.radio(
            f"{i + 1}) [{q['topico']}] {q['pergunta']}",
            q["opcoes"],
            index=None,
            key=f"q_{quiz_id}_{i}",
        )
        respostas.append(resposta)

    if st.button("Corrigir"):
        acertos = 0
        st.subheader("Resultado")
        for i, q in enumerate(questoes_ativas):
            correta = q["opcoes"][q["correta"]]
            marcada = respostas[i]
            if marcada == correta:
                acertos += 1
                st.markdown(
                    f"<div style='background-color:#d4edda; color:#155724; padding:10px; "
                    f"border-radius:8px; margin-bottom:8px;'>"
                    f"<strong>{i + 1}) [{q['topico']}] {q['pergunta']}</strong><br>"
                    f"Você marcou: {marcada}<br>✅ Correto!"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            else:
                texto_marcada = marcada if marcada else "Não respondida"
                st.markdown(
                    f"<div style='background-color:#f8d7da; color:#721c24; padding:10px; "
                    f"border-radius:8px; margin-bottom:8px;'>"
                    f"<strong>{i + 1}) [{q['topico']}] {q['pergunta']}</strong><br>"
                    f"Você marcou: {texto_marcada}<br>"
                    f"❌ Errado. Gabarito: <strong>{correta}</strong>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

        percentual = (acertos / len(questoes_ativas)) * 100
        st.info(f"Pontuação final: {acertos}/{len(questoes_ativas)} ({arredonda(percentual)}%)")
