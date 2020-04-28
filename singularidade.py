import gauss_legendre
import newton_cotes


def simples(a, b, equacao, tolerancia=0.000001, grau=2, metodo=gauss_legendre):
    ''' `metodo`: metodo de integracao '''

    x_s = str((a+b)/2) +' + ('+ str((b-a)/2) +' * tanh(x))'
    dxs_ds = str((b-a)/2) +' * 1 / cosh(x)**2'
    equacao = '(' + equacao.replace('x', '('+x_s+')') + ') * (' + dxs_ds + ')'
    
    integral = 0
    erro = 999999999
    c = 0

    while erro > tolerancia:
        c += 0.1
        integral_anterior = integral
        integral, _ = metodo.integral(-c, c, equacao, tolerancia, grau)
        erro = abs((integral - integral_anterior) / integral)

    return integral, (round(-c, 2), round(c, 2))


def dupla(a, b, equacao, tolerancia=0.000001, grau=2, metodo=gauss_legendre):
    ''' `metodo`: metodo de integracao '''

    x_s = str((a+b)/2) +' + ('+ str((b-a)/2) +' * tanh((pi/2)*sinh(x)))'
    dxs_ds = str((b-a)/2) +' * (pi/2) * (cosh(x) / ((cosh((pi/2) * sinh(x))) ** 2))'
    equacao = equacao.replace('x', '('+x_s+')') + ' * ' + dxs_ds

    integral = 0
    erro = 999999999
    c = 0

    while erro > tolerancia:
        c += 0.01
        integral_anterior = integral
        integral, _ = metodo.integral(-c, c, equacao, tolerancia, grau)
        erro = abs((integral - integral_anterior) / integral)
        
    return integral, (round(-c, 2), round(c, 2))


if __name__ == '__main__':

    equacao = '1/sqrt(x)'  # = 2
    integral, intervalo = simples(0, 1, equacao)
    print(f'função:{equacao}, estratégia:simples, integral:{integral}, intervalo:{intervalo}')
    integral, intervalo = dupla(0, 1, equacao)
    print(f'função:{equacao}, estratégia:simples, integral:{integral}, intervalo:{intervalo}')

    equacao = '1/(sqrt(4-(x**2)))'  # = 1.57079633
    integral, intervalo = simples(0, 1, equacao)
    print(f'função:{equacao}, estratégia:simples, integral:{integral}, intervalo:{intervalo}')
    integral, intervalo = dupla(0, 1, equacao)
    print(f'função:{equacao}, estratégia:simples, integral:{integral}, intervalo:{intervalo}')

    equacao = '1/((x**2)**(1/3))'  # = 6
    integral1, intervalo1 = simples(-1, 0, equacao)
    integral2, intervalo2 = simples(0, 1, equacao)
    print(f'função:{equacao}, estratégia:simples, integral:{integral1+integral2}, intervalos:{intervalo1, intervalo2}')

    integral3, intervalo3 = dupla(-1, 0, equacao)
    integral4, intervalo4 = dupla(0, 1, equacao)
    print(f'função:{equacao} estratégia:dupla, integral:{integral3+integral4}, intervalos:{intervalo3, intervalo4}')
