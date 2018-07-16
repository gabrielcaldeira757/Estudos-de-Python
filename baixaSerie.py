import urllib.request
import urllib.parse


try:
    imp = str(input('digite a pesquisa no piratbay'))
    url = 'https://thepiratebay.org/search'
    k= 0
    pesquisa = "";
    while  k<len(imp):
        if imp[k]in ' ':
            pesquisa = pesquisa + "%20"
        else:
            pesquisa = pesquisa + imp[k]
        k+=1
    url = url + '/' + pesquisa
    print(url)

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

    
    dta = urllib.parse.urlencode(url)
    dta = dta.encode('utf-8')
    results = urllib.request.Request(url,, headers=headers)
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
    


