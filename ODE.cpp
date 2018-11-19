#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;
#define PI 3.14159265358979323846

float r_prima(float v);
float x_prima2(float c, float vx, float vy, float m);
float y_prima2(float c, float vx, float vy, float m, float g);
void angulo(float h, float g, float c, float m, float v0, float ang);
void barrer(float h, float g, float c, float m, float v0, float ang_i, float ang_f, float ang_esp);

int main()
{
	float h = 0.001;
	float g = 10;
	float c = 0.2;
	float m = 0.2;
	float ang = 45;
	float v0 = 300;
	angulo(h,g,c,m,v0,ang);

	float ang_i = 10;
	float ang_f = 70;
	float ang_esp = 10;
	barrer(h,g,c,m,v0,ang_i,ang_f,ang_esp);
	return 0;
}

float r_prima(float v)
{
	return v;
}

float x_prima2(float c, float vx, float vy, float m)
{
	float v = pow((pow(vx,2)+pow(vy,2)),0.5);
	float a = -(c*(pow(v,2)/m)*(vx/v));
	return a;
}

float y_prima2(float c, float vx, float vy, float m, float g)
{
	float v = pow((pow(vx,2)+pow(vy,2)),0.5);
	float a = -g -(c*(pow(v,2)/m)*(vy/v));
	return a;
}

void angulo(float h, float g, float c, float m, float v0, float ang)
{
	float x[10000];
	float y[10000];
	float vx[10000];
	float vy[10000];

	ang = ang * (PI/180);
	x[0] = 0;
	y[0] = 0;
	vy[0] = v0 * sin(ang);
	vx[0] = v0 * cos(ang);

	int i = 0;
	float y_a = y[i];

	while (y_a >= 0)
	{
		i = i + 1;

		float k1, k2, k3, k4;
		float l1, l2, l3, l4;
		float m1, m2, m3, m4;
		float n1, n2, n3, n4;
		
		k1 = h * r_prima(vx[i-1]);
		k2 = h * r_prima(vx[i-1] + 0.5 * k1);
		k3 = h * r_prima(vx[i-1] + 0.5 * k2);
		k4 = h * r_prima(vx[i-1] + k3);
		float k_prom = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);	
	        x[i] = x[i-1] + k_prom;

		l1 = h * r_prima(vy[i-1]);
		l2 = h * r_prima(vy[i-1] + 0.5 * l1);
		l3 = h * r_prima(vy[i-1] + 0.5 * l2);
		l4 = h * r_prima(vy[i-1] + l3);
		float l_prom = (1.0/6.0)*(l1 + 2.0*l2 + 2.0*l3 + l4);	
	        y[i] = y[i-1] + l_prom;

		m1 = h * x_prima2(c,vx[i-1],vy[i-1],m);
		n1 = h * y_prima2(c,vx[i-1],vy[i-1],m,g);

		m2 = h * x_prima2(c,vx[i-1] + 0.5 * m1,vy[i-1] + 0.5 * n1,m);
		n2 = h * y_prima2(c,vx[i-1] + 0.5 * m1,vy[i-1] + 0.5 * n1,m,g);

		m3 = h * x_prima2(c,vx[i-1] + 0.5 * m2,vy[i-1] + 0.5 * n2,m);
		n3 = h * y_prima2(c,vx[i-1] + 0.5 * m2,vy[i-1] + 0.5 * n2,m,g);

		m4 = h * x_prima2(c,vx[i-1] + m3,vy[i-1] + n3,m);
		n4 = h * y_prima2(c,vx[i-1] + m3,vy[i-1] + n3,m,g);

		float m_prom = (1.0/6.0)*(m1 + 2.0*m2 + 2.0*m3 + m4);	
	        vx[i] = vx[i-1] + m_prom;

		float n_prom = (1.0/6.0)*(n1 + 2.0*n2 + 2.0*n3 + n4);	
		vy[i] = vy[i-1] + n_prom;

		y_a = y[i];
	}
	
	ofstream file1;
	file1.open("angulo.dat");
	for (int j = 0; j < i; j++)
		file1 << x[j] << " " << y[j] << " " << vx[j] << " " << vy[j] << std::endl;
	file1.close();
}




void barrer(float h, float g, float c, float m, float v0, float ang_i, float ang_f, float ang_esp)
{
	float ang_a = ang_i;
	ofstream file2;
	file2.open("barrer.dat");
	while (ang_a <= ang_f)
	{
		float x[10000];
		float y[10000];
		float vx[10000];
		float vy[10000];

		ang_a = ang_a * (PI/180);
		x[0] = 0;
		y[0] = 0;
		vy[0] = v0 * sin(ang_a);
		vx[0] = v0 * cos(ang_a);

		int i = 0;
		float y_a = y[i];

		while (y_a >= 0)
		{
			i = i + 1;

			float k1, k2, k3, k4;
			float l1, l2, l3, l4;
			float m1, m2, m3, m4;
			float n1, n2, n3, n4;
		
			k1 = h * r_prima(vx[i-1]);
			k2 = h * r_prima(vx[i-1] + 0.5 * k1);
			k3 = h * r_prima(vx[i-1] + 0.5 * k2);
			k4 = h * r_prima(vx[i-1] + k3);
			float k_prom = (1.0/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4);	
			x[i] = x[i-1] + k_prom;

			l1 = h * r_prima(vy[i-1]);
			l2 = h * r_prima(vy[i-1] + 0.5 * l1);
			l3 = h * r_prima(vy[i-1] + 0.5 * l2);
			l4 = h * r_prima(vy[i-1] + l3);
			float l_prom = (1.0/6.0)*(l1 + 2.0*l2 + 2.0*l3 + l4);	
			y[i] = y[i-1] + l_prom;

			m1 = h * x_prima2(c,vx[i-1],vy[i-1],m);
			n1 = h * y_prima2(c,vx[i-1],vy[i-1],m,g);

			m2 = h * x_prima2(c,vx[i-1] + 0.5 * m1,vy[i-1] + 0.5 * n1,m);
			n2 = h * y_prima2(c,vx[i-1] + 0.5 * m1,vy[i-1] + 0.5 * n1,m,g);

			m3 = h * x_prima2(c,vx[i-1] + 0.5 * m2,vy[i-1] + 0.5 * n2,m);
			n3 = h * y_prima2(c,vx[i-1] + 0.5 * m2,vy[i-1] + 0.5 * n2,m,g);

			m4 = h * x_prima2(c,vx[i-1] + m3,vy[i-1] + n3,m);
			n4 = h * y_prima2(c,vx[i-1] + m3,vy[i-1] + n3,m,g);

			float m_prom = (1.0/6.0)*(m1 + 2.0*m2 + 2.0*m3 + m4);	
	        	vx[i] = vx[i-1] + m_prom;

			float n_prom = (1.0/6.0)*(n1 + 2.0*n2 + 2.0*n3 + n4);	
			vy[i] = vy[i-1] + n_prom;

			y_a = y[i];
		}
	
		ang_a = ang_a * (180/PI);

		file2 << ang_a << " " << ang_a << " " << ang_a << " " << ang_a << std::endl;
		for (int j = 0; j < i; j++)
			file2 << x[j] << " " << y[j] << " " << vx[j] << " " << vy[j] << std::endl;

		ang_a = ang_a + ang_esp;
	}
	file2.close();
}

