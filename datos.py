import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

datos = np.genfromtxt("fijos.dat")
n = len(datos)/50

M = []
for i in range(n):
	m = datos[i*50:(i+1)*50][0::]
	M.append(m)



def data(i, z, line):
	z = M[i]
	ax.clear()
	line = ax.plot_surface(x, y, z,color='b')
	return line

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0,49,50,dtype='int')
y = np.linspace(0,49,50,dtype='int')
x,y = np.meshgrid(x,y)
z = M[0]
line = ax.plot_surface(x, y, z,color='b')

ani = animation.FuncAnimation(fig, data, fargs=(M, line), frames = len(M)+1, interval=30, blit=False)
ani.save("fijos.gif",writer = "imagemagick",fps=1)



