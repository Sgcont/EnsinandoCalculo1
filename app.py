import streamlit as st


st.set_page_config(page_title="Ensinando Cálculo 1", page_icon="📘", layout="wide")

st.title("📘 Ensinando Cálculo 1")
st.write(
    "Material introdutório para quem está começando Cálculo 1, com conteúdo teórico e quiz."
)

pagina = st.sidebar.radio("Navegação", ["Conteúdo", "Questões"])

conteudos = [
    {
        "titulo": "Funções e interpretação gráfica",
        "texto": "Função relaciona cada x a um único y. No gráfico, observe domínio, imagem, "
        "crescimento, decrescimento e pontos importantes (raízes e interceptos).",
    },
    {
        "titulo": "Limites",
        "texto": "Limite descreve o comportamento de f(x) quando x se aproxima de um valor. "
        "Não depende necessariamente do valor da função no ponto.",
    },
    {
        "titulo": "Indeterminações",
        "texto": "Formas como 0/0 e ∞/∞ exigem manipulações algébricas, fatoração, racionalização "
        "ou regra de L'Hôpital (quando permitida).",
    },
    {
        "titulo": "Continuidade",
        "texto": "f é contínua em a quando lim x→a f(x) existe, f(a) existe e ambos são iguais. "
        "Sem 'saltos', 'buracos' ou assíntotas no ponto.",
    },
    {
        "titulo": "Definição de derivada",
        "texto": "f'(a) = lim h→0 [f(a+h)-f(a)]/h. Mede a taxa de variação instantânea da função.",
    },
    {
        "titulo": "Derivada como inclinação da reta tangente",
        "texto": "A derivada no ponto dá a inclinação da reta tangente ao gráfico naquele ponto.",
    },
    {
        "titulo": "Regras de derivação",
        "texto": "Incluem linearidade, potência, produto, quociente e cadeia para simplificar "
        "derivações sem voltar sempre à definição.",
    },
    {
        "titulo": "Regra do produto",
        "texto": "(uv)' = u'v + uv'. Derive um fator por vez, mantendo o outro.",
    },
    {
        "titulo": "Regra do quociente",
        "texto": "(u/v)' = (u'v - uv')/v², com v ≠ 0.",
    },
    {
        "titulo": "Regra da cadeia",
        "texto": "Se y = f(g(x)), então y' = f'(g(x))·g'(x). Fundamental para funções compostas.",
    },
    {
        "titulo": "Derivadas de funções trigonométricas, exponenciais e logarítmicas",
        "texto": "Exemplos: (sen x)'=cos x, (cos x)'=-sen x, (e^x)'=e^x, (ln x)'=1/x.",
    },
    {
        "titulo": "Máximos e mínimos",
        "texto": "Pontos críticos ocorrem quando f'(x)=0 ou não existe. Use derivadas para classificar.",
    },
    {
        "titulo": "Crescimento e decrescimento",
        "texto": "Se f'(x)>0 a função cresce; se f'(x)<0, decresce.",
    },
    {
        "titulo": "Concavidade",
        "texto": "Analisada por f''(x): positiva indica concavidade para cima; negativa, para baixo.",
    },
    {
        "titulo": "Problemas de otimização",
        "texto": "Modelar a quantidade a otimizar, impor restrições e usar derivadas para achar extremos.",
    },
    {
        "titulo": "Integral definida",
        "texto": "∫[a,b] f(x)dx representa acumulação líquida da grandeza no intervalo.",
    },
    {
        "titulo": "Soma de Riemann",
        "texto": "A integral definida surge como limite de somas de áreas de retângulos.",
    },
    {
        "titulo": "Integral como área acumulada",
        "texto": "Para f(x)≥0, integral representa área geométrica sob o gráfico.",
    },
    {
        "titulo": "Teorema Fundamental do Cálculo",
        "texto": "Conecta derivada e integral: se F' = f, então ∫[a,b] f(x)dx = F(b)-F(a).",
    },
    {
        "titulo": "Integração por substituição",
        "texto": "Troca de variável para simplificar integrais compostas (u = g(x)).",
    },
    {
        "titulo": "Integração por partes",
        "texto": "∫u dv = uv - ∫v du. Útil para produtos como x·e^x, x·sen x.",
    },
    {
        "titulo": "Área entre curvas",
        "texto": "Área = ∫(função de cima - função de baixo) dx, nos limites de interseção.",
    },
    {
        "titulo": "Volume por discos",
        "texto": "V = π∫[a,b] (R(x))² dx para sólidos de revolução sem furo.",
    },
    {
        "titulo": "Volume por anéis",
        "texto": "V = π∫[a,b] (R(x)² - r(x)²) dx quando há raio externo e interno.",
    },
    {
        "titulo": "Comprimento de arco",
        "texto": "L = ∫[a,b] √(1 + (f'(x))²) dx para y=f(x).",
    },
]

