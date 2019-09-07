from DOU_HTML.DOU_HTML.model import licitacao_out
from DOU_HTML.DOU_HTML.service import dou_service

objs = dou_service.find_all("classificado")
for obj in objs:
    novo = licitacao_out.LicitacaoOut(obj.get("data").get("titulos")[0],
                                      obj.get("data").get("corpo")[0],
                                      obj.get("tag_pregao"),
                                      obj.get("tag_tipo"))
    dou_service.salva_obj(novo, "licitacao_saida")
