# !/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
@desc: recommendations
@version: 1.0
@author: keefe
@date: 2017/6/21
'''

import recommendations
import pydelicious

if __name__ == "__main__":
    ''' 以用户为中心，计算用户相似度
    与以物品为中心，计算物品相似度的思路是一致的。
    只需进行数据集的矩阵倒置 
    '''
    print 5, len(recommendations.critics), type(recommendations.critics)
    # 相似度度量距离：distance/pearson
    # print 'sim_distance=', recommendations.sim_distance(recommendations.critics, 'Lisa Rose', 'Gene Seymour')
    # print 'sim_pearson=', recommendations.sim_pearson(recommendations.critics, 'Lisa Rose', 'Gene Seymour')

    # 获取线上链接推荐, 数据集从线上获取
    # print pydelicious.get_popular(tag='unix')
    
    # get recommendations：需要计算所有用户
    print 'topMatches=', recommendations.topMatches(recommendations.critics, 'Toby', n=3, similarity=recommendations.sim_pearson)
    print 'getRecommendations=', recommendations.getRecommendations(recommendations.critics, 'Toby', recommendations.sim_distance)
    # print 'getRecommendations=',recommendations.getRecommendations(recommendations.critics, 'Toby', recommendations.sim_pearson)
    # itemsin为物品相似度表，一次获取后可以供以后多次使用
    itemsin = recommendations.calculateSimilarItems(recommendations.critics, n=10)
    print 'getRecommendedItems=', recommendations.getRecommendedItems(recommendations.critics, itemsin, 'Toby')

    # load dataset movies: '/d/data/movie' - > 'd:\data\movie'
    # u.data{userid, movieid, score, time}
    prefs = recommendations.loadMovieLens('D:\data\movie')
    prefs_movies = recommendations.transformPrefs(prefs)
    print len(prefs), len(prefs_movies), 'user_r_movies=', len(prefs['87']), prefs['87']
    # 向某用户prefs['87']推荐一组电影
    print 'getRecommendations=', recommendations.getRecommendations(prefs, '87', recommendations.sim_distance)[0:2]
