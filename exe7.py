import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_majors')

fig ,ax1 = plt.subplots(figsize=(11,8))
ax1.scatter(my_dataset.SIO2, my_dataset.MGO, marker='o', edgecolor='k', color='#c7ddf4', label='CFC recent Activity')

betas = np.polyfit(my_dataset.SIO2, my_dataset.MGO, 2)
func = np.poly1d(betas)

x1 = np.linspace(my_dataset.SIO2.min(),my_dataset.SIO2.max(),1000)
y1 = func(x1)
ax1.plot(x1, y1, color='red', linestyle='--', label="Linear model of order 2")
ax1.set_xlabel(r'SiO$_2$ [wt%]')
ax1.set_ylabel(r'MgO [wt%]')
ax1.legend()

plt.show()