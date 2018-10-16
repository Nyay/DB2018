import sqlite3 as sql
from collections import defaultdict

conn = sql.connect('sis.db')

cdf = conn.cursor()
cdf.fetchall()


def add_data(conn, param, target):
    cmd1 = 'INSERT INTO "workers" ("full_name") VALUES ("{}")'
    cmd2 = 'INSERT INTO "equipment" ("nomination") VALUES ("{}")'
    cmd3 = 'INSERT INTO "belonging" ("equipment_id", "worker_id") VALUES ("{}", "{}")'
    if target == 'equipment':
        if type(param) is str:
            conn.execute(cmd2.format(param))
            conn.commit()
        elif type(param) is list:
            for item in param:
                conn.execute(cmd2.format(item))
                conn.commit()
    elif target == 'worker':
        if type(param) is str:
            conn.execute(cmd1.format(param))
            conn.commit()
        elif type(param) is list:
            for item in param:
                conn.execute(cmd1.format(item))
                conn.commit()
    elif target == 'belong':
        if type(param) is list:
            conn.execute(cmd3.format(param[0], param[1]))
            conn.commit()
    else:
        print('Wrong target to add')


def add_data_file(conn, path, target):
    if target == 'equipment':
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                add_data(conn, line.split('\t'), 'equipment')
    elif target == 'worker':
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                add_data(conn, line.split('\t'), 'worker')
    else:
        print('Wrong target to add')


def get_id(conn, param, target):
    cmd1 = 'SELECT "worker_id" FROM "workers" WHERE "full_name" == "{}"'
    cmd2 = 'SELECT * FROM "equipment" WHERE "nomination" IS "{}"'
    if target == 'equipment':
        if type(param) is str:
            crsr = conn.cursor()
            crsr.execute(cmd2.format(param))
            return crsr.fetchone()
        elif type(param) is list:
            result = defaultdict()
            for item in param:
                crsr = conn.cursor()
                crsr.execute(cmd2.format(param))
                result[item] = crsr.fetchone()
            return result
    elif target == 'worker':
        if type(param) is str:
            crsr = conn.cursor()
            crsr.execute(cmd1.format(param))
            return crsr.fetchone()
        elif type(param) is list:
            result = defaultdict()
            for item in param:
                crsr = conn.cursor()
                crsr.execute(cmd1.format(item))
                result[item] = crsr.fetchone()[0]
            return result
    else:
        print('Wrong target to add')


print(get_id(conn,
       ['Татаринов Юрий Владимирович',
        'Минина Ольга Игоревна',
        'Татаринов Артем Юрьевич'],
       'worker'))

#add_data_file(conn, '/Users/macbook/Desktop/DB2018/equipment.txt', 'equipment')

#add_data(conn, [1, 1], 'belong')
