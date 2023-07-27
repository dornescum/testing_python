import spacy
from spacy.lang.ro.examples import sentences

nlp = spacy.load("ro_core_news_sm")
text = 'Curtea de Justiție a Uniunii Europene (CJUE) a decis, luni, în urma sesizării Curtii de A' \
      'pel Brașov că deciziile de încetare a proceselor penale ca urmare a prescripţiei sunt contrare ' \
      'dreptului european. Amintim că în baza unei decizii din mai 2022 a Curții Constituționale privind' \
      ' aplicarea retroactivă a prescripției, au ' \
      'fost închise mii de dosare penale, hotărârea declanșând un val de achitări.'

doc = nlp(text)
# print(doc)

# value = []
for token in doc.ents:
    # print(token.text, token.pos_, token.dep_)
    print(token.text, token.label_)
    # value.extend(token.text, token.label_)