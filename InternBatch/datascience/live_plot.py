import matplotlib.pyplot as plt
from time import sleep
from psutil import cpu_percent
from matplotlib.animation import FuncAnimation

plt.rcParams['animation.html'] = 'jshtml'

data = [ cpu_percent() for _ in range(50) ]

fig, ax = plt.subplots()

ax.plot(data, 'r--o')

def update(frame):
    global data
    # FIFO
    #print(frame)
    data.pop(0)
    # removing first value
    sleep(0.1)
    data.append(cpu_percent())
    # adding new value
    ax.clear()
    # removing old values
    ax.plot(data, 'r--o')

obj = FuncAnimation(fig, update)
plt.show()
