import jwt
import requests
import secrets
import json
from time import time

# create a function to generate a token using the pyjwt library
def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & expiration time
        {"iss": 'YuMhlZO6TBeKDb5ZGaBtRw', "exp": time() + 5000},
        # Secret used to generate token signature
        'El8Z7bHHVVKByjJxkhnaW59yB31sjlcRZ7Fs',
        # Specify the hashing alg
        algorithm='HS256'
        # Convert token to utf-8
    ).decode('utf-8')

    return token


print(generateToken())

def getUsers():
    url = "https://api.zoom.us/v2/users"

    token = generateToken()

    payload={}
    headers = {
    'Authorization': f'Bearer {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


getUsers()