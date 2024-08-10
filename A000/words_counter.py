# 用于实现词频的统计
import collections

import jieba


def read_text(file_path):
    # 1. 打开文件
    with open(file_path, "r", encoding='utf-8') as f: # 打开文件
        data = f.readlines()
        word_list = []
        # 2.按行遍历文件
        for line in data:
            line = line.strip()
            words = jieba.cut(line)
            for word in words:
                word_list.append(word)
    print(word_list)
    # 3. 统计列表中每个字符出现的次数
    counter = collections.Counter(word_list).most_common()
    print(counter)


if __name__ == '__main__':
    read_text('data/poem.txt')