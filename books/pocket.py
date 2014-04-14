#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return pocket

class pocket(BaseFeedBook):
    title                 = u'My Pocket Feeds'
    description           = u' Pocket ebook'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "mh_lifeweek.gif"
    #coverfile             = "cv_lifeweek.jpg"
    oldest_article        = 100
    
    #deliver_days          = ['Saturday']
    
    feeds = [
            (u'Current Feeds', 'http://getpocket.com/users/arpanchavdaeng/feed/read'),
           ]