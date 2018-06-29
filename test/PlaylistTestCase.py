import json
import unittest
import requests
import json
from collections import namedtuple


class PlaylistTestCase(unittest.TestCase):

    def setUp(self):
        jsonData = {'name': 'Max',
                    'lastName': 'Powell',
                    'userName': 'Max01',
                    'password': 'Password1234'}
        requests.put('http://localhost:8080/apiv1/users', json=jsonData)

    def test_add_Playlist_RockClassics_to_user_Max01(self):

        playlistJsonData = {'playlistName': 'RockClassics',
                         'userName': 'Max01',
                         'description': 'Classic rock songs'}
        addPlaylistReq = requests.put('http://localhost:8080/apiv1/playlists', json=playlistJsonData)
        self.assertEqual(addPlaylistReq.status_code, 200)
        self.assertEqual(addPlaylistReq.reason, 'OK')
        self.assertEqual(addPlaylistReq.text, 'Playlist added')

    def test_get_Nonexistent_Playlist(self):
        getData = {'playlistLikeName': 'something'}
        getPlaylistReq = requests.get('http://localhost:8080/apiv1/playlists', data=getData)
        self.assertEqual(getPlaylistReq.status_code, 200)
        self.assertEqual(getPlaylistReq.reason, 'OK')
        jsonResponse = json.loads(getPlaylistReq.text)
        self.assertEqual(len(jsonResponse), 0)

    def test_get_Playlists_With_Name_Like_Rock(self):

        firstPlaylistJsonData = {'playlistName': 'classicrock',
                            'userName': 'Max01',
                            'description': 'Classic rock songs'}
        requests.put('http://localhost:8080/apiv1/playlists', json=firstPlaylistJsonData)

        secondPlaylistJsonData = {'playlistName': 'oldrocksongs',
                                 'userName': 'Max01',
                                 'description': 'Very old rock songs'}
        requests.put('http://localhost:8080/apiv1/playlists', json=secondPlaylistJsonData)

        getData = {'playlistLikeName': 'rock'}
        getPlaylistReq = requests.get('http://localhost:8080/apiv1/playlists', data=getData)
        self.assertEqual(getPlaylistReq.status_code, 200)
        self.assertEqual(getPlaylistReq.reason, 'OK')
        jsonResponse = json.loads(getPlaylistReq.text)
        self.assertEqual(len(jsonResponse), 2)

    def test_update_Playlist_RockClassics_Data(self):

        playlistJsonData = {'playlistName': 'RockClassics',
                            'userName': 'Max01',
                            'description': 'Classic rock songs'}
        requests.put('http://localhost:8080/apiv1/playlists', json=playlistJsonData)

        jsonUpdate = {'description': 'Rock songs from the 80'}
        updatePlaylistReq = requests.put('http://localhost:8080/apiv1/playlists/RockClassics', json=jsonUpdate)

        self.assertEqual(updatePlaylistReq.status_code, 200)
        self.assertEqual(updatePlaylistReq.reason, 'OK')

        getPlaylistReq = requests.get('http://localhost:8080/apiv1/playlists/RockClassics')
        updateResponse = json.loads(getPlaylistReq.text, object_hook=lambda d: namedtuple('Playlist', d.keys())(*d.values()))
        self.assertEqual('Rock songs from the 80', updateResponse.playlist.description)

    def test_add_track_Song1_to_playlist_RockClassics(self):
        secondUserJsonData = {'name': 'Tom',
                            'lastName': 'Johnson',
                            'userName': 'Tom99',
                            'password': 'Password4567'}
        requests.put('http://localhost:8080/apiv1/users', json=secondUserJsonData)

        playlistJsonData = {'playlistName': 'RockClassics',
                            'userName': 'Max01',
                            'description': 'Classic rock songs'}
        requests.put('http://localhost:8080/apiv1/playlists', json=playlistJsonData)

        trackData = {'trackName': 'Song1', 'fileContent': 'content', 'owner': 'Tom99'}
        requests.put('http://localhost:8080/apiv1/tracks', json=trackData)

        playlistTrackData = {'tracks': ['Song1']}
        addTrackReq = requests.put('http://localhost:8080/apiv1/playlists/RockClassics', json=playlistTrackData)
        self.assertEqual(addTrackReq.status_code, 200)
        self.assertEqual(addTrackReq.reason, 'OK')
        self.assertEqual(addTrackReq.text, 'Playlist updated')

    def test_delete_track_Song1_from_playlist_RockClassics(self):
        secondUserJsonData = {'name': 'Tom',
                            'lastName': 'Johnson',
                            'userName': 'Tom99',
                            'password': 'Password4567'}
        requests.put('http://localhost:8080/apiv1/users', json=secondUserJsonData)

        playlistJsonData = {'playlistName': 'RockClassics',
                            'userName': 'Max01',
                            'description': 'Classic rock songs'}
        requests.put('http://localhost:8080/apiv1/playlists', json=playlistJsonData)

        trackData = {'trackName': 'Song1', 'fileContent': 'content', 'owner': 'Max01'}
        requests.put('http://localhost:8080/apiv1/tracks', json=trackData)

        playlistTrackData = {'tracks': ['Song1']}
        requests.put('http://localhost:8080/apiv1/playlists/RockClassics', json=playlistTrackData)

        playlistTrackData2 = {'tracks': ['Song1']}
        deleteTrackReq = requests.delete('http://localhost:8080/apiv1/playlists/RockClassics', json=playlistTrackData2)

        self.assertEqual(deleteTrackReq.status_code, 200)
        self.assertEqual(deleteTrackReq.reason, 'OK')
        self.assertEqual(deleteTrackReq.text, 'Tracks deleted from playlist')

    def tearDown(self):
        jsonData = {'playlistName': 'RockClassics'}
        requests.delete('http://localhost:8080/apiv1/users/Max01')
        requests.delete('http://localhost:8080/apiv1/users/Tom99')
        requests.delete('http://localhost:8080/apiv1/tracks/Song1')
        requests.delete('http://localhost:8080/apiv1/playlists/RockClassics')
        requests.delete('http://localhost:8080/apiv1/playlists/classicrock')
        requests.delete('http://localhost:8080/apiv1/playlists/oldrocksongs')

