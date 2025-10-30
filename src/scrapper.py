"""
Pequeño scrapper para extraer los enlaces de las provincias desde
la página del Directorio de Órganos Judiciales del Consejo General del
Poder Judicial.

Uso:
	python src/scrapper.py
	python src/scrapper.py https://www.poderjudicial.es/cgpj/es/Servicios/Directorio/Directorio_de_Organos_Judiciales

El script intenta usar requests + BeautifulSoup si están instalados.
Si no, cae a urllib y una extracción por expresiones regulares.
"""

from __future__ import annotations
import requests
from bs4 import BeautifulSoup
import sys
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import json

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
options = Options()
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled") # Oculta "soy un bot"
RUTADATOS = '../data'
rutas = {
  'ficheroProvincias': f'{RUTADATOS}/provincias.json',
  'ficheroJuzgados': f'{RUTADATOS}/juzgados.json'
}
provinciaClass = {
  'nombre': '',
  'url': '',
  'juzgados': []
}
juzgadoClass = {
  'nombre': '',
  'url': '',
  'municipio': '',
  'telefonos': '',
  'direccion': '',
  'codigopostal': '',
  'detallesObtenidos': False,
  'fax': '',
  'email': '',
  'jueces': []
}

selectoresDetalleJuzgado = {
  'coordenadasMapa': 'div.google-maps-link a',
  'regexLatitudLongitud': r'@(-?\d+\.\d+),(-?\d+\.\d+)',
  'magistrados': 'div[id=listaTit] table tbody tr td[not(@class)]',
  'textosDetalle': 'div.txtMapa dl', # Pares dt/dd 
  'email': 'dd.wrapMail a'
}


CGPJ_ROOTURL = 'https://www.poderjudicial.es'
SLEEP_TIME = 0.5  # segundos
CGPJ_URLS = {
	'provincias': f'{CGPJ_ROOTURL}/cgpj/es/Servicios/Directorio/Directorio_de_Organos_Judiciales',
  'juzgados': ''
}
MI_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
CABECERAS = {
    'User-Agent': MI_USER_AGENT,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1', # (Do Not Track)
}

def ListarProvincias():
  """
  Extrae y devuelve una lista de provincias y sus URLs desde la página del
  Directorio de Órganos Judiciales del CGPJ.
  """
  result = []
  driver.get(CGPJ_URLS['provincias'])
  time.sleep(3)  # Espera a que la página cargue completamente
  html = driver.page_source
  soup = BeautifulSoup(html, 'html.parser')
  enlaces = soup.select('div.divListado a')
  for link in enlaces:
    provincia = provinciaClass.copy()
    provincia['nombre'] = link.text
    provincia['url'] = f'{CGPJ_ROOTURL}{link['href']}'
    provincia['juzgados'] = []
    result.append(provincia)
  return result  

def ListarJuzgadosProvincia(provincia):
  """
  Extrae todos los juzgados de la provincia a partir de la URL proporcionada
  """
  juzgados = []  
  url = provincia['url']
  while True:
    driver.get(url)
    time.sleep(SLEEP_TIME)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    datos = soup.select_one('table.tablaDatos.tablaDatos1 tbody')
    if datos:
      filas = datos.find_all('tr')
      for fila in filas:
        juzgado = juzgadoClass.copy()
        municipio = fila.select_one('th[data-cabecera="Municipio"] span')
        if (municipio):
          juzgado['municipio'] = municipio.text.strip()
        enlace_tag =fila.select_one('td[data-cabecera="Juzgado"] a')
        if (enlace_tag):
          juzgado['nombre'] = enlace_tag.text.strip()
          juzgado['url'] = f'{CGPJ_ROOTURL}{enlace_tag['href']}'
        telefonos = fila.select_one('td[data-cabecera="Teléfono/s"] span')
        if (telefonos):
          juzgado['telefonos'] = telefonos.text.strip()
        direccion = fila.select_one('td[data-cabecera="Dirección"] span')
        if (direccion):
          juzgado['direccion'] = direccion.text.strip()
        codigopostal = fila.select_one('td[data-cabecera="Código Postal"] span')
        if (codigopostal):
          juzgado['codigopostal'] = codigopostal.text.strip()
        juzgado['provincia']=provincia['nombre']
        juzgados.append(juzgado)
    #Siguiente página
    siguiente = soup.select_one('li.liSiguiente a')
    if siguiente and siguiente.has_attr('href') and len(siguiente['href'].strip())>0:
      url = f"{CGPJ_ROOTURL}{siguiente['href']}"
    else:
      break       
  provincia['juzgados']=juzgados
  return juzgados

def ObtenerDetalleJuzgados(juzgado: dict)-> dict:
  driver.get(juzgado['url'])
  time.sleep(SLEEP_TIME)
  soup = BeautifulSoup(driver.page_source, 'html.parse')
  detalles = soup.find_all(selectoresDetalleJuzgado['textosDetalle'])
  
  return juzgado

provincias = None
juzgados = None
if(os.path.isfile(rutas['ficheroProvincias'])):
  with open(rutas['ficheroProvincias'], 'r', encoding='utf-8') as f:
    provincias = json.load(f)

with webdriver.Chrome(options=options) as driver:  
  if provincias is None:
    provincias =ListarProvincias()  
  juzgadosProvincia = []
  for provincia in provincias:
    print(f'Obteniendo juzgados de {provincia}...')
    juzgados = ListarJuzgadosProvincia(provincia)
    with open(rutas['ficheroJuzgados'], 'w', encoding='utf-8'):
      json.dump(juzgados)

