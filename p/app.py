from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index()->None:
    return render_template("index.html",pagetitle="imagepicker")
    
if __name__=="__main__":
    app.run(debug=True)