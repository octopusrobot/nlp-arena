# 用于验证不同模式的中文分词

# 结论：
# 精确模式能获得句子的语义信息，因此自然语言处理的各种任务常常使用精确模式。
# 全模式和搜索引擎模式适用于搜索和推荐领域，
# 而paddle模式则和精确模式类似，不同之处在于paddle模式匹配会对包含语义最大的词组进行切分。

# 步骤一：导入模块
import jieba


# 步骤二：创建 word_segment 函数，实现不同模式的分次
def word_segment():
    strs = '我来到北京清华大学'

    seg_list = jieba.cut(strs, cut_all=True)
    print('Full Mode：' + '/ '.join(seg_list))  # 全模式

    seg_list = jieba.cut(strs, cut_all=False)
    print('Default Mode：' + '/ '.join(seg_list))  # 精确模式

    # jieba.enable_paddle()
    # seg_list = jieba.cut(strs, use_paddle=True)
    # print('Paddle Mode：' + '/ '.join(seg_list))  # paddle 模式

    seg_list = jieba.cut_for_search(strs)
    print('Search Mode：' + '/ '.join(seg_list))  # 搜索引擎模式


# 步骤三：自定义 main 方法编写及主函数处理
if __name__ == '__main__':
    word_segment()
