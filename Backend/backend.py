from config import *
from models import Telefone

@app.route("/")
def listar_telefones():
    telefones = db.session.query(Telefone).all()
    telefone_json = [x.json() for x in telefones]
    lista__JS = jsonify(telefone_json)
    lista__JS.headers.add("Access-Control-Allow-Origin", "*")
    return lista__JS

app.run(debug=True)