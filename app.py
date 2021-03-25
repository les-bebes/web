from flask import Flask, render_template, request
import librairie.offlib as lib 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['name']
  s = lib.search(n)
  return render_template("resultat.html", produits=s)

app.run(debug=True)