import json
import unittest

import requests


class AudioFileTestCase(unittest.TestCase):

    def test_addAudioFile_Music_MP3(self):
        postData = {'isAudioFile': True, 'filename': 'MusicMP3'}
        addAudioFileReq = requests.post('http://localhost:8080/apiv1/audiofile/MusicMP3', data=postData)

        self.assertEqual(addAudioFileReq.status_code, 200)
        self.assertEqual(addAudioFileReq.reason, 'OK')
        self.assertEqual(addAudioFileReq.text, 'Audio file added')

        getData ={'filename':'MusicMP3'}
        getAudioFileReq = requests.get('http://localhost:8080/apiv1/audiofile.search',params=getData)
        self.assertEqual(getAudioFileReq.status_code, 200)
        jsonResponse = json.loads(getAudioFileReq.text)
        audiofile = jsonResponse[0]
        self.assertEqual(audiofile['filename'], 'MusicMP3')
        self.assertEqual(audiofile['isAudioFile'], True)

    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/audiofile/MusicMP3')

if __name__ == '__main__':
    unittest.main()
