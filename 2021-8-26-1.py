import pandas as pd
import matplotlib.pyplot as plt

my_dataset = pd.read_excel(
    'Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

epochs = ['one', 'two', 'three', 'three-b']
# Using an arbitrary color palette
colors = ['#c8b4ba', '#f3ddb3', '#c1cd97', '#e18d96']
markers = ['o', 's', 'd', 'v']

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,5))

for (epoch, color, marker) in zip(epochs, colors, markers):
    my_data = my_dataset[(my_dataset.Epoch == epoch)]
    ax1.scatter(my_data.Zr, my_data.Ba, marker=marker, s=80, c=color, 
                edgecolor='0', label="Epoch " + epoch)
    ax2.scatter(my_data.Rb, my_data.Sr, marker=marker, s=80, c=color, 
                edgecolor='0', label="Epoch " + epoch)

ax1.set_title("Fig 4d (Smith et al., 2011)")
ax1.set_xlabel("Zr [ppm]")
ax1.set_ylabel("Ba [ppm]")
ax2.set_title("Fig 4e (Smith et al., 2011)")
ax2.set_xlabel("Rb [ppm]")
ax2.set_ylabel("Sr [ppm]")


ax1.legend(title="Phlegraean Fields \n Age < 15 ky")

plt.show()