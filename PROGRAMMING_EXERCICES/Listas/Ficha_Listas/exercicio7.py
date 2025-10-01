#7) Crie um programa que leia um conjunto de valores inteiros do
# utilizador e os coloque num vetor. O programa deverá terminar a
# leitura quando for introduzido um número que já exista no vetor, ou
# seja, quando for introduzido um número repetido. No final deverá
# apresentar o vetor.

vetor = []  # Vetor (lista) vazia
i = 0
a = 0

while True:
    while a == 0:
        inserir= True
        num = int(input((f"Digite o {i + 1}º valor inteiro: ")))
        if i != 0:
            for x in range (0,i):
                if vetor[x] == num:
                    inserir = False
                    a = 1
                    break
                    

        if inserir:
            vetor.append(num)
            i += 1

        else:
            print("fim de Programa inseriu um numero repetido (já existente na lista)")
            print(vetor)

