#author : kawasaki


import numpy as np
import pandas as pd

bun01 = "Time flies like an arrow"  #入力する文章
part_of_speech_list = ['N', 'V', 'D', 'J']  #品詞のリスト

#空白を区切りにして、単語別で分解する
word_list = bun01.split()
print(word_list)    #出力


df = pd.read_csv('test.csv', header = None)
print(df)
