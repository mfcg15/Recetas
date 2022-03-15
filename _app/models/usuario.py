from _app.config.connection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios (first_name, last_name, email, password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        idUsuario = connectToMySQL('esquema_recetas').query_db( query, data)
        return idUsuario

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name'])<2:
            flash('First name must be at least 2 characters', 'registro')
            is_valid = False
        if len(data['last_name'])<2:
            flash('Last name must be at least 2 chatacters', 'registro')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email", 'registro')
            is_valid = False
        if  len(data['password'])<8:
            flash('Password must be at least 8 characters', 'registro')
            is_valid = False
        if data['password'] != data['cont_password']:
            flash("Passwords aren't the same", 'registro')
            is_valid = False

        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL('esquema_recetas').query_db(query,data)
        if len(results) >= 1:
            flash('Email already exists!', 'registro')
            is_valid = False

        return is_valid
    
    @staticmethod
    def validate_user_login(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash('Invalid Email', 'login')
            is_valid = False
        if len(data['password'])<8:
            flash('Password must be at least 8 characters', 'login')
            is_valid = False
        return is_valid

    @classmethod
    def search_email(cls, data):
        query = "SELECT * FROM usuarios where email = %(email)s;"
        result = connectToMySQL('esquema_recetas').query_db(query,data)
        if len(result) < 1:
            return False
        else :
            usuario = result[0]
            return usuario

    @classmethod
    def get_usuario (cls, data):
        query = "SELECT * FROM usuarios where id = %(id)s;"
        result = connectToMySQL('esquema_recetas').query_db(query,data)
        usuario = []
        for i in result:
            usuario.append(i)
        return usuario
