from sqlmodel import SQLModel,Field
import uuid

class Cliente(SQLModel,table=True):
    __tablename__ = "cliente"
    id: str | None = Field(default_factory=lambda : str(uuid.uuid4()),primary_key=True)
    nome: str
    senha: str