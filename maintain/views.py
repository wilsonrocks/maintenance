from flask import render_template

from maintain import app
from maintain import models

@app.route("/")
def root():
    return("Root of the App...")

@app.route("/all")
def all_tasks():
    return render_template("grouped.html",
            jobs=models.Job.select(),
            categories=models.Category.select())
