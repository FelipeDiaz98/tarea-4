#include <iostream>
#include <cmath>

float r_prima(float v);
float x_prima2(float c, float vx, float vy, float m);
float y_prima2(float c, float vx, float vy, float m, float g);
void solucionar(float h, float g, float c, float m, float angulo, float v0);

int main()
{
	float h = 0.001;
	float g = 10;
	float c = 0.2;
	float m = 0.2;
	float angulo = 45;
	float v0 = 300;
	solucionar(h, g, c, m, angulo, v0);
	return 0;
}

float r_prima(float v)
{
	return v;
}

float x_prima2(float c, float vx, float vy, float m)
{
	float v = pow((pow(vx,2)+pow(vy,2)),0.5);
	float a = -(c*(pow(abs(v),2)/m)*(vx/abs(v)));
	return a;
}

float y_prima2(float c, float vx, float vy, float m, float g)
{
	float v = pow((pow(vx,2)+pow(vy,2)),0.5);
	float a = -g -(c*(pow(abs(v),2)/m)*(vy/abs(v)));
	return a;
}

void solucionar(float h, float g, float c, float m, float angulo, float v0)
{
	float x[10000];
	float y[10000];
	float vx[10000];
	float vy[10000];

	x[0] = 0;
	y[0] = 0;
	vy[0] = v0 * sin(angulo);
	vx[0] = v0 * cos(angulo);

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
		m2 = h * x_prima2(c,vx[i-1] + 0.5 * m1,vy[i-1] + 0.5 * m1,m);
		m3 = h * x_prima2(c,vx[i-1] + 0.5 * m2,vy[i-1] + 0.5 * m2,m);
		m4 = h * x_prima2(c,vx[i-1] + m3,vy[i-1] + m3,m);
		float m_prom = (1.0/6.0)*(m1 + 2.0*m2 + 2.0*m3 + m4);	
	        vx[i] = vx[i-1] + m_prom;

		n1 = h * y_prima2(c,vx[i-1],vy[i-1],m,g);
		n2 = h * y_prima2(c,vx[i-1] + 0.5 * n1,vy[i-1] + 0.5 * n1,m,g);
		n3 = h * y_prima2(c,vx[i-1] + 0.5 * n2,vy[i-1] + 0.5 * n2,m,g);
		n4 = h * y_prima2(c,vx[i-1] + n3,vy[i-1] + n3,m,g);
		float n_prom = (1.0/6.0)*(n1 + 2.0*n2 + 2.0*n3 + n4);	
		vy[i] = vy[i-1] + n_prom;

		y_a = y[i];
	}
	
	for (int j = 0; j < i; j++)
		std::cout << x[j] << " " << y[j] << " " << vx[j] << " " << vy[j] << std::endl;
}

