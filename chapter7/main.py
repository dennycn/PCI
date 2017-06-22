# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: decide tree
@version: 1.0
@author: keefe
@date: __updated__ 2017/6/21
'''

import treepredict

def get_entropy():
    # gini 基尼不纯度
    print treepredict.giniimpurity(treepredict.my_data)
    # entroy 熵
    print treepredict.entropy(treepredict.my_data)     
 
 
if __name__ == "__main__":
    ''' 
    '''
    # get_entropy()
    tree = treepredict.buildtree(treepredict.my_data)        
    # treepredict.printtree(tree)      
    # treepredict.drawtree(tree, jpeg='treeview.jpg')
    print treepredict.classify(['direct', 'USA', 'yes', 51], tree)
    