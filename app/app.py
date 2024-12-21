from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("proyect/index1.html")
    
@app.route('/corazon')
def corazon():
    return render_template("proyect/corazon.html")

if __name__ == '__main__':
    app.run(debug=True)