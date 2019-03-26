import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer 
from nltk.stem import WordNetLemmatizer
from collections import Counter
from itertools import chain
from nltk.corpus import wordnet
import logging
import sys

# Initialize logging to stdout messages. Setting level to DEBUG.
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

# TEMP VARS
doc = 'espn_earl_thomas.txt'


def tokenize_doc(doc):
    logger = logging.getLogger('TOKENIZE_DOC')
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')

    with open(doc, 'r') as f:
        logger.info('Reading in document')
        doc_strp = [line.strip() for line in f.readlines()]

    logger.info('Tokenizing sentences')
    doc_token = [tokenizer.tokenize(sent) for sent in doc_strp]

    unique_words_pre = len(set(
        chain(*(
            set(entry) for entry in doc_token
            ))
    ))
    logger.info('Unique word pre tokenize: ' + str(unique_words_pre))

    logger.info('Removing stop words and lower casing')
    doc_stopped = []
    for sent in doc_token:
        lower_tokens = [token.lower() for token in sent]
        stopped_tokens = [token for token in lower_tokens if not token in stop_words]
        doc_stopped.append(stopped_tokens)

    logger.info('Token sample: ' + str(doc_stopped[0]))

    unique_words_post = len(set(
        chain(*(
            set(entry) for entry in doc_stopped
            ))
    ))
    logger.info('Unique word post tokenize: ' + str(unique_words_post))

    return doc_stopped


def lemmatize_doc(tokenized_doc):
    logger = logging.getLogger('LEMMATIZE_DOC')
    lemmatizer = WordNetLemmatizer().lemmatize

    pos_dict = {
    'RB': 'r',
    'NN': 'n',
    'VB': 'v',
    'JJ': 'a'
    }

    doc_lem = []
    for entry in tokenized_doc:
        entry_lem = []
        for token in entry:
            """tag = nltk.pos_tag([token])[0][1]
            try:
                pos_dict[tag]
            except KeyError:
                pos = 'n'
            else:
                pos = pos_dict[tag]
            token_lem = lemmatizer(token, pos=pos)"""
            token_lem = lemmatizer(token, pos='v')
            entry_lem.append(token_lem)
        doc_lem.append(entry_lem)

    unique_words_lem = len(set(
    chain(*(
        set(entry) for entry in doc_lem
        ))
    ))
    logger.info('Unique word post lemmatization: ' + str(unique_words_lem))

    return doc_lem


def main():
    doc_token = tokenize_doc(doc)
    doc_lem = lemmatize_doc(doc_token)
    print(doc_lem)


if __name__ == "__main__":
    main()