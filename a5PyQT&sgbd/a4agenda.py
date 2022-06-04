import sqlite3


class Agenda:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()

    def insert(self, nome, tel):
        cons = 'INSERT OR IGNORE INTO clientes (nome, tel) VALUES (?, ?)'
        self.cur.execute(cons, (nome, tel))
        self.con.commit()

    def edit(self, nome, tel, ide):
        cons = 'UPDATE OR IGNORE clientes SET nome=?, tel=? WHERE id=?'
        self.cur.execute(cons, (nome, tel, ide))
        self.con.commit()

    def dl(self, ide):
        cons = 'DELETE FROM clientes WHERE id=?'
        self.cur.execute(cons, (ide,))
        self.con.commit()

    def list(self):
        self.cur.execute('SELECT * FROM clientes')
        for linha in self.cur.fetchall():
            print(linha)

    def busca(self, val):
        cons = 'SELECT * FROM clientes WHERE nome LIKE ?'
        self.cur.execute(cons, (f'%{val}%',))
        for linha in self.cur.fetchall():
            print(linha)

    def close(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    ag = Agenda('a4agenda.db')
    ag.insert('Luiz', '123')
    ag.insert('ZE', '1233')
    ag.insert('JO', '1234')
    ag.insert('De', '1237')
    ag.insert('Luis', '1236')
    ag.edit('Luisa', '12345', 5)
    ag.dl(4)
 #   ag.list()
    ag.busca('lu')
    ag.close()

# cur.execute('CREATE TABLE IF NOT EXISTS clientes ('
#             'id  INTEGER PRIMARY KEY AUTOINCREMENT,'
#             'nome TEXT,'
#             'tel TEXT UNIQUE'
#             ')')
#
# cur.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Leoz', 35))
# cur.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'A', 'peso': 85})
# cur.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'S', 'peso': 50})
#
# cur.execute('UPDATE clientes SET peso=? WHERE id=?', (94, 1))
# cur.execute('DELETE FROM clientes WHERE id=?', (4,))
#
# con.commit()
#
# cur.execute('SELECT * FROM clientes')
#
# for linha in cur.fetchall():
#     idt, nome, peso = linha
#     print(idt, nome, peso)
