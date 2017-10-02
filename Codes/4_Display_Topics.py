import logging

from gensim.models import LdaModel
from gensim import corpora


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary_path = "models/dictionary.dict"
corpus_path = "models/corpus.lda-c"
lda_num_topics = 50
lda_model_path = "models/lda_model_20_topics.lda"

dictionary = corpora.Dictionary.load(dictionary_path)
corpus = corpora.BleiCorpus(corpus_path)
lda = LdaModel.load(lda_model_path)

i = 0
for topic in lda.show_topics(lda_num_topics,15):
    print topic
    i += 1

