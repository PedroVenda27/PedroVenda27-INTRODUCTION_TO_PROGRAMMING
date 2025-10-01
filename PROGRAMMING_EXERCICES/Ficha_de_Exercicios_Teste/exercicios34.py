# 34) Máximo Divisor Comum: Escreva um programa que leia dois
# números inteiros e determine o seu Máximo Divisor Comum (MDC).


try:
    # Solicita ao usuário para digitar dois números inteiros
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))

    # Verifica qual número é maior e atribui aos valores máximo e mínimo
    if num1 > num2:
        maximo = num1
        minimo = num2
    else:
        maximo = num2
        minimo = num1

    # Algoritmo para encontrar o MDC
    while minimo != 0:
        resto = maximo % minimo
        maximo = minimo
        minimo = resto

    # O MDC é o último divisor não nulo
    mdc = maximo

    # Verifica se o MDC é zero (quando os números iniciais são ambos zero)
    if mdc == 0:
        mdc_texto = "(não existe)"
    else:
        mdc_texto = str(mdc)

    # Exibe o resultado
    print("O maior divisor comum é:", mdc_texto)

except ValueError:
    # Trata o erro se o usuário não inserir números inteiros
    print("Por favor, insira um número inteiro válido.")
