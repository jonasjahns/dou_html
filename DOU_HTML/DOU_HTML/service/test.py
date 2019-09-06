import pandas as pd

from DOU_HTML.DOU_HTML.service import dou_service

treinados = list(dou_service.find_all("classificado"))
df = pd.DataFrame.from_dict(treinados)
tags = df.iloc[:, 2]
print(tags)
