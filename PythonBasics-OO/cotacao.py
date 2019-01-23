import requests
import json
def requisicao(moeda):
    try:
        req = requests.get('https://api.hgbrasil.com/finance?fields=only_results,'+moeda+'&key=6270e302')
        cotacao = json.loads(req.text)
        return cotacao
    except Exception as e:
        print('Erro no(a):', e)
        return

def PegarTaxas(tipodetaxa):
    return True
while not sair:
    op = input('Digite qual o tipo de consulta ou SAIR:')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        dicmoeda = requisicao(op)
        if dicmoeda['Response'] == 'False':
            print('Informação não está presente.')
        else:
            printar_taxas(PegarTaxas(dicmoeda))