import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u"he was running late for school bus and hence booked a cab")
for token in doc:
    print('{} ­­> {}'.format(token, token.lemma_))