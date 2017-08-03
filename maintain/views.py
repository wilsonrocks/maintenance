from flask import render_template, redirect, request, url_for, flash

from maintain import app
from maintain.models import Job, Room, Category, jobs_count
from maintain.forms import CreateForm


@app.route("/")
def root():
    return redirect("/todo")

@app.route("/shopping")
def shopping():
    procure = Category.get(name="Procure")
    to_buy = (Job
        .select()
        .join(Room)
        .switch(Job)
        .join(Category)
        .where((Job.completed == None) & (Job.category == procure))
        .order_by(Room.name, Job.created))

    return render_template('grouped.html', jobs=to_buy, title='Shopping List', count=jobs_count())


@app.route("/todo")
def todo():
    to_do = (Job
        .select()
        .join(Room)
        .switch(Job)
        .join(Category)
        .where(Job.completed == None)
        .order_by(Room.name,
            Category.name,
            Job.created))

    return render_template('grouped.html', jobs=to_do, categories=Category.select(),title='To Do List',count=jobs_count())

@app.route("/complete/<id>")
def complete(id):
    job = Job.get(Job.id==id)
    job.complete()
    flash("Well done! Completed job #{}: {}".format(job.id,job.info))

    return redirect("/todo")

@app.route("/delete/<id>")
def delete(id):
    job = Job.get(Job.id==id)
    job.delete_instance()

    return "Deleted job #{}: {}".format(job.id,job.info)

@app.route("/create", methods=['GET', 'POST'])
def create():
    form = CreateForm()
    #set up choices for the SelectFields by querying the database
    form.room.choices = [(i.id, i.name) for i in Room.select()]
    form.category.choices = [(i.id, i.name) for i in Category.select()]

    if request.method == 'POST' and form.validate():
        room = Room.get(id=form.room.data)
        category = Category.get(id=form.category.data)
        new_job = Job.create(info=form.info.data,room=room,category=category)
        flash("Created {} Job {}:\n{} in {}".format(new_job.category.name,
            new_job.id,
            new_job.info,
            new_job.room.name))
        return redirect(url_for('todo'))

    return render_template('create.html', form=form)
