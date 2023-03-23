#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Grape, Winery, Bottle

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/wines_library.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    breakpoint()

    import ipdb; ipdb.set_trace