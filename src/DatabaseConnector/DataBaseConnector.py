from src.sqlAlchemyConnector.Connector import *


class DatabaseConnector:
    __instance = None

    @classmethod
    def __haveInstance(cls):
        return True if cls.__instance else False

    @classmethod
    def instance(cls):
        if not cls.__haveInstance():
            cls.__instance = DatabaseConnector()
            return cls.__instance
        return cls.__instance

    def __init__(self):
        self.__connector = Connector()

    # User managemet methods

    def addUser(self, userName, password, name, lastName):
        self.__connector.addUser(userName, password, name, lastName)

    def getUser(self, userName):
        return self.__connector.getUser(userName)

    def deleteUser(self, userName):
        return self.__connector.deleteUser(userName)

    def updateUser(self, userName, data):
        return self.__connector.updateUser(userName, data)

    # def updateUserCredentials(self, userName, password):
    #     return self.__connector.updateUserCredentials(userName, password)

    # Playlist management methods

    def addPlaylist(self, playlistName, userName, description):
        return self.__connector.addPlaylist(playlistName, userName, description)

    def deletePlaylist(self, playlistName):
        return self.__connector.deletePlaylist(playlistName)

    def getPlaylist(self, playlistName):
        return self.__connector.getPlaylist(playlistName)

    def addPlaylistAudioFile(self, audioFile, playlistName):
        return self.__connector.addPlaylistAudioFile(audioFile, playlistName)

    # Artist File management methods

    def addArtistAudioFile(self, fileName, isAudioFile, artist):
        return self.__connector.addArtistAudioFile(fileName, isAudioFile, artist)

    def deleteArtistAudioFile(self, filename, artist):
        return self.__connector.deleteArtistAudioFile(filename, artist)

    def addAudioFile(self, fileName, isAudioFile):
        return self.__connector.addAudioFile(fileName, isAudioFile)

    def deleteAudioFile(self, filename):
        return self.__connector.deleteAudioFile(filename)

    def getAudioFile(self, filename):
        return self.__connector.getAudioFile(filename)

    # Album methods

    def addAlbum(self, albumName, albumYear, albumOwner):
        self.__connector.addAlbum(albumName, albumYear, albumOwner)

    def getAlbumLikeName(self, albumName):
        return self.__connector.getAlbumLikeName(albumName)

    def deleteAlbum(self, albumName):
        return self.__connector.deleteAlbum(albumName)
