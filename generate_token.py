import jwt
import requests
from time import time

# create a function to generate a token using the pyjwt library
def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & expiration time
        {"iss": 'whoops', "exp": time() + 5000},
        # Secret used to generate token signature
        'whoops',
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