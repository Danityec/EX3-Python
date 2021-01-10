# DANIT

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#def task2_func1():

mobiles = pd.read_csv('mobile_price_1.csv', index_col="id")
print(mobiles.head())
df = mobiles.select_dtypes(np.number)
corrMatrix = df.corr()
# sns.heatmap(corrMatrix, annot=True, vmin=-1, vmax=1)
# plt.show()

#def task2_func1():

cores_order = ['single', 'dual', 'triple', 'quad', 'penta', 'hexa', 'hepta', 'octa']
mobiles.cores.value_counts().reindex(cores_order).plot.bar()
plt.show()


#if __name__ == "__task_2__":
    #task2()
    #plt.show
