# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:55:34 2017

@author: mtinti-x
"""

exclude_feature = ['CHAIN']

file_open = open('P02920.txt')
for line in file_open:
    if line.startswith('FT'):
        feature_type = line.split('\t')[0]