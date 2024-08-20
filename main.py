from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('fname')
        email = request.form.get('lname')
        return f"Form submitted! Name: {name}, Email: {email}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=2999)