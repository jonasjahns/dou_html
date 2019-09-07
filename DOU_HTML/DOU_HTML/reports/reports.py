from DOU_HTML.DOU_HTML.service import dou_service


def report_raiz():
    filewriter = open("todos.txt", "a")
    lista = dou_service.find_all("licitacoes_v2")
    for obj in lista:
        string = obj.get("titulo") + "," + \
                 obj.get("dados") + "," + \
                 obj.get("pregao") + "," + \
                 obj.get("tipo") + "," + \
                 obj.get("empresa")
        print(string)
        filewriter.write(string)
    filewriter.close()
