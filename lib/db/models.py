from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table

Base = declarative_base()


# Many to many relationships between assetlist and asset table
assetlist_asset_intermediary = Table(
    'assetlist_asset_intermediary',
    Base.metadata,
    Column('assetlist_id', Integer, ForeignKey('assetlist.id')),
    Column('asset_id', Integer, ForeignKey('asset.id'))
)


class Owner(Base):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True)
    ownername = Column(String(), unique=True, nullable=False)
    # One to may relationship between owners and assetlists
    assetlists = relationship("Assetlist", back_populates="owner")

class Assetlist(Base):
    __tablename__ = 'assetlist'
    id = Column(Integer, primary_key=True)
    name = Column(String(), nullable=False)
    # Linking assetlist with the owner using a foreign key
    owner_id = Column(Integer, ForeignKey('owner.id'))
    # Starting relationship between the assetlist and the owner
    owner = relationship("Owner", back_populates="assetlists")
    # Starting relationship between the assetlist and the asset
    assets = relationship(
        "Asset", secondary=assetlist_asset_intermediary, back_populates="assetlists")


class Asset(Base):
    __tablename__ = 'asset'
    id = Column(Integer, primary_key=True)
    title = Column(String(), nullable=False)
    location = Column(String())
    value = Column(Integer())
    # Establishing relationship between assets and assetlists
    assetlists = relationship(
        "Assetlist", secondary=assetlist_asset_intermediary, back_populates="assets")