# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
# Imprima a idade e a altura na ordem inversa a ordem lida.

n=1
idades = []
alturas = []

while n <= 5:
        idade = int(input(f" Insira a {n}ª idade: "))
        altura = float(input(f" Insira a {n}ª idade:: "))
        if idade <= 0 or altura <= 0:
            print("insira valores validos valido")
        else:
            idades.append(idade)
            alturas.append(altura)
            n = n + 1


print(idades[5::-1])
print(alturas[len(alturas)::-1])
