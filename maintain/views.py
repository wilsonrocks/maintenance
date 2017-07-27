from maintain import app

from maintain import models


@app.route("/")
def root():
    return("Root of the App...")

@app.route("/all")
def all_tasks():
    answer = ""
    for m in models.Job.select():
        answer += "\n" + str(m)

    return answer

