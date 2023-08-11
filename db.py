#Create a data base
import sqlite3

db = sqlite3.connect('users.db')

cur = db.cursor()

cur.execute('CREATE TABLE if not exists users(id INTEGER, name TEXT)')

cur.execute('CREATE TABLE if not exists skills(name TEXT, progress INTEGER, id INTEGER)')


list = ['James', 'Lulu', 'Mohammed', 'nawa', 'Rose', 'Sakura', 'Naoki', 'Tanaka']

for i, emp in enumerate(list):

    cur.execute(f'INSERT INTO users(id, name) values({i + 1}, "{emp}")')


cur.execute('SELECT id, name FROM users')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())

print(cur.fetchall())

print(cur.fetchmany(2))
#Save Commit Changes
db.commit()


# db.execute('CREATE TABLE skills (name TEXT, progress INTEGER, id INTEGER)')

# cur.execute('INSERT INTO users(id, name) values(1, "Jane")')
# cur.execute('INSERT INTO users(id, name) values(2, "David")')
# cur.execute('INSERT INTO users(id, name) values(3, "Omar")')
# cur.execute('INSERT INTO users(id, name) values(4, "Tanaka")')
# cur.execute('INSERT INTO users(id, name) values(5, "Naoki")')
