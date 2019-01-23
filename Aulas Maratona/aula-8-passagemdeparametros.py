import sys
argumentos = sys.argv
def soma(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
if argumentos[1] == 'soma':
    print(soma(float(argumentos[2]),float(argumentos[3])))
else:
    print(sub(float(argumentos[2]),float(argumentos[3])))
print(argumentos)