import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, act, animal, blurb, usstate, months) VALUES (?,?,?,?,?,?)",
            ('Salamander Crossing', 'yes','amphibian','help salamanders cross the road','indiana','march')
            )

cur.execute("INSERT INTO posts (title, act, animal, blurb, usstate, months) VALUES (?,?,?,?,?,?)",
            ('Monarch Migration', 'yes','insect','see the monarch migration','arkansas','may')
            )

connection.commit()
connection.close()