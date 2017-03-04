# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:12:24 2016

@author: tzupan
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import webScraping as ws
import tableFunctions as tf
import s as selen
reload(ws)
reload(tf)
reload(selen)


def addSongstoDB(url):
    # create table if it does not exist

    tf.createTable()
    songsAdded = 0
    songList = ws.getSongList(url)
    for song, artist, album, showDate in songList:
        if tf.recordInTable(song):
            print 'Song already in database'
            continue
        else:
            tf.addNewRecord(song, artist, album, showDate)
            print 'Added song'
            songsAdded += 1
    return 'Completed Update, added {} songs'.format(songsAdded)


def playVideos(queries):
    for q in queries:
        video_id, video_length = selen.firstVideoId(q)


        chrome_options = Options()
        extensionPath = '/Users/johnzupan/mystuff/python_all/wdetMusic/AdBlock_v3.8.8.crx'
        chrome_options.add_extension(extensionPath)
        
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get('https://www.youtube.com/watch?v={}'.format(video_id))

        try:
            m,s = video_length.split(':')
        except ValueError:
            m,s = 5,30
            
        seconds = min(((int(m) * 60) + int(s) + 5),(330))
            
                # convert to seconds 
        time.sleep(seconds)

        driver.close()
        driver.quit()
        
def songList():
    finalList = []
    songList = tf.returnAllSongsInTable()
    for i in songList:
        song = ''
        song += (i[1] + " " + i[2] + " " + i[3])
        finalList.append(song)
    return finalList

def main(url):
    #optional, will add choice to command line args
    addSongstoDB(url)
    finalList = songList()
    print finalList
    playVideos(finalList)
    
        