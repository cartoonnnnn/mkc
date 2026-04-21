#lab2
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags

# downloads
for d in ['punkt','punkt_tab','maxent_ne_chunker','maxent_ne_chunker_tab',
          'averaged_perceptron_tagger_eng','words']:
    nltk.download(d, quiet=True)

text = """Apple Inc. is planning to open a new headquarters
in Austin, Texas.
CEO Tim Cook announced the plan along with Harry Potter"""

# processing
bio = tree2conlltags(ne_chunk(pos_tag(word_tokenize(text))))

print(word_tokenize(text))
print(pos_tag(word_tokenize(text)))
print(ne_chunk(pos_tag(word_tokenize(text))))
print(bio)

# entity extraction (minimum possible logic)
e, c, t = [], [], None
for w, _, tag in bio:
    if tag.startswith('B-'):
        if c: e.append((' '.join(c), t))
        c, t = [w], tag[2:]
    elif tag.startswith('I-') and t == tag[2:]:
        c.append(w)
    else:
        if c: e.append((' '.join(c), t)); c, t = [], None

if c: e.append((' '.join(c), t))

print(e)
