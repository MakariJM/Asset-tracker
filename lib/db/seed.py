from models import Assetlist, Asset, Owner, Base
from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

fake = Faker()

# Starting connection to the database which is in the lib directory
db_path = '../assettracker.db'

# engine = create_engine('sqlite:///assettracker.db')
engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':

    # populating the owner table
    for i in range(70):
        # creating names for the asset to test the names table
        owner = Owner(ownername=fake.name())
        session.add(owner)
    session.commit()

    print("owner seeded in the database")

    # populating the asset table
    for i in range(70):
        asset = Asset(
            title=fake.word(),
            location=fake.name(),
            value=random.randint(120, 600)
        )
        session.add(asset)
    session.commit()

    # print("asset seeded in the database")

    # populating the assetlist table
    owners = session.query(Owner).all()

    for i in range(70):
        assetlist = Assetlist(
            name=fake.sentence(nb_words=3),
            # associating random owner with the assetlist
            owner=random.choice(owners)
        )
        session.add(assetlist)

    session.commit()
    print("Assetlist seeded in the database")