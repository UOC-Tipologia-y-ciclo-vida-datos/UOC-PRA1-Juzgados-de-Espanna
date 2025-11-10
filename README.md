# UOC-PRA1-Juzgados-de-España
Dataset con datos recopilados desde la página web del Consejo General del Poder Judicial sobre los juzgados españoles
# Dataset de Juzgados de España - CGPJ

## Descripción del Proyecto

Este repositorio contiene un script en Python desarrollado para extraer y estructurar datos del directorio de órganos judiciales del **Consejo General del Poder Judicial (CGPJ)**, publicados en su web oficial. El proyecto tiene como objetivo crear un dataset limpio, estructurado y reutilizable con información detallada sobre los juzgados de España, su tipología, ubicación, datos de contacto y jueces titulares de cada uno de ellos.

## Objetivo

El propósito de este proyecto es facilitar el acceso y análisis de información sobre el sistema judicial español mediante la creación de un dataset estructurado que contenga datos relevantes sobre los órganos judiciales, específicamente juzgados ubicados en España. Esta información puede ser útil para investigadores, desarrolladores, periodistas y cualquier persona interesada en el funcionamiento del sistema judicial español.

## Fuente de Datos

Los datos se extraen del **Directorio de Órganos Judiciales** del Consejo General del Poder Judicial (CGPJ), disponible públicamente en su sitio web oficial:
- **URL**: [https://www.poderjudicial.es](https://www.poderjudicial.es)
- **Organismo**: Consejo General del Poder Judicial (CGPJ)
- **Ámbito geográfico**: España.

## Características Principales

- 🔍 **Web Scraping ético**: Extracción de datos respetando las políticas del sitio web y los términos de uso
- 🧹 **Limpieza de datos**: Procesamiento y estructuración de información en formato reutilizable
- 📊 **Dataset estructurado**: Generación de archivos JSON con información normalizada
- 📝 **Documentación completa**: Memoria detallada del proceso y metodología empleada
- ⚖️ **Cumplimiento legal**: Respeto a la normativa de protección de datos y uso de información pública

## Contenido del Repositorio

```
📦 UOC-PRA1-Juzgados-de-España
├── 📄 README.md                    # Este archivo
├── 📄 .gitignore                   # Archivos ignorados por Git
├── 📂 src/                         # Código fuente del proyecto
│   └── 📄 scraper.py              # Script de extracción de datos
├── 📂 data/                        # Datasets generados
│   ├── 📄 juzgados_españoles.csv  # Dataset principal
│   └── 📄 juzgados_españoles.json # Dataset en formato JSON
├── 📂 docs/                        # Documentación del proyecto
│   └── 📄 memoria.pdf             # Memoria del proyecto
└── 📄 requirements.txt             # Dependencias de Python
```

## Principios Éticos y Legales

Este proyecto se ha desarrollado siguiendo estrictos principios éticos y legales:

### ✅ Cumplimiento Legal
- **Datos públicos**: Solo se extraen datos públicamente disponibles en el sitio web oficial del CGPJ
- **LOPD/RGPD**: Cumplimiento con la Ley Orgánica de Protección de Datos y el Reglamento General de Protección de Datos
- **Propiedad intelectual**: Respeto a los derechos de autor y atribución correcta de la fuente

### 🤝 Buenas Prácticas
- **robots.txt**: Respeto a las directrices del archivo robots.txt del sitio web
- **Rate limiting**: Implementación de pausas entre peticiones para no sobrecargar el servidor
- **User-Agent identificable**: Uso de un User-Agent que identifica claramente el propósito del scraping
- **Transparencia**: Documentación completa del proceso y metodología

### 🎯 Uso Responsable
- **Finalidad educativa**: Este proyecto se desarrolla con fines educativos y de investigación
- **No comercial**: Los datos extraídos se utilizan sin ánimo de lucro
- **Atribución**: Reconocimiento explícito de la fuente de datos (CGPJ)

## Requisitos e Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/UOC-Tipologia-y-ciclo-vida-datos/UOC-PRA1-Juzgados-de-Espanna.git
cd UOC-PRA1-Juzgados-de-Espanna
```

2. Crear un entorno virtual (recomendado):
```bash
python -m venv uoc-pra1-tipologia-y-ciclo-de-vida-datos
#Con Linux:
#source uoc-pra1-tipologia-y-ciclo-de-vida-datos/bin/activate  
#Con Windows: 
source uoc-pra1-tipologia-y-ciclo-de-vida-datos\Scripts\activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar el script de extracción:
```bash
python src/scraper.py
```

El script realizará las siguientes acciones:
1. Conectará con el sitio web del CGPJ
2. Extraerá los datos de las provincias de España donde hay juzgados [https://www.poderjudicial.es/cgpj/es/Servicios/Directorio/Directorio_de_Organos_Judiciales]
3. Por cada provincia, enumerará la lista de juzgados registrados.
4. Para cada juzgado, extraerá sus datos.
5. Procesará y limpiará la información
6. Generará los archivos CSV y JSON en la carpeta `data/`

## Estructura del Dataset

El dataset generado contiene las siguientes columnas:

| Campo | Descripción | Tipo |
|-------|-------------|------|
| ... | ... | String/Entero/Flotante/Guid/etc. |
| pdte. | pdte. | pdte. |

## Contexto Académico

Este proyecto se desarrolla como parte de la **Práctica 1 (PRA1)** de la asignatura **Tipología y ciclo de vida de los datos** del programa de la **Universitat Oberta de Catalunya (UOC)**.

### Competencias Desarrolladas
- Web scraping y extracción de datos
- Limpieza y transformación de datos
- Consideraciones éticas y legales en el tratamiento de datos
- Documentación de proyectos de ciencia de datos

## Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal
- **BeautifulSoup4**: Librería para parsing de HTML
- **Requests**: Librería para realizar peticiones HTTP
- **Pandas**: Manipulación y análisis de datos
- **JSON/CSV**: Formatos de salida del dataset

## Limitaciones y Consideraciones

- El dataset se centra únicamente en juzgados de España
- La información está sujeta a cambios en el sitio web fuente
- Los datos reflejan la información disponible en el momento de la extracción
- Se recomienda verificar la información directamente con el CGPJ para usos oficiales

## Contribuciones

Este proyecto es de carácter educativo. Las sugerencias y mejoras son bienvenidas a través de issues y pull requests.

## Licencia

Este proyecto se distribuye bajo una licencia CC BY-NC-SA 4.0 (Creative Commons Attribution‑NonCommercial‑ShareAlike 4.0 International). 
Los datos extraídos son propiedad del CGPJ y se utilizan únicamente con fines académicos y de investigación.

## Autores

Proyecto desarrollado como parte del Máster en Ciencia de Datos de la UOC por los alumnos Angel Barrón Almendros y Pedro José Berberana Martín.

## Agradecimientos

- **Consejo General del Poder Judicial (CGPJ)**: Por mantener información pública accesible
- **Universitat Oberta de Catalunya (UOC)**: Por el marco académico y orientación

## Contacto y Soporte

Para preguntas, sugerencias o reportar problemas:
- Abrir un issue en este repositorio
- Contactar a través de la plataforma de la UOC

## Referencias

- [Consejo General del Poder Judicial](https://www.poderjudicial.es)
- [Directorio de Órganos Judiciales](https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunales/)
- [Reglamento General de Protección de Datos (RGPD)](https://gdpr-info.eu/)
- [Ley Orgánica de Protección de Datos (LOPD)](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673)

---

**Nota**: Este repositorio contiene código, documentación (memoria) y resultados (dataset) como parte de un proyecto académico de la UOC. El uso de los datos debe realizarse de forma responsable y respetando la normativa vigente.
