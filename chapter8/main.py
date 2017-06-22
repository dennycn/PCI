# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: KNN~ K-Nearest Neighbors
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import numpredict

def generate_dataset():
    # dataset(rating, age)
    numpredict.wineprice(95, 3)
    numpredict.wineprice(95, 8)
    numpredict.wineprice(99, 1)
    data = numpredict.wineset1()
    print data     
    return data
    
def get_weight():
    print numpredict.subtractweight(0.1)
    print numpredict.inverseweight(0.1)
    print numpredict.gaussian(0.1)
 
    print numpredict.subtractweight(1)
    print numpredict.inverseweight(1)
    print numpredict.gaussian(1)

def knninverse(d, v):
    return numpredict.weightedknn(d, v, weightf=numpredict.inverseweight)
       
            
if __name__ == "__main__":
    ''' 
    '''
    # get_weight()
    data = generate_dataset()  
    print numpredict.euclidean(data[0]['input'], data[1]['input'])
    print numpredict.weightedknn(data, (99,5), k=3)
    print numpredict.weightedknn(data, (99,5), k=5)    
    # 交叉验证
    print numpredict.crossvalidate(knninverse, data)
 