questoes = [
    {
        "pergunta": "1) Qual expressão representa a definição de derivada em x=a?",
        "opcoes": [
            "lim h→0 [f(a+h)-f(a)]/h",
            "lim h→∞ [f(a+h)-f(a)]/h",
            "[f(a)-f(h)]/a",
            "f(a+h)/h",
        ],
        "correta": 0,
    },
    {
        "pergunta": "2) A derivada em um ponto representa geometricamente:",
        "opcoes": [
            "Área sob a curva",
            "Inclinação da reta tangente",
            "Volume do sólido",
            "Concavidade da função",
        ],
        "correta": 1,
    },
    {
        "pergunta": "3) Regra do produto de u(x)v(x):",
        "opcoes": ["u'v'", "u'v + uv'", "(u'+v')", "(u/v)'"],
        "correta": 1,
    },
    {
        "pergunta": "4) Regra do quociente (u/v)':",
        "opcoes": ["(u'v+uv')/v²", "(u'v-uv')/v²", "u'/v'", "(u-v)'"],
        "correta": 1,
    },
    {
        "pergunta": "5) Para função composta f(g(x)), usamos:",
        "opcoes": ["Regra da cadeia", "Regra do quociente", "Soma de Riemann", "Regra de sinais"],
        "correta": 0,
    },
    {
        "pergunta": "6) Qual é a derivada de ln(x), para x>0?",
        "opcoes": ["x", "1/x", "e^x", "ln(x)"],
        "correta": 1,
    },
    {
        "pergunta": "7) Se f'(x)>0 em um intervalo, então f é:",
        "opcoes": ["Decrescente", "Constante", "Crescente", "Côncava para baixo"],
        "correta": 2,
    },
    {
        "pergunta": "8) O Teorema Fundamental do Cálculo diz que ∫[a,b] f(x)dx =",
        "opcoes": ["f(b)-f(a)", "F(b)-F(a), com F'=f", "f'(b)-f'(a)", "0"],
        "correta": 1,
    },
    {
        "pergunta": "9) Integração por partes é dada por:",
        "opcoes": ["∫u dv = uv - ∫v du", "∫u dv = u+v", "∫u dv = du/dv", "∫u dv = uv"],
        "correta": 0,
    },
    {
        "pergunta": "10) O volume por discos usa, em geral:",
        "opcoes": ["π∫R² dx", "2π∫R dx", "∫(R-r)dx", "∫√(1+f'²)dx"],
        "correta": 0,
    },
]

if pagina == "Conteúdo":
    st.header("Página de conteúdo")
    st.write("Estude os tópicos abaixo antes de iniciar os exercícios:")
    for item in conteudos:
        with st.expander(item["titulo"], expanded=False):
            st.write(item["texto"])

if pagina == "Questões":
    st.header("Página de questões de marcar")
    st.write("Marque uma alternativa por questão e clique em **Corrigir** para ver o gabarito.")

    respostas = []
    for i, q in enumerate(questoes):
        resposta = st.radio(
            q["pergunta"],
            q["opcoes"],
            key=f"q_{i}",
            index=None,
        )
        respostas.append(resposta)

    if st.button("Corrigir"):
        acertos = 0
        st.subheader("Resultado")
        for i, q in enumerate(questoes):
            correta = q["opcoes"][q["correta"]]
            marcada = respostas[i]

            if marcada == correta:
                acertos += 1
                st.markdown(
                    f"<div style='background-color:#d4edda; color:#155724; padding:10px; "
                    f"border-radius:8px; margin-bottom:8px;'>"
                    f"<strong>{q['pergunta']}</strong><br>"
                    f"Você marcou: {marcada}<br>✅ Correto!"
                    f"</div>",
                    unsafe_allow_html=True,
                )
            else:
                texto_marcada = marcada if marcada is not None else "Não respondida"
                st.markdown(
                    f"<div style='background-color:#f8d7da; color:#721c24; padding:10px; "
                    f"border-radius:8px; margin-bottom:8px;'>"
                    f"<strong>{q['pergunta']}</strong><br>"
                    f"Você marcou: {texto_marcada}<br>"
                    f"❌ Errado. Gabarito: <strong>{correta}</strong>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

        st.info(f"Pontuação final: {acertos}/{len(questoes)}")
