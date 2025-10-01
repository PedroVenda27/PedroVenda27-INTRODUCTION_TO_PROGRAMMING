
# 32) Maior Sequência Crescente: Escreva um programa que leia uma sequência de 
# números inteiros terminada com o número 0 (zero) e indique a maior sequência 
# crescente encontrada.



tam_maior_seq = 0

tam_seq_atual = 0

num_ant = -9999

maior_seq = ""

seq_atual = ""
 
while True:

    try:

        num = int(input("Digite um numero (zero para terminar): "))
 
        if num == 0:

            break
 
        if num >= num_ant:

            tam_seq_atual += 1

            seq_atual += f"{num} "

        else:

            tam_seq_atual = 1

            seq_atual = f"{num} "
 
        if tam_seq_atual > tam_maior_seq:

            tam_maior_seq = tam_seq_atual

            maior_seq = seq_atual
 
        num_ant = num
 
    except ValueError:

        print("Dados inválidos!")
 
if tam_maior_seq > 1:

    print(f"A maior sequência tem o tamanho {tam_maior_seq}")

    print(f"Núnmero que fazem parte da maior sequência: {maior_seq}")



