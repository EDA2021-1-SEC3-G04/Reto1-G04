"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo de videos del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos del archivo en la estrucura de datos
    """
    loadVideos(catalog)
    loadCategoryIds(catalog)


def loadVideos(catalog):
    """
    Carga los videos del archivo.  
    Por cada video se toma su categoria y su pais y por cada uno de estos se crea un lista, donde se guardan los videos correspondientes a esa categoria/pais
    """
    videosFiles = cf.data_dir + "Videos/videos-large.csv"
    input_file = csv.DictReader(open(videosFiles, encoding="utf-8"))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategoryIds(catalog):
    """
    Carga todos los category ids del archivo y los agrega a la lista de category ids
    """
    categoriesFiles = cf.data_dir + "Videos/category-id.csv"
    input_file = csv.DictReader(
        open(categoriesFiles, encoding="utf-8"), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)


# Funciones de ordenamiento

def sortVideoId(category_list):
    """
    Ordena los libros por video_id
    """
    return model.sortVideoId(category_list)


def sortViews(views_list):
    """
    Ordena los libros por views
    """
    return model.sortViews(views_list)

def sortLikes(list_sort): 
    """
    Ordena los libros por likes
    """
    return model.sortLikes(list_sort)

# Funciones de consulta sobre el catálogo

def getId(category_ids, category_name):
    """
    Retorna los el id que corresponde al el nombre de una categoria 
    """
    return model.getId(category_ids, category_name)

def getCountry(countries, country):
    """
    Retorna la informacion de ese pais: nombre + lista de videos correspondientes
    """
    return model.getCountry(countries, country)

def getCategory(catalog, category_id):
    """
    Retorna la informacion de esa categoria: lista de videos correspondientes
    """
    return model.getCategory(catalog, category_id)






def topCountryCategory(catalog, number, country, category): 
    """
    Función base requerimiento 1. 
    Retorna lista con los top x videos con más views de un pais y una categoria
    """
    category_id = getId(catalog['category-id'], category)
    category_list = getCategory(catalog, category_id)
    sorted_cat_list = sortViews(category_list['videos'])
    top_vids = findTopsCountryCategory(sorted_cat_list, number, country)
    return top_vids


def topVidByCountry(country_list):
    """
    Función base requerimiento 2. 
    Retorna lista con el video que más dias a sido trending 
    """
    sorted_country_lst = sortVideoId(country_list['videos'])
    top_countries = findTopVideoCountry(sorted_country_lst)
    return top_countries


def topVidByCategory(catalog, category_id):
    """
    Función base requerimiento 3. 
    """
    category_list = getCategory(catalog, category_id)
    sorted_cat_lst = sortVideoId(category_list['videos'])
    top_vid = findTopVideo(sorted_cat_lst)
    return top_vid

def listVidTag(list_vid_countries, tag, cant):
    """
    Función base requerimiento 4. 
    """
    list_tags = findWithTags(list_vid_countries, tag)
    list_by_likes = sortLikes(list_tags)
    top_videos = findMostLikes(list_by_likes, cant)
    return top_videos


def findTopsCountryCategory(sorted_cat_list, number, country): 
    """
    Llama a funcion del modelo que busca y retorna los x videos con más views que son del 
    pais correspondiente
    """
    return model.findTopsCountryCategory(sorted_cat_list, number, country)

def findTopVideo(category_list):
    """
    Llama al a función del modelo que busca el video que más dais a sido trending de esa categoria
    """
    return model.findTopVideo(category_list)

def findTopVideoCountry(country_list):
    """
    Llama al a función del modelo que busca el video que más dais a sido trending de ese país
    """
    return model.findTopVideoCountries(country_list)

def findWithTags(list_vid_countries, tag): 
    """
    Llama al a función del modelo que busca los videos de un pais que tengan el tag indicado
    """
    return model.findWithTags(list_vid_countries, tag)

def findMostLikes(list_by_likes, cant): 
    """
    Llama a funcion del modelo que busca y retorna los x videos con más likes
    """
    return model.findMostLikes(list_by_likes, cant)



