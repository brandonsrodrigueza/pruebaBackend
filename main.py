
import requests
import json
import pandas as pd
from random import randrange
import hashlib
import time
import funciones, crearBase, insertarTabla

url = "https://restcountries-v1.p.rapidapi.com/all"

headers = {
    'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
    'x-rapidapi-key': "5a7c65786amsh346d87b85a868e0p13be34jsnd408b7c2c262"
    }

response =  requests.request("GET", url, headers=headers).json()


regiones = funciones.obtenerRegion(response)
paises = funciones.obtenerCiudadIdioma(response)[0]
idioma = funciones.obtenerCiudadIdioma(response)[1]
time = funciones.tomaTiempo(response)

df = pd.DataFrame({'Regiones': regiones, 
'Paises': paises,
'Idioma': idioma,
'Time':time
})
df.to_json (r'.\data.json')
print (df)
print("Tiempo Máximo",df['Time'].max())
print("Tiempo Mínimo",df['Time'].min())
print("Tiempo Total",df['Time'].sum())
print("Tiempo Promedio",df['Time'].mean())

crearBase.crearBase()
insertarTabla.insertarTabla(regiones,paises,idioma,time)
