import csv
import os

from sqlite3 import IntegrityError

import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method


engine = sa.create_engine('sqlite:///:memory:', echo=True)
Session = sa.orm.sessionmaker(bind=engine)
Base = declarative_base()

# What should tests look like for this?

# Defining column size restrictions allows the database engine to optimise the
# sparseness of the database (i.e. there's less wasted space)
# Also quicker to index shorter fields

# Look at how to implement restrictions with database migrations.

# Look at plugins for sqlalchemy or pytest that support tests.

class StarportFacilities(Base):
    __tablename__ = 'starport_facilities'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.String(1), unique=True)
    quality = sa.Column(sa.String(15))
    berthing = sa.Column(sa.String(15))
    fuel = sa.Column(sa.String(15))
    facilities = sa.Column(sa.String(50))


class Size(Base):
    __tablename__ = 'size'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer, unique=True)
    examples = sa.Column(sa.String(50))
    gravity = sa.Column(sa.String(50))

    @hybrid_property
    def diameter(self):
        return f'{str(self.rating * 1600)}km'


class Atmosphere(Base):
    __tablename__ = 'atmosphere'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer, unique=True)
    composition = sa.Column(sa.String(50))
    examples = sa.Column(sa.String(50))
    pressure = sa.Column(sa.String(50))
    survivalgear = sa.Column(sa.String(50))


class Hydrography(Base):
    """Describing the Hydrography table"""
    __tablename__ = 'hydrography'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer, unique=True)
    description = sa.Column(sa.String(250))

    @hybrid_property
    def water_percentage(self):
        start = self.rating * 10 - 4
        end = self.rating * 10 + 5
        if start < 0:
            start = 0
        if end > 100:
            end = 100
        return f'{start}% - {end}%'


class Government(Base):
    """Describing the government information table"""
    __tablename__ = 'government'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer, unique=True)
    government_type = sa.Column(sa.String(50))
    description = sa.Column(sa.String)
    examples = sa.Column(sa.String(250))
    contraband = sa.Column(sa.String(250))


class LawLevel(Base):
    """Describing the law level information table"""
    __tablename__ = 'lawlevel'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer, unique=True)
    restricted_arms = sa.Column(sa.String(250))
    restricted_armor = sa.Column(sa.String(250))


# Are database migration (revision) files supposed to have lots of duplication of the models,
# to ensure rollbacks? What's a manageable way to reduce the duplication without endangering the
# integrity of the migration? Maybe tie the revision to the git commit, so you can always checkout the
# working version of the models for a specific revision?


Base.metadata.create_all(engine)
session = Session()


starports = os.path.join(
    os.path.dirname(__file__), 'datafiles/starport_facilities.csv')
sizes = os.path.join(os.path.dirname(__file__), 'datafiles/size.csv')
atmosphere_ratings = os.path.join(os.path.dirname(__file__), 'datafiles/atmosphere.csv')


def data_from_csvfile(csvf):
    with open(csvf, newline='', encoding='utf-8-sig') as csvfile:
        yield from csv.DictReader(csvfile)


def seed_database(csvf, tablecls):
    """Iterate over a csv.DictReader object and add each row to the database or catch
    an IntegrityError"""
    for row in data_from_csvfile(csvf):
        try:
            session.add(tablecls(**row))
            session.flush()
        except sa.exc.IntegrityError:
            session.rollback()
            print(f'ERROR: Cannot add row as there is already an entry for rating {row["rating"]}')


seed_database(starports, StarportFacilities)
seed_database(sizes, Size)
seed_database(atmosphere_ratings, Atmosphere)

session.commit()
qa = session.query(Size).filter_by(rating='3').first()
print(qa.rating, qa.examples, qa.diameter)

# Need to figure out a way to take notes on the app without commenting all over the code.
# Look in to jupyter notes/journalling?