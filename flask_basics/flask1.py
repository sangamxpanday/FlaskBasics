from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jinja2')
def jinja2():
    user = {'username': 'Sangam', 'age': 21}
    items = ['Flask', 'Django', 'Python']
    return render_template('jinja2.html', user=user, items=items)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('q', '')
        return f'Searching for: {query}'
    return render_template('search.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        name = request.form['name']
        email = request.form['email']
        return render_template('submit.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)