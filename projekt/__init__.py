# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Projekt_3
                                 A QGIS plugin
 
                             -------------------
        begin                : 2024-06-04
        copyright            : (C) 2024 by Wiktor Gogacz
        email                : 01159569@pw.edu.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Projekt_3 class from file Projekt_3.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .moja_wtyczka_proj_3 import Projekt_3
    return Projekt_3(iface)
