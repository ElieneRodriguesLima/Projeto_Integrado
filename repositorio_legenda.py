from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioLegenda():

    def __init__(self, db: Session):
        self.db = db


    def criar(self, legenda: schemas.Legenda):
        db_legenda = models.Legenda(nome=legenda.nome,
                                    pais=legenda.pais,
                                    genero=legenda.genero,
                                    ano=legenda.ano)
        self.db.add(db_legenda)
        self.db.commit()
        self.db.refresh(db_legenda)
        return db_legenda

    def listar(self):
        legendas = self.db.query(models.Legenda).all()
        return legendas

    def obter(self):
        pass

    def remover(self):
        pass