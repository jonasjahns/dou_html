import random

from DOU_HTML.DOU_HTML.service import dou_service
from DOU_HTML.DOU_HTML.model import licitacao_com_tags


todas = list(dou_service.find_all("licitacoes"))
for separado in todas:
    print(separado["corpo"])
    tag_pregao = input("Informe tipo do pregao: ")
    tag_tipo = input("Informe servico produto ou ambos: ")
    obj = licitacao_com_tags.LicitacaoComTags(separado, tag_pregao, tag_tipo)
    print(dou_service.salva_obj(obj, "classificado"))
