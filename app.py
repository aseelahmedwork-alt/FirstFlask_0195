from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()

        if name and age:
            message = f'Hello, {name}! You are {age} years old.'
        else:
            message = 'Please enter your name and age.'

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
