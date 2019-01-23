import re
import requests
string_de_teste = 'gabriel.kepler@happycodeschool.com'
req = requests.get('http://www.planetprinter.com.br/?page_id=19')
padrao = re.findall(r'.+@[\w-]+\.[\w\.-]+', req.text)
if padrao:
    print(padrao)
else:
    print('Padrão não encontrado')
