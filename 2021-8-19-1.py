import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

sub_data1=data[data.Zr>450]
sub_data2=data[data.Zr<450]

fig,ax=plt.subplots(figsize=[8,6])

x1=sub_data1.Zr
y1=sub_data1.Th

ax.scatter(x1,y1,color='blue',label='Zr > 450 [ppm]')

x2=sub_data2.Zr
y2=sub_data2.Th

ax.scatter(x2,y2,color='red',label='Zr < 450 [ppm]')

ax.set_title("My First Diagram")
ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")

ax.legend()

plt.show()