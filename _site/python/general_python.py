# -*- coding: utf-8 -*-
"""
Created on Tue May  3 00:16:11 2016

@author: maurizio
"""


def find_path():
    import sys
    s = sys.path
    path = "export PYTHONPATH="
    for elem in s:
        path += "{};".format(elem)
    return path 
