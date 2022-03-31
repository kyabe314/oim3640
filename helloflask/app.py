from flask import Flask, render_template, request
from temp_helper import get_temp

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

@app.route('/weather/', methods=["GET","POST"])

def show_weather():
    if request.method == "POST":
        city_name = request.form['city']
        temperature = get_temp(city_name)

        return render_template('weather-result.html',
        city=city_name, temp=temperature)
    else:
        return render_template('weather-form.html')


if __name__ == '__main__':
    app.run(debug=True)