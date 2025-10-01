# 8) Crie um programa que leia um vetor de n inteiros, sendo n um
# valor introduzido pelo utilizador, não havendo restrições. O
# programa deverá converter todos os valores negativos do vetor para
# 0, imprimir o vetor resultante e indicar quantos valores foram
# alterados. 



vetor = []  # Vetor (lista) vazia
i = 0
n = int(input((f"Digite o numero de numeros que de numeros que deseja inserir a lista: ")))

while i < n:
        num = int(input((f"Digite o {i + 1}º valor inteiro: ")))
        if num >=0:
            vetor.append(num)
        else:
            num = 0
            vetor.append(num)
        i=i+1

print(vetor)
print("fim de Programa")
