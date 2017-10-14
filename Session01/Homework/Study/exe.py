
from flask import Flask, render_template , redirect #import redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/school')
def school():
    return  redirect("http://techkids.vn/") #link trang web , 


if __name__ == '__main__':
  app.run( debug=True)
