from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi/<int:cannang>/<int:chieucao>')
def bmi(cannang , chieucao):
    s = cannang / (chieucao/100 * chieucao/100)
    return str(s)

if __name__ == '__main__':
  app.run( debug=True)
