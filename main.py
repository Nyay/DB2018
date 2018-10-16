from flask import render_template, request, Flask
from test import add_data, add_data_file, get_spare, get_workers
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def hello():
    with sql.connect('sis.db') as con:
        cur = con.cursor()
        spare = get_spare(cur)
        workers = get_workers(cur)
    return render_template('welcome.html', workers=workers, spare=spare)


@app.route('/new_belong')
def set_belong():
    with sql.connect('sis.db') as con:
        cur = con.cursor()
        add_data(cur,
                 [request.args['equipment'],
                  request.args['worker']],
                 'belong')
        spare = get_spare(cur)
        workers = get_workers(cur)

    return render_template('welcome.html', workers=workers, spare=spare)


@app.route('/new_worker')
def new_worker():
    with sql.connect('sis.db') as con:
        cur = con.cursor()
        add_data(cur,
                 request.args['new_worker'],
                 'worker')
        spare = get_spare(cur)
        workers = get_workers(cur)
    return render_template('welcome.html', workers=workers, spare=spare)


@app.route('/new_spare')
def new_spare():
    with sql.connect('sis.db') as con:
        cur = con.cursor()
        spare = get_spare(cur)
        workers = get_workers(cur)
        add_data(cur,
                 request.args['new_spare'],
                 'equipment')
    return render_template('welcome.html', workers=workers, spare=spare)


if __name__ == '__main__':
    app.run()
