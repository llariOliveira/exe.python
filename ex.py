#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil

def copiaarquivo():
    if path.exists("novoarquivo.txt"):
        pathatual = path.realpath("novoarquivo.txt")
        novopath = pathatual + ".bkp"
        shutil.copy(pathatual, novopath)

        shutil.copystat(pathatual, novopath)


copiaarquivo()

def renomeararquivo():
    if path.exists("novoarquivo.txt.bkp"):
        os.rename("novoarquivo.txt.bkp", "aquivoalterado.txt")

#renomeararquivo()

#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
import zipfile

def criazipmodo1():
    shutil.make_archive("arquivocompactado", "zip", "C:\\Users\Pessoal\\Desktop\\curso python\\Cap. 03")

#criazipmodo1()

def criaZipModo2():
        with ZipFile("arquivozipmodo2.zip", "w") as novozip:
            novozip.write("NovoArquivo.txt.bkp")
            novozip.write("novoarquivo.txt")
            novozip.write("arquivocompactado.zip")
        
#criaZipModo2()


def deletaarquivo():
    os.remove("arquivozipmodo2.zip")


#deletaarquivo()