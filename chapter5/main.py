# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: profile
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import optimization
from gunicorn.six import print_

domain = [(0, 9)] * (len(optimization.people) * 2)

def print_s(s):
    # print domain    
    optimization.printschedule(s)
    print optimization.schedulecost(s)
    print '------'
    
def test1():
    s = [1, 4, 3, 2, 7, 3, 6, 3, 2, 4, 5, 3]
    print_s(s)

def test_random():
    # method 1: random
    s = optimization.randomoptimize(domain, optimization.schedulecost)
    print_s(s)

def test_climbing():
    # hill clibming 爬山法
    s = optimization.hillclimb(domain, optimization.schedulecost)
    print_s(s)

def test_annealing():
    # annealing 模拟退火法
    s = optimization.annealingoptimize(domain, optimization.schedulecost)
    print_s(s)
                  
                 
if __name__ == "__main__":
    ''' 
    '''
    # test1()
    test_random()
    # test_climbing()
    test_annealing()
    