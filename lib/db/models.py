from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///wines_library.db')

Base = declarative_base()


class Winery(Base):
    __tablename__ = 'wineries'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    bottles = relationship('Bottle', backref=backref('winery'))

    def __repr__(self):
        return f'Winery(id={self.id}, ' + \
            f'name={self.name})'
    
class Grape(Base):
    __tablename__ = 'grapes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    bottles = relationship('Bottle', backref=backref('grape'))

    def __repr__(self):
        return f'Grape(id={self.id}, ' + \
            f'name={self.name})'

class Bottle(Base):
    __tablename__ = 'bottles'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    price = Column(Integer())
    grape_id = Column(Integer(), ForeignKey('grapes.id'))
    winery_id = Column(Integer(), ForeignKey('wineries.id'))

    # grape = relationship('Grape', backref_populates='bottles')
    # winery = relationship('Winery', backref_populates='bottles')

    def __repr__(self):
        return f'Bottle(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'price={self.price}, ' + \
            f'grape_id={self.grape_id})' + \
            f'winery_id={self.winery_id})'