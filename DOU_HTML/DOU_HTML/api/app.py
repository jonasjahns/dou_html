from flask import Flask
from flask import jsonify

from DOU_HTML.DOU_HTML.model import licitacao_out
from DOU_HTML.DOU_HTML.service import dou_service

app = Flask(__name__)


@app.route("/v2")
def v2():
    testes = dou_service.find_all("licitacao_v2")
    saida = []
    for teste in testes:
        obj = licitacao_out.LicitacaoOut2(teste.get("titulo"),
                                          teste.get("dados"),
                                          teste.get("pregao"),
                                          teste.get("tipo"),
                                          teste.get("empresa"))
        saida.append(obj)
    return jsonify(saida)


if __name__ == '__main__':
    app.run(debug=True)
