import requests
from bs4 import BeautifulSoup

url = 'https://dockerlabs.es/'

# Realizar una solicitud GET al sitio web
respuesta = requests.get(url)

# Comprobar si la solicitud fue exitosa
if respuesta.status_code == 200:
    # Analizar el contenido HTML de la respuesta
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    # Puedes agregar aquí más lógica para extraer información del objeto soup
    maquinas = soup.find_all('div', onclick=True)
    conteo_maquinas = 1
    autores = set()
    for maquina in maquinas:
        onclick_text = maquina['onclick']
        autor = onclick_text.split("'")[7]
        autores.add(autor)
        nombre_maquina = onclick_text.split("'")[1]
        conteo_maquinas += 1

    print('Los autores son : ')
    for autor in autores:
        print(autor)

    for maquina in maquinas:
        onclick_text = maquina['onclick']
        nombre = onclick_text.split("'")[1]
        dificultad = onclick_text.split("'")[3]
        autor = onclick_text.split("'")[7]
        print(f'{nombre} --> {dificultad }-->{autor}')




    # print(f'El número de maquinas total es {conteo_maquinas}')

else:
    print(
        f"Error al acceder a la página. Código de estado: {respuesta.status_code}")
