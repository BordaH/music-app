import json


def getAudioFileParser(audiofile):
    return json.dumps({'audiofile': {'filename': audiofile.filename,
                                     'isAudioFile': audiofile.isAudioFile}})


def getAudioFileLikeNameParser(files):
    return json.dumps([{'filename': audifile.filename, 'isAudioFile': audifile.isAudioFile} for audifile in files])
