import unittest
import requests


class PlaylistTestCase(unittest.TestCase):

    def test_addPlaylist_RockClassics_JoseYYY_OldRockClassics(self):

        jsonDataUser = {'name': 'Jose',
                    'lastName': 'Perez',
                    'age': 34,
                    'userName':'JoseYYY',
                    'password': 'Clave1234._5'}
        addUserReq = requests.post('http://localhost:8080/apiv1/user', json=jsonDataUser)

        self.assertEqual(addUserReq.status_code, 200)
        self.assertEqual(addUserReq.reason, 'OK')
        self.assertEqual(addUserReq.text, 'User Created')

        jsonDataSong1 = {'isAudioFile': True, 'filename': 'Rock baby'}
        jsonDataSong2 = {'isAudioFile': True, 'filename': 'All night'}
        addAudioFileReq1 = requests.post('http://localhost:8080/apiv1/audiofile/Rock baby', data=jsonDataSong1)
        addAudioFileReq2 = requests.post('http://localhost:8080/apiv1/audiofile/All night', data=jsonDataSong2)

        self.assertEqual(addAudioFileReq1.status_code, 200)
        self.assertEqual(addAudioFileReq1.reason, 'OK')
        self.assertEqual(addAudioFileReq1.text, 'Audio file added')

        self.assertEqual(addAudioFileReq2.status_code, 200)
        self.assertEqual(addAudioFileReq2.reason, 'OK')
        self.assertEqual(addAudioFileReq2.text, 'Audio file added')

        jsonDataPlaylist = {'playlistName': 'Rock Classics',
                    'userName': 'JoseYYY',
                    'description': 'Old rock classics',
                    'songs': ['Rock baby', 'All night']}
        addPlaylistReq = requests.post('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        self.assertEqual(addPlaylistReq.status_code, 200)
        self.assertEqual(addPlaylistReq.reason, 'OK')
        self.assertEqual(addPlaylistReq.text, 'Playlist added')

    def tearDown(self):
        jsonDataPlaylist = {'playlistName': 'Rock Classics'}
        requests.delete('http://localhost:8080/apiv1/playlist', json=jsonDataPlaylist)

        jsonDataUser = {'userName':'JoseYYY'}
        requests.delete('http://localhost:8080/apiv1/user',json=jsonDataUser)

        requests.delete('http://localhost:8080/apiv1/audiofile/Rock baby')
        requests.delete('http://localhost:8080/apiv1/audiofile/All night')
