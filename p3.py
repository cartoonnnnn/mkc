#lab 3
import math,nltk,pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt',quiet=True); nltk.download('punkt_tab',quiet=True)

docs=[
"This movie was fantastic and I loved every minute of it",
"The acting was terrible and the plot made no sense",
"Great special effects but the story was predictable",
"I fell asleep during this boring movie",
"The soundtrack was amazing and the cinematography stunning"
]

tok=[word_tokenize(d.lower()) for d in docs]

tf=[{w:c/len(d) for w,c in Counter(d).items()} for d in tok]
print("Term Frequency (TF):"); [print(f"Document {i+1}: {t}") for i,t in enumerate(tf)]

df={}
for d in tok:
    for w in set(d): df[w]=df.get(w,0)+1

idf={w:math.log(len(tok)/df[w]) for w in df}
print("\nDocument Frequency (DF):",df)
print("\nInverse Document Frequency (IDF):",idf)

tfidf=[{w:tf[i][w]*idf[w] for w in tf[i]} for i in range(len(tf))]
print("\nTF-IDF Scores:"); [print(f"Document {i+1}: {t}") for i,t in enumerate(tfidf)]

v=TfidfVectorizer(); X=v.fit_transform(docs)
df2=pd.DataFrame(X.toarray(),columns=v.get_feature_names_out(),
                 index=[f"Doc {i+1}" for i in range(len(docs))])

for i in df2.index:
    print(f"\n{i} - Words present with TF-IDF scores:")
    print(df2.loc[i][df2.loc[i]>0].sort_values(ascending=False))
