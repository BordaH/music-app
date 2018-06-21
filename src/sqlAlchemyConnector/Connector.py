from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.models import *
from src.parsers.ArtistParser import getArtistParser
from src.parsers.PlaylistParser import getPlaylistLikeNameParser
from src.parsers.PlaylistParser import getPlaylistParser
from src.parsers.AudioFileParser import getAudioFileParser
from src.parsers.AlbumParser import getAlbumLikeNameParser

class Connector:

    def __init__(self):
        dbRoot = 'mysql+pymysql://ci:ci@localhost:3306/ci'
        self.__engine = create_engine(dbRoot)
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker()
        self.__session.configure(bind=self.__engine)
        self.__dbSession = self.__session()


    # Artist management

    def addArtist(self, stageName, name, lastName, age):
        self.__dbSession.add(Artist(stageName=stageName, name=name, lastName=lastName, age=age))
        self.__dbSession.commit()

    def getArtist(self, stageName):
        return getArtistParser(self.__dbSession.query(Artist).filter_by(stageName=stageName).first())

    def deleteArtist(self, stageName):
        first = self.__dbSession.query(Artist).filter_by(stageName=stageName).first()
        if(first != None):
            self.__dbSession.delete(first)
            self.__dbSession.commit()

    # Playlist management

    def getPlaylistLikeName(self, playlistName):
        return getPlaylistLikeNameParser(
                self.__dbSession.query(Playlist).filter(Playlist.playlistName.like("%" + playlistName + "%")).all())

    def addPlaylist(self, playlistName, userName, description):
        newPlaylistData = Playlist(playlistName=playlistName, description=description)
        newPlaylistUserData = PlaylistUser(playlistName=playlistName, userName=userName)
        self.__dbSession.add(newPlaylistData)
        self.__dbSession.commit()
        self.__dbSession.add(newPlaylistUserData)
        self.__dbSession.commit()

    def getPlaylist(self, playlistName):
        return getPlaylistParser(self.__dbSession.query(Playlist).
                                 filter(Playlist.playlistName.__eq__(playlistName)).first())

    def updatePlaylist(self, playlistName, data):
        self.__dbSession.query(Playlist).filter_by(playlistName=playlistName).update(data)
        self.__dbSession.commit()

    def deletePlaylist(self, playlistName):
        playlistToBeDeleted = self.__dbSession.query(Playlist).filter_by(playlistName=playlistName).first()
        if (playlistToBeDeleted != None):
            self.__dbSession.delete(playlistToBeDeleted)
            self.__dbSession.commit()

    # Artist Audio File management

    def addArtistAudioFile(self, fileName, isAudioFile, artist):
        self.__dbSession.add(AudioFile(filename=fileName, isAudioFile=isAudioFile))
        self.__dbSession.commit()
        self.__dbSession.add(AudioFileByArtist(stageName=artist, filename=fileName))
        self.__dbSession.commit()

    def deleteArtistAudioFile(self, filename, artist):
        self.__dbSession.delete(self.__dbSession.query(AudioFile).filter_by(filename=filename))
        self.__dbSession.commit()
        self.__dbSession.delete(self.__dbSession.query(AudioFileByArtist).filter_by(filename=filename, artist=artist))
        self.__dbSession.commit()

    def getAudioFile(self, fileName):
        return getAudioFileParser(self.__dbSession.query(AudioFile).filter_by(filename=fileName).first())

    def addAudioFile(self, filename, isAudioFile):
        self.__dbSession.add(AudioFile(filename=filename, isAudioFile=isAudioFile))
        self.__dbSession.commit()

    def deleteAudioFile(self, filename):
        self.__dbSession.delete(self.__dbSession.query(AudioFile).filter_by(filename=filename).first())
        self.__dbSession.commit()

    # User management

    def addUser(self,userName,password, name, lastName, age):
        newUserData = User_Data(userName=userName, name=name, lastName = lastName, age=age)
        newUserLogin = User_Login(userName=userName, password=password)

        self.__dbSession.add(newUserData)
        self.__dbSession.commit()
        self.__dbSession.add(newUserLogin)
        self.__dbSession.commit()

    def deleteUser(self, userName):

        self.__dbSession.delete(self.__dbSession.query(User_Data).filter_by(userName=userName).first())
        self.__dbSession.commit()


    def addAlbum(self, albumName, albumYear, albumOwner):
        newAlbumData = Album(albumName=albumName,albumYear=albumYear)
        newAlbumUserData= AlbumUser(albumName=albumName,ownerName=albumOwner)
        self.__dbSession.add(newAlbumData)
        self.__dbSession.commit()
        self.__dbSession.add(newAlbumUserData)
        self.__dbSession.commit()

    # Album managment

    def getAlbumLikeName(self,albumName):
        return getAlbumLikeNameParser(self.__dbSession.query(Album).filter(Album.albumName.like("%"+albumName+"%")).all())

    def deleteAlbum(self, albumName):
        itemToBeDeleted = self.__dbSession.query(Album).filter_by(albumName=albumName).first()
        if(itemToBeDeleted != None):
            self.__dbSession.delete(itemToBeDeleted)
            self.__dbSession.commit()

