# -*- coding: utf-8 -*-

import urllib2
import bs4
import re
from itertools import izip_longest


def getSongList(url='http://wdet.org/posts/2016/08/21/83741-the-progressive-underground-show-183-feat-jeff-canady/'):
    
   # url = 'http://wdet.org/posts/2016/08/21/83741-the-progressive-underground-show-183-feat-jeff-canady/'
    html = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    
    ##########################################################################
    #get song data
    rawSongData = soup.findAll("table", class_="table table-striped")
    fullSongList = re.findall(r'<td>(.*?)</td>', str(rawSongData))
    
    cleanedSongList = []
    for i in fullSongList: 
        if i == '\\n':
            continue
        cleanedSongList.append(i.strip('</strong>'))
        
    if len(cleanedSongList) % 3 != 0:
        print 'List is missing song information'
    
    #iterools magic to break list down into groups of three
    listOfSongs = list(izip_longest(*([iter(cleanedSongList)]*3)))
    ##########################################################################
    #get show date
    showDateRaw = soup.findAll("div", class_="article-date")[0]
    showDate = re.findall(r'''>(.*)</div''', str(showDateRaw))[0]
    
    return listOfSongs, showDate