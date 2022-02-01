import numpy as np
from matplotlib import pyplot as plt
from numpy import arctan, sin, sqrt, cos


def atan(x):
    return arctan(x)


def sec(x):
    return 1 / cos(x)


def f(e, x):
    return (
        atan(e * sin(x) / sqrt(-1 + e ** 2 - (e ** 2) * sin(x) ** 2))
        * sqrt(-2 + e ** 2 + e ** 2 * cos(2 * x))
        * sec(x)
        / (e * sqrt(2 - 2 * sec(x) ** 2 / e ** 2))
    )


def gen2(e, t):
    return


def main():
    fig, ax = plt.subplots()
    eta = np.linspace(-np.pi / 4, np.pi / 4, 1000)

    ax.plot(eta, np.pi - f(1.1, eta), "b-")
    ax.plot(eta, f(1.1, eta), "b-")
    ax.plot(eta, -np.pi - f(1.1, eta), "b-")

    plt.tight_layout()
    plt.plot()
    plt.show()


if __name__ == "__main__":
    main()
