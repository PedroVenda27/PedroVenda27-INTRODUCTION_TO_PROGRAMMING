#8.4 REUTILIZAÇÃO DA FUNÇÃO EPAR EM OUTRA FUNÇÃO

def epar(x):
    return (x % 2 == 0) 

def par_ou_impar(x):
    if epar(x):
        return "par"
    else:
        return "ímpar"  
    
print(par_ou_impar(4))
print(par_ou_impar(5))