from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='My Portfolio Website')

@app.route('/ds.html')
def myth():
    return render_template('web_dev.html', the_title='Data Science')

@app.route('/web_dev.html')
def symbol():
    return render_template('ds.html', the_title='Web Development')


if __name__ == '__main__':
    app.run(debug=True)
