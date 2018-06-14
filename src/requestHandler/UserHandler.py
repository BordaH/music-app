import tornado.web
from src.validationFunctions import validPassword
from hashlib import sha512
import json

class UserHandler(tornado.web.RequestHandler):


    def post(self):

        statusCode = 200
        statusMessage = 'User Created'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            userName = data['userName']
            name = data['name']
            lastName = data['lastName']
            age = int(data['age'])
            password = data['password']

            if validPassword(password):
                cryptPass = sha512(password.encode('utf-8')).hexdigest()
                self.application.db.addUser(userName,cryptPass, name, lastName, age)
            else:
                statusCode = 400
                statusMessage = "Bad request"
        except Exception as e:
            statusCode = 400
            statusMessage = "Artist not added"
        self.set_status(statusCode)
        self.write(statusMessage)


    def delete(self):
        statusCode = 200
        statusMessage = 'User deleted'
        try:
            data = json.loads(self.request.body.decode('utf-8'))
            userName = data['userName']
            self.application.db.deleteUser(userName)
        except Exception as e:
            statusCode = 400
            statusMessage = "Bad request"
        self.set_status(statusCode)
        self.write(statusMessage)
