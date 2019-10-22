#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import pandas as pd
import jieba
import string
import re
import numpy as np

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
    print("content:")
    print(train_data.count()) # 数据条数
    print("label:")
    print(train_label.count())
    print("merge: ")
    print(train_merge.count())
    return train_merge.values


# 脏数据处理
def etl(data):
    exclude = set(string.punctuation)
    re_expression='＂＃＄％＆＇（）＊＋。，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏'
    # zhon包有专门对中文的处理
    err_array=list()
    suc_array=list()

    for row in data:
        id = row[0]
        label = row[1]
        title = row[2]
        content = row[3]
        try:
            # 处理title

            # 处理content
            content=''.join(ch for ch in content if ch not in exclude)
            suc_array.append((id,label,title,content))
        except:
            err_array.append((id,label,title,content))
            pass

    print("err num: ",len(err_array))
    print("suc num: ",len(suc_array))

    return suc_array,err_array

# 分词
def cut_words(suc_array):
    words=[]
    for line in suc_array:
        cut_word = jieba.cut(line[3])
        try:
            r=" ".join(cut_word)
            words.append(r)
        except:
            pass
    return words

# 分词，合并label

# 其他数据处理

# 输出npz

xlsx_file_path = "/Users/zhangzhiyong/Downloads/emoji_data.xlsx"
merge_data=read_xlsx(xlsx_file_path)
suc_data,err_data=etl(merge_data)
words=cut_words(suc_data)
for w in words:
    print(w)