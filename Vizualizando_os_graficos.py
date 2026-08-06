import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2


def integral_exata(a, b):
    return (b**3 - a**3) / 3


def soma_riemann_esquerda(a, b, boxes):
    h = (b - a) / boxes
    x_n = a + np.arange(boxes) * h
    area = np.sum(f(x_n) * h)
    return area, h, x_n


def soma_riemann_direita(a, b, boxes):
    h = (b - a) / boxes
    x_n = a + np.arange(1, boxes + 1) * h
    area = np.sum(f(x_n) * h)
    return area


def soma_riemann_ponto_medio(a, b, boxes):
    h = (b - a) / boxes
    x_n = a + (np.arange(boxes) + 0.5) * h
    area = np.sum(f(x_n) * h)
    return area


def desenhar_boxes(ax, a, b, boxes):
    area, h, x_n = soma_riemann_esquerda(a, b, boxes)
    x = np.linspace(a, b, 400)

    ax.plot(x, f(x), color="tab:blue", linewidth=2, label="f(x) = x²")
    ax.bar(
        x_n,
        f(x_n),
        width=h,
        align="edge",
        alpha=0.3,
        edgecolor="black",
        color="tab:orange",
        label=f"{boxes} boxes",
    )
    ax.set_title(f"{boxes} boxes | Área ≈ {area:.4f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")
    return area


def desenhar_integral(ax, a, b, area_exata):
    x = np.linspace(a, b, 400)
    y = f(x)

    ax.plot(x, y, color="tab:blue", linewidth=2, label="f(x) = x²")
    ax.fill_between(x, y, color="tab:green", alpha=0.35, label="Área exata da integral")
    ax.set_title(f"Integral definida | Área exata = {area_exata:.4f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left")


def main():
    a, b = 0, 4
    boxes_opcoes = [5, 10, 20]
    area_exata = integral_exata(a, b)

    fig, eixos = plt.subplots(2, 2, figsize=(12, 8))
    eixos = eixos.flatten()

    aproximacoes = {}
    for i, boxes in enumerate(boxes_opcoes):
        aproximacoes[boxes] = desenhar_boxes(eixos[i], a, b, boxes)

    desenhar_integral(eixos[3], a, b, area_exata)
    fig.suptitle("Vizualizando os gráficos: boxes (Riemann) x integral", fontsize=14)
    plt.tight_layout()
    plt.show()

    print("\nComparação numérica (método dos retângulos pela esquerda):")
    for boxes in boxes_opcoes:
        erro = abs(area_exata - aproximacoes[boxes])
        h = (b - a) / boxes
        print(f"- {boxes:>2} boxes | h = Δx/{boxes} = {h:.4f} | área ≈ {aproximacoes[boxes]:.6f} | erro = {erro:.6f}")

    print(f"\nIntegral exata ∫[{a},{b}] x² dx = {area_exata:.6f}")

    print("\nOutras ideias nesse contexto (mesmo conceito y[x(n)]·h):")
    for boxes in boxes_opcoes:
        area_dir = soma_riemann_direita(a, b, boxes)
        area_med = soma_riemann_ponto_medio(a, b, boxes)
        print(
            f"- {boxes:>2} boxes | esquerda = {aproximacoes[boxes]:.6f}, "
            f"direita = {area_dir:.6f}, ponto médio = {area_med:.6f}"
        )


if __name__ == "__main__":
    main()
