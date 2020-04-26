
import requests
import json
import pandas as pd
from random import randrange
import hashlib
import time


def obtenerRegion(response):
    regiones = [ i["region"] for i in response]
    contador = 0
    for i in regiones:
        if i == '':
            regiones.remove(i)
    return regiones

def obtenerUrlsCiudad(response):
    urls = []
    regiones = obtenerRegion(response)
    for i in regiones:
       urls.append("https://restcountries.eu/rest/v2/region/"+i)
    return urls

def obtenerCiudadIdioma(response):
    urlsParaConsumir = obtenerUrlsCiudad(response)
    headers = {}
    consulta = [requests.request("GET", i, headers=headers).json() for i in urlsParaConsumir]
    pais = []
    idioma = []
    for i in consulta:
        aleatorio = randrange(len(i))
        pais.append(i[aleatorio]["name"])
        idioma.append(i[aleatorio]["languages"][0]["name"])
    return [pais,idioma]


def tomaTiempo(response):
    regiones = obtenerRegion(response)
    tiempos = []
    for i in range(len(regiones)):
        start_time = time.time()
        obtenerRegion(response)
        obtenerCiudadIdioma(response)[0]
        obtenerCiudadIdioma(response)[1]
        finish_time = time.time()
        tiempos.append(finish_time-start_time)
    return tiempos



