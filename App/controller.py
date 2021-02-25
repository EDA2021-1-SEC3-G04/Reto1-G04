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
def initCatalog(tipo_de_dato):
    catalog = model.newCatalog(tipo_de_dato)
    return catalog

# Funciones para la carga de datos


def loadData(catalog):
    loadVideos(catalog)
    loadCategories(catalog)
    # print(catalog["category-id"])


def loadVideos(catalog):
    videosFiles = cf.data_dir + "Videos/videos-large.csv"
    input_file = csv.DictReader(open(videosFiles, encoding="utf-8"))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    categoriesFiles = cf.data_dir + "Videos/category-id.csv"
    input_file = csv.DictReader(
        open(categoriesFiles, encoding="utf-8"), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)


def sortViews(catalog, size, sort_type):
    if sort_type == 1:
        return model.sortVideosSelection(catalog, size)
    if sort_type == 2:
        return model.sortVideosInsertion(catalog, size)
    if sort_type == 3:
        return model.sortVideosShell(catalog, size)
    if sort_type == 4:
        return model.sortVideosMerge(catalog, size)
    if sort_type == 5:
        return model.sortVideosQuick(catalog, size)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
