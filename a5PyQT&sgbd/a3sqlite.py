import sqlite3
con = sqlite3.connect('a3sqlitebd.db')
cur = con.cursor()

# cur.execute('CREATE TABLE IF NOT EXISTS clientes ('
#             'id  INTEGER PRIMARY KEY AUTOINCREMENT,'
#             'nome TEXT,'
#             'peso REAL'
#             ')')

# cur.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Leoz', 35))
# cur.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'A', 'peso': 85})
# cur.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'S', 'peso': 50})

# cur.execute('UPDATE clientes SET peso=? WHERE id=?', (94, 1))
# cur.execute('DELETE FROM clientes WHERE id=?', (4,))

con.commit()

cur.execute('SELECT * FROM clientes')

for linha in cur.fetchall():
    idt, nome, peso = linha
    print(idt, nome, peso)

cur.close()
con.close()
