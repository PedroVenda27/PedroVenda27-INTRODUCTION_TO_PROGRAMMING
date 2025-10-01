# 35) Números Amigos: Dois números são amigos se a soma dos
# divisores de um for igual ao outro número e vice-versa. Peça ao
# utilizador para introduzir dois números e indique se são amigos.


num1, num2 = 0, 0

soma_div_num1 = 0

soma_div_num2 = 0
 
num1 = int(input("Digite o 1º numero: "))

num2 = int(input("Digite o 2º número: "))
 
for x in range(1, max(num1, num2)):

    if x < num1 and num1 % x == 0:

        soma_div_num1 += x
 
    if x < num2 and num2 % x == 0:

        soma_div_num2 += x
 
if soma_div_num1 == num2 and soma_div_num2 == num1:

    print(f"{num1} e {num2} são números amigos!")

else:

    print(f"{num1} e {num2} não são números amigos.")