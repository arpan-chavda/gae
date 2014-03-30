#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return fmias

class fmias(BaseFeedBook):
    title                 = u'ForumIAS Blog'
    description           = u'ForumIAS Blog ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 7
    fulltext_by_readability = True
    deliver_days          = ['Saturday']
    
    feeds = [
            (u'Current Feeds', 'http://my.forumias.com/feed/ '),
           ]