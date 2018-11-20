import sqlite3 as sql


def add_data(conn, param, target):
    if target == 'equipment':
        conn.execute('INSERT INTO "equipment" ("equipment_id", "nomination") VALUES (None, "{}")'.format(param))
    elif target == 'worker':
        conn.execute('INSERT INTO "workers" ("worker_id", "full_name") VALUES (None, "{}")'.format(param))
    else:
        print('Wrong target to add')