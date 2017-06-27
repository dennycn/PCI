# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: 
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import advancedclassify


def plot_match():
    agesonly = advancedclassify.loadmatch('agesonly.csv', allnum=True)
    matchmaker = advancedclassify.loadmatch('matchmaker.csv')    
    advancedclassify.plotagematches(agesonly)     
    
def test_svm():
    pass
    # from svm import import *
    # prob = svm_problem([1,-1],[[1,0,1],[-1,0,-1]])
    
    
    
if __name__ == "__main__":  
    ''' 
    '''
    plot_match()
