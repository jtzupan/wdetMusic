# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 13:02:17 2016

@author: tzupan
"""

import sqlite3
import time


def createTable():
    '''
    Creates a base table called musicIndex, if this table does not already exist.
    If the table does exist, this query does nothing.
    
    INPUT:
        NONE
    OUTPUT:
        creates table (with no output)
        STRING: completed step 1
    '''
    
    conn = sqlite3.connect('WDET_Music_DB.sqlite')
    cur = conn.cursor()
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS musicIndex
                (ID             INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                SongName        varchar(255),
                ArtistName      varchar(255),
                AlbumName       varchar(100),
                ShowDate        varchar(100),
                SongAddedDate   varchar(100)
                )'''
                )
    conn.commit()
    return 'completed step 1'
    
    
    
def recordInTable(songName):
    '''
    Checks if a given SQL file already has a record in the table queryIndex
    
    INPUT: 
        tableName(str): the name of the table to be checked
    RETURN:
        the result of the query for tableName, will return an empty list if the 
        record does not exist
    '''
    conn = sqlite3.connect('WDET_Music_DB.sqlite')
    cur = conn.cursor()
    
    cur.execute('''SELECT SongName
                    FROM musicIndex 
                    WHERE songName = ?''',(songName,))
    return cur.fetchall() != []
    
    
def addNewRecord(song, artist, album, showDate):
    '''
    creates a new record and associated data for a SQL file
    INPUT: 
        song(str):
        artist(str):
        album(str):
    RETURN:
        NONE
        Adds new record and associated data to the table
    
    '''
    
    #open database connection
    conn = sqlite3.connect('WDET_Music_DB.sqlite')
    cur = conn.cursor()
    

    addedDate = time.ctime()
    
    cur.execute('''
                INSERT INTO musicIndex
                ( SongName, ArtistName, AlbumName, ShowDate, SongAddedDate)
                VALUES(?,?,?,?,?);'''
                ,(song, artist, album, showDate, addedDate))
    conn.commit()
     
    return 'Record added to database'
    
    
def returnAllSongsInTable():
    '''
    Returns all songs from database
    
    INPUT: 
        None
    RETURN:
        the result of the query for tableName, will return an empty list if the 
        record does not exist
    '''
    conn = sqlite3.connect('WDET_Music_DB.sqlite')
    cur = conn.cursor()
    
    cur.execute('''SELECT *
                    FROM musicIndex 
                    ''')
    return cur.fetchall()