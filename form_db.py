import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS users')
cur.execute('DROP TABLE IF EXISTS sectors')
cur.execute('DROP TABLE IF EXISTS variaveis')

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
        PROPRIETARIO INTEGER REFERENCES users(ID),
        NOME TEXT,
        CAPACIDADE_RESERVATORIO INTEGER,
        POCO_PROFUNDIDADE INTEGER
    )
''')

cur.execute('''
    CREATE TABLE variaveis (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SETOR INTEGER REFERENCES sectors(ID),
        DATA DATE,
        IRRIGACAO BOOLEAN,
        TEMPERATURA FLOAT,
        UMIDADE FLOAT,
        CHUVA FLOAT,
        VENTO FLOAT,
        RAD_SOLAR FLOAT
    )
''')

cur.execute("INSERT INTO users (NOME, EMAIL, SENHA) VALUES (?, ?, ?)", 
            ('admin', 'pao@dequeijo.com', 'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec'))

cur.execute("INSERT INTO sectors (PROPRIETARIO, NOME, CAPACIDADE_RESERVATORIO, POCO_PROFUNDIDADE) VALUES (?, ?, ?, ?)", (1, 'Setor A', 1000, 50)) 

cur.execute("INSERT INTO variaveis (SETOR, DATA, IRRIGACAO, TEMPERATURA, UMIDADE, CHUVA, VENTO, RAD_SOLAR) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (1, '2021-01-01', 1, 30, 50, 11, 5, 111))
cur.execute("INSERT INTO variaveis (SETOR, DATA, IRRIGACAO, TEMPERATURA, UMIDADE, CHUVA, VENTO, RAD_SOLAR) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (2, '2021-01-02', 1, 31, 51, 12, 6, 222))
cur.execute("INSERT INTO variaveis (SETOR, DATA, IRRIGACAO, TEMPERATURA, UMIDADE, CHUVA, VENTO, RAD_SOLAR) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (3, '2021-01-03', 1, 32, 52, 12, 7, 333))

con.commit()
con.close()