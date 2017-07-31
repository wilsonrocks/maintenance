import flask

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "I love Shelley"
from maintain import views
from maintain import models

database = models.db

@app.before_request
def db_connect():
    models.db.get_conn()

@app.after_request
def db_disconnect(response):
    if not database.is_closed():
        models.db.close()
    return response #because response could be modified and this is what does it?


@app.route("/TEST")
def test():
    return "WHAAAAAAAAAAAAAAAAT"

if __name__ == "__main__":

    app.run(host="192.168.1.32", debug=True)
