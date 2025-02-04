import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS users')
cur.execute('DROP TABLE IF EXISTS sectors')

cur.execute('''
    CREATE TABLE users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT,
        EMAIL TEXT,
        SENHA TEXT
    )
''')

cur.execute('''
    CREATE TABLE sectors (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT,
        SENHA TEXT
    )
''')

cur.execute("INSERT INTO users (NOME, EMAIL, SENHA) VALUES (?, ?, ?)", 
            ('mikael', 'mikael@123.com', 'mikael123'))

con.commit()
con.close()
