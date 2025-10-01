# 6) Crie um programa para escrever a série de quadrados entre 1 e
# um valor inteiro inferior a 100 introduzido pelo utilizador. (1,
# 4, 9, 25...)




y=0
total=0

while y != 1:
    valormaximo = int(input("Insira o valor maximo ate qual deseja calcular os quadrados (1-99):"))

    if valormaximo < 1 or valormaximo > 99:
        print("O número não está inserido entre os valores de 1 e 99")
    else:
        y = 1

if y==1:
    x = 1
    while total<=valormaximo:
        total=x*x
        if total<valormaximo:
            print(x ,"x", x , "=", total)
        x=x+1


        