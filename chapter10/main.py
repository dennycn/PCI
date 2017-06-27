# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: matrix~ finding independent features
@version: 1.0
@author: keefe
@date: 2017/6/21
'''
from numpy import *

list1 = [[1, 2, 3], [4, 5, 6]]
list2 = [[1, 2], [3, 4], [5, 6]]   
m1 = matrix(list1)
m2 = matrix(list2)
    
def get_martix():
    import newsfeatures
    allw, artw, artt = newsfeatures.getarticlewords()
    wordmatrix, wordvec = newsfeatures.makematrix(allw, artw)
    print wordvec[0:10]

def get_cluster(wordmatrix, artt):
    import clusters
    clust = clusters.hcluster(wordmatrix)
    clusters.drawdendrogram(clust, artt, jpeg='news.jpeg')
    
def calc_matrix():
    print 'm1=', m1, shape(m1)
    print 'm2=', m2, shape(m2)
    print 'm1*m2=', m1 * m2
    # 同行列的矩阵运算
    print 'm1*m2=', m1.A * array(list1)

def calc_matrix2():
    import nnmf
    w, h = nnmf.factorize(m1 * m2, pc=3, iter=100)
    print w, h
    print 'w*h=',w*h
    print 'm1*m2=', m1*m2
  
    
if __name__ == "__main__":
    ''' 
    '''
    calc_matrix2()

    
