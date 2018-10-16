from flask import render_template, request, Flask
app = Flask(__name__)


@app.route('/')
def hello():

    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()