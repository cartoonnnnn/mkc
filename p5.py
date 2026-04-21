
#lab 5
import gensim.downloader as api
from numpy import dot
from numpy.linalg import norm

print("Loading pretrained Word2Vec model...")
m = api.load("word2vec-google-news-300")
print("Model loaded successfully!")

# similarity function
sim = lambda a,b: dot(a,b)/(norm(a)*norm(b))

# similarities
print("\nWord Similarity Demonstration\n----------------------------------")
print(f"Similarity between 'king' and 'queen': {sim(m['king'],m['queen']):.4f}")
print(f"Similarity between 'king' and 'apple': {sim(m['king'],m['apple']):.4f}")

# top similar words
print("\nTop 5 words similar to 'computer':")
for w,s in m.most_similar("computer", topn=5):
    print(f"{w} : {s:.4f}")
