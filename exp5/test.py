from gensim.models import word2vec
import multiprocessing
from gensim.models.word2vec import LineSentence
from gensim.models import KeyedVectors
import logging
import os.path
import sys

wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')
vector = wv['清华大学']   # Get numpy vector of a word
print(vector)
print(wv.most_similar('自然语言', topn=10))