from math import sqrt
from auxiliar import calc


def integral_2(x_min, x_max, n_particoes, equacao):
	a = x_min
	h = (x_max - x_min) / n_particoes
	b = a + h
	soma_part = 0
	area = 0

	for i in range(n_particoes):
		#area = (b-a)/2 * ( cos( (b-a)/2*-1/sqrt(3) + (b+a)/2 ) + 
		#				   cos( (b-a)/2*+1/sqrt(3) + (b+a)/2 ))
		
		area = (b-a)/2 * ( calc( equacao, (b-a)/2*-1/sqrt(3) + (b+a)/2 ) + 
						   calc( equacao, (b-a)/2*+1/sqrt(3) + (b+a)/2 ))

		soma_part += area
		a = b
		b = b + h

	return soma_part


def integral_3(x_min, x_max, n_particoes, equacao):
	a = x_min
	h = (x_max - x_min) / n_particoes
	b = a + h
	w1 = 5/9
	w2 = 8/9
	w3 = w1
	a1 = -sqrt(3/5)
	a2 = 0
	a3 = sqrt(3/5)
	soma_part = 0
	area = 0

	for i in range(n_particoes):
		area = (b-a)/2 * (w1 * calc( equacao, (b-a)/2*a1 + (b+a)/2 ) + 
						  w2 * calc( equacao, (b-a)/2*a2 + (b+a)/2 ) + 
						  w3 * calc( equacao, (b-a)/2*a3 + (b+a)/2 ))

		soma_part += area
		a = b
		b = b + h

	return soma_part


def integral_4(x_min, x_max, n_particoes, equacao):
	a = x_min
	h = (x_max - x_min) / n_particoes
	b = a + h
	w1 = (18+sqrt(30))/36
	w2 = w1
	w3 = (18-sqrt(30))/36
	w4 = w3
	a1 = sqrt((3-2*sqrt(6/5))/7)
	a2 = -sqrt((3-2*sqrt(6/5))/7)
	a3 = sqrt((3+2*sqrt(6/5))/7)
	x4 = -sqrt((3+2*sqrt(6/5))/7)
	soma_part = 0
	area = 0

	for i in range(n_particoes):
		area = (b-a)/2*(w1*calc(equacao, (b-a)/2*a1 + (b+a)/2) + 
						w2*calc(equacao, (b-a)/2*a2 + (b+a)/2) + 
						w3*calc(equacao, (b-a)/2*a3 + (b+a)/2) + 
						w4*calc(equacao, (b-a)/2*x4 + (b+a)/2))

		soma_part += area
		a = b
		b = b + h

	return soma_part


def integral(x_min, x_max, equacao, tolerancia=0.000001, grau=2):
	
	integral_anterior = 0
	integral = 0
	contador = 0
	erro = 999999999
	n = 1

	while erro > tolerancia:
		contador += 1
		n = n*2
		integral_anterior = integral

		if grau == 2:
			integral = integral_2(x_min, x_max, n, equacao)
		if grau == 3:
			integral = integral_3(x_min, x_max, n, equacao)
		if grau == 4:
			integral = integral_4(x_min, x_max, n, equacao)

		erro = abs((integral - integral_anterior) / integral)
		
	return integral, contador


if __name__ == '__main__':

	equacao = '(sin(2*x)+4*x**2+3*x)**2'

	I, cont = integral(0, 1, equacao, 0.000001, 2)
	print(f'grau:2, resultado:{I}, quantidade de iteracoes:{cont}')

	I, cont = integral(0, 1, equacao, 0.000001, 3)
	print(f'grau:3, resultado:{I}, quantidade de iteracoes:{cont}')

	I, cont = integral(0, 1, equacao, 0.000001, 4)
	print(f'grau:4, resultado:{I}, quantidade de iteracoes:{cont}')
