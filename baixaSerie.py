import urllib.request
import urllib.parse


try:
    pesquisa = str(input('digite a pesquisa no piratbay'))
    url = 'http://thepiratebay.org/'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    dic = {'q': pesquisa, 'submit': 's'}
    dta = urllib.parse.urlencode(dic)
    dta = dta.encode('utf-8')
    results = urllib.request.Request(url, dta, headers=headers)
    resposta = urllib.request.urlopen(results)
    texto = str(resposta.read())
    magnetico = texto.find('"magnet:')
    saveFile = open('codethe.txt', 'w')
    print('linha1')
    saveFile.write(texto)
    print('linha1')
    saveFile.close()
    print('linha1')
    
except Exception as e:
    print(str(e)) 
    


