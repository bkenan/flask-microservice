from flask import Flask, render_template
application = Flask(__name__)

# two decorators, same function
@application.route('/')
@application.route('/index.html')
def index():
    return render_template('index.html', the_title='My Portfolio Website')

@application.route('/data-science.html')
def ds():
    return render_template('data_science.html', the_title='Data Science')

@application.route('/web-development.html')
def wd():
    return render_template('web_development.html', the_title='Web Development')

if __name__ == '__main__':
    application.debug = True
    application.run()