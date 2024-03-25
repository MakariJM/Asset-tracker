from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Asset, Base, Assetlist, Owner

# Establishing a connection to the database
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
    print("4. Display Asset")
    print("5. Quit")


def add_asset():
    print("Add Asset")

    title = input("Enter asset title: ")
    location = input("Enter location of the asset: ")
    value_dollars = int(input("Enter value of the asset in dollars: "))

    asset = Asset(title=title, location=location, value=value_dollars)
    session.add(asset)
    session.commit()

    print("Asset added successfully!")


def search_asset():
    print("Search Asset")
    print("1. Search by Title")
    print("2. Search by Location")
    print("3. Back to Main Menu")

    search_option = input("Enter Option: ")

    if search_option == "1":
        title = input("Enter the title of the asset: ")
        assets = session.query(Asset).filter(
            Asset.title.ilike(f"%{title}%")).all()
        display_asset(assets)
    elif search_option == "2":
        location = input("Enter the location: ")
        assets = session.query(Asset).filter(
            Asset.location.ilike(f"%{location}%")).all()
        display_asset(assets)
    elif search_option == "3":
        return
    else:
        print("Invalid Choice")


def display_asset(assets):
    if not assets:
        print("No matching assets found. ")
    else:
        print("Matching Assets: ")


def view_assetlists(owner_id):
    print("View Assetlists")
    owner = session.query(Owner).filter_by(id=owner_id).first()

    if not owner:
        print("Owner not found")
        return

    assetlists = owner.assetlists

    if not assetlists:
        print("No assetlists found for this owner ")
    else:
        print("Assetlists: ")
        for assetlist in assetlists:
            print(f"Assetlist Name: {assetlist.name}")
            print("Assets")


def display_asset():
    print("Displaying Assets")
    title = input("Enter title of asset to be displayed: ")

    asset = session.query(Asset).filter_by(title=title).first()


def cli():
    owner_id = 3
    while True:
        main_menu()
        option = input("Enter your option: ")

        if option == "1":
            add_asset()
            break
        elif option == "2":
            search_asset()
            break
        elif option == "3":
            view_assetlists(owner_id)
            break
        elif option == "4":
            display_asset()
            break
        elif option == "5":
            print("Quiting....")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    cli()