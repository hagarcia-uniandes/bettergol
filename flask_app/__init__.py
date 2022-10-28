from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.secret_key = "shhhhhh"


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bettergol593@gmail.com'
app.config['MAIL_PASSWORD'] = 'naemyihtbazfwfau'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False

#Prueba gitignore
