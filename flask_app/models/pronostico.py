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
class Pronostico:
    db_name = "bettergol"

    def __init__( self , db_data ):
        self.id_pronostico = db_data['id_pronostico']
        self.usuarios_id_usuario = db_data['usuarios_id_usuario']
        self.a1 = db_data['A1']
        self.b2 = db_data['B2']
        self.c1 = db_data['C1']
        self.d2 = db_data['D2']
        self.e1 = db_data['E1']
        self.f2 = db_data['F2']
        self.g1 = db_data['G1']
        self.h2 = db_data['H2']
        self.a2 = db_data['A2']
        self.b1 = db_data['B1']
        self.c2 = db_data['C2']
        self.d1 = db_data['D1']
        self.e2 = db_data['E2']
        self.f1 = db_data['F1']
        self.g2 = db_data['G2']
        self.h1 = db_data['H1']
        self.a1b2 = db_data['A1B2']
        self.c1d2 = db_data['C1D2']
        self.e1f2 = db_data['E1F2']
        self.g1h2 = db_data['G1H2']
        self.a2b1 = db_data['A2B1']
        self.c2d1 = db_data['C2D1']
        self.e2f1 = db_data['E2F1']
        self.g2h1 = db_data['G2H1']
        self.o1o2 = db_data['O1O2']
        self.o3o4 = db_data['O3O4']
        self.o5o6 = db_data['O5O6']
        self.o7o8 = db_data['O7O8']
        self.semi1 = db_data['SEMI1']
        self.semi2 = db_data['SEMI2']
        self.ps1ps2 = db_data['PS1PS2']
        self.final = db_data['final']
        self.cuarto = db_data['cuarto']
        self.segundo = db_data['segundo']
        self.puntos = db_data['puntos']
        
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        

# ahora usamos métodos de clase para consultar nuestra base de datos

#METODOS PARA VALIDACION Y GUARDADO DE FORMULARIO
    def desplegar(self, objeto):
        print(objeto.__dict__)
#Metodo para crear un nuevo usuario y guardarlo en nuestra base de datos
    @classmethod
    def save(cls,data):
        query = "INSERT INTO pronosticos (usuarios_id_usuario, A1, B2, C1, D2, E1, F2, G1, H2, A2, B1, C2, D1, E2, F1, G2, H1, A1B2, C1D2, E1F2, G1H2, A2B1, C2D1, E2F1, G2H1, O1O2, O3O4, O5O6, O7O8, SEMI1, SEMI2, PS1PS2, final, cuarto, segundo) VALUES(%(id_usuario)s, %(A1)s, %(B2)s, %(C1)s, %(D2)s, %(E1)s, %(F2)s, %(G1)s, %(H2)s, %(A2)s, %(B1)s, %(C2)s, %(D1)s, %(E2)s, %(F1)s, %(G2)s, %(H1)s, %(A1B2)s, %(C1D2)s, %(E1F2)s, %(G1H2)s, %(A2B1)s, %(C2D1)s, %(E2F1)s, %(G2H1)s, %(O1O2)s, %(O3O4)s, %(O5O6)s, %(O7O8)s, %(SEMI1)s, %(SEMI2)s, %(PS1PS2)s, %(final)s, %(hcuarto)s, %(hsegundo)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

#Metodo para crear un nuevo codigo
    @classmethod
    def savecod(cls,data):
        query = "INSERT INTO codigos (id_codigo, Nombre) VALUES(%(id_codigo)s, %(Nombre)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)


    #!Metodo para guardar un vacio
    @classmethod
    def save_vacio(cls,data):
        query = "INSERT INTO pronosticos (usuarios_id_usuario) VALUES(%(id_usuario)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    #Metodo para obtener todos los datos de tabla y guardarlos en una lista
    @classmethod
    def obtener_resultado_real(cls):
        query = "SELECT * FROM pronosticos WHERE id_pronostico = 1;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print("QUE ES EL RESULTADO DE ESTA QUERY", results)
        pronostico_real = []
        for pronostico in results:
            pronostico_real.append( cls(pronostico))
        return pronostico_real
    
    @classmethod
    def obtener_pronostico_admin(cls):
        query = "SELECT * FROM pronosticos WHERE id_pronostico = 1;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return cls(results[0])
        

    @classmethod
    def obtener_resultado_usuario(cls):
        query = "SELECT * FROM pronosticos WHERE id_pronostico != 1;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print("QUE ES EL RESULTADO DE ESTA QUERY", results)
        pronostico_usuario = []
        for pronostico in results:
            pronostico_usuario.append( cls(pronostico))
        return pronostico_usuario

    @classmethod
    def update_puntaje(cls,data):
        query = "UPDATE pronosticos SET puntos = %(puntos)s WHERE id_pronostico = %(id_pronostico)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print("QUE ES EL RESULTADO DE ESTA QUERY", results)
        return results

    @classmethod
    def actualizar(cls, data):
        query = "UPDATE pronosticos SET A1=%(a1)s,B2=%(b2)s,C1=%(c1)s,D2=%(d2)s,E1=%(e1)s,F2=%(f2)s,G1=%(g1)s,H2=%(h2)s,A2=%(a2)s,B1=%(b1)s,C2=%(c2)s,D1=%(d1)s,E2=%(e2)s,F1=%(f1)s,G2=%(g2)s,H1=%(h1)s,A1B2=%(a1b2)s,C1D2=%(c1d2)s,E1F2=%(e1f2)s,G1H2=%(g1h2)s,A2B1=%(a2b1)s,C2D1=%(c2d1)s,E2F1=%(e2f1)s,G2H1=%(g2h1)s,O1O2=%(o1o2)s,O3O4=%(o3o4)s,O5O6=%(o5o6)s,O7O8=%(o7o8)s,SEMI1=%(semi1)s,SEMI2=%(semi2)s,PS1PS2=%(ps1ps2)s,final=%(final)s,cuarto=%(cuarto)s,segundo=%(segundo)s,updated_at=NOW() WHERE usuarios_id_usuario = 1;"
        return connectToMySQL(cls.db_name).query_db(query,data)



    # #metodo para seleccionar un usuario mediante el id
    # @classmethod
    # def get_one(cls,data):
    #     query  = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s";
    #     result = connectToMySQL(cls.db_name).query_db(query,data)
    #     return cls(result[0])


    # #Metodo para seleccionar el usuario mediante el email
    # @classmethod
    # def get_by_email(cls,data):
    #     query  = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
    #     result = connectToMySQL(cls.db_name).query_db(query,data)
    #     print('RESULTADO DE LA QUERY', result)
    #     if len(result) < 1:
    #         return False
    #     return cls(result[0])

    # def get_by_id(cls,data):
    #     query = "SELECT * FROM usuarios WHERE id_usuario = %(id_usuario)s;"
    #     results = connectToMySQL(cls.db_name).query_db(query,data)
    #     return cls(results[0])

    # #*Metodo para validar el email
    # @staticmethod
    # def validar_email(user):
    #     is_valid = True
    #     query = "SELECT * FROM usuarios WHERE correo = %(correo)s;"
    #     results = connectToMySQL('bettergol').query_db(query,user)
    #     if len(results) >= 1:
    #         flash("Este email ya esta registrado","register")
    #         is_valid=False
    #     if not EMAIL_REGEX.match(user['correo']):
    #         flash("Correo Invalido","register")
    #         is_valid=False
    #     return is_valid