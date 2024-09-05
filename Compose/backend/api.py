from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:8080",  # URL del frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/getMyInfo')
def get_my_info():
    value = {
        "name": "Vergil",
        "lastname": "De La Torre",
        "socialMedia":
            {
                "linkedin": "in/adltv",
                "githubUser": "DragonBlade1219"
            }
        ,
        "website": "http://localhost:8080/linktree.html",
        "author": "Vergil"
    }
    return value

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)