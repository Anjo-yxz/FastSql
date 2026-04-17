from sqlalchemy import create_engine
import uvicorn
from src.server.Server import Server
from src.Execet.lerEnv import Env
from src.routes.User import User
from src.LimiteIp.ratelimite import Rate


servido = Server()
db = Env()
database = create_engine(db)
rate = Rate()
user = User(servido,database,rate)
user.execute()
if __name__ == "__main__":
    uvicorn.run(servido.app, host="0.0.0.0", port=8000)