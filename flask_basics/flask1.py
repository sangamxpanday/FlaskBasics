from flask import Flask, render_template, redirect, url_for, abort
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
    
#Redirecting to another page
@app.route('/redirect')
def redirect_example():
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    abort(403)  # Forbidden

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

if __name__ == '__main__':
    app.run(debug=True)