from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.usuario import Usuario
from flask_app.models.pronostico import Pronostico

#Importar el modulo Bcrypt
from flask_bcrypt import Bcrypt
#Llamar a Bcrypt app
bcrypt = Bcrypt(app)
from flask_mail import Message
from flask_mail import Mail
#llamar a Mail app
mail = Mail(app)

@app.route("/")
def index():
    return render_template("login.html")

# #Ruta para crear un nuevo usuario
@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    if request.form['clave'] != request.form['conf_clave']:
        flash("Contraseñas no coinciden", "register")
        return redirect('/')

    if not Usuario.validar_email(request.form):
        return redirect('/')
    data ={ 
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "correo": request.form['correo'],
        "dni": request.form['dni'],
        "celular": request.form['celular'],
        "codigo": request.form['codigo'],
        "terminos": request.form['terminos'],
        "recuperarpsw": request.form['recuperarpsw'],
        "conf_clave": request.form['conf_clave'],
        "clave": bcrypt.generate_password_hash(request.form['clave'])
        
    }
    id = Usuario.save(data)
    session['user_id'] = id
    return redirect('/')

@app.route("/login", methods=['POST'])
def login():
    # ver si el email de usuario proporcionado existe en la base de datos
    usuario = Usuario.get_by_email(request.form)
    # usuario no está registrado en la base de datos
    if not usuario:
        flash("Correo o Contraseña incorrectas", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.clave, request.form['clave']):
        # si obtenemos False después de verificar la contraseña
        flash("Correo o Contraseña incorrectas", "login")
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['user_id'] = usuario.id_usuario
    session['perfil'] = usuario.perfiles_id_perfil
    session['recuperar_psw'] = usuario.recuperarpsw

    if usuario.perfiles_id_perfil == 1:
        return redirect("/dashboard_admin")

    return redirect("/dashboard")
#* Usuario
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session or session['perfil'] != 2 or session['recuperar_psw'] != 0:
        return redirect('/logout')
    data ={
        'id_usuario': session['user_id']
    }
    return render_template("dashboard.html", usuario_ingreso = Usuario.get_one(data))

#* Admin
@app.route("/dashboard_admin")
def dashboard_admin():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    data ={
        'id_usuario': session['user_id']
    }
    return render_template("dashboardadmin.html", usuario_ingreso = Usuario.get_one(data))

#* Usuario
@app.route("/crear_pronostico", methods=['POST'])
def crear_pronostico():
    if 'user_id' not in session or session['perfil'] != 2 or session['recuperar_psw'] != 0:
        return redirect('/logout')
    Pronostico.save(request.form)
    flash("Pronóstico guardado exitosamente, esperamos que seas el ganador!!! Participa otra vez para que tengas más oportunidades de ganar", "pronostico")
    return redirect("/dashboard")
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#* Usuario
@app.route("/calendario")
def calendario():
    if 'user_id' not in session or session['perfil'] != 2 or session['recuperar_psw'] != 0:
        return redirect('/logout')
    data ={
        'id_usuario': session['user_id']
    }
    return render_template("calendario.html",usuario_ingreso = Usuario.get_one(data))

#* Usuario
@app.route("/reglamento")
def reglamento():
    if 'user_id' not in session or session['perfil'] != 2 or session['recuperar_psw'] != 0:
        return redirect('/logout')
    data ={
        'id_usuario': session['user_id']
    }
    return render_template("reglamento.html",usuario_ingreso = Usuario.get_one(data))

#* Admin
@app.route("/ver_usuarios")
def ver_usuarios():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    return render_template("ver_usuarios.html", usuarios = Usuario.join_prono_usu())

#* Usuario
@app.route("/enviar_email", methods=['POST'])
def enviar_email():
    usuario = Usuario.get_by_email_omc(request.form)
    if usuario:
        msg = Message("Ayuda para recuperar la contraseña",
                sender='bettergol593@gmail.com',
                recipients=[request.form['correoomc']])
        msg.body = 'Siga las instrucciones para recuperar su contraseña'
        msg.html = '<p>Siga las instrucciones para recuperar su contraseña</p> <br> <a href="http://localhost:5000/recuperar_contraseña">Ingrese a este link para recuperar su contraseña</a>'
        data = {
            'id' : usuario.id_usuario
        }
        data1= {
            'id_usuario' : usuario.id_usuario
        }
        Usuario.update_campo_1(data)
        usu = Usuario.get_by_id(data1)
        session['user_id'] = usu.id_usuario
        session['recuperar_psw'] = usu.recuperarpsw
        session['perfil'] = usu.perfiles_id_perfil
        print('SESION USER ID', session['user_id'])
        print('SESION RECUPERAR PSW', session['recuperar_psw'])
        print('SESION PERFIL', session['perfil'])
        mail.send(msg)
        flash("Correo enviado, revise su email por favor", "enviocorreo")
        #! poner flash de corre enviado, revise su email y siga las instrucciones
    else:
        flash("Correo no registrado", "enviocorreo2")
        #! poner un flash de correo no existente
    return redirect("/")

#* Usuario
@app.route("/recuperar_contraseña")
def recuperar_psw():
    if 'user_id' not in session or session['recuperar_psw'] != 1:
        return redirect('/logout')
    return render_template("recuperar_contraseña.html")

#* Usuario
@app.route("/actualizar_contraseña", methods=['POST'])
def actualizar_psw():
    if 'user_id' not in session or session['recuperar_psw'] != 1:
        return redirect('/logout')

    if request.form['nuevo_psw'] != request.form['conf_nuevo_psw']:
        flash("Contraseñas no coinciden", "cambioclave")
        return redirect('/recuperar_contraseña')
    data = {
            'id' : session['user_id']
        }
    data1 = {
        'id' : session['user_id'],
        'nuevo_psw' : bcrypt.generate_password_hash(request.form['nuevo_psw'])
    }
    Usuario.update_contraseña(data1)
    Usuario.update_campo_0(data)
    flash("Cambio de contraseña exitoso,", "cambioclave")
    return redirect("/logout")
    