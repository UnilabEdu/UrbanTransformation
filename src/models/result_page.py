from src.ext import db
from src.models.base import BaseModel

class Result(BaseModel):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    pdf = db.Column(db.String(), nullable=True)

    translations = db.relationship(
        'ResultTranslation',
        back_populates='result',
    )

    timelines = db.relationship('Timeline', back_populates='result')

    def __repr__ (self):
        return f'{[tr.title for tr in self.translations]}'

class ResultTranslation(BaseModel):
    __tablename__ = 'result_translations'

    id = db.Column(db.Integer(), primary_key=True)
    result_id = db.Column(db.Integer(), db.ForeignKey('results.id'), nullable=False)
    result = db.relationship('Result', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    title = db.Column(db.String)
    nav_title = db.Column(db.String)

    __table_args__ = (
        db.UniqueConstraint('result_id', 'lang', name='uq_result_lang'),
    )

    def __repr__ (self):
        return f'{self.result_id}, {self.lang}, {self.title}'

class Timeline(BaseModel):
    __tablename__ = 'timelines'

    id = db.Column(db.Integer, primary_key=True)
    result_id = db.Column(db.Integer(), db.ForeignKey('results.id'), nullable=False)
    result = db.relationship('Result', back_populates='timelines')

    img = db.Column(db.String())
    year = db.Column(db.Integer())

    translations = db.relationship('TimelineTranslation', back_populates='timeline', cascade="all, delete-orphan",)
    
    typologies = db.relationship('Typology', back_populates='timeline', cascade="all, delete-orphan",)

    def __repr__ (self):
        return f'{self.year}, {[rt.title for rt in self.result.translations]}'

class TimelineTranslation(BaseModel):
    __tablename__ = 'timeline_translations'

    id = db.Column(db.Integer, primary_key=True)
    timeline_id = db.Column(db.Integer(), db.ForeignKey('timelines.id'), nullable=False)
    timeline = db.relationship('Timeline', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    description = db.Column(db.Text())

    __table_args__ = (
        db.UniqueConstraint('timeline_id', 'lang', name='uq_timeline_lang'),
    )

class Typology(BaseModel):
    __tablename__ = 'typologies'

    id = db.Column(db.Integer, primary_key=True)
    timeline_id = db.Column(db.Integer(), db.ForeignKey('timelines.id'), nullable=False)
    timeline = db.relationship('Timeline', back_populates='typologies')

    img = db.Column(db.String())

    translations = db.relationship('TypologyTranslation', back_populates='typology', cascade="all, delete-orphan",)

    def __repr__(self):
        return f'{[t.title for t in self.translations]}'

class TypologyTranslation(BaseModel):
    __tablename__ = 'typology_translations'

    id = db.Column(db.Integer, primary_key=True)
    typology_id = db.Column(db.Integer(), db.ForeignKey('typologies.id'), nullable=False)
    typology = db.relationship('Typology', back_populates='translations')
    lang = db.Column(db.String(5), nullable=False)

    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
