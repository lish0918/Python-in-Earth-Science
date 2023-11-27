import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel(
    'Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

epochs = ['one', 'two', 'three', 'three-b']
colors = ['#c8b4ba', '#f3ddb3', '#c1cd97', '#e18d96']
numbers = [1,2,3,4]
my_bins= np.arange(0,1100,50)

fig = plt.figure(figsize=(13,10))

for (epoch, color, number) in zip(epochs, colors, numbers):
    my_data = data[(data.Epoch == epoch)]
    ax = fig.add_subplot(2,2,number)
    ax.hist(my_data.Sr,bins=my_bins,color=color,edgecolor='black',
             alpha=0.6,density=True,label="Epoch " + epoch)
    stddev = my_data['Sr'].std() 
    #numpy.std() 除n 有偏标准差
    #pandas.std() 除n-1 无偏标准差
    ax.axvline(my_data['Sr'].mean()-stddev, color='purple', label=r'mean - 1$\sigma$', linewidth=2)
    ax.axvline(my_data['Sr'].mean()+stddev, color='green', label=r'mean + 1$\sigma$', linewidth=2)
    ax.axvspan(my_data['Sr'].mean()-stddev, my_data['Sr'].mean()+stddev, alpha=0.1, color='orange', label=r'mean $\pm$ 1$\sigma$')
    ax.set_xlabel("Sr [ppm]")
    ax.set_ylabel("Probabilitu Density")
    ax.legend()

fig.tight_layout()
plt.show()