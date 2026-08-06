# Integrais como somatórios de \(y\cdot dx\)

Uma forma intuitiva de entender integral definida é pensar em **somar caixinhas (retângulos)**.

## 1) A ideia geométrica
Considere uma função \(y=f(x)\) no intervalo \([a,b]\).

- Dividimos a base \([a,b]\) em pedaços pequenos.
- Cada pedaço tem largura \(dx\) (ou \(\Delta x\), quando ainda é finito).
- Em cada pedaço, montamos um retângulo com altura aproximada \(y=f(x_i)\).

A área de cada caixinha é aproximadamente:

\[
\text{área da caixinha} \approx y\cdot dx = f(x_i)\,dx
\]

## 2) Soma de várias caixinhas
Somando todas as caixinhas:

\[
\text{Área total aproximada} \approx \sum f(x_i)\,\Delta x
\]

Isso é uma **soma de Riemann**.

## 3) Quando \(dx\) fica muito pequeno
Quanto menor o \(dx\):

- melhor a aproximação da curva pelos retângulos;
- maior a quantidade de caixinhas;
- mais próxima a soma fica da área real.

No limite, quando o tamanho tende a zero:

\[
\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i)\,\Delta x
\]

Então, a integral é exatamente a ideia de:

> **somar infinitas contribuições pequenas do tipo \(y\cdot dx\)**.

## 4) Exemplo rápido
Para \(f(x)=x^2\) em \([0,2]\):

\[
\int_0^2 x^2\,dx
\]

interpreta-se como a soma das áreas de muitas caixinhas sob a curva \(y=x^2\), cada uma com área aproximada \(x_i^2\,dx\).

## 5) Resumo didático
- **Derivada**: mede variação instantânea.
- **Integral**: mede acumulação.
- **Soma de Riemann**: ponte entre “caixinhas” e integral.
- **\(y\cdot dx\)**: área de cada contribuição elementar.
