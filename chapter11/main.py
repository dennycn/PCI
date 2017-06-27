# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: gp~ genetic programming
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import gp

def make_tree():
    exampletree = gp.exampletree()
    print exampletree.evaluate([2, 3])
    print exampletree.evaluate([3, 5])

if __name__ == "__main__":
    ''' 
    '''
    make_tree()
