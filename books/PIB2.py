#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return PIB2

class PIB2(BaseFeedBook):
    title                 = u'PIB2xx'
    description           = u'PUBLIC INFORMATION BEURO'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    #mastheadfile          = "pib.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    #fulltext_by_readability = True
    oldest_article        = 20
    #max_articles_per_feed = 
    deliver_days          = ['Saturday']
    keep_only_tags = [dict(name='span', attrs={'id':'title'}),dict(name='div', attrs={'class':'Section1'}),]
    feeds = [
            (u'News', 'http://pib.nic.in/newsite/rssenglish_fea.aspx'),
           ]