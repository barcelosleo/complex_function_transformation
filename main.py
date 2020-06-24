import matplotlib.pyplot as plt
import numpy as np

from ComplexFunctionTransformation import Curve, Transformation, Point

def f(z):
    return (z - 1)/(z + 1)

if __name__ == "__main__":
    circulo = Curve.circle(r=2, center=(2, 2))
    caixa = Curve.box(width=4, height=4, center=(2, 2))
    reta = Curve.rect_segment(origin=(0, 0), end=(4, 4))

    t_dir = Curve.rect_segment((1, 0), (2, 1), color='r')
    t_esq = Curve.rect_segment((0, 0), (1, 1), color='r')
    t_sup = Curve.rect_segment((1, 1), (2, 1), color='r')
    t_inf = Curve.rect_segment((0, 0), (1, 0), color='r')
    trapezio = (t_dir, t_sup, t_esq, t_inf)

    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)

    sin_curve = Curve(points=[(x[i], y[i]) for i in range(len(x))], color='k')

    a = Point(0, 0, legend='A', color='k')
    b = Point(1, 1, legend='B', color='k')
    c = Point(2, 1, legend='C', color='k')
    d = Point(1, 0, legend='D', color='k')

    pontos = (a, b, c, d)

    curvas = (circulo, caixa, reta)
    # curvas = (sin_curve,)
    
    e = Transformation(t_function=lambda z: np.exp(z), curves=trapezio, points=pontos)
    sin = Transformation(t_function=lambda z: np.sin(z), curves=trapezio, points=pontos)
    cos = Transformation(t_function=lambda z: np.cos(z), curves=trapezio, points=pontos)

    # e.plot(plot_title=r'$z \longrightarrow e^z$')
    # plt.show()

    # sin.plot(plot_title=r'$z \longrightarrow sin(z)$')
    # plt.show()

    # cos.plot(plot_title=r'$z \longrightarrow cos(z)$')
    # plt.show()

    t = Transformation(t_function=f, curves=trapezio, points=pontos)
    
    t.plot(plot_title=r'$z \longrightarrow \frac{z-1}{z+1}$')
    plt.show()