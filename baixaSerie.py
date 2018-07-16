import urllib.request
import urllib.parse


try:
    pesquisa = str(input('digite a pesquisa no piratbay'))
    url = 'http://thepiratebay.org/'
    dic = {'q': pesquisa, 'submit': 's'}   
    dta = urllib.parse.urlencode(dic)    
    dta = dta.encode('utf-8')    
    results = urllib.request.Request(url, dta)    
    resposta = urllib.request.urlopen(results)    
    texto = resposta.read()    
    magnetico = texto.find('"magnet:')    
    magnetico = magnetico + 15
    print(texto)
except Exception as e:
    print(str(e))
