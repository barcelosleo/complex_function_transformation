import matplotlib.pyplot as plt
import numpy as np

from ComplexFunctionTransformation import Curve, Transformation, Point

def f(z):
    return (z - 1)/(z + 1)

if __name__ == "__main__":
    t_esq = Curve.rect_segment((-2, -1), (0, 2))
    t_dir = Curve.rect_segment((0, 2), (2, -1))
    t_inf = Curve.rect_segment((2, -1), (-2, -1))

    triangulo = (t_esq, t_dir, t_inf)

    reta = Curve.rect_segment((0, -1), (0, 2))

    circulo = Curve.circle(r=1.05, center=(0, 0.05))

    curvas = triangulo + (reta, circulo)
    
    e = Transformation(t_function=np.exp, curves=curvas)
    sin = Transformation(t_function=np.sin, curves=curvas)
    cos = Transformation(t_function=np.cos, curves=curvas)
    c_f = Transformation(t_function=f, curves=curvas)

    e.plot(plot_title=r'$z \longrightarrow e^z$')
    plt.show()

    sin.plot(plot_title=r'$z \longrightarrow sin(z)$')
    plt.show()

    cos.plot(plot_title=r'$z \longrightarrow cos(z)$')
    plt.show()

    c_f.plot(plot_title=r'$z \longrightarrow \frac{z-1}{z+1}$')
    plt.show()