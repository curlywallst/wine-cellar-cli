#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.db.models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///wines_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace