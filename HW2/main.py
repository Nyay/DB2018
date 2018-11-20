from flask import render_template, request, Flask
from search import add, look_something, change_status, delete_by_status, mod_ver
from collections import defaultdict
app = Flask(__name__)


def get_company():
    company_list = defaultdict()
    if look_something('Manufacturer', 'id, Name') != ():
        for el in look_something('Manufacturer', 'id, Name'):
            if el[1] not in company_list:
                company_list[el[1]] = el[0]
    return company_list


def get_code():
    codes_list = []
    if look_something('Product', 'Code') != ():
        for el in look_something('Product', 'Code'):
            if el[0] not in codes_list:
                codes_list.append(el[0])
    return codes_list


def get_status():
    codes_list = []
    if look_something('Claim', '*') != ():
        for el in look_something('Claim', '*'):
            if el not in codes_list:
                codes_list.append(el)
    return codes_list


@app.route('/')
def hello():
    advanced = ()
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)


@app.route('/add_company')
def add_company():
    company = request.args['company']
    email = request.args['email']
    country = request.args['country']
    address = request.args['address']
    add('Manufacturer',
        ['Name', 'Mail', 'Address', 'Сountry'],
        [company, email, address, country])
    advanced = ()
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)


@app.route('/add_claim')
def add_claim():
    Declarant = request.args['Declarant']
    Code = request.args['Code']
    Text = request.args['Text']
    add('Claim',
        ['Declarant', 'Code', 'Text'],
        [Declarant, Code, Text])
    advanced = ()
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)


@app.route('/add_product')
def add_product():
    Denomination = request.args['Denomination']
    Code = request.args['Code']
    Manufacturer = request.args['Manufacturer']
    Price = request.args['Price']
    add('Product',
        ['Denomination', 'Code', 'ManufacturerID', 'Price'],
        [Denomination, Code, Manufacturer, Price])
    advanced = ()
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)


@app.route('/change_status')
def new_status():
    Claim = request.args['Claim']
    Status = request.args['Status']
    change_status('Claim', Claim, Status)
    advanced = ()
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)


@app.route('/delete_claim')
def delete_claim():
    Status = request.args['Status']
    delete_by_status('Claim', Status)
    advanced = ()
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)


@app.route('/ModX')
def mod_x():
    Price = request.args['Price']
    advanced = mod_ver(Price)
    return render_template('welcome.html', company_list=get_company(), codes_list=get_code(), status_list=get_status(),
                           advanced=advanced)

if __name__ == '__main__':
    app.run()
