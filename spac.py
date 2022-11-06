import spacy
import os


os.environ["SPACY_WARNING_IGNORE"] = "W008"
nlp = spacy.load('en_core_web_lg')

newpass = "Smokey"
existing = "Snake"
words = newpass+" "+existing

tokens = nlp(words)

token1, token2 = tokens[0], tokens[1]

print("Similarity:", token1.similarity(token2))
