
import matplotlib.pyplot as plt

def distancia(ordem,f,g):
    plt.title(ordem)
    plt.plot([float(g)], 'go',label='g(n)')
    plt.plot([float(f)], 'bo', label='f(n)')
    plt.legend()
    plt.show()


def omega(f,g):
    if f >= g:
        print('f(',f,') >= g(',g,') [Omega]')
        return True
    return False

def big_o(f,g):
    if f <= g:
        print('f(',f,') <= g(',g,') [Big O]')
        return True
    return False

def analise_assintotica(f, g):
    if omega(f,g) is True:
        return str('Omega')
    else:
        return str('Big O')

if __name__ == '__main__':

    print()

    n = 1000

    f = 10*(n**55)
    g = (2**n)

    distancia(analise_assintotica(f,g),f,g)