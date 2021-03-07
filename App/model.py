'''
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 '''


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

'''
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de los mismos.
'''


# Construccion de modelos
def newCatalog():
    catalog = {'videos': None,
               'by_countries': None,
               'by_categories': None,
               'category-id': None}

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['by_countries'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['by_categories'] = lt.newList(
        datastructure='ARRAY_LIST', cmpfunction=cmpCategories)
    catalog['category-id'] = lt.newList(datastructure='ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    country = video['country'].strip()
    category = int(video['category_id'].strip())

    addVideoCountry(catalog, country, video)
    addVideoCategory(catalog, category, video)


def addCategory(catalog, category):
    c = newCategoryId(category['id'], category['name'])
    lt.addLast(catalog['category-id'], c)


def addVideoCountry(catalog, country, video):
    pass


def addVideoCategory(catalog, category_id, video):
    categories = catalog['by_categories']
    posCategory = lt.isPresent(categories, category_id)

    if posCategory > 0:  # La categoria ya ha sido creada dentro de la lista
        category = lt.getElement(categories, posCategory)
    else:  # Debemos crear una nueva categoria
        category = newCategory(category_id)
        lt.addLast(categories, category)

    lt.addLast(category['videos'], video)


# Funciones para creacion de datos
def newCategory(category_id):
    category_dict = {'id': 0, "videos": None}
    category_dict['id'] = category_id
    category_dict['videos'] = lt.newList('ARRAY_LIST')
    return category_dict


def newCategoryId(id, name):
    """
        Crea un diccionario en el que guarda el nombre de la categoria y su id correpondiente
    """
    category = {'id': '', 'name': ''}
    category['id'] = int(id)
    category['name'] = name.strip()
    return category

# Funciones de consulta


def getCategory(catalog, category_id):
    pos_id = lt.isPresent(catalog['by_categories'], category_id)
    if pos_id > 0:
        category_list = lt.getElement(catalog['by_categories'], pos_id)
        return category_list
    return None


def getId(category_ids, category_name):
    for item in lt.iterator(category_ids):
        if item['name'] == category_name:
            return item['id']


def findTopVideo(category_list):
    pos = 1
    reps_per_video = []
    current_reps = 1
    while pos < lt.size(category_list) - 1:
        current_elem = lt.getElement(category_list, pos)
        next_elem = lt.getElement(category_list, pos + 1)

        if current_elem['title'] == next_elem['title']:
            current_reps += 1
        else:
            reps_per_video.append(
                {'video': current_elem, 'reps': current_reps})
            current_reps = 1

        pos += 1

    top_video = []
    top_reps = 0
    for item in reps_per_video:
        if item['reps'] > top_reps:
            top_reps = item['reps']
            top_video = item['video']

    return top_video, top_reps

def findTopsCountryCategory(sorted_cat_list, number, country): 
    topVideos = lt.newList()
    
    pos = 1
    while number > 0: 
        video = lt.getElement(sorted_cat_list, pos)
        if video['country'] == country: 
            lt.addLast(topVideos, video)
            number -= 1
        pos += 1

    return topVideos
        

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideoIdSort(video1, video2):
    return video1['video_id'] < video2['video_id']


def cmpCategories(category_id, category):
    if category_id < category['id']:
        return -1
    elif category_id > category['id']:
        return 1
    else:
        return 0


def cmpCategoriesSort(video1, video2):
    return video1['category_id'] < video2['category_id']


def compVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    views1 = int(video1["views"])
    views2 = int(video2["views"])

    if views1 == views2:
        return 0
    elif views1 > views2:
        return 1
    else:
        return 0



# Funciones de ordenamiento

def sortVideoId(category_list):
    vid_id_sort = category_list.copy()
    vid_id_sort = mer.sort(vid_id_sort, cmpVideoIdSort)
    return vid_id_sort

def sortViews(catalog):
    sub_list = catalog.copy()
    sorted_list = mer.sort(sub_list, compVideosByViews)
    return sorted_list

def sortCategory(category_list):
    cat_sort = category_list.copy()
    cat_sort = mer.sort(cat_sort, cmpCategories)
    return cat_sort


# def sortVideosSelection(catalog, size):
#     sub_list = lt.subList(catalog['videos'], 0, size)
#     sub_list = sub_list.copy()
#     start_time = time.process_time()
#     sorted_list = sel.sort(sub_list, compVideosByViews)
#     stop_time = time.process_time()
#     elapsed_time_mseg = (stop_time - start_time)*1000
#     return elapsed_time_mseg, sorted_list


# def sortVideosInsertion(catalog, size):
#     sub_list = lt.subList(catalog['videos'], 0, size)
#     sub_list = sub_list.copy()
#     start_time = time.process_time()
#     sorted_list = ins.sort(sub_list, compVideosByViews)
#     stop_time = time.process_time()
#     elapsed_time_mseg = (stop_time - start_time)*1000
#     return elapsed_time_mseg, sorted_list


# def sortVideosShell(catalog, size):
#     sub_list = lt.subList(catalog['videos'], 0, size)
#     sub_list = sub_list.copy()
#     start_time = time.process_time()
#     sorted_list = sa.sort(sub_list, compVideosByViews)
#     stop_time = time.process_time()
#     elapsed_time_mseg = (stop_time - start_time)*1000
#     return elapsed_time_mseg, sorted_list





# def sortVideosQuick(catalog, size):
#     sub_list = lt.subList(catalog['videos'], 0, size)
#     sub_list = sub_list.copy()
#     start_time = time.process_time()
#     sorted_list = quk.sort(sub_list, compVideosByViews)
#     stop_time = time.process_time()
#     elapsed_time_mseg = (stop_time - start_time)*1000
#     return elapsed_time_mseg, sorted_list
  


