import pandas as pd
from DOU_HTML.DOU_HTML.service import dou_service
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import TfidfTransformer


treinados = list(dou_service.find_all("classificado"))
df = pd.DataFrame.from_dict(treinados)
dados = df.iloc[:, 1]
tags = df.iloc[:, 2]
documentos = []

stemmer = WordNetLemmatizer()

for info in range(0, len(dados)):
    # Remove os caracteres especiais
    documento = re.sub(r'\W', ' ', str(dados[info]))
    # Remove espacos multiplos
    documento = re.sub(r'\s+', ' ', documento, flags=re.I)
    # Converte para caixa baixa
    documento = documento.lower()
    documento = documento.split()

    documento = [stemmer.lemmatize(word) for word in documento]
    documento = ' '.join(documento)
    # print(documento)
    documentos.append(documento)

vector = CountVectorizer(max_features=100, min_df=3, max_df=0.8)
x = vector.fit_transform(documentos).toarray()
tfid = TfidfTransformer()
x = tfid.fit_transform(x).toarray()
print(x)