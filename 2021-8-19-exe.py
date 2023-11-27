import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

x=data.Zr
y=data.Ba

def ec(f,d,c0):
    cl=c0*f**(d-1)
    return cl

my_f = np.linspace(1, 0.3, 8)
Ba = ec(f= my_f,d= 4,c0= 2000)
Zr = ec(f= my_f,d= 0.01,c0= 250)

fig,ax=plt.subplots(figsize=[8,6]) #create a figure containing one axes 

ax.scatter(x,y,label='CFC = recent activity')
ax.plot(Zr,Ba,label='fc model',color='red')

ax.set_title("excercise")
ax.set_xlabel("Zr[ppm]")
ax.set_ylabel("Ba[ppm]")
ax.legend()

plt.show()