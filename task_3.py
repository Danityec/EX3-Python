import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def ordinal_columns():
    core_list = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
    data['cores_ord'] = pd.Categorical(data.cores, ordered=True, categories=core_list).codes+1

    speed_list = ['low', 'medium', 'high']
    data['speed_ord'] = pd.Categorical(data.speed, ordered=True, categories=speed_list).codes+1

    sim_list = ['Single', 'Dual']
    data['sim_ord'] = pd.Categorical(data.sim, ordered=True, categories=sim_list).codes

    wifi_list = ['none', 'b', 'a', 'g', 'n']
    data['wifi_ord'] = pd.Categorical(data.wifi, ordered=True, categories=wifi_list).codes+1


def nominal_columns():
    bluetooth_list = ['No', 'Yes']
    data['bluetooth_bin'] = pd.Categorical(data.bluetooth, ordered=False, categories=bluetooth_list).codes

    screen_list = ['LCD', 'Touch']
    data['screen_bin'] = pd.Categorical(data.screen, ordered=False, categories=screen_list).codes


def modified_heatmap():
    df = data.select_dtypes(np.number)
    corr_matrix = round(df.corr(), 3)
    sns.heatmap(corr_matrix, annot=True, vmin=-1, vmax=1)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("mobile_prices_task_1.csv", index_col="id")

    # 3.1
    ordinal_columns()

    # 3.2
    nominal_columns()

    # 3.3
    modified_heatmap()

    # 3.4
    data.to_csv('mobile_prices_converted.csv', index=False)



