import numpy as np
import matplotlib.pyplot as plt
from .Curve import Curve
from .Point import Point


class Transformation():
    def __init__(self, t_function, curves, points = []):
        self.curves = curves
        self.points = points
        self.t_function = t_function

    @property
    def t_curves(self):
        t_curves = []
        for curve in self.curves:
            t_curve = self.transform(curve, self.t_function)
            t_curves.append(t_curve)

        return t_curves

    @property
    def t_points(self):
        t_points = []
        for point in self.points:
            t_point = self.transform_point(point, self.t_function)
            t_points.append(t_point)

        return t_points

    def plot(self, plot_title = ''):
        plt.suptitle(plot_title)
        plt.subplot(121)
        plt.grid(True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.axis('equal')
        plt.ylabel('y')
        plt.xlabel('x')

        for curve in self.curves:
            curve.plot()

        for point in self.points:
            point.plot()

        plt.subplot(122)
        plt.grid(True)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.axis('equal')
        plt.ylabel('u')
        plt.xlabel('v')

        for t_curve in self.t_curves:
            t_curve.plot()

        for t_point in self.t_points:
            t_point.plot()

    @staticmethod
    def transform(curve, t_function):
        points = []
        for point in curve.points:
            complex_point = point[0] + 1j * point[1]
            transformed_point = t_function(complex_point)
            points.append((transformed_point.real, transformed_point.imag))

        return Curve(points, curve.color)

    @staticmethod
    def transform_point(point, t_function):
        complex_point = point.x + 1j * point.y
        transformed_point = t_function(complex_point)
        return Point(transformed_point.real, transformed_point.imag, point.legend, point.color)