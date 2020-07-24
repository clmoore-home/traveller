import sqlite3

conn = sqlite3.connect('traveller.db')

curs = conn.cursor()

result = curs.execute("""select * from starport_ratings""")
print(result.fetchall())
