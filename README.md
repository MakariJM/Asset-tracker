                                Asset Tracker CLI App

The Asset Tracker app is a command-line interface application designed to simplify the task of tracking assets.



                    Problem Statement:

Entities such as family households and small, medium, and large enterprises usually have a hard time trying to track their assets, especially their portable or mobile assets. Therefore, the asset tracking app enables any entity, through authorised users, to create an up-to-date central record of all assets, irrespective of various factors.



                    Applications Models:

Owner
This stores all the people granted custody of any asset.

Assetlist
This model keeps records of all assets owned by the entity or organisation.

Asset
This model keeps a record of the characteristics of an individual asset.



                    Application Key Features

    Managing "Owners"

Adding owners who will be allocated assets

View owner details

Managing and updating owner details

Removing owners from the system


    Managing "Assetlist"

Viewing all assets in the system

Adding new assets to the system

Updating asset details

List all assets.


    Managing "Asset"

Capture the title, name, or description of the asset.

Record the location of an asset.

Indicate the value of an asset.

Removing an asset from the system



                    Technologies Used

The following tools have been used on this project:

Python3

Pytest

SQLAlchemy

Alembic

Faker



            Project Setup

Clone the repository to your machine: git clone <repository-url>

Navigate to the cloned repository: cd Asset-tracker

Create a Pipenv environment and install dependencies: pipenv install

Activate environment: pipenv install and then pipenv shell

Create database migrations.

create db from migrations with alembic: cd lib/db && alembic upgrade heads

Navigate to the lib/db directory: cd lib/db



                How to run an app
After cloning the project, navigate to Asset Tracker/Library.
Run the application: Execute the cli.py script to launch the asset-tracker application: python3 cli.py



Contributions to the project are most welcome.



                            Author
                            Julius Makari.

