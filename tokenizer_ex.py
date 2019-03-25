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

tokenize_doc(doc)