#include <iostream>
#include <cmath>

float calcular_vx(float angulo, float v0);
float calcular_vy(float angulo, float v0);
float r_prima(float v);
float x_prima2(float c, float vx, float m, float v);
float y_prima2(float c, float vy, float m, float v, float g);
void solucionar(float tf, float h, float g, float c, float m, float angulo, float v0);

int main()
{
	float tf = 0.103;
	float h = 0.0001;
	float g = 10;
	float c = 0.2;
	float m = 0.2;
	float angulo = 45;
	float v0 = 300;
	solucionar(tf, h, g, c, m, angulo, v0);
	return 0;
}

float calcular_vx(float angulo, float v0)
{
	float vx = v0 * cos(angulo);
	return vx;
}

float calcular_vy(float angulo, float v0)
{
	float vy = v0 * sin(angulo);
	return vy;
}

float r_prima(float v)
{
	return v;
}

float x_prima2(float c, float vx, float m, float v)
{
	float a = -(c*(pow(abs(v),2)/m)*(vx/abs(v)));
	return a;
}

float y_prima2(float c, float vy, float m, float v, float g)
{
	float a = -g -(c*(pow(abs(v),2)/m)*(vy/abs(v)));
	return a;
}

void solucionar(float tf, float h, float g, float c, float m, float angulo, float v0)
{
	int n = tf/h;
	float x[n];
	float y[n];
	float vx[n];
	float vy[n];

	x[0] = 0;
	y[0] = 0;
	vy[0] = calcular_vy(angulo,v0);
	vx[0] = calcular_vx(angulo,v0);

	float v = pow((pow(vx[0],2)+pow(vy[0],2)),0.5);
	x[1] = h*r_prima(vx[0]) + x[0];
	y[1] = h*r_prima(vy[0]) + y[0];
	vx[1] = h*x_prima2(c,vx[0],m,v) + vx[0];
	vy[1] = h*y_prima2(c,vy[0],m,v,g) + vy[0];

	for (int i = 1; i < (n-1); i++)
	{
		v = pow((pow(vx[i],2)+pow(vy[i],2)),0.5);
		x[i+1] = 2*h*r_prima(vx[i]) + x[i-1];
		y[i+1] = 2*h*r_prima(vy[i]) + y[i-1];
		vx[i+1] = 2*h*x_prima2(c,vx[i],m,v) + vx[i-1];
		vy[i+1] = 2*h*y_prima2(c,vy[i],m,v,g) + vy[i-1];
		std::cout << x[i] << " " << y[i] << " " << vx[i] << " " << vy[i] << std::endl;		
	}
}

