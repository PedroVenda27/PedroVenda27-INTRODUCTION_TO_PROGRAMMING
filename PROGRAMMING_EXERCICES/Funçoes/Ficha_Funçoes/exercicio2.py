# 2) Crie uma função que receba 3 valores float como argumento e
# retorne o maior valor absoluto.

def maior_valor_absoluto(a, b, c):
    # Calcula os valores absolutos
    abs_a = abs(a)
    abs_b = abs(b)
    abs_c = abs(c)

    # Encontra o maior valor absoluto
    maior_absoluto = max(abs_a, abs_b, abs_c)

    return maior_absoluto

print(maior_valor_absoluto(3.33,4.78,2.11))

