import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 3 * x


def f_linha(x):
    return 3 * x**2 - 3


def f_duas_linhas(x):
    return 6 * x


def reta_tangente(x, x0):
    return f(x0) + f_linha(x0) * (x - x0)


def grafico_reta_tangente():
    x = np.linspace(-3, 3, 500)
    x0 = 1
    y = f(x)
    y_tangente = reta_tangente(x, x0)

    plt.figure(figsize=(10, 4.5))
    plt.plot(x, y, label="f(x) = x³ - 3x", linewidth=2)
    plt.plot(x, y_tangente, "--", label=f"Reta tangente em x={x0}", linewidth=2)
    plt.scatter([x0], [f(x0)], color="red", zorder=5, label=f"Ponto ({x0}, f({x0}))")
    plt.title(f"f'({x0}) = {f_linha(x0):.2f} é a inclinação da reta tangente")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", alpha=0.3)
    plt.axvline(0, color="black", alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()


def grafico_concavidade():
    x = np.linspace(-3, 3, 500)
    y = f(x)
    concavidade = f_duas_linhas(x)

    mascara_cima = concavidade > 0
    mascara_baixo = concavidade < 0

    plt.figure(figsize=(10, 4.5))
    plt.plot(x, y, color="black", linewidth=1.8, label="f(x) = x³ - 3x")
    plt.scatter(x[mascara_cima], y[mascara_cima], s=8, color="tab:blue", label="f''(x) > 0 (U para cima)")
    plt.scatter(x[mascara_baixo], y[mascara_baixo], s=8, color="tab:orange", label="f''(x) < 0 (U para baixo)")
    plt.axvline(0, linestyle="--", alpha=0.6, label="f''(x)=0 (ponto de inflexão)")
    plt.title("f''(x) indica a concavidade do gráfico")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()


def main():
    grafico_reta_tangente()
    grafico_concavidade()
    plt.show()


if __name__ == "__main__":
    main()
