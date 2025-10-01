#11) Crie um programa de modo a que uma string seja impressa do seguinte modo:
#S
#St
#Str
#Stri
#Strin
#string


def tira_espacos(string):
  nova_string = ""
  for caracter in string:
    if caracter != " ":
      nova_string += caracter

  return nova_string

# Solicita ao usuário o texto da String
string = input("Introduza o texto da String: ")
string = string.strip()
string_sem_espacos = tira_espacos(string)

# Imprime a string de forma progressiva
for i in range(1, len(string_sem_espacos) + 1):
    print(string_sem_espacos[:i])#primeiro para o ultimo





