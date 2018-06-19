import tornado.web
from src.DatabaseConnector.DataBaseConnector import DatabaseConnector
from src.requestHandler.AlbumHandler import AlbumHandler
from src.requestHandler.ArtistHandler import ArtistHandler
from src.requestHandler.RootHandler import RootHandler
from src.requestHandler.PlaylistHandler import PlaylistHandler
from src.requestHandler.AudioFileHandler import AudioFileHandler
from src.requestHandler.UserHandler import UserHandler


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
        (r"/", RootHandler),
        (r"/apiv1/artist/(.*)", ArtistHandler),
        (r"/apiv1/playlist", PlaylistHandler),
        (r"/apiv1/audiofile/(.*)", AudioFileHandler),
        (r"/apiv1/audiofile", AudioFileHandler),
        (r"/apiv1/user", UserHandler),
        (r"/apiv1/album", AlbumHandler)

        ]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = DatabaseConnector.instance()
