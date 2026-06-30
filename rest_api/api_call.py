from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)
cart=[]

# index.html
@app.route('/')
def index():
    return render_template('index.html',cart=cart)


@app.route('/api/add',methods=['POST'])
def add_to_cart():
    product={
        name:request.form['name'],
    }
    cart.append(product)
    return redirect(url_for('index'))