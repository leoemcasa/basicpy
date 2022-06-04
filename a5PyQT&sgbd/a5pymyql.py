import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def con():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='sales',
        password='87651234',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conn
    finally:
        conn.close()


# with con() as conn:
#     with conn.cursor() as cur:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         cur.execute(sql, ('Jack', 'Moon', 112, 220))
#         conn.commit()

# with con() as conn:
#     with conn.cursor() as cur:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('Muriel', 'Coragem', 19, 55),
#             ('Rose', 'Coragem', 12, 22),
#             ('Jose', 'Coragem', 11, 20)
#         ]
#
#         cur.executemany(sql, dados)
#         conn.commit()

# with con() as conn:
#     with conn.cursor() as cur:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cur.execute(sql, (6,))
#         conn.commit()

# with con() as conn:
#     with conn.cursor() as cur:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s, %s)'
#         cur.execute(sql, (7, 8, 9, 10))
#         conn.commit()

# with con() as conn:
#     with conn.cursor() as cur:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cur.execute(sql, (11, 13))
#         conn.commit()

with con() as conn:
    with conn.cursor() as cur:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cur.execute(sql, ('Joana', 5))
        conn.commit()

with con() as con:
    with con.cursor() as cur:
        cur.execute('SELECT * FROM clientes')
        res = cur.fetchall()
        for linha in res:
            print(linha['nome'], linha['sobrenome'])
            print(linha)
            print()
