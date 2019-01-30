import matplotlib.pyplot as plt
import numpy as np

fs=8000
f=1000
x=np.arange(-1,1,0.02)
plt.figure(1)
y=np.exp(x)

plt.plot(x,y,'red')



plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()