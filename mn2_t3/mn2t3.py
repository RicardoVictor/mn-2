from math import *


def integral_n(a, b, n, equacao, filosofia, grau=1):
    ''' Calcula a integral pelo metodo de Newton-Cotes com base na quantidade de iteracoes n '''

    I = 0
    delta_x = (b - a)/n

    if filosofia is 'fechada':
        h = delta_x / grau
    if filosofia is 'aberta':
        h = delta_x / (grau + 2)

    for k in range(n):
        x_inicial = a + k * delta_x
        x_final = x_inicial + delta_x

        if filosofia is 'fechada' and grau == 1:
            I += h/2 * \
                ( calc(equacao, x_inicial) \
                + calc(equacao, x_final))

        if filosofia is 'fechada' and grau == 2:
            I += h/3 * \
                ( calc(equacao, x_inicial) \
                + 4*calc(equacao, x_inicial + h) \
                + calc(equacao, x_final))

        if filosofia is 'fechada' and grau == 3:
            I += 3*h/8 * \
                ( calc(equacao, x_inicial) \
                + 3*calc(equacao, x_inicial + h) \
                + 3*calc(equacao, x_inicial + 2*h) \
                + calc(equacao, x_final))

        if filosofia is 'fechada' and grau == 4:
            I += 2*h/45 * \
                ( 7*calc(equacao, x_inicial) \
                + 32*calc(equacao, x_inicial + h) \
                + 12*calc(equacao, x_inicial + 2*h) \
                + 32*calc(equacao, x_inicial + 3*h) \
                + 7*calc(equacao, x_final))

        if filosofia is 'aberta' and grau == 1:
            I += delta_x/2 * \
                ( calc(equacao, x_inicial + h) \
                + calc(equacao, x_inicial + 2*h))

        if filosofia is 'aberta' and grau == 2:
            I += 4*h/3 * \
                ( 2*calc(equacao, x_inicial + h) \
                - calc(equacao, x_inicial + 2*h) \
                + 2*calc(equacao, x_inicial + 3*h))

        if filosofia is 'aberta' and grau == 3:
            I += 5*h/24 * \
                ( 11*calc(equacao, x_inicial + h) \
                + calc(equacao, x_inicial + 2*h) \
                + calc(equacao, x_inicial + 3*h) \
                + 11*calc(equacao, x_inicial + 4*h))

        if filosofia is 'aberta' and grau == 4:
            I += 3*h/10 * \
                ( 11*calc(equacao, x_inicial + h) \
                - 14*calc(equacao, x_inicial + 2*h) \
                + 26*calc(equacao, x_inicial + 3*h) \
                - 14*calc(equacao, x_inicial + 4*h) \
                + 11*calc(equacao, x_inicial + 5*h))

    return I


def integral(x_inicial, x_final, equacao, filosofia='fechada', grau=1, tolerancia=0.000001):
    ''' Calcula a integral pelo metodo de Newton-Cotes com base em uma tolerancia '''

    delta_x = x_final - x_inicial
    I_anterior = 0
    I = delta_x/2 * (calc(equacao, x_inicial) + calc(equacao, x_final))
    contador = 0
    erro = abs((I - I_anterior)/I)
    n = 1

    while erro > tolerancia:
        n = n*2
        contador += 1
        I_anterior = I
        I = integral_n(x_inicial, x_final, n, equacao, filosofia, grau)
        erro = abs((I - I_anterior)/I)

    return I, contador


def calc(equacao, x):
    ''' Calcula o valor de uma equacao matematica em determinado ponto x '''

    return eval(equacao)


if __name__ == '__main__':

    equacao = '(sin(2*x)+4*x**2+3*x)**2'
    x_inicial = 0
    x_final = 1
    tolerancia = 0.000001

    filosofia = 'fechada'
    grau = 1
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')
    grau = 2
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')
    grau = 3
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')
    grau = 4
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')

    filosofia = 'aberta'
    grau = 1
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')
    grau = 2
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')
    grau = 3
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')
    grau = 4
    I, cont = integral(x_inicial, x_final, equacao, filosofia, grau=grau, tolerancia=tolerancia)
    print(f'filosofia:{filosofia}, grau:{grau}, resultado:{I}, quantidade de iteracoes:{cont}')

