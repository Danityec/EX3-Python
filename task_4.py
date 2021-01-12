import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def price_transformation():
    color_map = plt.cm.get_cmap('rocket')
    reversed_color_map = color_map.reversed()

    data_two = pd.read_csv("mobile_price_2.csv", index_col="id")

    data_two['price'] = data['price']
    data_two['ram'] = data['ram']
    data_two['gen'] = data['gen']
    data_two['battery_power'] = data['battery_power']

    sns.heatmap(data_two[data_two.corr().index].corr(), annot=True, cmap=reversed_color_map)
    plt.show()

    x = data_two['price_2']
    y = data_two['price']
    c = data_two['ram']
    plt.scatter(x, y, c=c, alpha=0.3, cmap=reversed_color_map)
    plt.colorbar(label='ram')
    plt.xlabel('price_2')
    plt.ylabel('price')
    plt.show()

    x = data_two['price']
    y = data_two['ram']
    c = data_two['price_2']
    plt.scatter(x, y, c=c, alpha=0.3, cmap=reversed_color_map)
    plt.colorbar(label='price_2')
    plt.xlabel('price')
    plt.ylabel('ram')
    plt.show()

    x = data_two['price_2']
    y = data_two['ram']
    c = data_two['price']
    plt.scatter(x, y, c=c, alpha=0.3, cmap=reversed_color_map)
    plt.colorbar(label='price')
    plt.xlabel('price_2')
    plt.ylabel('ram')
    plt.show()


def pair_plot():
    g = sns.PairGrid(data, vars=['price', 'ram', 'DPI_w', 'battery_power'])
    g.map(plt.scatter, alpha=0.4, color='#9e0b46')
    plt.show()


def four_d_plot():
    sorted_cores = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    core_sizes = pd.Categorical(data['cores'], ordered=True, categories=sorted_cores)

    x = data['px_width']
    y = data['px_height']
    c = data['price']

    plt.scatter(x, y, s=(core_sizes.codes+1)*10, c=c, alpha=0.3, cmap='rocket')
    plt.colorbar(label='price')
    plt.xlabel('px_width')
    plt.ylabel('px_height')

    core_names = {10: 'single', 20: 'dual', 30: 'triple', 40: 'quad', 50: 'penta', 60: 'hexa', 70: 'hepta', 80: 'octa'}

    for core in [10, 20, 30, 40, 50, 60, 70, 80]:
        plt.scatter([], [], c='k', alpha=0.3, s=core, label=core_names[core])
    plt.legend(scatterpoints=1, frameon=False, labelspacing=0.5)
    plt.show()


if __name__ == '__main__':

    data = pd.read_csv("task_1.csv", index_col="id")

    # 4.1
    # pair_plot()

    # 4.2
    # four_d_plot()

    # 4.3
    # price_transformation()



