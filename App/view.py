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
    """
    Imprime el menu
    """
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
    """
    Imprime el primer video que se cargo en el catalogo
    """
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
    """
    Imprime los id de las categorias y su respectivo nombre
    """
    print('\nCategorías cargadas (Id y nombre)')
    for id_name in category_ids['elements']:
        print('Id #:', id_name['id'], '\tName:', id_name['name'])
    print('\n')


def printTopVideos(video_list): 
    """
    Imprime los videos del requerimiento 1 con los datos trending date, title, cahnnel, publish time
    views, likes, dislikes
    """ 
    for video in video_list['elements']: 
        print('Trending date:', video['trending_date'], '––Title:', video['title'], '––Channel:', video['channel_title'], '––Publish time:', video['publish_time'], '––Views:', video['views'], '––Likes:', video['likes'], '––Dislikes:', video['dislikes'])
        input('Presione enter para ver el siguente video')
        print('*'*50)
    print('Fin\n')

def printTopVideosTags(list_vid_tag): 
    """
    Imprime los videos del requerimiento 4 con los datos title, channel, publish time, views, likes, dislikes, tags
    """ 
    for video in list_vid_tag['elements']:
        print('Title:',  video['title'], '––Channel:', video['channel_title'],'––Publish Time: ', video['publish_time'], '––Views:', video['views'], '––Likes:', video['likes'], '––Dislikes:', video['dislikes'], '––Tags:', video['tags'])
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
        valid_category = controller.getId(catalog['category-id'], category)
        valid_country = controller.getCountry(catalog['by_countries'], country)
        if valid_category is not None and valid_country is not None:
            result = controller.topCountryCategory(catalog, number, country, category)
            print("\nLos top", number, "videos de", country, "&", category, "son:\n")
            printTopVideos(result)
        else:
            print('Pais o categoria no válida')
        

    elif int(inputs[0]) == 3:
        country = input(
            "País a consultar el video trending x más dias: ")
        countries_list = catalog['by_countries']
        valid_country = controller.getCountry(countries_list, country)
        if valid_country is not None:
            top_video = controller.topVidByCountry(valid_country)
            video = top_video[0]
            trend_days = top_video[1]
            print('\nEl video más trending de', country, 'fue:')
            print('Título:', video['title'], ' Canal: ', video['channel_title'],
                  '  Country: ', video['country'])
            print('Días trending: ', trend_days, '\n')
        else:
            print('País no válido')

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

    elif int(inputs[0]) == 5: 
        cant = input("Cantidad a consultar de videos con más likes: ")
        tag = input("Tag específico a consultar de videos con más likes: ")
        country = input("País a consultar el video trending x más dias: ")
        list_vid_countries = controller.getCountry(catalog['by_countries'], country)
        if list_vid_countries is not None: 
            list_vid_tag = controller.listVidTag(list_vid_countries, tag, int(cant))
            printTopVideosTags(list_vid_tag)
        else: 
            print('País no válido')

    else:
        sys.exit(0)
sys.exit(0)
