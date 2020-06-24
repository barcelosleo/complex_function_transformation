import numpy as np
import matplotlib.pyplot as plt

class Curve():
    def __init__(self, points, color = None):
        self.points = points
        self.color = color

    @property
    def xs(self):
        return [p[0] for p in self.points]

    @property
    def ys(self):
        return [p[1] for p in self.points]

    def plot(self, **kwargs):
        plt.plot(self.xs, self.ys, color = self.color, **kwargs)

    @staticmethod
    def circle(r = 1, center = (0, 0), **kwargs):
        points = []
        angles = np.linspace(0, 2 * np.pi, 100)
        for angle in angles:
            points.append((r * np.cos(angle) + center[0], r * np.sin(angle) + center[1]))

        return Curve(points, **kwargs)

    @staticmethod
    def box(width = 1, height = 1, center = (0, 0), **kwargs):
        points = []
        
        horizontal_line = np.linspace(-(width / 2) + center[0], (width / 2) + center[0])
        vertical_line = np.linspace(-(height / 2) + center[1], (height / 2) + center[1])

        for x in horizontal_line:
            points.append((x, -(height / 2) + center[1]))

        for y in vertical_line:
            points.append(((width / 2)  + center[0], y))

        for x in horizontal_line[::-1]:
            points.append((x, (height / 2) + center[1]))

        for y in vertical_line[::-1]:
            points.append((-(width / 2)  + center[0], y))

        return Curve(points, **kwargs)

    @staticmethod
    def rect_segment(origin = (0,0), end = (1, 1), **kwargs):
        m = (end[1] - origin[1]) / (end[0] - origin[0])

        b = origin[1] - m * origin[0]

        points = []

        for x in np.linspace(origin[0], end[0], 100):
            points.append((x, m * x + b))

        return Curve(points, **kwargs)