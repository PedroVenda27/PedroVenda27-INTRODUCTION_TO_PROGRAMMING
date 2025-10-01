# Faça um programa que leia um número indeterminado de valores, 
# correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
# Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

contador = 0
n=1
numeros = []
superior_media = []
menor_sete = []


while True:
        numero = int(input(f" Insira o {n}º numero: "))
        if numero == -1:
             break
        if numero <= 0 :
            print("insira valores validos valido")
        else:
            numeros.append(numero)
            n = n + 1

# Mostre a quantidade de valores que foram lidos;
print("Quantidade de Numeros Lidos: " , len(numeros))

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print("Numeros na ordem Normal: " , numeros)

# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("Numeros na ordem Invertida: ")
for num in reversed(numeros):
    print(num)

# Calcule e mostre a soma dos valores;
soma_numeros = sum(numeros)
print("Soma dos Numeros: " , soma_numeros)

# Calcule e mostre a média dos valores;
media_numeros = sum(numeros) / len(numeros)
print("Media dos Numeros: " , media_numeros)

# Calcule e mostre a quantidade de valores acima da média calculada;
for num in numeros:
     if num > media_numeros:
        superior_media.append(num)
        contador = contador + 1

print("Numeros superiores a Media: " , superior_media)
print(" Quantidade de Numeros superiores a Media: " , contador)

# Calcule e mostre a quantidade de valores abaixo de sete;
contador = 0
for num in numeros:
     if num < 7:
        menor_sete.append(num)
        contador = contador + 1

print("Numeros infeririores a 7: " , menor_sete)
print(" Quantidade de Numeros inferiores a 7: " , contador)


# Encerre o programa com uma mensagem;
print("Fim de Programa")


