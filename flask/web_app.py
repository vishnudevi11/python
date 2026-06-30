from flask import Flask,render_template

# created obj
app = Flask(__name__) #create a flask web app
# url
@app.route('/')
def hello_world():
    return render_template('index.html')  #Load the html file
@app.route('/about')
def about():
    return render_template('about.html')  #Load the html file

if(__name__=='__main__'):
    app.run(debug=True)