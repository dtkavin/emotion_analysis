#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import pandas as pd
import jieba
import string
import re

# 加载xlsx文件
def read_xlsx(file_path):
    # ['Train_DataSet', 'Train_DataSet_Label', 'Test_DataSet', 'Test_submit_example']
    train_data=pd.read_excel(file_path,sheet_name='Train_DataSet')
    train_label=pd.read_excel(file_path,sheet_name='Train_DataSet_Label')
    print(train_data.keys())
    print(train_label.keys())
    train_merge=pd.merge(train_label,train_data)
    print(train_merge.keys())
    # print(train_data.get('id'))
    # print(train_data.get('title'))
    return train_merge


# 脏数据处理
def etl(dataframe):
    exclude = set(string.punctuation)
    re_expression='＂＃＄％＆＇（）＊＋。，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏'
    # zhon包有专门对中文的处理
    contents=dataframe.get('content')
    for line in contents:
        f1_line=re.sub(re_expression,' ',line)
        print(''.join(ch for ch in f1_line if ch not in exclude))

# 分词
def cut_words(dataframe):
    a = dataframe.get('content')
    for line in a:
        cut_word = jieba.cut(line)
        print(" ".join(cut_word))

# 分词，合并label

# 其他数据处理

# 输出npz

xlsx_file_path = "/Users/zhangzhiyong/Downloads/emoji_data.xlsx"
merge_data=read_xlsx(xlsx_file_path)
print(merge_data['content'])
# etl(merge_data)
# cut_words(merge_data)