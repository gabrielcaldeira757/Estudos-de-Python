import urllib.request
import urllib.parse
import re


def magLink(imp):
        try:
            # imp = str(input('digite a pesquisa no piratbay: '))
            url = 'https://thepiratebay.org/search'
            k = 0
            pesquisa = "";
            while k < len(imp):
                if imp[k] in ' ':
                    pesquisa = pesquisa + "%20"
                else:
                    pesquisa = pesquisa + imp[k]
                k += 1
            url = url + '/' + pesquisa
            print(url)

            headers = {}
            headers[
                'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

            results = urllib.request.Request(url, headers=headers)
            resposta = urllib.request.urlopen(results)
            texto = str(resposta.read())

            link = re.findall(r'\w href="magnet(.*?)"\s', str(texto))

            k = 0
            soma = '"magnet'
            mag[]

            while k < len(link):
                mag[k] = soma + link[k] + '"'
                k += 1

            return mag

            saveFile = open('LINKSMAG.txt', 'w')
            saveFile.write(mag)
            saveFile.close()
        except Exception as e:
            print(str(e))


def infoTorrent(imp):
        try:
            url = 'https://thepiratebay.org/search'
            k = 0
            pesquisa = "";
            while k < len(imp):
                if imp[k] in ' ':
                    pesquisa = pesquisa + "%20"
                else:
                    pesquisa = pesquisa + imp[k]
                k += 1
             url = url + '/' + pesquisa
            print(url)

             headers = {}
             headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
                



















