from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('HomePage.html')

@app.route('/draw')
def draw():
    return render_template('draw.html')


@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/manga')
def manga():
    return render_template('manga.html')


@app.route('/figures')
def figures():
    return render_template('figures.html')

@app.route('/tv')
def tv():
    return render_template('tv.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/suggest')
def suggest():
    return render_template('suggest.html')


@app.route('/thank', methods=['GET', 'POST'])
def thank():
    return render_template('thank.html')

if __name__ == "__main__":
    app.run(debug=True)
