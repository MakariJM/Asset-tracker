from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Asset, Base

# Connection to the database
db_path = './db/assettracker.db'

engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def main_menu():
    print("Main Menu")
    print("1. Add Asset")
    print("2. Search Asset")
    print("3. View Assetlists")
    print("4. Display Assets")
    print("5. Quit")


def add_asset():
    print("Add Asset")

    title = input("Enter asset title: ")
    location = input("Enter location of the asset: ")
    value = int(input("Enter value of the asset: "))

    asset = Asset(title=title, location=location, value=value)
    session.add(asset)
    session.commit()

    print("Asset added successfully!")


def cli():
    while True:
        main_menu()
        option = input("Enter your option: ")

        if option == "1":
            add_asset()
            break
        elif option == "2":
            pass
            break
        elif option == "3":
            pass
            break
        elif option == "4":
            pass
            break
        elif option == "5":
            print("Quiting....")
            break
        else:
            print("Invalid Option")


if __name__ == "__main__":
    cli()