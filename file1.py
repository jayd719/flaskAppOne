from flask import Flask, render_template, request
from json import dump
app = Flask(__name__)

@app.route('/')
def index():
    data =[1,2]
    return  render_template("homepage.html",data=data)

@app.route('/home1')
def matchOne():
    return render_template("page2.html")

@app.route('/couponCode')
def couponCode():
    return render_template("components/couponCode.html")


@app.route('/cart')
def viewCart():
    return render_template ("cart.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000,debug=True)