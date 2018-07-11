import urllib.request
import time
finalizar = 'a'
dindin = 99.99
while dindin >= 4.74:	
	pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices.html')
	texto = pagina.read().decode('utf8')
	preco = texto.find('$')
	dindin = float(texto[preco+1: preco+5])
	if dindin < 4.74:
		print(dindin)
	else :
		print('Valor maior que 4.74. Valor atual %.2f' %dindin)
	time.sleep(0.5)
	

