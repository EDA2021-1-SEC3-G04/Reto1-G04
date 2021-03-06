﻿"""
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
 """

import config as cf
# import time
from DISClib.ADT import list as lt
# from DISClib.Algorithms.Sorting import shellsort as sa
# from DISClib.Algorithms.Sorting import selectionsort as sel
# from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
# from DISClib.Algorithms.Sorting import quicksort as quk
assert cf




# Construccion de modelos

def newCatalog():
    """
    Se define la estructura de un catálogo de videos. El catálogo tendrá tres 4, una para los videos, una para los category ids, otra para las categorias de los mismos y otra para los paises de los mismos.
    """
    catalog = {'videos': None,
               'by_countries': None,
               'by_categories': None,
               'category-id': None}

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['by_countries'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpCountries)
    catalog['by_categories'] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpCategories)
    catalog['category-id'] = lt.newList(datastructure='ARRAY_LIST')
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """
    Se añade un video a a lista de videos
    """
    lt.addLast(catalog['videos'], video)
    country = video['country'].strip()
    category = int(video['category_id'].strip())

    # Funciones para añadir datos a las listas de pais y categoria
    addVideoCountry(catalog, country, video)
    addVideoCategory(catalog, category, video)


def addCategory(catalog, category):
    """
    Se añade una categoria (su id y nombre) a a lista de categoria
    """
    c = newCategoryId(category['id'], category['name'])
    lt.addLast(catalog['category-id'], c)


def addVideoCountry(catalog, country, video):
    """
    Adiciona un pais a lista de paises.
    Las listas de cada pais guarda referencias a los videos de dicho pais
    """
    countries_list = catalog['by_countries']
    posCountry = lt.isPresent(countries_list, country)

    if posCountry > 0:  # El pais ya ha sido creada dentro de la lista
        new_country = lt.getElement(countries_list, posCountry)
    else:   # Debemos crear nuevo pais
        new_country = newCountry(country)
        lt.addLast(countries_list, new_country)
    lt.addLast(new_country['videos'], video)

def addVideoCategory(catalog, category_id, video):
    """
    Adiciona una categoria a lista de categorias si este no esta.
    Las listas de cada pais guarda referencias a los videos de dicho pais
    """
    categories_list = catalog['by_categories']
    posCategory = lt.isPresent(categories_list, category_id)

    if posCategory > 0:  # La categoria ya ha sido creada dentro de la lista
        category = lt.getElement(categories_list, posCategory)
    else:  # Debemos crear una nueva categoria
        category = newCategory(category_id)
        lt.addLast(categories_list, category)

    lt.addLast(category['videos'], video)


# Funciones para creacion de datos
def newCategory(category_id):
    """
    Crea una nueva estructura para modelar los videos de un category id
    """
    category_dict = {'id': 0, "videos": None}
    category_dict['id'] = category_id
    category_dict['videos'] = lt.newList(datastructure='ARRAY_LIST')
    return category_dict


def newCountry(country):
    """
    Crea una nueva estructura para modelar los videos de un pais
    """
    country_dict = {'name': '', "videos": None}
    country_dict['name'] = country
    country_dict["videos"] = lt.newList(datastructure='ARRAY_LIST')
    return country_dict


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
    """
    Retorna la lista de un dado id de categorias. Si no lo encuentra retorna None
    """
    pos_id = lt.isPresent(catalog['by_categories'], category_id)
    if pos_id > 0:
        category_list = lt.getElement(catalog['by_categories'], pos_id)
        return category_list
    return None


def getId(category_ids, category_name):
    """
    Retorna la el id correspondiente a una categoria. Si no lo encuentra retorna None
    """
    for item in lt.iterator(category_ids):
        if item['name'] == category_name:
            return item['id']
    return None

def getCountry(countries, country):
    """
    Retorna los datos de una pais (Nombre y videos correspondientes). Si no lo encuentra retorna None
    """
    for item in lt.iterator(countries):
        if item['name'] == country:
            return item
    return None


def findTopsCountryCategory(sorted_cat_list, number, country): 
    """
    Requerimiento 1
    Crea una lista con los x videos con más views que corresponda a un  pais de una lista ordenada por views. 
    """
    topVideos = lt.newList(datastructure='ARRAY_LIST')
    pos = 1
    while number > 0 and pos < lt.size(sorted_cat_list): 
        video = lt.getElement(sorted_cat_list, pos)
        if video['country'] == country: 
            lt.addLast(topVideos, video)
            number -= 1
        pos += 1

    return topVideos


