import matplotlib.pyplot as plt

class Point():
    def __init__(self, x, y, legend, color = 'r'):
        self.x = x
        self.y = y
        self.legend = legend
        self.color = color

    def plot(self):
        plt.plot([self.x], [self.y], '.', color=self.color)
        plt.text(self.x, self.y, self.legend, color=self.color)