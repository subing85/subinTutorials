'''
resource 0.0.1 
Date: February 11, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import platform

from assetLibrary.utils import platforms

CURRENT_PATH = os.path.dirname(__file__)
MODULE = platforms.get_tool_kit()[0]


def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs')


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')

def getImageFormats():
    formats = '(*.jpg *.tga *.png)'
    return formats 


def getPreferencePath():
    return os.path.join(getWorkspacePath(), 'preference')


def getWorkspacePath():
    if platform.system()=='Windows':
        return os.path.abspath (
            os.getenv('USERPROFILE') + '/Documents').replace ('\\', '/')
    if platform.system()=='Linux':
        return os.path.join(os.getenv('HOME'), 'Documents', MODULE)


def getToolKitLink():
    return 'https://www.subins-toolkits.com'


def getToolKitHelpLink():
    return 'https://vimeo.com/314966208'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/shader-library'

# end ####################################################################