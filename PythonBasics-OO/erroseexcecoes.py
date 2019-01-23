import time
def abre_arquivo():
    try:
        arquivo = open('arquivodido.txt')
        return arquivo
    except Exception as erro:
        print("Aconteceu um erro", erro)
        return False
while not abre_arquivo():
    print("Tentando abrir arquivo.")
    time.sleep(5)
print('Consegui abrir arquivo')