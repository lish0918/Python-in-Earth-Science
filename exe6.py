import pandas as pd
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

my_dataset = pd.read_excel('Smith_glass_post_NYT_data.xlsx', sheet_name='Supp_majors')

fig ,ax = plt.subplots(figsize=(6,6))
ax.scatter(my_dataset.SIO2, my_dataset.NA2O, marker='o', edgecolor='k', color='#c7ddf4', label='CFC recent Activity')

b1, b0, rho_value, p_value, std_err = st.linregress(my_dataset.SIO2, my_dataset.NA2O)
# 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
x = np.linspace(my_dataset.SIO2.min(),my_dataset.SIO2.max())
#np.linspace(a,b,c) 图像仅在a到b之间显示，显示c个点
y = b0 + b1*x
ax.plot(x, y, linewidth=1, color='#ff464a', linestyle='--', label=r"fit param.: $\beta_0$ = " + '{:.1f}'.format(b0) + r" - $\beta_1$ = "  + '{:.1f}'.format(b1) + r" - $r_{xy}^{2}$ = " + '{:.2f}'.format(rho_value**2))
ax.set_xlabel('SiO2 [ppm]')
ax.set_ylabel('Na2O [ppm]')
ax.legend(loc= 'upper left')

plt.show()