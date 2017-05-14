import sqlite3


conn = sqlite3.connect('sinonimos.db')
c = conn.cursor()

c.execute('CREATE TABLE sinonimos (word TEXT, url TEXT, font TEXT, synonymous TEXT, PRIMARY KEY (word))')

conn.close()
