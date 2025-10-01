#12) Altere o programa para produzir o seguinte efeito:
#g
#ng
#ing
#ring
#tring
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
for i in range(len(string_sem_espacos),-1,-1):
    (print(string_sem_espacos[i:]))#ultimo parar primeiro

