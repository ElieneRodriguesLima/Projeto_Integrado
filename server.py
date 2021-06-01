from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Legenda
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_legenda import RepositorioLegenda

#criar_bd()

subtitle = FastAPI()


@subtitle.post('/legendas', status_code=status.HTTP_201_CREATED, response_model=Legenda)
def criar_legendas(legenda: Legenda, db: Session = Depends(get_db)):
    legenda_criada = RepositorioLegenda(db).criar(legenda)
    return legenda_criada


@subtitle.get('/legendas', status_code=status.HTTP_200_OK, response_model=List[Legenda])
def listar_legendas(db: Session = Depends(get_db)):
    legendas = RepositorioLegenda(db).listar()
    return legendas






