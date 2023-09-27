#!/usr/bin/env python3

import spacy
from spacy import displacy

# Load English model and text
nlp = spacy.load("en_core_web_lg")
text = open("input_en.txt", "r").read()

# nlp = spacy.load("ro_core_news_lg")
# text = open("input_ro.txt", "r").read()

doc = nlp(text)

# Tokenization + morphological analysis
for token in doc:
    print(token.text, token.morph)
print()

# Part-of-speech tagging (noun, verb, adjective, etc.)
for token in doc:
    print(token.text, token.pos_)
print()

# Dependency parsing ?? look into this
for token in doc:
    print(token.text, token.dep_, token.head.text)
print()

# Lemmatization (converts words to their base form)
for token in doc:
    print(token.text, token.lemma_)

# Visualize named entities
displacy.serve(doc, style="ent")
