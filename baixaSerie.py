import urllib.request

url = "https://thepiratebay.org/"
def conectaPagina():
	pagina = urllib.request.urlopen(url)
	texto = pagina.read().decode('utf8')
	print(texto)


conectaPagina()

