from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my web application!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        message = f"Hello, {name}! Thanks for submitting the form."
        return render_template('response.html', message=message)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
