import logging

from gensim.models import LdaModel
from gensim import corpora
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

english_vocab = set(w.lower() for w in nltk.corpus.words.words())

class Predict():
    def __init__(self):
        dictionary_path = "models/dictionary.dict"
        lda_model_path = "models/lda_model_20_topics.lda"
        self.dictionary = corpora.Dictionary.load(dictionary_path)
        self.lda = LdaModel.load(lda_model_path)

    def load_stopwords(self):
        stopwords = {}
        with open('stopwords.txt', 'rU') as f:
            for line in f:
                stopwords[line.strip()] = 1

        return stopwords

    def extract_lemmatized_nouns(self, new_review):
        stopwords = self.load_stopwords()
        words = []

        sentences = nltk.sent_tokenize(new_review.lower())
        for sentence in sentences:
            tokens = nltk.word_tokenize(sentence)
            text = [word for word in tokens if word in english_vocab]
            tagged_text = nltk.pos_tag(text)

            for word, tag in tagged_text:
                words.append({"word": word, "pos": tag})

        lem = WordNetLemmatizer()
        nouns = []
        for word in words:
            if word["pos"] in ["RB", "JJ", "JJR", "VBG", "VBP", "WP"]:
                nouns.append(lem.lemmatize(word["word"]))

        return nouns

    def run(self, new_review):
        nouns = self.extract_lemmatized_nouns(new_review)
        new_review_bow = self.dictionary.doc2bow(nouns)
        new_review_lda = self.lda[new_review_bow]

        print new_review_lda
	label=open('Output_LDA.txt','w')
	label.write("%s"% new_review_lda)
	labels = []
	input_label=open('labelling.txt',"rb")
    	for line in input_label:
        	line = line.strip() #or someother preprocessing
        	labels.append(line)
	max1=0
	max2=0
	ind1=0
	ind2=0
	for i in range(0,20):
		if new_review_lda[i][1] > max1:
			max1=new_review_lda[i][1]
			ind1=i
		elif new_review_lda[i][1] > max2:
			max2=new_review_lda[i][1]
			ind2=i
	print(labels[ind1],max1)
	print(labels[ind2],max2)
			


def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    myfile=open('test.txt',"rb")
   
    new_review = myfile.read().replace('\n', '')

    print(new_review)
    predict = Predict()
    predict.run(new_review)


if __name__ == '__main__':
    main()


