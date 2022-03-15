from _app.config.connection import connectToMySQL
from flask import flash

class Receta:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under = data['under']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recetas (name, description, instructions, date, under,usuario_id,created_at,updated_at) VALUES (%(name)s,%(description)s,%(instructions)s,%(date)s,%(under)s,%(usuario_id)s,NOW(),NOW());"
        return connectToMySQL('esquema_recetas').query_db( query, data)
    

    @staticmethod
    def validate_receta(data):
        is_valid = True
        if  len(data['name']) < 3:
            flash('Name must be at least 3 characters', 'receta')
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters", 'receta')
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters", 'receta')
            is_valid = False
        if data['date'] == '':
            flash("Must enter a date", 'receta')
            is_valid = False
        if data['under'] == '2':
            flash("Must choose an option", 'receta')
            is_valid = False

        return is_valid
    
    @classmethod
    def all_receta (cls):
        query = "SELECT id,name,under, usuario_id FROM recetas;"
        result = connectToMySQL('esquema_recetas').query_db(query)
        recetas = []
        for receta in result:
            recetas.append(receta)
        return recetas

    @classmethod
    def get_receta (cls, data):
        query = "SELECT * FROM recetas where id = %(id)s;"
        result = connectToMySQL('esquema_recetas').query_db(query,data)
        receta = []
        for i in result:
            receta.append(i)
        return receta
    
    @classmethod
    def update_receta(cls,data):
        query = "UPDATE recetas SET name = %(name)s , description = %(description)s, instructions = %(instructions)s, date = %(date)s, under = %(under)s, updated_at = NOW() where id =  %(id)s;"
        return connectToMySQL('esquema_recetas').query_db(query,data)
    
    @classmethod
    def delete_receta(cls,data):
        query = "DELETE FROM recetas where id =  %(id)s;"
        return connectToMySQL('esquema_recetas').query_db(query,data)