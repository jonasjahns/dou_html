import re

import pandas as pd
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split

from DOU_HTML.DOU_HTML.service import dou_service

treinados = list(dou_service.find_all("classificado"))
df = pd.DataFrame.from_dict(treinados)
dados = df.iloc[:, 1]
tags = df.iloc[:, 3]
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
x_treino, x_teste, tags_treino, tags_teste = train_test_split(x, tags, test_size=0.2, random_state=0)
classificador = RandomForestClassifier(n_estimators=1000, random_state=0)
classificador.fit(x_treino, tags_treino)
tags_pred = classificador.predict(x_teste)
print(confusion_matrix(tags_teste, tags_pred))
print(classification_report(tags_teste, tags_pred))
print(accuracy_score(tags_teste, tags_pred))
