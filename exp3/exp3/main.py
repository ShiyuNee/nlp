import jieba
import jieba.analyse
import jieba.posseg as pseg
from snownlp import SnowNLP
import thulac
import pynlpir
from stanfordcorenlp import StanfordCoreNLP
import nltk
import spacy


def jieba_test(data):
    kw = jieba.analyse.extract_tags(data, withWeight=True, allowPOS=('v'))
    print(kw)
    # for item in kw:
    #     print(item[0], item[1])


def snow_nlp(data):
    s = SnowNLP(data)
    ans = []
    ent = ['np']  # 需要提取的实体种类
    for i in s.tags:
        if i[1] in ent:
            ans.append(i)
    print(ans)


def thulac_nlp(data):
    thu1 = thulac.thulac()  # 默认模式
    text = thu1.cut(data, text=True)  # 进行一句话分词
    text = text.split(' ')
    ent = ['ns']
    ans = []
    for i in text:
        i = i.split('_')
        if i[1] in ent:
            ans.append(i)
    print(ans)


def pynlpir_nlp(data):
    pynlpir.open()
    tagged = pynlpir.segment(data)
    ent = ['noun']
    ans = []
    for i in tagged:
        if i[1] in ent:
            ans.append(i)
    print(ans)


def stanford_nlp(data):
    # _*_coding:utf-8_*_
    with StanfordCoreNLP(r'D:\stanford-corenlp-full-2018-02-27', lang='zh') as nlp:
        # print(nlp.word_tokenize(data))
        # print(nlp.pos_tag(data))
        print(nlp.ner(data))
        # print(nlp.parse(data))
        # print(nlp.dependency_parse(data))


def nltk_nlp(data):
    ans = nltk.word_tokenize(data)
    tagged = nltk.pos_tag(ans)

    entities = nltk.chunk.ne_chunk(tagged)
    out = [i for i in entities]
    print(out)
    # print(tagged)


def spacy_nlp(data):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(data)
    ans = []
    for ent in doc.ents:
        ans.append({ent.text: ent.label_})
    print(ans)

file = open("../exp4/Chinese.txt", 'r', encoding='utf-8')
file2 = open("../exp4/English.txt", 'r', encoding='utf-8')
Chinese_data = file.read()
English_data = file2.read()
# jieba_test(Chinese_data)
# snow_nlp(Chinese_data)
# thulac_nlp(Chinese_data)
pynlpir_nlp(Chinese_data)
# stanford_nlp(Chinese_data)

# English
# nltk_nlp(English_data)
# spacy_nlp(English_data)
# stanford_nlp(English_data)