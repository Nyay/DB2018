import sqlite3 as sql
from collections import defaultdict, Iterable


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


def chain(*iterables):
    for iterable in iterables:
        if not isinstance(iterable, Iterable):
            yield iterable
        else:
            for item in iterable:
                if item != iterable:
                    yield from chain(item)
                else:
                    yield item


def add_data(cursor, param, target):
    cmd1 = 'INSERT INTO "workers" ("full_name") VALUES ("{}")'
    cmd2 = 'INSERT INTO "equipment" ("nomination") VALUES ("{}")'
    cmd3 = 'INSERT INTO "belonging" ("equipment_id", "worker_id") VALUES ("{}", "{}")'
    if target == 'equipment':
        if type(param) is str:
            cursor.execute(cmd2.format(param))
        elif type(param) is list:
            for item in param:
                cursor.execute(cmd2.format(item))
    elif target == 'worker':
        if type(param) is str:
            cursor.execute(cmd1.format(param))
        elif type(param) is list:
            for item in param:
                cursor.execute(cmd1.format(item))
    elif target == 'belong':
        if type(param) is list:
            cursor.execute(cmd3.format(param[0], param[1]))
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


def get_spare(cursor):
    cmd3 = 'SELECT "equipment_id" FROM "equipment"'
    cmd4 = 'SELECT "equipment_id" FROM "belonging"'
    cmd5 = 'SELECT "nomination" FROM "equipment" WHERE "equipment_id" == "{}"'
    cursor.execute(cmd3)
    eq_ids = list(chain(cursor.fetchall()))
    cursor.execute(cmd4)
    inuse = list(chain(cursor.fetchall()))
    cursor.execute(cmd4)
    result = defaultdict()
    for item in list(set(eq_ids) - set(inuse)):
        cursor.execute(cmd5.format(item))
        result[item] = cursor.fetchone()[0].strip('\n')
    return result


def get_workers(cursor):
    cmd3 = 'SELECT * FROM "workers"'
    cursor.execute(cmd3)
    workers = cursor.fetchall()
    result = defaultdict()
    for item in workers:
        result[item[0]] = item[1]
    return result

#print(get_spare())

#conn.close()

#add_data_file(conn, '/Users/macbook/Desktop/DB2018/equipment.txt', 'equipment')

#add_data(conn, [1, 1], 'belong')
