# EnsinandoCalculo1

Aplicativo em Python para introdução a Cálculo 1 com:

1. **Página de conteúdo** com os principais tópicos.
2. **Página de simuladores** (limites, reta tangente e soma de Riemann).
3. **Página de questões objetivas** com simulado, correção automática (verde para certo, vermelho para errado) e gabarito.
4. **Script extra de visualização** comparando área por boxes (5, 10 e 20) com a integral exata.

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