# let's write another python code
import matplotlib.pyplot as plt
# import is used to access library code 
# matplotlib is python library for plots / graphs
import numpy as np
# here numpy as another library of python to process numerical information
x = np.linspace(0, 4*3.14, 200)
# np.linspace it generates equal distance number from start to endswit
y1 = np.sin(x)
# sin coversion of angles
y2 = np.cos(x)
plt.plot(x, y1, 'ro--', label='SIN')
plt.plot(x, y2, 'g+--', label='COS')
plt.legend()
plt.show()