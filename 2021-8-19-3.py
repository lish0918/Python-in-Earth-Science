#2021-8-19-2 another approach
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('Smith_glass_post_NYT_data.xlsx',sheet_name='Supp_traces')

epochs=['one','two','three','three-b']

fig,ax=plt.subplots(figsize=[8,6])

for epoch in epochs:
    my_data=data[(data.Epoch==epoch)]
    ax.scatter(my_data.Zr,my_data.Th,label='Epoch '+epoch)

ax.set_title("My Third Diagram")
ax.set_xlabel("Zr [ppm]")
ax.set_ylabel("Th [ppm]")

ax.legend()

plt.show()