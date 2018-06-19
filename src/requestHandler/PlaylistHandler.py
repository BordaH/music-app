import tornado.web
import json


class PlaylistHandler(tornado.web.RequestHandler):

    def get(self):
        statusCode = 400
        statusMessage = 'Bad request'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            statusCode = 200
            statusMessage = self.application.db.getPlaylist(playlistName)
        except Exception as e:
            raise (e)
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def post(self):

        statusCode = 200
        statusMessage = 'Playlist added'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            userName = data['userName']
            description = data['description']
            self.application.db.addPlaylist(playlistName, userName, description)
            songs = data['songs']
            for song in songs:
                self.application.db.addPlaylistAudioFile(song, playlistName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Playlist not added"
        self.set_status(statusCode)
        self.write(statusMessage)

    def delete(self):
        statusCode = 200
        statusMessage = 'Playlist deleted'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            playlistName = data['playlistName']
            self.application.db.deletePlaylist(playlistName)
        except Exception as e:
            raise e
            statusCode = 400
            statusMessage = "Playlist not deleted"
        self.set_status(statusCode)
        self.write(statusMessage)

