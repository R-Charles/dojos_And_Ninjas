# routes
from flask_app import app 
from flask_app.model import ninja, dojo 
from flask import render_template, request, session, redirect

@app.route('/ninja')
def new_ninja():
    dojos = dojo.Dojo.get_all()
    print(dojos)
    return render_template("ninjas.html", all_dojos = dojos)


@app.route('/ninja',methods=['POST'])
def add_ninja():
    data={
        "dojos_id": request.form["dojos_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
        # "updated_at": request.form["updated_at"],
        # "actions": request.form["actions"]
    }
    print(request.form)
    ninja.Ninja.save(data)
    data_id = data['dojos_id']
    return redirect(f'/dojo/{data_id}')

