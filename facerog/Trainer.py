from facerog.trainer.train import train
from facerog.trainer.collect import collect
from db import DataBase

class Trainer():
    def __init__(self, db) -> None:
        self.db:DataBase = db

    def start_collecting(self, name: str):
        print("collecting")
        id = self.db.add_or_get_face(name)
        collect(id)
        print('trainnig')
        train()

    def retraint_model(self):
        train()
