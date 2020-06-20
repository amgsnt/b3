#!/usr/bin/python

#mês corrente:
#bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_D05052020.ZIP
#
#últimos 12 meses:
#bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_M052020.ZIP
#
#desde 1986:
#http://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2020.ZIP
#
#Nome do arquivo diário: COTAHIT_D[DDMMAAAA]
#Nome do arquivo mensal: COTAHIT_M[MMAAAA]
#Nome do arquivo anual: COTAHIT_A[AAAA]

import urllib.request
import urllib.error
from datetime import datetime

import os, zipfile

def downloadB3Hist():

    baseURL = "http://bvmf.bmfbovespa.com.br/InstDados/SerHist/"

    baseName = "COTAHIST_A{:04d}.ZIP"

    baseDate = datetime.now()

    lOk = True

    print("Starting...{}".format(datetime.now()))


    ano = baseDate.year

    while(lOk):
        
        fileName = baseName.format(ano)

        url = baseURL + fileName

        try:
            urllib.request.urlretrieve(url, filename=fileName)
            print("Download OK: {}".format(fileName))

        except urllib.error.HTTPError as e:
            if e.code != 404:
                print("HTTPError error: {0}".format(e.code))
                raise
            else:
                lOk = False            

        urllib.request.urlcleanup()

        ano = ano - 1
  
    for item in os.listdir(os.getcwd()):
        if item.endswith(".ZIP"):
            print("Extracting: {}".format(item))
            
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall(os.getcwd())
            zip_ref.close()
            
            print("Removing: {}".format(item))

            os.remove(file_name)
    
    print("Finish...{}".format(datetime.now()))
    
downloadB3Hist()
