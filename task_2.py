import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def correlation_heatmap():
    df = data.select_dtypes(np.number)
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, vmin=-1, vmax=1)
    plt.show()


def cores_correlation():
    data_correlation = pd.concat([data, pd.get_dummies(data['cores'])], axis=1)
    correlation_graph(data_correlation)


def speed_correlation():
    data_correlation = pd.concat([data, pd.get_dummies(data['speed'])], axis=1)
    correlation_graph(data_correlation)


def sim_correlation():
    data_correlation = pd.concat([data, pd.get_dummies(data['sim'])], axis=1)
    correlation_graph(data_correlation)


def wifi_correlation():
    data_correlation = pd.concat([data, pd.get_dummies(data['wifi'])], axis=1)
    correlation_graph(data_correlation)


def bluetooth_correlation():
    data_correlation = pd.concat([data, pd.get_dummies(data['bluetooth'])], axis=1)
    correlation_graph(data_correlation)


def screen_correlation():
    data_correlation = pd.concat([data, pd.get_dummies(data['screen'])], axis=1)
    correlation_graph(data_correlation)


def correlation_graph(data_correlation):
    corr = data_correlation.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    f, ax = plt.subplots(figsize=(15, 8))
    cmap = sns.diverging_palette(200, 10, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, vmax=1, vmin=-1)
    plt.show()


def price_battery_power_correlation():
    plt.scatter(data.battery_power, data.price, alpha=0.3, cmap='jet', edgecolors='none')
    plt.title('Price VS Battery power correlation'.format(data.battery_power, data.price))
    plt.xlabel('Price')
    plt.ylabel('battery power')
    plt.show()


def price_ram_correlation():
    plt.scatter(data.ram, data.price, alpha=0.3, cmap='jet', edgecolors='none')
    plt.title('Price VS Ram correlation'.format(data.ram, data.price))
    plt.xlabel('Price')
    plt.ylabel('Ram')
    plt.show()


def price_gen_correlation():
    plt.scatter(data.gen, data.price, alpha=0.3, cmap='jet', edgecolors='none')
    plt.title('Price VS Gen correlation'.format(data.gen, data.price))
    plt.xlabel('Price')
    plt.ylabel('Gen')
    plt.show()


def price_pivot_table():
    ram = pd.cut(data['ram'], [0, 1000, 2000, 3000, 4000, 5000])
    battery_power = pd.cut(data['battery_power'], [0, 500, 1000, 1500])
    price = data.pivot_table('price', [ram, battery_power], 'gen')
    print(price)


if __name__ == '__main__':
    data = pd.read_csv("mobile_prices_task_1.csv", index_col="id")

    # 2.1
    correlation_heatmap()

    # 2.3
    cores_correlation()
    speed_correlation()
    sim_correlation()
    wifi_correlation()
    bluetooth_correlation()
    screen_correlation()

    # 2.4
    price_battery_power_correlation()
    price_ram_correlation()
    price_gen_correlation()

    # 2.5
    price_pivot_table()
