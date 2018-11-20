from config_info import server, user, password, database
import pymysql


def add(table, columns, values):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        sql = "INSERT INTO {}({}) VALUES ({})"
        cursor.execute(sql.format(table,
                                  ", ".join(columns),
                                  "'" + str("', '".join(values)) + "'"))
    db.commit()
    db.close()


def look(table):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        sql = "SELECT * FROM {}"
        cursor.execute(sql.format(table))
    db.commit()
    db.close()


def look_something(table, thing):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        sql = "SELECT {} FROM {}"
        cursor.execute(sql.format(thing, table))
        items = cursor.fetchall()
    db.commit()
    db.close()
    return items


def delete(table, condition):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        if condition == 'all':
            sql = "DELETE FROM {}"
            cursor.execute(sql.format(table))
        else:
            conditions = []
            for name in condition:
                conditions.append("{}='{}'".format(name,
                                                   condition[name]))
            sql = "DELETE FROM {} WHERE {}"
            cursor.execute(sql.format(table,
                                      ' AND '.join(conditions)))
    db.commit()
    db.close()


def change_status(table, params, condition):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        query = '''UPDATE {}
                SET Status = "{}"
                WHERE id = "{}"'''
        cursor.execute(query.format(table,
                                    condition,
                                    params))
    db.commit()
    db.close()


def delete_by_status(table, condition):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        query = '''DELETE FROM {} WHERE Status = "{}"'''
        cursor.execute(query.format(table,
                                    condition))
    db.commit()
    db.close()


def mod_ver(price):
    db = pymysql.connect(server, user, password, database)
    with db.cursor() as cursor:
        query = '''SELECT Claim.id, Claim.Text, Claim.Status, Product.Denomination, Product.Code, Product.Price
                FROM Claim
                INNER JOIN Product ON Claim.Code = Product.Code
                HAVING Product.Price > {}'''
        cursor.execute(query.format(price))
        items = cursor.fetchall()
    db.commit()
    db.close()
    return items

#add('Product', ['Denomination', 'Code', 'ManufacturerID', 'Price'], ['Sofa', 'HGT1263', '4', '120000'])
#add('Product', ['Denomination', 'Code', 'ManufacturerID', 'Price'], ['Стул без спинки', 'OPR1263', '4', '100000'])
#add('Claim', ['Text', 'Code', 'Declarant'], ['This is the worst sofa in the world!', 'HGT1263', 'Mark Mc.Loden'])
#add('Claim', ['Text', 'Code', 'Declarant'], ['I found a pie in my sofa?!', 'HGT1263', 'Kirill Avrorov'])
#add('Claim', ['Text', 'Code', 'Declarant'], ['Can i return it?!', 'OPR1263', 'Mitya Jorin'])

#delete('Product', 'all')

#look('Claim')
#look('Product')

