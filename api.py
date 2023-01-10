from flask import Flask, render_template, jsonify, Response, request,redirect
from sqlalchemy import *
import baza
import pdb

app = Flask(__name__,template_folder='template')
#Prikaz svih nekretnina u bazi.
@app.route('/all', methods=['GET'])
def get_all_items():
  items = []
  for item in baza.session.query(baza.Oglas).all():
    del item.__dict__['_sa_instance_state']
    items.append(item.__dict__)
  return jsonify(items)

#Prikaz svih nekretnina u bazi sa paginaciojm.
@app.route('/all/paginations/<number_of_items>', methods=['GET'])
def get_all_items_paginations(number_of_items):
  items = []
  for item in baza.session.query(baza.Oglas).limit(number_of_items):
    del item.__dict__['_sa_instance_state']
    items.append(item.__dict__)
  return jsonify(items)

#Prikaz nekretnine sa odredjenim ID-jem u bazi.
@app.route('/all/<id>', methods=['GET'])
def get_item(id):
    if baza.session.query(baza.Oglas).filter(baza.Oglas.id==id).first():
        item = baza.session.query(baza.Oglas).filter(baza.Oglas.id==id).first()
        del item.__dict__['_sa_instance_state']
        return jsonify(item.__dict__)
    else:
        return "ID does not exist, please enter a new ID value!"

#Prikaz nekretnina koje imaju ispunjene neki od uslova(Unet odredjeni grad, kvadraturu vecu od unete minimalne,
#kvadraturu manju od unete maksimalne, i da je transakcija(Prodaja/Izdavanje) )
@app.route('/parameters', methods=['GET'])
def query_strings():
    grad = request.args.get('grad',None)
    kvadMin = request.args.get('kvadMin',0.0)
    kvadMax= request.args.get('kvadMax',1000000)
    Tran = request.args.get('Tran', None)
    return '''<h1>{}:{}:{}:{}</h1>''' .format(grad,kvadMin,kvadMax,Tran)



#Kreiranje nove nekretnine i dodavanje iste u bazi.
@app.route('/all/create', methods=['GET', 'POST'])
def createNewItem():
    if request.method == 'GET':
        return render_template('addData.html')

    if request.method == 'POST':
        transakcija = request.form['transakcija']
        vrsta = request.form['vrsta']
        cenaNek = (float(request.form['cenaNek']))
        kvadratura = (float(request.form['kvadratura']))
        grad = request.form['grad']
        naselje = request.form['naselje']

        if cenaNek<0:
            return "Value cenaNek is negative, please enter a new positive value!"
        elif kvadratura<0:
            return "Value kvadratura is negative, please enter a new positive value!"
        else:
            nova_nekretnina = baza.Oglas(transakcija=transakcija, vrsta=vrsta,cenaNek=cenaNek,kvadratura=kvadratura,grad=grad,naselje=naselje)
            baza.session.add(nova_nekretnina)
            baza.session.commit()
            return "Data added!"



#Promena podataka nekretnine sa odredjenim ID-jem u bazi.
@app.route('/all/update/<id>', methods=['GET', 'POST'])
def updateData(id):
    if request.method == 'GET':
        return render_template('updateData.html')

    if request.method == 'POST':

        nekretnina_koja_se_menja = baza.session.query(baza.Oglas).filter(baza.Oglas.id ==int(id)).first()
        nekretnina_koja_se_menja.transakcija = request.form['transakcija']
        nekretnina_koja_se_menja.vrsta=request.form['vrsta']
        nekretnina_koja_se_menja.cenaNek=request.form['cenaNek']
        nekretnina_koja_se_menja.kvadratura=request.form['kvadratura']
        nekretnina_koja_se_menja.grad=request.form['grad']
        nekretnina_koja_se_menja.naselje=request.form['naselje']
        baza.session.commit()
        return "Data updated!"

app.run()
