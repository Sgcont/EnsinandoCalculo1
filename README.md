# EnsinandoCalculo1

Aplicativo em Python para introdução a Cálculo 1 com:

1. **Página de conteúdo** com os principais tópicos.
2. **Página de simuladores** (limites, reta tangente e soma de Riemann).
3. **Página de questões objetivas** com simulado, correção automática (verde para certo, vermelho para errado) e gabarito.
4. **Script extra de visualização** comparando área por boxes (5, 10 e 20) com a integral exata.
5. **Script extra de derivadas** mostrando reta tangente (f'(x)) e concavidade (f''(x)).

## Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Script adicional: Vizualizando os gráficos

Para visualizar a comparação entre somas de Riemann (boxes) e integral:

```bash
python Vizualizando_os_graficos.py
```

## Script adicional: Reta tangente e concavidade

Para visualizar que f'(x) representa a inclinação da reta tangente e que f''(x)
indica a concavidade (U para cima se positivo, U para baixo se negativo):

```bash
python retas_tangentes_e_concavidade.py
```