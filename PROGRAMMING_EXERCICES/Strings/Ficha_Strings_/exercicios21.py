# 21) Crie um método que verifique se uma password (passada como string) é válida.
# Para isso deverá ter pelo menos 6 caracteres (pelo menos 4 caracteres alfabéticos e
# um caracter numérico). Não deverá ter espaços. O método deverá retornar true se a
# password for válida e false em caso contrário.
alfabetico = 0
numerico = 0
tem_espaco = False

# Solicita ao utilizador que introduza uma string
password = input("Introduza uma password:")

# Verifica os critérios para cada caractere na senha
for caractere in password:
    if caractere.isalpha():
        alfabetico = alfabetico + 1
    elif caractere.isdigit():
        numerico = numerico + 1
    elif caractere == " ":
        tem_espaco = True

# Verifica se a senha é válida
if (len(password) >= 6 and
    alfabetico >= 4 and
    numerico >= 1 and not tem_espaco):
    print("A password é válida.")
else:
    print("A password não é válida.")