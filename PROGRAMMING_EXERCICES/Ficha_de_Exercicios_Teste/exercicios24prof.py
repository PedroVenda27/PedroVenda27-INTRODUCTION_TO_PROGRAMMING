#24) Crie um programa para escrever a série de Fibonacci até a um
#limite pedido pelo utilizador. (0, 1, 2, 3, 5, 8, 13, 21...)
 
lim = 0
 
while lim <= 0:
    lim = int(input("Até que limite quer visualizar a série de Fibonacci: "))
 
p0 = 0
p1 = 1
 
serie_fib = ""
 
while p0 <= lim:
    serie_fib += f"{p0} "
    fib = p0 + p1
    p0 = p1
    p1 = fib

print(serie_fib)