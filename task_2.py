# DANIT

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt




#def task2_func1():

mobiles = pd.read_csv('mobile_price_1.csv', index_col="id")
#print(mobiles.head())
df = mobiles.select_dtypes(np.number)
corrMatrix = df.corr()
# sns.heatmap(corrMatrix, annot=True, vmin=-1, vmax=1)
# plt.show()



#def task2_func2():

# -------- categorical ordinali --------

#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['cores'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['speed'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['sim'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['wifi'])], axis=1)

#--------  categorical nominali ---------

#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['bluetooth'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['screen'])], axis=1)
# print(mobiles.head())
# corr_oh = mobiles_oh.corr()
# mask = np.triu(np.ones_like(corr_oh, dtype=bool))
# f, ax = plt.subplots(figsize=(15, 8))
# cmap = sns.diverging_palette(200, 10, as_cmap=True)
# sns.heatmap(corr_oh, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, vmax=1, vmin=-1)
# #plt.show()

#def task2_func3():

#  ------ Battery_power --------
# plt.scatter(mobiles.battery_power, mobiles.price, s=mobiles.price/20, alpha=0.3, cmap='jet', edgecolors='none')
# plt.title('Price VS Battery power correlation'.format(mobiles.battery_power, mobiles.price))
# plt.xlabel('Price')
# plt.ylabel('battery power')
##plt.plot(np.unique(mobiles.price), np.poly1d(np.polyfit(mobiles.battery_power, mobiles.price, 1))np.unique(mobiles.price), color='red', linewidth=2.9)
#plt.show()

#  --------- ram ----------
# plt.scatter(mobiles.ram, mobiles.price, s=mobiles.price/20, alpha=0.3, cmap='jet', edgecolors='none')
# plt.title('Price VS Ram correlation'.format(mobiles.ram, mobiles.price))
# plt.xlabel('Price')
# plt.ylabel('Ram')
# plt.show()

#  --------- gen ----------
# plt.scatter(mobiles.gen, mobiles.price, s=mobiles.price/20, alpha=0.3, cmap='jet', edgecolors='none')
# plt.title('Price VS Gen correlation'.format(mobiles.gen, mobiles.price))
# plt.xlabel('Price')
# plt.ylabel('Gen')
# plt.show()



#def task2_func4():

ram = pd.cut(mobiles['ram'], [0, 1000, 2000, 3000, 4000, 5000])
battery_power = pd.cut(mobiles['battery_power'], [0, 500, 1000, 1500])
price = mobiles.pivot_table('price', [ram, battery_power], 'gen')
print(price)

#if __name__ == "__task_2__":
    #task2_func1()
    #plt.show
    #task2_func2()
    #task2_func3()
    #task2_func4()

