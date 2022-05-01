from zhconv import convert
import jieba
import re
# print(convert('Python是一种动态的、面向对象的脚本语言', 'zh-hant'))
# print(convert('Python是一種動態的、面向對象的腳本語言', 'zh-cn'))

def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    print(chinese)


processed_data = []
cnt = 0
input = open('input.txt', "w", encoding="utf8")

with open('corpus_cn.txt', "r", encoding="utf8") as f:
    for line in f.readlines():
        cnt += 1
        line = convert(line, 'zh-cn')  # 将繁体转化为简体
        words = jieba.cut(line)  # 分词
        ans = []
        for i in words:
            pattern = re.compile(r'[^\u4e00-\u9fa5]')  # 去除不是中文的词
            i = re.sub(pattern, '', i)  # 不是中文的都被置为空 ''
            if len(i) > 0:
                ans.append(i)
        input.write(' '.join(ans) + '\n')
        # processed_data.append(ans)
        if cnt % 10000 == 0:
            print(f'{cnt} preprocess finished')

input.close()

# cnt = 0
# with open('input.txt', "w", encoding="utf8") as f:
#     for line in processed_data:
#         line = ' '.join(line)
#         f.write(line + '\n')
#         cnt += 1
#         if cnt % 10000 == 0:
#             print(f'{cnt} write finished')




