import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

epochs = ['one', 'two', 'three', 'three-b']
colors = ['#e69f00', '#56b3e9', '#f0e442', '#cc79a7']

bins_Zr=np.arange(100,1100,50)
bins_Ba=np.arange(0,2300,100)

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,5))

for (epoch, color) in zip(epochs, colors):
    my_data = data[(data.Epoch == epoch)]
    ax1.hist(my_data.Zr,bins=bins_Zr,color=color,
             alpha=0.6,density=True,label="Epoch " + epoch)
    ax2.hist(my_data.Ba,bins=bins_Ba,color=color,
             alpha=0.6,density=True,label="Epoch " + epoch)

ax1.set_xlabel("Zr [ppm]")
ax1.set_ylabel("Probabilitu Density")
ax1.legend(title="Phlegraean Fields \n Age < 15 ky")

ax2.set_xlabel("Ba [ppm]")
ax2.set_ylabel("Probabilitu Density")
ax2.legend(title="Phlegraean Fields \n Age < 15 ky")

plt.show()