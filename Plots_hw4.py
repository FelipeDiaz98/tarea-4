import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#PUNTO 2

angulo = np.genfromtxt("angulo.dat")
barrer = np.genfromtxt("barrer.dat")

xa = angulo[:,0]
ya = angulo[:,1]

plt.figure()
plt.plot(xa,ya,label="recorrido proyectil")
plt.legend(loc="best")
plt.title("Grafica del recorrido del proyectil lanzado a un angulo de 45 grados")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("Parabolico1.pdf")

print "La distancia recorrida por el proyectil a un angulo de 45 grado es de", xa[-1]

largo, ancho = np.shape(barrer)
i = 1
Mc = []
while (i <= 7):
	com = 0
	fin = 0
	
	if (i < 7):	
		for j in range(largo):
			if ((barrer[j][0] == i*10) and (barrer[j][1] == i*10) and (barrer[j][2] == i*10) and (barrer[j][3] == i*10)):
				com = j+1
		for k in range(largo):
			if ((barrer[k][0] == (i+1)*10) and (barrer[k][1] == (i+1)*10) and (barrer[k][2] == (i+1)*10) and (barrer[k][3] == (i+1)*10)):
				fin = k
		m = barrer[com:fin][0::]
		Mc.append(m)

	if (i == 7):
		for j in range(largo):
			if ((barrer[j][0] == i*10) and (barrer[j][1] == i*10) and (barrer[j][2] == i*10) and (barrer[j][3] == i*10)):
				com = j+1
		m = barrer[com::][0::]
		Mc.append(m)

	i = i + 1

xf = []
plt.figure()
for i in range(len(Mc)):
	x = Mc[i][:,0]
	y = Mc[i][:,1]
	xf.append(Mc[i][:,0][-1])
	label = (i+1)*10
	plt.plot(x,y,label=label)
	
plt.legend(loc="best")
plt.title("Grafica del recorrido del proyectil lanzado a diferentes angulos")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("Parabolico2.pdf")

indice = xf.index(max(xf))
ang_max = (indice + 1) * 10
print "El angulo para el cual la distancia recorrida es mayor es para", ang_max, "grados."

#PUNTO 3 (BONO)

datos1 = np.genfromtxt("fijos.dat")
n1 = len(datos1)/50

M1 = []
for i in range(n1):
	m = datos1[i*50:(i+1)*50][0::]
	M1.append(m)

def data1(i, z1, line1):
	z1 = M1[i]
	ax1.clear()
	ax1.set_xlim(0, 50)
	ax1.set_ylim(0, 50)
	ax1.set_zlim(10, 100)
	ax1.set_xlabel("x (cm)")
	ax1.set_ylabel("y (cm)")
	ax1.set_zlabel("Temperatura (C)")
	plt.title("Temperatura de la placa para condiciones fijas")
	line1 = ax1.plot_surface(x1,y1,z1,cmap=cm.coolwarm,linewidth=0, antialiased=False)
	return line1

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

