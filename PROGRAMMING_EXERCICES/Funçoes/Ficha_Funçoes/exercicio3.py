# 3) Crie uma função que receba dois valores float como argumentos e
# retorne o valor da raiz quadrada da soma dos quadrados.

import math

def raiz_da_soma(a,b):

    quadrado_a = (a * a)
    quadrado_b = (b * b)
    soma_quadrados = (quadrado_a + quadrado_b)

    return math.sqrt(soma_quadrados)

print(raiz_da_soma(2,3))
