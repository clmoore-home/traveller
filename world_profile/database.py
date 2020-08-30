import os
import inspect

import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base


engine = sa.create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()
Session = sa.orm.sessionmaker(bind=engine)

# How can I create a constructor for the Base so that the default is args assignment not kwargs?
# *args version works for tables with a small number of columns, but too many and you should be using kwargs

# What should tests look like for this?

# Define common attributes outside of classes?

# Defining column size restrictions allows the database engine to optimise the sparseness of the database (i.e. there's less wasted space)
# Also quicker to index shorter fields
# Look at how to implement restrictions with database migrations.
# Remember about uniqueness constraints on other columns in the table.

# Look at plugins for sqlalchemy or pytest that support tests.

sarating = sa.Column(sa.String)

class StarportFacilities(Base):
    __tablename__ = 'starport_facilities'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sarating
    quality = sa.Column(sa.String)
    berthing = sa.Column(sa.String)
    fuel = sa.Column(sa.String)
    facilities = sa.Column(sa.String)


# Should we store the actual size in the database or should it be
# a calculation in the model classes? Seems cleaner and quicker
# to store the size in the database but is there an advantage to
# making the size a calculation? Look at virtual columns


class Size(Base):
    __tablename__ = 'size'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer, unique=True)
    examples = sa.Column(sa.String)
    gravity = sa.Column(sa.String)


class Atmosphere(Base):
    __tablename__ = 'atmosphere'

    id = sa.Column(sa.Integer, primary_key=True)
    rating = sa.Column(sa.Integer)
    composition = sa.Column(sa.String)
    examples = sa.Column(sa.String)
    pressure = sa.Column(sa.String)
    survivalgear = sa.Column(sa.String)



Base.metadata.create_all(engine)

session = Session()


def data_from_tabfile(tabfile):
    """Read a file and yield tuples of the line"""
    with open(tabfile) as inf:
        for line in inf:
            yield tuple(line.strip().split('\t'))


def mapping_from_tabfile(tabfile, keys):
    """Returns a dictionary for each line"""
    with open(tabfile) as inf:
        for line in inf:
            yield dict(zip(keys, line.strip().split('\t')))

# Use csv files and parse with the csv module so that you get the column names and don't need the mapping_from_tabfile functionality.
# Seed data files are then wholly self contained.

# What can I do to reduce the duplication here? Or do I need to?
starports = os.path.join(
    os.path.dirname(__file__), 'datafiles/starport_facilities.txt')
sizes = os.path.join(os.path.dirname(__file__), 'datafiles/size.txt')
atmosphere_ratings = os.path.join(os.path.dirname(__file__), 'datafiles/atmosphere.txt')

starport_data = mapping_from_tabfile(starports, ['rating', 'quality', 'berthing', 'fuel', 'facilities'])
size_data = mapping_from_tabfile(sizes, ['rating', 'examples', 'gravity'])
atmospheric_data = mapping_from_tabfile(atmosphere_ratings,
    ['rating', 'composition', 'examples', 'pressure', 'survivalgear'])

# session.add_all([StarportFacilities(**starport) for starport in starport_data])
session.add_all([Size(**s) for s in size_data])
# session.add_all([Atmosphere(**atmo) for atmo in atmospheric_data])
session.add_all([Size(**s) for s in size_data])
session.commit()
qa = session.query(Size).filter_by(rating='1').first()
print(qa.rating, qa.examples)

