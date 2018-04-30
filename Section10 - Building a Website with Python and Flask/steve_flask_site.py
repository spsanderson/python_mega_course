from flask import Flask, render_template

app=Flask(__name__)

# Homepage
@app.route('/')
def home():
    #return "Homepate goes here"
    return render_template("home.html")

# About page
@app.route('/about/')
def about():
    #return "About page"
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)