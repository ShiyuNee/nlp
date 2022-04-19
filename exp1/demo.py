from collections import defaultdict
import nltk
from math import log

needless_words = ['!', ',', '.', '?', ':', ';', '<', '>']  # 常见标点符号

uni_ppl = []
bi_ppl = []
total_words = 0


def read_train_file(file_path):
    """
    param file_path: 读取 train 文件的路径
    return: 所有的词,格式是二维列表,每个句子的词组成一个列表
    """
    res_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = f.readlines()
        for line in reader:
            split_line = line.strip().split('__eou__')  # 分句
            words = [nltk.word_tokenize(each_line) for each_line in split_line]  # 分词,每句的词都是一个列表
            for i in words:
                need_word = [word.lower() for word in i if word not in needless_words]  # 删除常见标点,并将所有词进行小写处理
                if len(need_word) > 0:
                    res_list.append(need_word)
    return res_list


def read_test_file(file_path):
    """
    param file_path: 读取 test 文件的路径
    return: 所有的句子,格式是二维列表,每个句子都是一个列表
    """
    res_list = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = f.readlines()
        for line in reader:
            split_line = line.strip().split('__eou__')  # 分句
            for i in split_line:
                if len(i) > 0:
                    res_list.append(i)
    return res_list


def uni_gram(word_list):  # 计算词频
    """
    param word_list: 从 train 中读取的结果(所有词),是一个二维列表
    return: 一个保留词频的字典
    """
    global total_words
    uni_dict = defaultdict(float)
    for line in word_list:
        for word in line:
            total_words += 1  # 计算总的词的个数
            uni_dict[word] += 1  # 计算词频
    return uni_dict


def ppl_compute(word_dict, sens):
    """
    param word_dict: uni_gram的字典
    param sens: 从 test 中读来的句子(没经过分词)
    return: uni_ppl
    """
    temp = []
    for sen in sens:
        words = nltk.word_tokenize(sen)
        need_words = [word.lower() for word in words if word not in needless_words]  # 提取出句子中所有的词项
        temp.append(need_words)
        for word in need_words:  # test语句中未在 train 时出现过的词，新加入
            if word not in word_dict:
                word_dict[word] = 0

    for word in word_dict:  # 所有词项的词频都加 1，进行平滑处理
        word_dict[word] += 1
        word_dict[word] /= len(word_dict) + total_words  # 每个词都加一后的增加量 + 原有的词的总数

    for need_words in temp:
        res_ppl = 1
        for word in need_words:
            res_ppl += log(word_dict[word], 2)  # 防止累乘出现 res_ppl = 0 的情况
        uni_ppl.append(pow(2, -(res_ppl / len(need_words))))


def bi_gram(word_list):
    """
    param word_list: 从 train 中读取的数据(所有词)
    return: 二维字典,统计了 bi_gram 的词频
    """
    bi_dict = defaultdict(dict)
    for words in word_list:
        words.insert(0, 'nsy6666')  # 每行的词加个开头
        words.append('nsy6666///')  # 每行的词加个结尾
        for index in range(len(words) - 1):
            if words[index + 1] not in bi_dict[words[index]]:  # 其他词作为子项
                bi_dict[words[index]][words[index + 1]] = 1
            else:
                bi_dict[words[index]][words[index + 1]] += 1
    return bi_dict


def ppl_compute_bi(bi_word, sens):
    """
    param bi_word: bi_gram 的字典
    param sens: 从 test 中读来的句子
    return: bi_ppl
    """
    temp = []
    for sen in sens:  # 遍历每个句子
        words = nltk.word_tokenize(sen)
        need_words = [word.lower() for word in words if word not in needless_words]  # 提取出句子中所有的词项
        need_words.insert(0, 'nsy6666')  # 每行的词加个开头
        need_words.append('nsy6666///')  # 每行的词加个结尾
        temp.append(need_words)

        for index in range(len(need_words) - 1):  # 添加 test 句子中同时出现的 bi_gram,但未在 train 中同时出现的 bi_gram
            if need_words[index + 1] not in bi_word[need_words[index]]:
                bi_word[need_words[index]][need_words[index + 1]] = 0

    for first_word in bi_word:  # 对 bi_gram 词项进行平滑处理
        for second_word in bi_word[first_word]:
            bi_word[first_word][second_word] += 1

    for first_word in bi_word:  # 对 bi_gram 词项进行平滑处理。不能只使用 need_words,因为中间有很多重复的词,会进行不该进行的除法
        tt = sum(bi_word[first_word].values())  # 需要提前定义在这里，否则后面进行除法之后，这个值就发生改变了
        for second_word in bi_word[first_word]:
            bi_word[first_word][second_word] /= tt

    for need_words in temp:
        res_ppl = 0
        for index in range(len(need_words) - 1):
            res_ppl += log(bi_word[need_words[index]][need_words[index + 1]], 2)
        bi_ppl.append(pow(2, -(res_ppl / (len(need_words) - 1))))


read_train = read_train_file('train_LM.txt')
read_test = read_test_file('test_LM.txt')
uni_word_dict = uni_gram(read_train)
ppl_compute(uni_word_dict, read_test)
bi_word_dict = bi_gram(read_train)
ppl_compute_bi(bi_word_dict, read_test)


print(sum(uni_ppl) / len(uni_ppl))  # 取所有句子困惑度的平均值
print(sum(bi_ppl) / len(bi_ppl))  # 取所有句子困惑度的平均值


