from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Owner, Assetlist, Asset

if __name__ == '__main__':

    db_path = '../lib/assettracker.db'

    engine = create_engine(f'sqlite:///{db_path}')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb
    ipdb.set_trace()