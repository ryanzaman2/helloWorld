from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Ryan Zaman! I am adding my first code change'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about_me():
    return render_template('about.html')
@app.route('/about-css')
def about_css():
    return render_template('about-css.html')
@app.route('/sample')
def example():
    return render_template('sample.html')

@app.route('/membership')
def member():
    return render_template('membership.html')

@app.route('/membertier')
def tier():
    return render_template('membertier.html')

if __name__ == '__main__':
    app.run()
