import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

my_data=data[['Ba','Zr','Th']]
sns.pairplot(my_data,height=3)

plt.show()