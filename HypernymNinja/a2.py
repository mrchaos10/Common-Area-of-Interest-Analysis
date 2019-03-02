#!/usr/bin/env python
from nltk.corpus import wordnet as wn
from itertools import chain
for i,j in enumerate(wn.synsets('apple')):
    print('Meaning', i, 'NLTK ID', j.name())
    print('Definition:', j.definition())
    print('Hypernyms:', ', '.join(list(chain(*[l.lemma_names() for l in j.hypernyms()]))))
