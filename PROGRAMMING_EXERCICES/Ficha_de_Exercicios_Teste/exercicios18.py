# 18) Escreva um programa em que o utilizador vai introduzindo
# números inteiros positivos até o número introduzido ser um número
# primo.


print("Introduza números inteiros positivos. O programa irá encerrar quando introduzir um número primo.")

while True:
    # Introdução de um número
    numero = int(input("Introduza um número: "))

    if numero <= 0:
        print("O número", numero, "não é primo.")
    elif numero == 1:
        print("O número 1 não é primo.")
    else:
        # Verifica se o número é primo
        for i in range(2, numero):
            if numero % i == 0:
                print("O número", numero, "não é primo.")
                break
        else:
            print("O número", numero, "é primo. O programa será encerrado.")
            break