# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: searchEngine
@version: 1.0
@author: keefe
@date: 2017/6/16
'''

import nn

if __name__ == "__main__":
    ''' 
    '''
    mynet = nn.searchnet('nn.db')
    #mynet.maketables()
    wWorld,wRiver,wBank = 101,102,103
    uWorldBank,uRiver,uEarth = 201,202,203
    # 创建带样例单词和URL ID的隐藏节点
    mynet.generatehiddennode([wWorld,wBank], [uWorldBank,uRiver,uEarth])
    for c in mynet.con.execute('select * from wordhidden'): print c
    for c in mynet.con.execute('select * from hiddenurl'): print c    
    
    print mynet.getresult([wWorld,wBank], [uWorldBank,uRiver,uEarth])
    