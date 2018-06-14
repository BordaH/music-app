import json


def getArtistParser(artist):

    return json.dumps({'artist': {'stageName': artist.stageName,
                       'name': artist.name,
                       'lastName': artist.lastName,
                       'age': artist.age}})

