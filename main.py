import matplotlib.pyplot as plt
import numpy as np

from ComplexFunctionTransformation import Curve, Transformation, Point

def f(z):
    return (z - 1)/(z + 1)

if __name__ == "__main__":
    circulo = Curve.circle(r=2, center=(2, 2))
    caixa = Curve.box(width=4, height=4, center=(2, 2))
    reta = Curve.rect_segment(origin=(0, 0), end=(4, 4))

    t_esq = Curve.rect_segment((0, 0), (1, 3), color='r')
    t_sup = Curve.rect_segment((1, 3), (4, 4), color='r')
    t_inf = Curve.rect_segment((0, 0), (3, 1), color='r')
    t_dir = Curve.rect_segment((3, 1), (4, 4), color='r')
    trapezio = (t_dir, t_sup, t_esq, t_inf)

    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)

    sin_curve = Curve(points=[(x[i], y[i]) for i in range(len(x))])

    a = Point(0, 0, legend='A', color='k')
    b = Point(1, 3, legend='B', color='k')
    c = Point(4, 4, legend='C', color='k')
    d = Point(3, 1, legend='D', color='k')

    pontos = (a, b, c, d)

    curvas = (circulo, caixa, reta) + trapezio
    sin_curve = (sin_curve,)
    
    e = Transformation(t_function=np.exp, curves=curvas, points=pontos)
    sin = Transformation(t_function=np.sin, curves=curvas, points=pontos)
    cos = Transformation(t_function=np.cos, curves=curvas, points=pontos)
    c_f = Transformation(t_function=f, curves=curvas, points=pontos)
    sin_c = Transformation(np.sin, sin_curve)

    e.plot(plot_title=r'$z \longrightarrow e^z$')
    plt.show()

    sin.plot(plot_title=r'$z \longrightarrow sin(z)$')
    plt.show()

    cos.plot(plot_title=r'$z \longrightarrow cos(z)$')
    plt.show()

    c_f.plot(plot_title=r'$z \longrightarrow \frac{z-1}{z+1}$')
    plt.show()

    sin_c.plot(plot_title=r'$z \longrightarrow sin(z)$')
    plt.show()