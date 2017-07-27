import flask

import models

database = models.db

app = flask.Flask(__name__)


@app.before_request
def db_connect():
    models.db.get_conn()

@app.after_request
def db_disconnect(response):
    if not database.is_closed():
        models.db.close()
    return response #because response could be modified and this is what does it?



@app.route("/")
def root():
    return("Root of the App...")

@app.route("/all")
def all_tasks():
    answer = ""
    for m in models.Job.select():
        answer += "\n" + str(m)

    return answer


app.run(host="192.168.1.32", debug=True)


