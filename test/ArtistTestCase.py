import unittest
import requests
import json

class ArtistTestCase(unittest.TestCase):

    def test_addArtist_JoseYYY_Jose_Perez_34(self):

        postData = {'name': 'Jose', 'lastName': 'Perez', 'age': 34}
        addArtistReq = requests.post('http://localhost:8080/apiv1/artist/JoseYYY', data=postData)

        self.assertEqual(addArtistReq.status_code, 200)
        self.assertEqual(addArtistReq.reason, 'OK')
        self.assertEqual(addArtistReq.text, 'Artist added')

        getArtistReq = requests.get('http://localhost:8080/apiv1/artist/JoseYYY')
        self.assertEqual(getArtistReq.status_code, 200)
        jsonResponse = json.loads(getArtistReq.text)
        self.assertEqual(jsonResponse['artist']['name'], 'Jose')
        self.assertEqual(jsonResponse['artist']['lastName'], 'Perez')
        self.assertEqual(jsonResponse['artist']['stageName'], 'JoseYYY')
        self.assertEqual(jsonResponse['artist']['age'], 34)


    def tearDown(self):
        requests.delete('http://localhost:8080/apiv1/artist/JoseYYY')



if __name__ == '__main__':
    unittest.main()
