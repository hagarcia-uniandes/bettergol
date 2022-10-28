# importar la función que devolverá una instancia de una conexión
from flask_app.config.mysqlconnection import connectToMySQL
#Importar el modulo regex para la validacion del email
import re
from flask import flash

#Importar el archivo travel para poder hacer las relaciones
#from flask_app.models import travel
# crea un objeto de expresión regular que usaremos más adelante
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# modelar la clase después de la tabla nuestra base de datos
class Usuario:
    db_name = "bettergol"

    def __init__( self , db_data ):
        self.id_usuario = db_data['id_usuario']
        self.nombre = db_data['nombre']
        self.apellido = db_data['apellido']
        self.dni = db_data['dni']
        self.celular = db_data['celular']
        self.correo = db_data['correo']
        self.clave = db_data['clave']
        # self.codigo = db_data['codigo']
        self.terminos = db_data['terminos']
        self.recuperarpsw = db_data['recuperarpsw']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.perfiles_id_perfil = db_data['perfiles_id_perfil']

# ahora usamos métodos de clase para consultar nuestra base de datos

#METODOS PARA VALIDACION Y GUARDADO DE FORMULARIO

#Metodo para crear un nuevo usuario y guardarlo en nuestra base de datos
    @classmethod
    def save(cls,data):
        query = "INSERT INTO usuarios (nombre,apellido,dni,celular,correo,clave,terminos,recuperarpsw,perfiles_id_perfil,codigo) VALUES(%(nombre)s,%(apellido)s,%(dni)s,%(celular)s,%(correo)s,%(clave)s,%(terminos)s,%(recuperarpsw)s,2,%(codigo)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    #Metodo para obtener todos los datos de tabla y guardarlos en una lista
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print("QUE ES EL RESULTADO DE ESTA QUERY", results)
        users = []
        for user in results:
            users.append( cls(user))
        return users

    #metodo para seleccionar un usuario mediante el id
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(result[0])


    #Metodo para seleccionar el usuario mediante el email
    @classmethod
    def get_by_email(cls,data):
        query  = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        print('RESULTADO DE LA QUERY', result)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_email_omc(cls,data):
        query  = "SELECT * FROM usuarios WHERE correo = %(correoomc)s;"
        result = connectToMySQL(cls.db_name).query_db(query,data)
        print('RESULTADO DE LA QUERY', result)
        if len(result) < 1:
            return False
        return cls(result[0])
        
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])

    @classmethod
    def join_prono_usu(cls):
        query = "SELECT * FROM usuarios JOIN pronosticos ON usuarios.id_usuario = pronosticos.usuarios_id_usuario WHERE usuarios.id_usuario != 1;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return results

    #*Metodo para validar el email
    @staticmethod
    def validar_email(user):
        is_valid = True
        query = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
        results = connectToMySQL('bettergol').query_db(query,user)
        if len(results) >= 1:
            flash("El correo que ingreso ya existe, registre otro correo","register")
            is_valid=False
        else:
            flash("Usuario registrado correctamente, ya puede iniciar sesión","ok")
            return is_valid

    @classmethod
    def update_campo_1(cls,data):
        query = "UPDATE usuarios SET recuperarpsw = 1, updated_at=NOW() WHERE id_usuario = %(id)s;"
        return connectToMySQL('bettergol').query_db(query,data)

    @classmethod
    def update_campo_0(cls,data):
        query = "UPDATE usuarios SET recuperarpsw = 0, updated_at=NOW() WHERE id_usuario = %(id)s;"
        return connectToMySQL('bettergol').query_db(query,data)

    @classmethod
    def update_contraseña(cls,data):
        query = "UPDATE usuarios SET clave = %(nuevo_psw)s, updated_at=NOW() WHERE id_usuario = %(id)s;"
        return connectToMySQL('bettergol').query_db(query,data)