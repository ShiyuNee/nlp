# 数据处理部分
from gensim.corpora import WikiCorpus
from gensim.models import word2vec
import zhconv  # 繁体字简体字转换
import jieba
import re
import multiprocessing

input_file_name = 'zhwiki-latest-pages-articles.xml.bz2'
output_file_name = 'corpus_cn.txt'
# 加载数据
input_file = WikiCorpus(input_file_name, dictionary={})
# 将lemmatize设置为False的主要目的是不使用pattern模块来进行英文单词的词干化处理，无论你的电脑#是否已经安装了pattern，因为使用pattern会严重影响这个处理过程，变得很慢
with open(output_file_name, 'w', encoding="utf8") as output_file:
    # 使用WikiCorpus类中的get_texts()方法读取文件，每篇文章转换为一行文本，并去掉标签符号等内容
    count = 0
    for text in input_file.get_texts():
        output_file.write(' '.join(text) + '\n')
        count = count + 1
        if count % 10000 == 0:
            print('已处理%d条数据' % count)
    print('处理完成！')

# 查看处理结果
with open('corpus_cn.txt', "r", encoding="utf8") as f:
    print(f.readlines()[:1])