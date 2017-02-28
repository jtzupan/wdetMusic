# -*- coding: utf-8 -*-

import requests
import json
import datetime
from collections import namedtuple


def getSongList(url='https://api.composer.nprstations.org/v1/widget/5182d007e1c809685c190ee6/playlist?t=1488122307580&limit=50&order=-1&datestamp=2017-02-26&time=20%3A00&prog_id=5589d32ac73b71e35604c77e&loadingMesgeId=widgetElement_55&errorMsg=Sorry%2C+there+is+no+playlist+to+display'):
    
    SongInfo = namedtuple('SongInfo',['songName', 'artist','album','showData'])    
    
    r = requests.get(url)
    parsed_json = json.loads(r.text)

    ##########################################################################
    # get song data
    songList = []
    for info in parsed_json['playlist'][0]['playlist']:
        album = info[u'collectionName']
        song = info[u'trackName']
        artist = info[u'artistName']
        showDate = datetime.datetime.strptime(info[u'_start_time'], '%m-%d-%Y %H:%M:%S')
        allInfo = SongInfo(song, artist, album, showDate)
        songList.append(allInfo)
    ##########################################################################
    # get show date


    return songList
