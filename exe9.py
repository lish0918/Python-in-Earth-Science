import numpy as np
from scipy import integrate

for i in [2,5,10,100,1000]:
    x = np.linspace(0,9,i+1) # 3 divisions $[x0,x1,x2], n=2 
    y = x**2
    sup_trapz = integrate.trapz(y,x)
        #使用复合梯形规则沿给定轴积分
    print('Using n=i, the trapezoidal rule returns a value of {:.0f}'.format(sup_trapz))