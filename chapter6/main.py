# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: classifier
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import docclass

def train_1():
    # don't use, haven't use sqlite db store
    cl = docclass.classifier(docclass.getwords)
    cl.train('the quick brown fox jumps over the lazy dog', 'good')
    cl.train('make quick money in the online casino', 'bad')
    cl.fcount('quick', 'good')

def train_fisher():
    # train
    cl = docclass.fisherclassifier(docclass.getwords)
    cl.setdb('test1.db')
    docclass.sampletrain(cl)
    # classify
    cl2 = docclass.naivebayes(docclass.getwords)
    cl2.setdb('test1.db')
    print cl2.classify('quick money')    
  
    
if __name__ == "__main__":
    ''' 
    '''
    train_fisher()
    
