from flask import render_template

from maintain import app
from maintain import models

@app.route("/")
def root():
    return("Root of the App...")

@app.route("/all")
def all():
    return render_template("grouped.html",
            jobs=models.Job.select(),
            categories=models.Category.select())

@app.route("/todo")
def todo():
    return render_template("grouped.html",
            jobs=models.Job.select().where(models.Job.completed == None),
            categories=models.Category.select(),
            title="To Do List")


@app.route("/complete/<id>")
def complete(id):
    job = models.Job.get(models.Job.id==id)
    job.complete()
    return "Completed job #{}: {}".format(job.id,job.info)

@app.route("/delete/<id>")
def delete(id):
    job = models.Job.get(models.Job.id==id)
    job.delete_instance()
    return "Deleted job #{}: {}".format(job.id,job.info)

@app.route("/edit/<id>")
def edit(id):
    return "EDITORY"

@app.route("/create")
def create():
    return "LET'S GET CREATIVE"
