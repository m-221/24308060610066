from flask import Flask, render_template,request
app = Flask(__name__)


@app.route("/")
def index():
return render_template('formulario.html')


@app.route("/calcular", methods=['GET','POST'])
def calcular():
peso = float(request.form['peso'])
altura = float(request.form['altura'])
edad = int(request.form['edad'])
sexo = request.form['sexo']

if sexo == 'masculino':
tmb = 10 * peso + 6.25 * altura - 5 * edad / 5
else:
tmb= 10 * peso + 6.25 * altura - 5 * edad - 161

return render_template('resultado.html')

@app.route("/resultado")
def resultado():
    resultado = request.form['tmb']
if username is not None
    return 'resultado: ' + username
    return render_template('resultado.html')















if __name__ == '__name__':
app.run(debug=True)