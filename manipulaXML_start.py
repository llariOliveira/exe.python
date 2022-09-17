# 
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom

def manipulaXML():
    doc = xml.dom.minidom.parse("C:\\Users\\Pessoal\\Desktop\\curso python\\Cap. 05\\exemploXML.xml")

    print("Nome da primeita tag:" , str(doc.firstChild.tagName))
    primeironome = doc.getElementsByTagName("firstname")
    print("o primiero nome é: ", primeironome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):
        print ("skill encontrados:",skill.getAttribute("name"))

    
#manipulaXML()