from flask import Flask, render_template
from flask import request, redirect
from calculadora import calculadora
import this

app = Flask(__name__)#Referência ao objeto Flask, criando uma variável APP que guarda os elementos do Flask
calc = calculadora()#referência a classe calculadora
this.resultadoFinal = ""

@app.route("/")#Pagina Index - Primeir página de quaquer site
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.somar(numero1,numero2)
    return render_template("soma.html", titulo="Soma", resultado=this.resultadoFinal)

@app.route("/subtracao", methods=['POST', 'GET'])
def subt():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.subtrair(numero1,numero2)
    return render_template("subtracao.html", titulo="Subtrair", resultado=this.resultadoFinal)

@app.route("/multiplicacao", methods=['POST', 'GET'])
def multi():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.multiplicar(numero1,numero2)
    return render_template("multiplicacao.html", titulo="Multiplicação", resultado=this.resultadoFinal)

@app.route("/tabuada", methods=['POST', 'GET'])
def tabu():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.tabuada(numero1,numero2)
    return render_template("tabuada.html", titulo="Tabuada", resultado=this.resultadoFinal)

@app.route("/raiz", methods=['POST', 'GET'])
def raz():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.raiz(numero1,numero2)
    return render_template("raiz.html", titulo="Raiz", resultado=this.resultadoFinal)

@app.route("/potencia", methods=['POST', 'GET'])
def pont():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.potencia(numero1,numero2)
    return render_template("potencia.html", titulo="Potência", resultado=this.resultadoFinal)

@app.route("/divisao", methods=['POST', 'GET'])
def divi():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.dividir(numero1,numero2)
    return render_template("divisao.html", titulo="Dividir", resultado=this.resultadoFinal)





        
        
if __name__ == '__main__':
    app.run(debug=True)