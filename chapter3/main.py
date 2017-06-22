    # show digram 1# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: clust
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import clusters

if __name__ == "__main__":
    ''' 
    '''
    blognames, words, data = clusters.readfile('blogdata.txt')
    clust = clusters.hcluster(data)
    print type(clust)
    # show digram 1
    # print clusters.printclust(clust.left, labels=blognames)
    clusters.drawdendrogram(clust, blognames, jpeg='blogclust.jpeg')
    # show digram 2
    coords = clusters.scaledown(data)
    clusters.draw2d(coords, blognames, jpeg='blogclust2.jpeg')
 
