import re

import pandas as pd
from nltk.stem import SnowballStemmer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split

from DOU_HTML.DOU_HTML.service import dou_service

# Sao recuperados todos as licitacoes classificadas
treinados = list(dou_service.find_all("classificado"))
# As licitacoes sao convertidas em um DataFrame
df = pd.DataFrame.from_dict(treinados)
# O DataFrame e dividio entre dados e tags
dados = df.iloc[:, 1]
tags = df.iloc[:, 2]
documentos = []

# Aqui comeca o processamento das palavras contidas nos dados
stemmer = SnowballStemmer("portuguese")
for info in range(0, len(dados)):
    # Remove os caracteres especiais
    documento = re.sub(r'\W', ' ', str(dados[info]))
    # Remove espacos multiplos
    documento = re.sub(r'\s+', ' ', documento, flags=re.I)
    # Converte para caixa baixa
    documento = documento.lower()
    # Separa as palavras
    documento = documento.split()
    # Junta as palavras similares em um so classificador
    documento = [stemmer.stem(word) for word in documento]
    # Inclue um espaco ao final da palavra
    documento = ' '.join(documento)
    # Adiciona ao array principal o documento trabalhado
    documentos.append(documento)

# Geracao de um vetor de 30 palavras
vector = CountVectorizer(max_features=30, min_df=3, max_df=0.8)
x = vector.fit_transform(documentos).toarray()
# Alteracao do vetor para um TFIDF
tfid = TfidfTransformer()
x = tfid.fit_transform(x).toarray()
# Divisao da base entre treino e teste
x_treino, x_teste, tags_treino, tags_teste = train_test_split(x, tags, test_size=0.2, random_state=0)
# Criacao de um classificador RandomForest
classificador = RandomForestClassifier(n_estimators=1000, random_state=0)
classificador.fit(x_treino, tags_treino)
# Utilizacao do classificador na base de testes
tags_pred = classificador.predict(x_teste)
# Exibicao dos resultados da classificacao
print(confusion_matrix(tags_teste, tags_pred))
print(classification_report(tags_teste, tags_pred))
print(accuracy_score(tags_teste, tags_pred))
