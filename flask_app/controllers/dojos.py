# routes
from flask_app import app 
from flask_app.model.dojo import Dojo 
from flask import render_template, request, session, redirect


@app.route('/dojo/<int:dojos_id>')
def index(dojos_id):
    data = {"id":dojos_id}
    dojos = Dojo.get_all_ninjas(data)
    print(dojos)
    return render_template("show_dojo.html", all_dojos = dojos)

@app.route('/dojo',methods=['POST'])
def Add_dojo():
    data={
        "name": request.form["name"]
        # "created_at": request.form["created_at"],
        # "updated_at": request.form["updated_at"],
        # "created_at": request.form["created_at"],
        # "actions": request.form["actions"]
    }
    print(request.form)
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojos.html", dojos=Dojo.get_all())