x1 = np.linspace(0,49,50,dtype='int')
y1 = np.linspace(0,49,50,dtype='int')
x1,y1 = np.meshgrid(x1,y1)
z1 = M1[0]
line1 = ax1.plot_surface(x1,y1,z1,cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig1.colorbar(line, shrink=0.5, aspect=5)
plt.title("Temperatura en distintos instantes")

ani1 = animation.FuncAnimation(fig1, data1, fargs=(M1, line1), frames = len(M1), interval=30, blit=False)
ani1.save("fijos.gif",writer = "imagemagick",fps=20)



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

#PUNTO 3 CONTINUACION (NO BONO)

def funcion(x,y,M):
	z = M[x][y]
	return z

l1 = len(M1)
f1 = int(l1/3)

M10 = M1[0]
M11 = M1[f1]
M12 = M1[2*f1]
M13 = M1[-1]

x10 = np.linspace(0,49,50,dtype="int")
y10 = np.linspace(0,49,50,dtype="int")
z10 = funcion(x10,y10,M10)
fig10 = plt.figure()
ax10 = fig10.gca(projection='3d')
ax10.set_xlim(0, 50)
ax10.set_ylim(0, 50)
ax10.set_zlim(10, 100)
ax10.set_xlabel("x (cm)")
ax10.set_ylabel("y (cm)")
ax10.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa la principio para condiciones fijas")
x10, y10 = np.meshgrid(x10, y10)
surf10 = ax10.plot_surface(x10,y10,z10, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig10.colorbar(surf10, shrink=0.5, aspect=5)
plt.savefig("Plot10.pdf")

x11 = np.linspace(0,49,50,dtype="int")
y11 = np.linspace(0,49,50,dtype="int")
z11 = funcion(x11,y11,M11)
fig11 = plt.figure()
ax11 = fig11.gca(projection='3d')
ax11.set_xlim(0, 50)
ax11.set_ylim(0, 50)
ax11.set_zlim(10, 100)
ax11.set_xlabel("x (cm)")
ax11.set_ylabel("y (cm)")
ax11.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa en un punto medio para condiciones fijas")
x11, y11 = np.meshgrid(x11, y11)
surf11 = ax11.plot_surface(x11,y11,z11, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig11.colorbar(surf11, shrink=0.5, aspect=5)
plt.savefig("Plot11.pdf")

x12 = np.linspace(0,49,50,dtype="int")
y12 = np.linspace(0,49,50,dtype="int")
z12 = funcion(x12,y12,M12)
fig12 = plt.figure()
ax12 = fig12.gca(projection='3d')
ax12.set_xlim(0, 50)
ax12.set_ylim(0, 50)
ax12.set_zlim(10, 100)
ax12.set_xlabel("x (cm)")
ax12.set_ylabel("y (cm)")
ax12.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa en un punto medio para condiciones fijas")
x12, y12 = np.meshgrid(x12, y12)
surf12 = ax12.plot_surface(x12,y12,z12, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig12.colorbar(surf12, shrink=0.5, aspect=5)
plt.savefig("Plot12.pdf")

x13 = np.linspace(0,49,50,dtype="int")
y13 = np.linspace(0,49,50,dtype="int")
z13 = funcion(x13,y13,M13)
fig13 = plt.figure()
ax13 = fig13.gca(projection='3d')
ax13.set_xlim(0, 50)
ax13.set_ylim(0, 50)
ax13.set_zlim(10, 100)
ax13.set_xlabel("x (cm)")
ax13.set_ylabel("y (cm)")
ax13.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa al final para condiciones fijas")
x13, y13 = np.meshgrid(x13, y13)
surf13 = ax13.plot_surface(x13,y13,z13, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig13.colorbar(surf13, shrink=0.5, aspect=5)
plt.savefig("Plot13.pdf")



l2 = len(M2)
f2 = int(l2/3)

M20 = M2[0]
M21 = M2[f2]
M22 = M2[2*f2]
M23 = M2[-1]

x20 = np.linspace(0,49,50,dtype="int")
y20 = np.linspace(0,49,50,dtype="int")
z20 = funcion(x20,y20,M20)
fig20 = plt.figure()
ax20 = fig20.gca(projection='3d')
ax20.set_xlim(0, 50)
ax20.set_ylim(0, 50)
ax20.set_zlim(10, 100)
ax20.set_xlabel("x (cm)")
ax20.set_ylabel("y (cm)")
ax20.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa la principio para condiciones abiertas")
x20, y20 = np.meshgrid(x20, y20)
surf20 = ax20.plot_surface(x20,y20,z20, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig20.colorbar(surf20, shrink=0.5, aspect=5)
plt.savefig("Plot20.pdf")

x21 = np.linspace(0,49,50,dtype="int")
y21 = np.linspace(0,49,50,dtype="int")
z21 = funcion(x21,y21,M21)
fig21 = plt.figure()
ax21 = fig21.gca(projection='3d')
ax21.set_xlim(0, 50)
ax21.set_ylim(0, 50)
ax21.set_zlim(10, 100)
ax21.set_xlabel("x (cm)")
ax21.set_ylabel("y (cm)")
ax21.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa en un punto medio para condiciones abiertas")
x21, y21 = np.meshgrid(x21, y21)
surf21 = ax21.plot_surface(x21,y21,z21, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig21.colorbar(surf21, shrink=0.5, aspect=5)
plt.savefig("Plot21.pdf")

x22 = np.linspace(0,49,50,dtype="int")
y22 = np.linspace(0,49,50,dtype="int")
z22 = funcion(x22,y22,M22)
fig22 = plt.figure()
ax22 = fig22.gca(projection='3d')
ax22.set_xlim(0, 50)
ax22.set_ylim(0, 50)
ax22.set_zlim(10, 100)
ax22.set_xlabel("x (cm)")
ax22.set_ylabel("y (cm)")
ax22.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa en un punto medio para condiciones abiertas")
x22, y22 = np.meshgrid(x22, y22)
surf22 = ax22.plot_surface(x22,y22,z22, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig22.colorbar(surf22, shrink=0.5, aspect=5)
plt.savefig("Plot22.pdf")

x23 = np.linspace(0,49,50,dtype="int")
y23 = np.linspace(0,49,50,dtype="int")
z23 = funcion(x23,y23,M23)
fig23 = plt.figure()
ax23 = fig23.gca(projection='3d')
ax23.set_xlim(0, 50)
ax23.set_ylim(0, 50)
ax23.set_zlim(10, 100)
ax23.set_xlabel("x (cm)")
ax23.set_ylabel("y (cm)")
ax23.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa al final para condiciones abiertas")
x23, y23 = np.meshgrid(x23, y23)
surf23 = ax23.plot_surface(x23,y23,z23, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig23.colorbar(surf23, shrink=0.5, aspect=5)
plt.savefig("Plot23.pdf")



l3 = len(M3)
f3 = int(l3/3)

M30 = M3[0]
M31 = M3[f3]
M32 = M3[2*f3]
M33 = M3[-1]

x30 = np.linspace(0,49,50,dtype="int")
y30 = np.linspace(0,49,50,dtype="int")
z30 = funcion(x30,y30,M30)
fig30 = plt.figure()
ax30 = fig30.gca(projection='3d')
ax30.set_xlim(0, 50)
ax30.set_ylim(0, 50)
ax30.set_zlim(10, 100)
ax30.set_xlabel("x (cm)")
ax30.set_ylabel("y (cm)")
ax30.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa la principio para condiciones periodicas")
x30, y30 = np.meshgrid(x30, y30)
surf30 = ax30.plot_surface(x30,y30,z30, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig30.colorbar(surf30, shrink=0.5, aspect=5)
plt.savefig("Plot30.pdf")

x31 = np.linspace(0,49,50,dtype="int")
y31 = np.linspace(0,49,50,dtype="int")
z31 = funcion(x31,y31,M31)
fig31 = plt.figure()
ax31 = fig31.gca(projection='3d')
ax31.set_xlim(0, 50)
ax31.set_ylim(0, 50)
ax31.set_zlim(10, 100)
ax31.set_xlabel("x (cm)")
ax31.set_ylabel("y (cm)")
ax31.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa en un punto medio para condiciones periodicas")
x31, y31 = np.meshgrid(x31, y31)
surf31 = ax31.plot_surface(x31,y31,z31, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig31.colorbar(surf31, shrink=0.5, aspect=5)
plt.savefig("Plot31.pdf")

x32 = np.linspace(0,49,50,dtype="int")
y32 = np.linspace(0,49,50,dtype="int")
z32 = funcion(x32,y32,M32)
fig32 = plt.figure()
ax32 = fig32.gca(projection='3d')
ax32.set_xlim(0, 50)
ax32.set_ylim(0, 50)
ax32.set_zlim(10, 100)
ax32.set_xlabel("x (cm)")
ax32.set_ylabel("y (cm)")
ax32.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa en un punto medio para condiciones periodicas")
x32, y32 = np.meshgrid(x32, y32)
surf32 = ax32.plot_surface(x32,y32,z32, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig32.colorbar(surf32, shrink=0.5, aspect=5)
plt.savefig("Plot32.pdf")

x33 = np.linspace(0,49,50,dtype="int")
y33 = np.linspace(0,49,50,dtype="int")
z33 = funcion(x33,y33,M33)
fig33 = plt.figure()
ax33 = fig33.gca(projection='3d')
ax33.set_xlim(0, 50)
ax33.set_ylim(0, 50)
ax33.set_zlim(10, 100)
ax33.set_xlabel("x (cm)")
ax33.set_ylabel("y (cm)")
ax33.set_zlabel("Temperatura (C)")
plt.title("Temperatura de la placa al final para condiciones periodicas")
x33, y33 = np.meshgrid(x33, y33)
surf33 = ax33.plot_surface(x33,y33,z33, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig33.colorbar(surf33, shrink=0.5, aspect=5)
plt.savefig("Plot33.pdf")



T1 = []
for i in range(len(M1)):
	temp = []
	largo, ancho = np.shape(M1[i])
	for j in range(largo):
		for k in range(ancho):
			if (M1[i][j][k] != 100):
				temp.append(M1[i][j][k])
	T1.append(np.average(temp))

T2 = []
for i in range(len(M2)):
	temp = []
	largo, ancho = np.shape(M2[i])
	for j in range(largo):
		for k in range(ancho):
			if (M2[i][j][k] != 100):
				temp.append(M2[i][j][k])
	T2.append(np.average(temp))

T3 = []
for i in range(len(M3)):
	temp = []
	largo, ancho = np.shape(M3[i])
	for j in range(largo):
		for k in range(ancho):
			if (M3[i][j][k] != 100):
				temp.append(M3[i][j][k])
	T3.append(np.average(temp))

t1 = np.linspace(0,len(T1)-1,len(T1))
t2 = np.linspace(0,len(T2)-1,len(T2))
t3 = np.linspace(0,len(T3)-1,len(T3))

plt.figure()
plt.plot(t1,T1,label="Temperatura promedio")
plt.legend(loc="best")
plt.title("Temperatura promedio de la placa en funcion del tiempo para condiciones fijas")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (C)")
plt.savefig("Prom1.pdf")

plt.figure()
plt.plot(t2,T2,label="Temperatura promedio")
plt.legend(loc="best")
plt.title("Temperatura promedio de la placa en funcion del tiempo para condiciones abiertas")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (C)")
plt.savefig("Prom2.pdf")

plt.figure()
plt.plot(t3,T3,label="Temperatura promedio")
plt.legend(loc="best")
plt.title("Temperatura promedio de la placa en funcion del tiempo para condiciones periodicas")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (C)")
plt.savefig("Prom3.pdf")

