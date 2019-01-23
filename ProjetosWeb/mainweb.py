import requests
import json
texto =''
def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=790b6e00&t=' + titulo)
        dicionario = json.loads(req.text)
        return  dicionario
    except Exception as e:
        print('Erro no(a):', e)
        return
def printar_detalhes(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('')
sair = False
while not sair:
    op = input('Digite o titulo do filme ou SAIR para fechar:')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)