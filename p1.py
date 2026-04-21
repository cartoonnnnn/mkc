
#lab1
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

t1 = "Wednesday Addams joins Nevermore Academy, a school for outcasts with unusual abilities."
t2 = "She investigates a series of mysterious attacks in the nearby town while uncovering secrets about her family’s past. With her sharp intelligence and dark humor, she solves clues that even the local police struggle to understand."

print("Tokenized Sentence 1 :")
print(sent_tokenize(t1))
print("Tokenized Sentence 2 :")
print(sent_tokenize(t2))

w1 = word_tokenize(t1)
w2 = word_tokenize(t2)

print("Tokenized Words 1 :")
print(w1)
print("Tokenized Words 2 :")
print(w2)

sw = set(stopwords.words('english'))
fw1 = [w for w in w1 if w.lower() not in sw]

print("After STOP WORDS REMOVAL:")
print(fw1)

print("Stemming:")
print([PorterStemmer().stem(w) for w in fw1])

print("Lemmatization:")
print([WordNetLemmatizer().lemmatize(w) for w in fw1])
