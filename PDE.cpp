#include <iostream>
#include <cmath>

void solucionar(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu);
float calccirc(float xc, float yc, float r);

int main()
{
	int x_max = 50;
	int y_max = 50;
	float tc = 100;
	float xc = 25;
	float yc = 25;
	float dc = 10;	
	float tao = 0.1;
	float t_max = 30000;
	float k = 1.62;
	float C_p = 820;
	float p = 2.71;
	float nu = k/(C_p * p);
	solucionar(x_max,y_max,tc,xc,yc,dc,tao,t_max,nu);
	
	return 0;
}

float calccirc(int i, float xc, int j, float yc, float r)
{
	float p = (pow((i-xc),2) + pow((j-yc),2));
	if (p <= pow(r,2))
		return 0;
	else
		return 1;
}

void solucionar(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu)
{
	float pasado[x_max][y_max];
	float presente[x_max][y_max];
	float r = dc/2;
	
	for (int i = 0; i < x_max; i++)
		for (int j = 0; j < y_max; j++)
		{
			if (calccirc(i,xc,j,yc,r) == 0)
				pasado[i][j] = 100;
			if (calccirc(i,xc,j,yc,r) == 1)
				pasado[i][j] = 0;
			if ((i == 0) or (i == x_max-1) or (j == 0) or (j == y_max-1))
				pasado[i][j] = 10;
		}

	float t = tao;
	while (t < t_max)
	{
		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
			{
				if (calccirc(i,xc,j,yc,r) == 0)
					presente[i][j] = 100;
				if ((i == 0) or (i == x_max-1) or (j == 0) or (j == y_max-1))
					presente[i][j] = 10;
				else
					presente[i][j] = (nu*tao*(pasado[i+1][j] + pasado[i-1][j] + pasado[i][j+1] + pasado[i][j-1] - (4*pasado[i][j])) + pasado[i][j]);
				
			}

		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
				pasado[i][j] = presente[i][j];

		t = t + tao;
	}

	for (int i = 0; i < x_max; i++)
	{
		for (int j = 0; j < y_max; j++)
			std::cout << presente[i][j] << " ";
		std::cout << std::endl;
	}
}














