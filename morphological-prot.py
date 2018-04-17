#author : kawasaki

import numpy as np
import pandas as pd

bun01 = "Time flies like an arrow"  #入力する文章
c_list = []  #品詞のリスト

#訓練データを文字列データに格納
f = open('data/sample.train')
corpus = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
print(corpus) # 文字列データ

#空白を区切りにして、単語別で分解する
word_list = corpus.split(' ')
print(word_list)    #出力

"""
df = pd.read_csv('testcorpus.txt', header = None)
print(df)
"""
