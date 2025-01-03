import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # *********************************************************
    # sql01 = 'CREATE TABLE IF NOT EXISTS tb01 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)'
    # cursor.execute(sql01)
    # *********************************************************
    # sql02 = '''INSERT INTO tb01 (name, age) VALUES (?, ?)'''
    # cursor.execute(sql02, ('张三', 20))
    # cursor.execute(sql02, ('李四', 21))
    # cursor.execute(sql02, ('王五', 22))
    # cursor.execute(sql02, ('赵六', 23))
    # cursor.execute(sql02, ('孙七', 24))
    # cursor.execute(sql02, ('周八', 25))
    # cursor.execute(sql02, ('吴九', 26))
    # cursor.execute(sql02, ('郑十', 27))
    # *********************************************************
    # sql03 = '''INSERT INTO tb01 (name, age) VALUES (?, ?)'''
    # datas = [
    #     ('张三2', 20),
    #     ('李四2', 21),
    #     ('王五2', 22),
    #     ('赵六2', 23),
    #     ('孙七2', 24),
    # ]
    # cursor.executemany(sql03, datas)
    # *********************************************************
    # sql04 = 'select id,name,age from tb01'
    # cursor.execute(sql04)
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)
    # *********************************************************
    sql05 = "update tb01 set name = 'XXXX' where id=1"
    a  = cursor.execute(sql05)
    


    conn.commit()
    conn.close()

    print('ok')


