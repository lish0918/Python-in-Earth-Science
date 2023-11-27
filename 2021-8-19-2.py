import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

fig,ax=plt.subplots(figsize=[8,6])

my_data1=data[(data.Epoch=='one')]
ax.scatter(my_data1.Zr,my_data1.Th,label='Epoch 1')

my_data2=data[(data.Epoch=='two')]
ax.scatter(my_data2.Zr,my_data2.Th,label='Epoch 2')

my_data3=data[(data.Epoch=='three')]
ax.scatter(my_data3.Zr,my_data3.Th,label='Epoch 3')

my_data4=data[(data.Epoch=='three-b')]
ax.scatter(my_data4.Zr,my_data4.Th,label='Epoch 3b')

ax.set_title("My Third Diagram")
ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")

ax.legend()

plt.show()