import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_majors')

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6,8))

ax1.scatter(my_dataset.SIO2, my_dataset.CAO, marker='o', edgecolor='k', color='#c7ddf4', label='CFC recent Activity')
b1, b0, rho_value, p_value, std_err = st.linregress(my_dataset.SIO2, my_dataset.CAO)
x = np.linspace(my_dataset.SIO2.min(),my_dataset.SIO2.max())
y = b0 + b1*x
ax1.plot(x, y, linewidth=1, color='#ff464a', linestyle='--', label=r"fit param.: $\beta_0$ = " + '{:.1f}'.format(b0) + r" - $\beta_1$ = "  + '{:.1f}'.format(b1) + r" - $r_{xy}^{2}$ = " + '{:.2f}'.format(rho_value**2))
ax1.set_xlabel(r'SiO$_2$ [wt%]')
ax1.set_ylabel('CaO [wt%]')
ax1.legend()

ax2.scatter(my_dataset.SIO2, my_dataset.K2O, marker='o', edgecolor='k', color='#c7ddf4', label='CFC recent Activity')
betas = np.polyfit(my_dataset.SIO2, my_dataset.K2O, 2)
func = np.poly1d(betas)
x2 = np.linspace(my_dataset.SIO2.min(),my_dataset.SIO2.max())
y2 = func(x2)
ax2.plot(x2, y2, color='red', linestyle='--', label="Linear model of order 2")
ax2.set_xlabel(r'SiO$_2$ [wt%]')
ax2.set_ylabel(r'K$_2$O [wt%]')
ax2.legend()

plt.show()