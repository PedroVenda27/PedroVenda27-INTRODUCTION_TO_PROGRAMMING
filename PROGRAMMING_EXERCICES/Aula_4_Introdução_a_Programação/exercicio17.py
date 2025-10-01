
idade = int(input("Insira a idade da Pessoa "))

if idade >= 0 and idade <= 12:
    print(" Fase da vida: Infância")
elif idade >= 13 and idade <= 17:
    print(" Fase da vida: Adolescência")
elif idade >= 18 and idade <= 59:
    print(" Fase da vida: Adulto")
else:
    print("Idoso")
