from DOU_HTML.DOU_HTML.model import licitacao_com_tags
from DOU_HTML.DOU_HTML.service import dou_service

# Metodo da camada de armazenamento que retorna todas os objetos salvos
todas = list(dou_service.find_all("licitacoes"))
# Para cada objeto retornado
for separado in todas:
    # Exibimos os dados do corpo da licitacao
    print(separado["corpo"])
    # O usuario informa o tipo de pregao
    tag_pregao = input("Informe tipo do pregao: ")
    if tag_pregao == "e":
        tag_pregao = "eletronico"
    else:
        tag_pregao = "presencial"
    # O usuario informa o tipo de licitacao
    tag_tipo = input("Informe servico produto ou ambos: ")
    if tag_tipo == "a":
        tag_tipo = "ambos"
    elif tag_tipo == "s":
        tag_tipo = "servico"
    else:
        tag_tipo = "produto"
    # A licitacao e carregada em um objeto
    obj = licitacao_com_tags.LicitacaoComTags(separado, tag_pregao, tag_tipo)
    # O id do objeto salvo no banco e exibido na tela
    print(dou_service.salva_obj(obj, "classificado"))
