import matplotlib.pyplot as plt
import numpy as np


class BarBuilder():
    def __init__(self, plot_amount, labels):
        self.plot_amount = plot_amount
        self.fig, self.ax = plt.subplots(3, 2)
        self.labels = labels
        self.width = 0.25
        self.ax[-1, -1].axis('off')

        plt.rcParams.update({'font.size': 6})

    def __plot_number(self, plot_number):
        return (plot_number // 2, plot_number % 2)

    def build_bar(self, plot_number, title, y_labels, x_ticks, x_ticks_labels, quarters):
        plot_number = self.__plot_number(plot_number)
        x_ticks = np.arange(len(x_ticks_labels))
        for i in range(len(quarters)):
            self.ax[plot_number].bar(
                x_ticks + (i * 2 + 1) * self.width / 2,
                quarters[i],
                self.width,
                label=f'{i + 1} квартал')

        self.ax[plot_number].set_ylabel(y_labels)
        self.ax[plot_number].set_title(title)

        self.ax[plot_number].set_xticks(x_ticks)
        self.ax[plot_number].set_xticklabels(x_ticks_labels)

        self.ax[plot_number].set_axisbelow(True)

        self.ax[plot_number].grid()

    def show_plot(self):
        self.fig.tight_layout()
        self.fig.set_figheight(12)
        self.fig.set_figwidth(12)
        plt.show()
