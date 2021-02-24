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


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x videos por país y categoría")
    print("3- Consultar el video que más días ha sido trending por país")
    print("4- Consultar el video que más días ha sido trending por categoria")
    print("5- Consultar los Top x videos con más likes en un país con un tag específico")
    print("0- Salir")


def initCatalog(tipo_de_dato):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(tipo_de_dato)


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


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        tipo_de_dato = int(input(
            "¿Qué tipo de estructura de datos quiere usar?\n 1.Array List\n 2.Single Linked\n"))
        if tipo_de_dato == 1:
            tipo_de_dato = 'ARRAY_LIST'
        elif tipo_de_dato == 2:
            tipo_de_dato = 'SINGLE_LINKED'

        catalog = initCatalog(tipo_de_dato)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        print('Primer video:')
        printVideos(lt.firstElement(catalog['videos']))

        category_ids = catalog['category-id']
        printCategories(category_ids)

    elif int(inputs[0]) == 2:
        size = int(input("Indique el tamaño de la muestra: "))
        if size <= lt.size(catalog['videos']):
            print(
                "¿Qué tipo de ordenamiento quiere?\n1.Selection Sort \n2.Insertion Sort \n3.Shell Sort\n")
            sort_type = int(input())

            # number = input("Buscando los top?: ")
            # country = input("¿De qué país quiere consultar los top", number, "videos?")
            # category = input("¿De qué categoria quiere consultar top", number, "videos? ")

            result = controller.sortViews(catalog, size, sort_type)
            print("Para la muestra de", size,
                  "elementos, el tiempo (mseg) es: ", str(result[0]))

        else:
            print('La muestra que desea es mayor a la cantidad de datos almacenados')
    else:
        sys.exit(0)
sys.exit(0)
