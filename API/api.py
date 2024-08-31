import json
from fastapi import FastAPI

app = FastAPI()

@app.get('/getMyInfo')
def get_my_info():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        [
            {"facebookUser": "andresdeatorrevilla"},
            {"instagramUser": "andresdeatorrevilla"},
            {"xUser": "andresdeatorrevilla"},
            {"linkedin": "/adltv"},
            {"githubUser": "DragonBlade"}
        ],
        "blog": "https://aandresdelatorrevilla.com",
        "author": "Andrés De La Torre Villa"
    }
    return value
