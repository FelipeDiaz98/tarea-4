import numpy as np
import matplotlib.pyplot as plt

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
plt.savefig("parabolico1.pdf")

print "La distancia recorrida por el proyectil a un angulo de 45 grado es de", xa[-1]

largo, ancho = np.shape(barrer)
i = 1
M = []
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
		M.append(m)

	if (i == 7):
		for j in range(largo):
			if ((barrer[j][0] == i*10) and (barrer[j][1] == i*10) and (barrer[j][2] == i*10) and (barrer[j][3] == i*10)):
				com = j+1
		m = barrer[com::][0::]
		M.append(m)

	i = i + 1

xf = []
plt.figure()
for i in range(len(M)):
	x = M[i][:,0]
	y = M[i][:,1]
	xf.append(M[i][:,0][-1])
	label = (i+1)*10
	plt.plot(x,y,label=label)
	
plt.legend(loc="best")
plt.title("Grafica del recorrido del proyectil lanzado a diferentes angulos")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("parabolico2.pdf")

indice = xf.index(max(xf))
ang_max = (indice + 1) * 10
print "El angulo para el cual la distancia recorrida es mayor es para", ang_max, "grados."

