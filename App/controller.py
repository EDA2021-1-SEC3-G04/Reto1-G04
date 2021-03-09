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
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos


def loadData(catalog):
    loadVideos(catalog)
    loadCategoryIds(catalog)


def loadVideos(catalog):
    videosFiles = cf.data_dir + "Videos/videos-large.csv"
    input_file = csv.DictReader(open(videosFiles, encoding="utf-8"))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategoryIds(catalog):
    categoriesFiles = cf.data_dir + "Videos/category-id.csv"
    input_file = csv.DictReader(
        open(categoriesFiles, encoding="utf-8"), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)


# Funciones de ordenamiento

def sortVideoId(category_list):
    return model.sortVideoId(category_list)


def sortViews(views_list):
    return model.sortViews(views_list)


# Funciones de consulta sobre el catálogo

def getId(category_ids, category_name):
    return model.getId(category_ids, category_name)


def topVidByCategory(catalog, category_id):
    category_list = model.getCategory(catalog, category_id)
    sorted_cat_lst = sortVideoId(category_list['videos'])
    top_vid = findTopVideo(sorted_cat_lst)
    return top_vid


def findTopVideo(category_list):
    return model.findTopVideo(category_list)


def topCountryCategory(catalog, number, country, category): 
    category_id = getId(catalog['category-id'], category)
    category_list = model.getCategory(catalog, category_id)
    sorted_cat_list = sortViews(category_list['videos'])
    top_vids = findTopsCountryCategory(sorted_cat_list, number, country)
    return top_vids

def findTopsCountryCategory(sorted_cat_list, number, country): 
    return model.findTopsCountryCategory(sorted_cat_list, number, country)


# Requerimiento 2

def getCountry(countries, country):
    return model.getCountry(countries, country)

def topVidByCountry(country_list):
    sorted_country_lst = sortVideoId(country_list['videos'])
    top_countries = findTopVideo(sorted_country_lst)
    return top_countries

# def sortVideoCountry(country_list):
#     return model.sortVideoCountry(country_list)

def findTopVideo(country_list):
    return model.findTopVideoCountries(country_list)


def listVidTag(list_vid_countries, tag, cant):
    list_tags = model.findWithTags(list_vid_countries, tag)
    list_by_likes = sortLikes(list_tags)
    top_videos = findMostLikes(list_by_likes, cant)

def sortLikes(list_sort): 
    return model.sortLikes(list_sort)

def findMostLikes(list_by_likes, cant): 
    return model.findMostLikes(list_by_likes, cant)