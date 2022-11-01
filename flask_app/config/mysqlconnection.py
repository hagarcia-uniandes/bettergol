from tokenize import Name
import pymysql.cursors
import boto3
ssm_client = boto3.client('ssm', region_name='myregion')
#endpoint
miendpoint = ssm_client.get_parameter(Name='endpoint')
valor_miendpoint = miendpoint['Parameter']['Value']
#user
miuser = ssm_client.get_parameter(Name='user')
valor_miuser = miuser['Parameter']['Value']
#endpoint
mipsw = ssm_client.get_parameter(Name='password')
valor_mipassword = mipsw['Parameter']['Value']


# esta clase nos dará una instancia de una conexión a nuestra base de datos
class MySQLConnection:
    def __init__(self, db):
        # cambiar el usuario y la contraseña según sea necesario
        connection = pymysql.connect(host = valor_miendpoint,#Endpoint
                                    user = valor_miuser, #User
                                    password = valor_mipassword, #Password
                                    db = db,#bettergol
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establecer la conexión a la base de datos
        self.connection = connection
    # el método para consultar la base de datos
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = self.connection.cursor().mogrify(query, data)
                print("Running Query:", query)

                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # las consultas INSERT devolverán el NÚMERO DE ID de la fila insertada
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # las consultas SELECT devolverán los datos de la base de datos como una LISTA DE DICCIONARIOS
                    result = cursor.fetchall()
                    return result
                else:
                    # las consultas UPDATE y DELETE no devolverán nada
                    self.connection.commit()
            except Exception as e:
                # si la consulta falla, el método devolverá FALSE
                print("ALGO ESTA PASANDO EN LA CONSULTA", e)
                return False
            finally:
                # cerrar la conexión
                self.connection.close() 
# connectToMySQL recibe la base de datos que estamos usando y la usa para crear una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
