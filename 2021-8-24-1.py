import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

fig,ax=plt.subplots(figsize=[8,6])
ax.hist(data.Zr,bins="doean",edgecolor="black",color="tab:blue",alpha=0.8,density=True)
# hist=直方图 bins=条数 alpha=透明度 density=区间数目/(总数*区间宽度) 
ax.set_title("excercise")
ax.set_xlabel("Zr[ppm]")
ax.set_ylabel("Ba")
ax.legend()


plt.show()