#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return PIB

class PIB(BaseFeedBook):
    title                 = u'PIB'
    description           = u'PUBLIC INFORMATION BEURO'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "pib.jpg"
    #coverfile             = "cv_lifeweek.jpg"
    fulltext_by_readability = True
    oldest_article        = 7
    
    deliver_days          = ['Saturday']
    
    feeds = [
            (u'News', '  http://pib.nic.in/newsite/rssenglish.aspx'),
           ]