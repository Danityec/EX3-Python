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



#def task2_func1():
# -------- categorical ordinali --------
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['cores'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['speed'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['sim'])], axis=1)
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['wifi'])], axis=1)

#--------  categorical nominali ---------
#mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['bluetooth'])], axis=1)
mobiles_oh = pd.concat([mobiles, pd.get_dummies(mobiles['screen'])], axis=1)

print(mobiles.head())
corr_oh = mobiles_oh.corr()
mask = np.triu(np.ones_like(corr_oh, dtype=bool))
f, ax = plt.subplots(figsize=(15, 8))
cmap = sns.diverging_palette(200, 10, as_cmap=True)
sns.heatmap(corr_oh, mask=mask, cmap=cmap, center=0, square=True, linewidths=.5, vmax=1, vmin=-1)
plt.show()

#if __name__ == "__task_2__":
    #task2()
    #plt.show
