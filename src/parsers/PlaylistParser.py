import json


def getPlaylistParser(playlist):
    return json.dumps({'playlist': {'playlistName': playlist.playlistName,
'userName': playlist.userName, 'description': playlist.description}})