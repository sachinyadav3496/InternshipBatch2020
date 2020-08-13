import time
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['animation.html'] = 'jshtml'
def update(interval):
    global data
    data.pop(0) # we are deleting first element from our data
    data.append(psutil.cpu_percent())
    ax.clear()
    ax.plot(data, 'c--o')
    print(interval)
    #time.sleep(interval)
data = [ psutil.cpu_percent() for _ in range(50) if not time.sleep(.1) ]
fig, ax = plt.subplots()
ax.plot(data, 'c--o')
func = FuncAnimation(fig, update)
plt.show()