def findTopVideo(category_list):
    """
    Requerimiento 3
    Crea lista con una estructura para modelar cada video y las veces que este aparece dentro de una lista (cuantos dias ha sido trending). 
    Con esa lista determina cuale de los videos ha tenido más dias trending. 
    """
    pos = 1
    reps_per_video = lt.newList(datastructure='ARRAY_LIST')
    current_reps = 1
    while pos < lt.size(category_list) - 1:
        current_elem = lt.getElement(category_list, pos)
        next_elem = lt.getElement(category_list, pos + 1)

        if current_elem['video_id'] != '#NAME?' and current_elem['video_id'] == next_elem['video_id']:
            current_reps += 1
        else:
            lt.addLast(reps_per_video,
                {'video': current_elem, 'reps': current_reps})
            current_reps = 1

        pos += 1

    top_video = ""
    top_reps = 0
    for item in lt.iterator(reps_per_video):
        if item['reps'] > top_reps:
            top_reps = item['reps']
            top_video = item['video']

    return top_video, top_reps

        
def findTopVideoCountries(country_list):
    """
    Requerimiento 2
    Crea lista con una estructura para modelar cada video y las veces que este aparece dentro de una lista (cuantos dias ha sido trending). 
    Con esa lista determina cuale de los videos ha tenido más dias trending. 
    """
    pos = 1
    reps_per_video = lt.newList(datastructure='ARRAY_LIST')
    current_reps = 1
    while pos < lt.size(country_list) - 1:
        current_elem = lt.getElement(country_list, pos)
        next_elem = lt.getElement(country_list, pos + 1)

        if current_elem['video_id'] != '#NAME?' and current_elem['video_id'] == next_elem['video_id']:
            current_reps += 1
        else:
            lt.addLast(reps_per_video, {'video': current_elem, 'reps': current_reps})
            current_reps = 1

        pos += 1

    top_video = ""
    top_reps = 0
    for item in lt.iterator(reps_per_video):
        if item['reps'] > top_reps:
            top_reps = item['reps']
            top_video = item['video']

    return top_video, top_reps


def findWithTags(list_vid_countries, tag):
    tag_list = lt.newList(datastructure='ARRAY_LIST')

    for video in lt.iterator(list_vid_countries['videos']):
        current_tags = video['tags']
        if tag in current_tags:
            lt.addLast(tag_list, video)
    return tag_list


def findMostLikes(list_by_likes, number):
    """
    Requerimiento 1
    Crea una lista con los x videos con más likes dentro de una lista que ya esta ordenada. 
    Si un video ya se encuntra en la lista no lo repite. 
    """
    pos = lt.size(list_by_likes)
    topVideos = lt.newList(datastructure='ARRAY_LIST', cmpfunction=cmpVideoId)
    lt.addLast(topVideos, lt.lastElement(list_by_likes))
    number -= 1
    while number > 0 and pos > 0:
        current_element = lt.getElement(list_by_likes, pos)
        pos_present = lt.isPresent(topVideos, current_element)
        if pos_present == 0:
            lt.addLast(topVideos, current_element)
            number -= 1
        pos -= 1
        
    return topVideos



# Funciones utilizadas para comparar elementos dentro de una lista

# Las funcionese para los sort deben retornar True o False. 
# El resto deben retornar -1, 0 , 1

def cmpVideoIdSort(video1, video2):
    return video1['video_id'] < video2['video_id']


def cmpCategories(category_id, category):
    if category_id < category['id']:
        return -1
    elif category_id > category['id']:
        return 1
    else:
        return 0

def cmpCountries(country1, country2):
    if country1 < country2['name']:
        return -1
    elif country1 > country2['name']:
        return 1
    else:
        return 0

def cmpCategoriesSort(video1, video2):
    return video1['category_id'] < video2['category_id']

def cmpLikes(video1, video2): 
    return int(video1['likes']) < int(video2['likes'])


def compVideosByViews(video1, video2):
    views1 = int(video1["views"])
    views2 = int(video2["views"])

    if views1 == views2:
        return 0
    elif views1 > views2:
        return 1
    else:
        return 0

def cmpVideoId(id1, id2):
    if id1['video_id'] < id2['video_id']:
        return -1
    elif id1['video_id'] > id2['video_id']:
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

def sortLikes(video_list): 
    likes_sort = video_list.copy()
    likes_sort = mer.sort(likes_sort, cmpLikes)
    return likes_sort
