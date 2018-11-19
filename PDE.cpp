#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

void fijos(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu, float ta);
void abiertos(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu, float ta);
void periodicos(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu, float ta);
float calccirc(float xc, float yc, float r);

int main()
{
	int x_max = 50;
	int y_max = 50;
	float tc = 100;
	float xc = 25;
	float yc = 25;
	float dc = 10;	
	float tao = 0.5;
	float t_max = 400000;
	float ta = 10;
	float k = 1.62;
	float C_p = 820;
	float p = 2.71;
	float nu = k/(C_p * p);
	//fijos(x_max,y_max,tc,xc,yc,dc,tao,t_max,nu,ta);
	//abiertos(x_max,y_max,tc,xc,yc,dc,tao,t_max,nu,ta);
	periodicos(x_max,y_max,tc,xc,yc,dc,tao,t_max,nu,ta);
	
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

void fijos(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu, float ta)
{
	float pasado[x_max][y_max];
	float presente[x_max][y_max];
	float r = dc/2;
	int c = 0;
	ofstream file1;
	file1.open("fijos.dat");

	for (int i = 0; i < x_max; i++)
		for (int j = 0; j < y_max; j++)
		{
			if (calccirc(i,xc,j,yc,r) == 0)
				pasado[i][j] = tc;
			if (calccirc(i,xc,j,yc,r) == 1)
				pasado[i][j] = ta;
		}

	for (int i = 0; i < x_max; i++)
	{
		for (int j = 0; j < y_max; j++)
			file1 << pasado[i][j] << " ";
		file1 << std::endl;
	}

	c = c + 1;
	float t = tao;
	while (t < t_max)
	{
		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
			{
				if (calccirc(i,xc,j,yc,r) == 0)
					presente[i][j] = tc;
				else
				{
					if ((i == 0) or (i == x_max-1) or (j == 0) or (j == y_max-1))
						presente[i][j] = ta;
					else
						presente[i][j] = (nu*tao*(pasado[i+1][j] + pasado[i-1][j] + pasado[i][j+1] + pasado[i][j-1] - (4*pasado[i][j])) + pasado[i][j]);
				}	
			}
		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
				pasado[i][j] = presente[i][j];

		if (c%10000 == 0)
			for (int i = 0; i < x_max; i++)
			{
				for (int j = 0; j < y_max; j++)
					file1 << pasado[i][j] << " ";
				file1 << std::endl;
			}

		c = c + 1;
		t = t + tao;
	}

	file1.close();
}




void abiertos(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu, float ta)
{
	float pasado[x_max][y_max];
	float presente[x_max][y_max];
	float r = dc/2;
	int c = 0;
	ofstream file2;
	file2.open("abiertos.dat");
	
	for (int i = 0; i < x_max; i++)
		for (int j = 0; j < y_max; j++)
		{
			if (calccirc(i,xc,j,yc,r) == 0)
				pasado[i][j] = tc;
			if (calccirc(i,xc,j,yc,r) == 1)
				pasado[i][j] = ta;
		}

	for (int i = 0; i < x_max; i++)
	{
		for (int j = 0; j < y_max; j++)
			file2 << pasado[i][j] << " ";
		file2 << std::endl;
	}

	c = c + 1;
	float t = tao;
	while (t < t_max)
	{
		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
			{
				if (calccirc(i,xc,j,yc,r) == 0)
					presente[i][j] = tc;
				else
				{
					if ((i == 0) or (i == x_max-1) or (j == 0) or (j == y_max-1))
					{
						if (i == 0)
							presente[i][j] = presente[i+1][j];
						if (i == x_max-1)
							presente[i][j] = presente[i-1][j];
						if (j == 0)
							presente[i][j] = presente[i][j+1];
						if (j == y_max-1)
							presente[i][j] = presente[i][j-1];
					}
					else
						presente[i][j] = (nu*tao*(pasado[i+1][j] + pasado[i-1][j] + pasado[i][j+1] + pasado[i][j-1] - (4*pasado[i][j])) + pasado[i][j]);
				}	
			}

		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
				pasado[i][j] = presente[i][j];

		if (c%10000 == 0)
			for (int i = 0; i < x_max; i++)
			{
				for (int j = 0; j < y_max; j++)
					file2 << pasado[i][j] << " ";
				file2 << std::endl;
			}

		c = c + 1;
		t = t + tao;
	}

	file2.close();
}



void periodicos(int x_max, int y_max, float tc, float xc, float yc, float dc, float tao, float t_max, float nu, float ta)
{
	float pasado[x_max][y_max];
	float presente[x_max][y_max];
	float r = dc/2;
	int c = 0;
	ofstream file3;
	file3.open("periodicos.dat");
	
	for (int i = 0; i < x_max; i++)
		for (int j = 0; j < y_max; j++)
		{
			if (calccirc(i,xc,j,yc,r) == 0)
				pasado[i][j] = tc;
			if (calccirc(i,xc,j,yc,r) == 1)
				pasado[i][j] = ta;
		}

	for (int i = 0; i < x_max; i++)
	{
		for (int j = 0; j < y_max; j++)
			file3 << pasado[i][j] << " ";
		file3 << std::endl;
	}

	c = c + 1;
	float t = tao;
	while (t < t_max)
	{
		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
			{
				if (calccirc(i,xc,j,yc,r) == 0)
					presente[i][j] = tc;
				else
				{
					if ((i == 0) or (i == x_max-1) or (j == 0) or (j == y_max-1))
					{
						if (i == 0)
							presente[i][j] = presente[x_max-2][j];
						if (i == x_max-1)
							presente[i][j] = presente[1][j];
						if (j == 0)
							presente[i][j] = presente[i][y_max-2];
						if (j == y_max-1)
							presente[i][j] = presente[i][1];
					}
					else
						presente[i][j] = (nu*tao*(pasado[i+1][j] + pasado[i-1][j] + pasado[i][j+1] + pasado[i][j-1] - (4*pasado[i][j])) + pasado[i][j]);
				}	
			}

		for (int i = 0; i < x_max; i++)
			for (int j = 0; j < y_max; j++)
				pasado[i][j] = presente[i][j];

		if (c%10000 == 0)
			for (int i = 0; i < x_max; i++)
			{
				for (int j = 0; j < y_max; j++)
					file3 << pasado[i][j] << " ";
				file3 << std::endl;
			}

		c = c + 1;
		t = t + tao;
	}

	file3.close();
}

