import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_traces')

fig = plt.figure(figsize=(11,5))
ax1= fig.add_subplot(1,2,1)
ax1.scatter(my_dataset.La, my_dataset.Ce, marker='o', edgecolor='k', color='#c7ddf4', 
            label='CFC recent Activity')
b1, b0, rho_value, p_value, std_err = st.linregress(my_dataset.La, my_dataset.Ce)
x = np.linspace(my_dataset.La.min(),my_dataset.La.max())
y = b0 + b1*x
ax1.plot(x, y, linewidth=1, color='#ff464a', linestyle='--', 
         label=r"fit param.: $\beta_0$ = " + '{:.1f}'.format(b0) 
         + r" - $\beta_1$ = "  + '{:.1f}'.format(b1) + r" - $r_{xy}^{2}$ = " 
         + '{:.2f}'.format(rho_value**2))
ax1.set_xlabel('La [ppm]')
ax1.set_ylabel('Ce [ppm]')
ax1.legend(loc= 'upper left')

ax2 = fig.add_subplot(1,2,2)
ax2.scatter(my_dataset.Sc, my_dataset.U, marker='o', edgecolor='k', color='#c7ddf4', 
            label='CFC recent Activity')
b1, b0, rho_value, p_value, std_err = st.linregress(my_dataset.Sc, my_dataset.U)
x = np.linspace(my_dataset.Sc.min(),my_dataset.Sc.max())
y = b0 + b1*x
ax2.plot(x, y, linewidth=1, color='#ff464a', linestyle='--', 
         label=r"fit param.: $\beta_0$ = " + '{:.1f}'.format(b0) 
         + r" - $\beta_1$ = "  + '{:.1f}'.format(b1) + r" - $r_{xy}^{2}$ = " 
         + '{:.2f}'.format(rho_value**2))
ax2.set_xlabel('Sc [ppm]')
ax2.set_ylabel('U [ppm]')
ax2.legend(loc= 'upper left')

plt.show()