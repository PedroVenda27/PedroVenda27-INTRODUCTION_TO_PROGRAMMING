# Foram anotadas as idades e alturas de 30 alunos. 
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
contador = 0
n=1
idades = []
alturas = []
maioresqmedia = []

while n <= 30:
        idade = int(input(f" Insira a {n}ª idade: "))
        altura = float(input(f" Insira a {n}ª idade:: "))
        if idade <= 0 or altura <= 0:
            print("insira valores validos valido")
        else:
            idades.append(idade)
            alturas.append(altura)
            n = n + 1


media_alturas = sum(alturas) / len(alturas)
print(f"Media das Alturas: {media_alturas}")

for i, altura in enumerate(alturas):
    if idade[i] > 13 and altura < media_alturas:
        contador = contador + 1

print(f"Alunos com mais de 13 anos e altura inferior à média: {contador}")



