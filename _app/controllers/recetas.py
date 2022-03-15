import re
from flask import render_template, request, redirect, session
from _app.models.receta import Receta
from _app.models.usuario import Usuario
from _app import app

@app.route('/create_receta', methods=["POST"])
def recetaNew():
    if 'idUsuario' not in session:
        return redirect('/')

    if not Receta.validate_receta(request.form):
        return redirect('/recipes/new')

    if int(request.form["under"]) == 0:
         estado = False
    else:
         estado = True
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date": request.form["date"],
        "under": estado,
        "usuario_id": int(session['idUsuario'])
    }
    Receta.save(data)
    return redirect('/dashboard')

@app.route("/recipes/edit/<int:id>")
def editrecipe(id):
    if 'idUsuario' in session:
         data = {"id": int(session['idUsuario'])}
    else:
        return redirect('/')

    dataReceta = {"id": id}
    usuario = Usuario.get_usuario(data)
    receta = Receta.get_receta(dataReceta)
    print(receta)
    return render_template('edit.html', usuario = usuario, receta = receta)

@app.route('/edit_receta', methods=["POST"])
def editReceta():
    if 'idUsuario' not in session:
        return redirect('/')

    if not Receta.validate_receta(request.form):
        return redirect(f'/recipes/edit/{request.form["id"]}')
    
    if int(request.form["under"]) == 0:
         estado = False
    else:
         estado = True

    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date": request.form["date"],
        "under": estado
    }

    Receta.update_receta(data)

    return redirect('/dashboard')

@app.route("/recipes/<int:id>")
def showrecipes(id):
    if 'idUsuario' in session:
         data = {"id": int(session['idUsuario'])}
    else:
        return redirect('/')
    usuario = Usuario.get_usuario(data)
    dataReceta = {"id": id}
    receta = Receta.get_receta(dataReceta)
    return render_template('view.html', usuario = usuario, receta = receta)

@app.route("/delete/<int:id>")
def deleReceta(id):
    if 'idUsuario' not in session:
        return redirect('/')
    dataReceta = {"id": id}
    Receta.delete_receta(dataReceta)
    return redirect('/dashboard')