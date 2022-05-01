from gensim.corpora import WikiCorpus
from gensim.models import word2vec
import zhconv  # 繁体字简体字转换
import jieba
import re
import multiprocessing
from gensim.models.word2vec import LineSentence
import logging
import os.path
import sys

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
#1.format: 指定输出的格式和内容，format可以输出很多有用信息，
#%(asctime)s: 打印日志的时间
#%(levelname)s: 打印日志级别名称
#%(message)s: 打印日志信息
# logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
# logging.root.setLevel(level=logging.INFO)
# #打印这是一个通知日志
# logger.info("running %s" % ' '.join(sys.argv))

inp = 'input.txt'  # inp:分好词的文本
model = word2vec.Word2Vec(LineSentence(inp),vector_size=256, window=5, min_count=5,workers=multiprocessing.cpu_count(),epochs=50)
model.save('model.model')

word_vectors = model.wv
word_vectors.save("word2vec.wordvectors")