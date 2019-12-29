from random_walk import Randomwalk
import matplotlib.pyplot as plt
rw=Randomwalk(5000)
rw.fill_walk()
plt.figure(figsize=(10,6))

plt.plot(rw.x_values,rw.y_values)

plt.plot(rw.x_values[-1],rw.y_values[-1],c="green",cmap=plt.cm.Blues,s=15)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
