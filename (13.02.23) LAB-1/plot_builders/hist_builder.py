import matplotlib.pyplot as plt
import numpy as np

class HistBuilder():

    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots(3, 2)
        self.ax[-1, -1].axis('off')
        plt.rcParams.update({'font.size': 6})

    def __plot_number(self, plot_number):
        return (plot_number // 2, plot_number % 2)

    def build_hist(self, plot_number, title,  values):
        plot_number = self.__plot_number(plot_number)
        self.ax[plot_number].hist(
            x=values,
            bins=32,
            edgecolor='black'
        )
        self.ax[plot_number].set_title(title)


    def show_plot(self):
        self.fig.tight_layout()
        self.fig.set_figheight(12)
        self.fig.set_figwidth(12)
        plt.show()