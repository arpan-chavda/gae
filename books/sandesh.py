#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return sandesh

class sandesh(BaseFeedBook):
    title                 = u'Sandesh'
    description           = u'Sandesh'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "pib.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    #fulltext_by_readability = True
    oldest_article        = 30
    max_articles_per_feed = 1
    #deliver_days          = ['Saturday']
    #keep_only_tags = [dict(name='div', attrs={'class':'contentdiv'}),]
    feeds = [
            (u'World News', 'http://www.sandesh.com/cms/xml/World.xml'),
           ]
    def fetcharticle(self, url, decoder):
        #每个URL都增加一个后缀full=y，如果有分页则自动获取全部分页
        url += '&lang=Read%20in%20English'
        return BaseFeedBook.fetcharticle(self,url,decoder)