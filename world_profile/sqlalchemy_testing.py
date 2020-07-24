import sqlalchemy as sa

engine = sa.create_engine('sqlite:///traveller.db', echo=True)

metadata = sa.MetaData()

starport_ratings = sa.Table('starport_ratings', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('rating', sa.String),
    sa.Column('quality', sa.String),
    sa.Column('berthing', sa.String),
    sa.Column('fuel', sa.String),
    sa.Column('facilities', sa.String)
    )

metadata.drop_all(engine)
metadata.create_all(engine)

ins = starport_ratings.insert()

conn = engine.connect()

conn.execute(ins, rating='B', quality='Good', 
    berthing='Cr500-Cr3000', fuel='Refined', facilities='Shipyard (spacecraft), Repair')

s = sa.select([starport_ratings])

result = conn.execute(s)
for row in result:
    print(row)

