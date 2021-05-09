from api import db
from sqlalchemy.sql import func
from enum import Enum


class CalculationMethods(Enum):
    MEAN = 1
    MEDIAN = 2


class RecordModel(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Float)
    model = db.Column(db.Enum(CalculationMethods), nullable=False)
    date = db.Column(db.DateTime(), default=func.now())

    def __init__(self, result, model):

        self.result = result
        self.model = model
