import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical

# Sample text data
text = (
    "I love natural language processing\n"
    "deep learning is powerful\n"
    "language models generate text\n"
    "machine learning is amazing"
)

# Tokenization
tok = Tokenizer()
tok.fit_on_texts([text])

v_size = len(tok.word_index) + 1

# Create sequences
sequences = []

for line in text.split('\n'):
    token_list = tok.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_seq = token_list[:i + 1]
        sequences.append(n_gram_seq)

# Pad sequences
seq = pad_sequences(sequences, padding='pre')

# Split predictors and labels
X = seq[:, :-1]
y = to_categorical(seq[:, -1], num_classes=v_size)

# Build model
model = Sequential([
    Embedding(v_size, 32, input_length=X.shape[1]),
    LSTM(64),
    Dense(v_size, activation='softmax')
])

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam'
)

# Train model
model.fit(X, y, epochs=200, verbose=1)

# Generate text
out = "language models"

for _ in range(5):
    p = pad_sequences(
        tok.texts_to_sequences([out]),
        maxlen=X.shape[1],
        padding='pre'
    )

    pred = model.predict(p, verbose=0)
    next_word = tok.index_word.get(np.argmax(pred), "")

    out += " " + next_word

print(out)
