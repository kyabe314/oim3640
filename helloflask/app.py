from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/') # routing
@app.route('/hello/<name>')

def hello(name=None):
    if name:
        # return f'Hello, {name}!'
        return render_template('hello, html', username=name)
    return 'Hello, world!'

# create another route like "/square/<number>" so the web app will display the sqyare of the number
# set FLASK_APP=app
# hyper text markup language
# run the entire code to rerun

@app.route('/square/<number>')
def square(number=None):
    return str(float(number) ** 2)

if __name__ == '__main__':
    app.run(debug=True)