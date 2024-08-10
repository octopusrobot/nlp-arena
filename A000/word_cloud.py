# 词云生成
import jieba

import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 导入模块

# 创建停用词列表
def stop_words_list(file_path):
    stop_words = [line.strip() for line in open(file_path, 'r', encoding='utf-8').readlines()]
    return stop_words


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stop_words = stop_words_list('resource/stopword.txt')  # 加载停用词
    out_str = ''
    for word in sentence_seged:
        if word not in stop_words:
            if word != '\t':
                out_str += word
                out_str += ' '
    return out_str


if __name__ == '__main__':
    # 读取文本文件，并对文本中的句子分词
    inputs = open('data/poem.txt', 'r', encoding='utf-8')
    outputs = open('data/output.txt', 'w', encoding='utf-8')
    for line in inputs:
        line_seg = seg_sentence(line)
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()
    # 调用 wordcloud 库构建词云，保存结果
    inputs = open('data/output.txt', 'r', encoding='utf-8') # 分词结果
    mytext = inputs.read()
    wordcloud = WordCloud(background_color='white', max_words=500,
                          width=2000, height=1600, margin=2,
                          font_path='/System/Library/Fonts/STHeiti Medium.ttc').generate(mytext)
    plt.imshow(wordcloud,interpolation='bilinear') # 构建词云
    plt.savefig('data/result.png') # 保存词云图
    plt.axis('off')
    plt.show()