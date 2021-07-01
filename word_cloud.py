#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:zhengaihua
@E-mail:zhengaihua@jd.com
@file: word_cloud.py
@time: 2021/7/1 17:10
@desc: 词頻，词云
"""

# 导入扩展库
import re
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt

# 读取文件
with open("resource/Speech.txt", "r") as f:
    string_data = f.read()

# print(string_data)

# 文本预处理
pattern = re.compile(r"\t|\n|。|，|：|；|（|）|！|、|\s|")  # 定义正则表达式匹配模式
string_data = re.sub(pattern, "", string_data)

# 文本分词
seg_list_extra = jieba.cut(string_data, cut_all=False)  # 精确模式分词
object_list = []
remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在',
                u'了', u'通常', u'如果', u'我们', u'需要']  # 自定义去除词库

# 过滤词库
for word in seg_list_extra:
    if word not in remove_words:
        object_list.append(word)

# 词频统计
word_counts = collections.Counter(object_list)  # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
print(word_counts_top10)  # 输出检查

# 词频展示
mask = np.array(Image.open("resource/China_Maps.jpeg"))  # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='/System/Library/Fonts/STHeiti Light.ttc',  # 设置字体格式
    mask=mask,  # 设置背景图
    max_words=200,  # 最多显示词数
    max_font_size=100   # 字体最大值
)

wc.generate_from_frequencies(word_counts)  # 从字典生成词云
image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
plt.imshow(wc)   # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()      # 显示图像





