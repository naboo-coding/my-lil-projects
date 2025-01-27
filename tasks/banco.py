from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///e/banco_dados.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    senha = Column("senha", String)
    uptodate = Column("uptodate", Boolean)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class Task(Base):
    __tablename__ = "tasks"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user = Column("user", ForeignKey("usuarios.nome"))
    todo = Column("to do", String)
    is_done = Column("done", Boolean)
    

    def __init__(self, todo, done=False):
        self.is_done = done
        self.todo = todo

class Note(Base):
    __tablename__ = "notes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user = Column("user", ForeignKey("usuarios.nome"))
    note = Column("note", LargeBinary)
    noteName = Column("noteName", String)

    def __init__(self, noteName, note, user):
        self.note = note
        self.noteName = noteName
        self.user = user

Base.metadata.create_all(bind=db)

# usuario = Usuario(nome="admin", senha="admin")
# session.add(usuario)  # Adiciona ao banco de dados
# session.commit()  # Salva o banco de dadosd

# usuario = Usuario(nome="", senha="")
# session.delete(usuario)  # Adiciona ao banco de dados
# session.commit()  # Salva o banco de dadosd

