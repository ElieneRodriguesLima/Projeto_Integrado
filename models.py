from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)

    legendas = relationship('Legenda', back_populates='usuario')

class Legenda(Base):
    __tablename__ = 'legenda'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    detalhes = Column(String)
    pais = Column(String)
    disponivel = Column(Boolean)
    genero = Column(String)
    ano = Column(Integer)
    tamanho = Column(String)
    Usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))

    usuario = relationship('usuario', back_populates='legendas')

    