from flask import render_template, request, redirect, session
from _app.models.receta import Receta
from _app.models.usuario import Usuario
from _app import app
from flask import flash

from  flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard")
def result():
    if 'idUsuario' in session:
         data = {"id": int(session['idUsuario'])}
    else:
        return redirect('/')

    usuario = Usuario.get_usuario(data)
    recetas = Receta.all_receta()
    idUsuario = int(session['idUsuario'])
    return render_template('dashboard.html', usuario = usuario, all_recetas = recetas, idUsuario = idUsuario )

@app.route('/create_usuario', methods=["POST"])
def usuarioNew():
    if not Usuario.validate_user(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pwd
    }

    id = Usuario.save(data)

    session['idUsuario'] = id

    return redirect('/dashboard')

@app.route('/ingresar_usuario', methods=["POST"])
def usuarioShow():
    if not Usuario.validate_user_login(request.form):
        return redirect('/')

    usuario = Usuario.search_email(request.form)

    if not usuario:
        flash("Email don't exists!", 'login')
        return redirect('/')
 
    if not bcrypt.check_password_hash(usuario["password"],request.form["password"]):
        flash("Wrong Password", 'login')
        return redirect('/')

    session['idUsuario'] = usuario["id"]
    return redirect('/dashboard')

@app.route("/recipes/new")
def pagerecipes():
    if 'idUsuario' in session:
         data = {"id": int(session['idUsuario'])}
    else:
        return redirect('/')
    usuario = Usuario.get_usuario(data)
    return render_template('recipes.html', usuario = usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
