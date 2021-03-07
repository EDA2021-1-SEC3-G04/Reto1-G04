"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 10000
sys.setrecursionlimit(default_limit*10)


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x videos por país y categoría")
    print("3- Consultar el video que más días ha sido trending por país")
    print("4- Consultar el video que más días ha sido trending por categoria")
    print("5- Consultar los Top x videos con más likes en un país con un tag específico")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def printVideos(dict_video):
    titulo = dict_video['title']
    channel_title = dict_video['channel_title']
    trending_date = dict_video['trending_date']
    country = dict_video['country']
    views = dict_video['views']
    likes = dict_video['likes']
    dislikes = dict_video['dislikes']

    print("Titulo: " + titulo +
          " \tChannel_title: " + channel_title +
          " \tTrending_date: " + trending_date +
          " \tCountry: " + country +
          " \tViews: " + views +
          "\tLikes: " + likes +
          "\tDislikes: " + dislikes)


def printCategories(category_ids):
    print('\nCategorías cargadas (Id y nombre)')
    for id_name in category_ids['elements']:
        print('Id #:', id_name['id'], '\tName:', id_name['name'])
    print('\n')


def printTopVideos(video_list):  
    for video in video_list['elements']: 
        print('Trending date:', video['trending_date'], '––Title:', video['title'], '––Channel:', video['channel_title'], '––Publish time:', video['publish_time'], '––Views:', video['views'], '––Likes:', video['likes'], '––Dislikes:', video['dislikes'])
        input('Presione enter para ver el siguente video')
        print('*'*50)
    print('Fin\n')
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        print('\n Primer video:')
        printVideos(lt.firstElement(catalog['videos']))

        category_ids = catalog['category-id']
        printCategories(category_ids)

    elif int(inputs[0]) == 2:
        
        number = int(input("Buscando los top: "))
        country = input("Pais a consultar los top " + str(number) + " videos: ")
        category = input("Categoria a consultar los top " + str(number) + " videos: ")
        result = controller.topCountryCategory(catalog, number, country, category)
        print("\nLos top", number, "videos de", country, "&", category, "son:\n")
        printTopVideos(result)
    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        category_name = input(
            "Categoria a consultar el video trending x más dias: ")
        category_ids = catalog['category-id']
        category_id = controller.getId(category_ids, category_name)
        if category_id is not None:
            top_video = controller.topVidByCategory(catalog, category_id)
            video = top_video[0]
            trend_days = top_video[1]
            print('\nEl video más trending de', category_name, 'fue:')
            print('Título:', video['title'], ' Canal: ', video['channel_title'],
                  '  Category Id', video['category_id'])
            print('Días trending: ', trend_days, '\n')
        else:
            print('Categoria no válida')

    else:
        sys.exit(0)
sys.exit(0)
