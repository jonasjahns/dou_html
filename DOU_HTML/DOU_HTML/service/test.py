from bson import ObjectId

from DOU_HTML.DOU_HTML.service import dou_service

lista = [{"_id": ObjectId("5d73c3bcb96ae88797e0390e")},
         {"_id": ObjectId("5d73c3f6b96ae88797e03914")}]

for item in lista:
    dou_service.delete("classificado", item)
