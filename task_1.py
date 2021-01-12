import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt


def calculate_screen_resolution(sc_w, px_width, sc_h, px_height):
    diagonal_px = math.sqrt((px_height ** 2) + (px_width ** 2))
    height_inch = sc_h / 2.54
    width_inch = sc_w / 2.54
    diagonal_inch = math.sqrt((height_inch ** 2) + (width_inch ** 2))
    if diagonal_inch == 0:
        return 0
    return round(diagonal_px / diagonal_inch, 2)


def calculate_dpi(sc_w, px_width):
    width_inch = sc_w / 2.54
    if width_inch == 0:
        return 0
    return round(px_width / width_inch, 2)


def calculate_call_ratio(battery_power, talk_time):
    if talk_time == 0:
        return 0
    return round(battery_power / talk_time, 2)


def calculate_mb_to_gb(memory):
    return round(memory / 1000, 2)


def price_histogram():
    hist_data = data['price']
    plt.hist(hist_data, color='#9e0b46', edgecolor='#520524')
    plt.xlabel('Price')
    plt.ylabel('Number of mobile phones')
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("mobile_price_1.csv", index_col="id")

    # 1.3
    data['resolution'] = data.apply(lambda row: calculate_screen_resolution(row['sc_w'], row['px_width'], row['sc_h'], row['px_height']), axis=1)

    # 1.4
    data['DPI_w'] = data.apply(lambda row: calculate_dpi(row['sc_w'], row['px_width']), axis=1)

    # 1.5
    data['call_ratio'] = data.apply(lambda row: calculate_call_ratio(row['battery_power'], row['talk_time']), axis=1)

    # 1.6
    data['memory'] = data.apply(lambda row: calculate_mb_to_gb(row['memory']), axis=1)

    # 1.7
    data.describe().to_csv('describe.csv')

    # 1.8
    price_histogram()

    # saving new columns to a file for future use
    data.to_csv('task_1.csv')
