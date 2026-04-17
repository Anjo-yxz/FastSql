from fastapi import Request
from sqlalchemy import Engine
from sqlmodel import Session, select
from src.LimiteIp.ratelimite import Rate
from src.server.Server import Server
from src.Model.model import Cliente
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

class User:
    def __init__(self,serve:Server,database:Engine,rate:Rate):
        self.__database = database
        self.__server = serve
        self.limiter = rate
        self.__server.app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
        self.__server.app.state.limiter = self.limiter


    def __create_user(self,request: Request,clienteTable: Cliente):
        with Session(self.__database) as user:
            user.add(clienteTable)
            user.commit()
            user.refresh(clienteTable)
            return {"status": "Success", "data": clienteTable}
    
    def __clienteUser(self,request: Request):
        with Session(self.__database) as user:
            cliente = user.exec(select(Cliente)).all()
            return cliente

    def __veryUser(self,request: Request,usuario:str, senha:str):
        with Session(self.__database) as user:
            bucas = select(Cliente).where(Cliente.nome == usuario)
            verfy = user.exec(bucas).first()

            if verfy and verfy.senha == senha:
                return "Logim Sucesso"
            return "Erro = Nome Or Senha Invalid"
        
    def rateLimite(self,tentativa:str,minute:str,serve):
        limit_decorator = self.limiter.limit(f"{tentativa}/{minute}")
        return limit_decorator(serve)
    
    def execute(self):
            self.__server.posts("/creat", self.rateLimite("2","5 minute",self.__create_user))
            self.__server.gets("/users", self.rateLimite("3","minute",self.__clienteUser))
            self.__server.gets("/userverfy", self.rateLimite("3","2 minute",self.__veryUser))
