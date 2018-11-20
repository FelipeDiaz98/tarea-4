Resultados_hw4.pdf: Resultados_hw4.tex Parabolico1.pdf Plot10.pdf
	pdflatex Resultados_hw4.tex

Parabolico1.pdf: Plots_hw4.py angulo.dat barrer.dat
	python Plots_hw4.py

Plot10.pdf: Plots_hw4.py fijos.dat abiertos.dat periodicos.dat
	python Plots_hw4.py

angulo.dat: a.out
	./a.out

a.out: ODE.cpp
	g++ ODE.cpp

fijos.dat: a.out
	./a.out

a.out: PDE.cpp
	g++ PDE.cpp

