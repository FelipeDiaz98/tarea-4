import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

datos = np.genfromtxt("fijos.dat")
n = len(datos)/50

M = []
for i in range(n):
	m = datos[i*50:(i+1)*50][0::]
	M.append(m)

def data(i, z, line):
	z = M[i]
	ax.clear()
	ax.set_xlim(0, 50)
	ax.set_ylim(0, 50)
	ax.set_zlim(10, 100)
	ax.set_xlabel("x (cm)")
	ax.set_ylabel("y (cm)")
	ax.set_zlabel("Temperatura (C)")
	plt.title("Temperatura de la placa para condiciones fijas")
	line = ax.plot_surface(x,y,z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
	return line

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0,49,50,dtype='int')
y = np.linspace(0,49,50,dtype='int')
x,y = np.meshgrid(x,y)
z = M[0]
line = ax.plot_surface(x,y,z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(line, shrink=0.5, aspect=5)
plt.title("Temperatura en distintos instantes")

ani = animation.FuncAnimation(fig, data, fargs=(M, line), frames = len(M), interval=30, blit=False)
ani.save("fijos.gif",writer = "imagemagick",fps=20)



datos2 = np.genfromtxt("abiertos.dat")
n2 = len(datos2)/50

M2 = []
for i in range(n2):
	m = datos2[i*50:(i+1)*50][0::]
	M2.append(m)

def data2(i, z2, line2):
	z2 = M2[i]
	ax2.clear()
	ax2.set_xlim(0, 50)
	ax2.set_ylim(0, 50)
	ax2.set_zlim(10, 100)
	ax2.set_xlabel("x (cm)")
	ax2.set_ylabel("y (cm)")
	ax2.set_zlabel("Temperatura (C)")
	plt.title("Temperatura de la placa para condiciones abiertas")
	line2 = ax2.plot_surface(x2,y2,z2,cmap=cm.coolwarm,linewidth=0, antialiased=False)
	return line2

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

x2 = np.linspace(0,49,50,dtype='int')
y2 = np.linspace(0,49,50,dtype='int')
x2,y2 = np.meshgrid(x2,y2)
z2 = M2[0]
line2 = ax2.plot_surface(x2,y2,z2,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig2.colorbar(line, shrink=0.5, aspect=5)
plt.title("Temperatura en distintos instantes")

ani2 = animation.FuncAnimation(fig2, data2, fargs=(M2, line2), frames = len(M2), interval=30, blit=False)
ani2.save("abiertos.gif",writer = "imagemagick",fps=20)



datos3 = np.genfromtxt("periodicos.dat")
n3 = len(datos3)/50

M3 = []
for i in range(n3):
	m = datos3[i*50:(i+1)*50][0::]
	M3.append(m)

def data3(i, z3, line3):
	z3 = M3[i]
	ax3.clear()
	ax3.set_xlim(0, 50)
	ax3.set_ylim(0, 50)
	ax3.set_zlim(10, 100)
	ax3.set_xlabel("x (cm)")
	ax3.set_ylabel("y (cm)")
	ax3.set_zlabel("Temperatura (C)")
	plt.title("Temperatura de la placa para condiciones periodicas")
	line3 = ax3.plot_surface(x3,y3,z3,cmap=cm.coolwarm,linewidth=0, antialiased=False)
	return line3

fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')

x3 = np.linspace(0,49,50,dtype='int')
y3 = np.linspace(0,49,50,dtype='int')
x3,y3 = np.meshgrid(x3,y3)
z3 = M3[0]
line3 = ax3.plot_surface(x3,y3,z3,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig3.colorbar(line, shrink=0.5, aspect=5)

ani3 = animation.FuncAnimation(fig3, data3, fargs=(M3, line3), frames = len(M3), interval=30, blit=False)
ani3.save("periodicos.gif",writer = "imagemagick",fps=20)



