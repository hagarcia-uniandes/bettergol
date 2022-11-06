from flask import render_template,redirect,request,session,flash

from flask_app import app
from flask_app.models.pronostico import Pronostico
from flask_app.models.usuario import Usuario

#JSON
import json
import requests
#Time
import time


#* Admin
@app.route("/codigo")
def codigo():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    return render_template("codigo.html")

#* Admin
@app.route("/crear_codigo", methods=['POST'])
def crear_codigo():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    data ={ 
        "id_codigo": request.form['id_codigo'],
        "Nombre": request.form['Nombre'],
    }
    Pronostico.savecod(data)
    return redirect('/codigo')


#* Admin
@app.route("/actualizacion")
def actualizacion():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    return render_template("actualizacion.html",editar = Pronostico.obtener_pronostico_admin())

#* Admin
@app.route("/guardar_vacio")
def guardar_vacio():
    data = {
        'id_usuario' : session['user_id']
    }
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    Pronostico.save_vacio(data)
    return redirect("/actualizacion")

#* Admin
@app.route('/actualizar',methods=['POST'])
def actualizar():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    Pronostico.actualizar(request.form)
    return redirect('/contador')

#* Admin
@app.route("/contador")
def contador():
    if 'user_id' not in session or session['perfil'] != 1:
        return redirect('/logout')
    pronostico_real = Pronostico.obtener_resultado_real()
    pronostico_usuario = Pronostico.obtener_resultado_usuario()
    puntaje = []
    lista = []
    for x in pronostico_real:
    
        for y in pronostico_usuario:
            cont = 0
            if x.a1 == y.a1:
                cont += 1
            if x.b2 == y.b2:
                cont += 1
            if x.c1 == y.c1:
                cont += 1
            if x.d2 == y.d2:
                cont += 1
            if x.e1 == y.e1:
                cont += 1
            if x.f2 == y.f2:
                cont += 1
            if x.g1 == y.g1:
                cont += 1
            if x.h2 == y.h2:
                cont += 1
            if x.a2 == y.a2:
                cont += 1
            if x.b1 == y.b1:
                cont += 1
            if x.c2 == y.c2:
                cont += 1
            if x.d1 == y.d1:
                cont += 1
            if x.e2 == y.e2:
                cont += 1
            if x.f1 == y.f1:
                cont += 1
            if x.g2 == y.g2:
                cont += 1
            if x.h1 == y.h1:
                cont += 1
            if x.a1b2 == y.a1b2:
                cont += 1
            if x.c1d2 == y.c1d2:
                cont += 1
            if x.e1f2 == y.e1f2:
                cont += 1
            if x.g1h2 == y.g1h2:
                cont += 1
            if x.a2b1 == y.a2b1:
                cont += 1
            if x.c2d1 == y.c2d1:
                cont += 1
            if x.e2f1 == y.e2f1:
                cont += 1
            if x.g2h1 == y.g2h1:
                cont += 1                
            if x.o1o2 == y.o1o2:
                cont += 1                
            if x.o3o4 == y.o3o4:
                cont += 1                
            if x.o5o6 == y.o5o6:
                cont += 1                
            if x.o7o8 == y.o7o8:
                cont += 1    
            if x.semi1 == y.semi1:
                cont += 1                             
            if x.semi2 == y.semi2:
                cont += 1                             
            if x.ps1ps2 == y.ps1ps2:
                cont += 1                             
            if x.final == y.final:
                cont += 1                             
            if x.segundo == y.segundo:
                cont += 1 
            if x.cuarto == y.cuarto:
                cont += 1                 
            puntaje.append(cont)
            lista.append(y.id_pronostico)
            data = {
                'puntos' : cont,
                'id_pronostico' : y.id_pronostico
            }
            Pronostico.update_puntaje(data)
    return redirect("/actualizacion") 

#* USUARIO
@app.route('/predicciones')
def predicciones():
    if 'user_id' not in session or session['perfil'] != 2 or session['recuperar_psw'] != 0:
        return redirect('/logout')
    pronostico_real = Pronostico.obtener_resultado_real()
    pronostico_usuario = Pronostico.obtener_resultado_usuario()
    data = {
        'id_usuario' : session['user_id']
    }
    return render_template("predicciones.html", pronostico_real = pronostico_real, pronostico_usuario = pronostico_usuario, usuario_ingreso = Usuario.get_one(data))

#*Respuesta para payphone
@app.route('/respuesta/')
def respuesta():
    if 'user_id' not in session or session['perfil'] != 2 or session['recuperar_psw'] != 0:
        return redirect('/logout')
    url = request.url
    transaccion = request.args.get("id")
    client = request.args.get("clientTransactionId")

    # JSON de la llamada
    data = {
        "id" : transaccion,
        "clientTxId" : client,
    }
    print('QUE ES LA DATA', data)

    # POST con requests
    url = "https://pay.payphonetodoesposible.com/api/button/V2/Confirm"
    headers = {"Authorization" : "bearer fa1hu88qg0A9QHzEZuMWfMs7wj4LDkMM91PxAFkzaehpoQ1ldJNCEsMvzMVXDaDYt_flUFPeY_nYXE-IG0Z0bldEY5ghhnrivaQkStNBsJQLoJrWJZoVUyic8-W7DEbDXy75ilvCVyuUad3WiKQXmGE3QozBiDbLOBxZB7wTPBYLdJ3YtYo2t-mTaOR5vpGAtE0Sy_eFhggT_jlXgcilnxuvTbYPmfKMBYK-ai4-yuneMgnxvjCmBUCYyr2Yf1991ddWcRxNBqRTMDCEa1YXZmpz27gHUZtwIY_iE6qyAZFFxClcrihdOvje27xNZWH2Muiqog", "Content-Type" : "application/json"}
    result = requests.post(url, headers = headers, json = data)
    time.sleep(300)
    return redirect("/dashboard")