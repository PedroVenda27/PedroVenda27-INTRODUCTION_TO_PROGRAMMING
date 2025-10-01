def maximo(a,b):
    if a < b:
        return(b)
    if a > b:
        return(a)
    else:
        return "Os valores são iguais" , a
    
print(maximo(5,6))
print(maximo(2,1))
print(maximo(7,7))