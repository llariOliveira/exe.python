# 
# Exemplo de processamento e parse de HTML
#

from html.parser import HTMLParser

class  meuParser(HTMLParser):
    def handle_starttag (self, tag, attrs):
        print("tag de abertura encontrado!")
        if attrs.__len__() > 0:
            for a in attrs:
                print("  valores encontrados: ", a[0], "=", a[1])
    def handle_endtag(self, tag):
        print("tag de fechamento enontrado")

    def handle_comment(self, data):
        print("comentario encontrado")

    def handle_data(self, data):
        print("valores encontrados")
        if data.isspace():
            print("o valor encontrado é um espaço")
        else:
            print("o valor encontrado é:", data)

def meuobjeto():
    meuparser1 = meuParser()
    arquivo = open("C:\\Users\\Pessoal\\Desktop\\curso python\\Cap. 05\\exemploXML.xml","r" )
    dados = arquivo.read()
    meuparser1.feed(dados)

#meuobjeto()
