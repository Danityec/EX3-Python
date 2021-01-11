# DANIT

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# def task3_func1():

mobiles = pd.read_csv('mobile_price_1.csv', index_col="id")
core_list = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
mobiles['cores_ord'] = pd.Categorical(mobiles.cores, ordered=True, categories=core_list).codes+1
speed_list = ['low', 'medium', 'high']
mobiles['speed_ord'] = pd.Categorical(mobiles.speed, ordered=True, categories=speed_list).codes+1
sim_list = ['Single', 'Dual']
mobiles['sim_ord'] = pd.Categorical(mobiles.sim, ordered=True, categories=sim_list).codes
wifi_list = ['none', 'n', 'g', 'b', 'a']
mobiles['wifi_ord'] = pd.Categorical(mobiles.wifi, ordered=True, categories=wifi_list).codes+1
bluetooth_list = ['No', 'Yes']
mobiles['bluetooth_bin'] = pd.Categorical(mobiles.bluetooth, ordered=True, categories=bluetooth_list).codes
screen_list = ['LCD', 'Touch']
mobiles['screen_bin'] = pd.Categorical(mobiles.screen, ordered=True, categories=screen_list).codes

df = mobiles.select_dtypes(np.number)
corrMatrix = df.corr()
sns.heatmap(corrMatrix, annot=True, vmin=-1, vmax=1)
plt.show()
print(mobiles.head(10))
np.savetxt('mobile_prices_converted.csv', (mobiles), delimiter=',')




