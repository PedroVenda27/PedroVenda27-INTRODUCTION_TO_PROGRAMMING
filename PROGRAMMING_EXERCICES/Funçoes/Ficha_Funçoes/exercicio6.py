# 6) Crie uma função que receba 2 notas (F1 e F2) de um aluno e
# retorne um booleano indicando se o aluno passou. Para passar, a
# soma das notas deve ser igual ou superior a 19 e ambas devem ser
# superiores a 7.

def notas(a,b):
    if a < 7 or b < 7:
        Passou = False
    if (a + b) < 19:
        Passou = False
    if (a + b) >= 19:
        Passou = True
    return Passou

if (notas(6,6)):
    print("PASSOU")
else:
    print("CHUMBOU")


if (notas(9,9)):
    print("PASSOU")
else:
    print("CHUMBOU")

if(notas(13,14)):
    print("PASSOU")
else:
    print("CHUMBOU")