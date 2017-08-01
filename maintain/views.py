from flask import render_template, redirect, request, url_for, flash

from maintain import app
from maintain import models
from maintain.forms import CreateForm

@app.route("/")
def root():
    return redirect("/todo")

@app.route("/all")
def all():
    return render_template("grouped.html",
            jobs=models.Job.select(),
            categories=models.Category.select())

@app.route("/todo")
def todo():
    to_do = (models.Job
    .select()
    .join(models.Room)
    .switch(models.Job)
    .join(models.Category)
    .where(models.Job.completed == None)
    .order_by(models.Room.name,
        models.Category.name,
        models.Job.created))
            

    return render_template('grouped.html', jobs=to_do, categories=models.Category.select(),title='To Do List')

    return render_template("grouped.html",
            jobs=models.Job.select().where(models.Job.completed == None),
            categories=models.Category.select(),
            title="To Do List")



@app.route("/complete/<id>")
def complete(id):
    job = models.Job.get(models.Job.id==id)
    job.complete()

    flash("Well done! Completed job #{}: {}".format(job.id,job.info))

    return redirect("/todo")

@app.route("/delete/<id>")
def delete(id):
    job = models.Job.get(models.Job.id==id)
    job.delete_instance()
    return "Deleted job #{}: {}".format(job.id,job.info)

@app.route("/edit/<id>")
def edit(id):
    return "EDITORY"

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    #set up choices for the SelectFields by querying the database
    form.room.choices = [(i.id, i.name) for i in models.Room.select()]
    form.category.choices = [(i.id, i.name) for i in models.Category.select()]

    if request.method == 'POST' and form.validate():
        room = models.Room.get(id=form.room.data)
        category = models.Category.get(id=form.category.data)
        new_job = models.Job.create(info=form.info.data,room=room,category=category)
        flash("Created {} Job {}:\n{} in {}".format(new_job.category.name,
            new_job.id,
            new_job.info,
            new_job.room.name))
        return redirect(url_for('todo'))

    return render_template('create.html', form=form)
