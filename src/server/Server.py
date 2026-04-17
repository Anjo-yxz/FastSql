from fastapi import FastAPI
import uvicorn

class Server:
    def __init__(self):
        self.app = FastAPI()
    
    def gets(self, rotas: str, fucao):
        self.app.get(rotas)(fucao)
    
    def posts(self, rotas: str, fucao):
        self.app.post(rotas)(fucao)
    
    def starter(self, porta: int):
        uvicorn.run(self.app, host="0.0.0.0", port=porta)