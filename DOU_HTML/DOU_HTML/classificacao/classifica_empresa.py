from DOU_HTML.DOU_HTML.model import licitacao_out
from DOU_HTML.DOU_HTML.service import dou_service

lista = dou_service.find_all("licitacao_saida")
resultado = []
for obj in lista:
    print(obj.get("dados"))
    empresa = input()
    novo = licitacao_out.LicitacaoOut2(obj.get("titulo"),
                                       obj.get("dados"),
                                       obj.get("pregao"),
                                       obj.get("tipo"),
                                       empresa)
    dou_service.salva_obj(novo, "licitacao_v2")
