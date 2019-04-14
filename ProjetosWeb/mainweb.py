import requests
import json
import hashlib
def requisicao(token):
    try:
        req = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + token)
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as e:
        print('Erro no(a):', e)
        return
def decifrar(cifrado):
    codigo = cifrado
    newcod = []
    for letra in codigo:
        if(letra != "."):
            if(letra != " "):
                if (ord('a') + 10) <= ord(letra):
                    newcod.append(chr((ord(letra) - ord('a') - 10) + ord('z')))
                else:
                    newcod.append(chr(ord(letra)-10))
            else:
                newcod.append(" ")
        else:
            newcod.append(".")

    return ''.join(newcod)


def printar_detalhes(filme):
    print('Numero de Casa:', filme['numero_casas'])
    print('Token', filme['token'])
    print('Cifrado:', filme['cifrado'])
    print('Decifrado:', decifrar(filme['cifrado']))
    print('Resumo Criptográfico', filme['resumo_criptografico'])
    print('')


print (chr(ord('a') + 10))
token = '156d18d132003b8e721e1c9c6587e75ac6a1e481'
aswner = requisicao(token)
printar_detalhes(aswner)
with open('aswner.json', 'w') as outfile:
    json.dump(aswner, outfile)
