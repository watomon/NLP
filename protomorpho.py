#author : kawasaki
#coding:utf-8
import sys
import re
import copy

def corpus_read():
    wordpos_list = [] #単語/品詞のリスト

    word_list = []  #単語のリスト
    pos_list = []  #品詞のリスト

    word_index = [] #単語の索引（重複なし）
    pos_index = []  #品詞の索引（重複なし）

    #空白とスラッシュを区切りにして偶数番目に語句、奇数番目に品詞にする
    f = open('data/sample.train','r')
    corpus1 = f.read()
    corpus = corpus1.replace("\n", " ")
    f.close()
    #print(corpus)

    wordpos_list = re.split('[/ ]', corpus)
    #print(wordpos_list)

    #改行文字の除去処理
    for i in wordpos_list:
        #print(i)
        i.rstrip("\n")

    for i in range(len(wordpos_list)) :
        if wordpos_list[i] == "\n" :
            wordpos_list.pop(i)
    """
    for k in range(len(wordpos_list)):
        if wordpos_list[k] == "\n" or wordpos_list[k] == "":
            del wordpos_list[k]
    #print(wordpos_list)
    """

    k = 0
    for k in range(len(wordpos_list)):
        if k % 2 == 0 :
            #if wordpos_list[k] == "\n"
            word_list.append(wordpos_list[k])
        elif k % 2 == 1 :
            pos_list.append(wordpos_list[k])
        else :
            break
    word_list.pop(-1)
    #print(word_list)
    #print(pos_list)

    #重複無しの単語のリストを作成
    for word in word_list :
        if  word not in word_index :
            word_index.append(word) #単語インデックスに追加する

    #重複無しの品詞のリストを作成
    for pos in pos_list :
        if pos not in pos_index :
            pos_index.append(pos)
    #print(pos_index)


    #辞書のValueを各品詞の回数を数える
    c_dict = {}
    word_dict = {}

    #品詞とその出現数の辞書を作成

    for p in pos_index :
        c_dict[p] = 0   #最初は全て出現数は０にする

    for w in word_index :
        word_dict[w] = copy.copy(c_dict)
    #print(word_dict)


    """
    #二重辞書の作成
    for w in word_index :
        word_dict[w] = word_dict.get(w,c_dict.copy())

    for w in word_index :
        #for p in pos_index :
        if w not in word_dict.keys():
            word_dict[w].get(c_dict.copy())
    """
    i=0
    j=0
    print(len(word_list))
    print(len(pos_list))
    #二重辞書へ出現数を登録する
    for i in range(len(word_list)) :
        """
        w = word_list[i]
        #print(w,word_dict[w])
        p = pos_list[i]
        """
        for j in range(len(pos_index)) :
            if pos_list[i] == pos_index[j]:
                word_dict[word_list[i]][pos_index[j]] += 1

    print("word_dict", word_dict)



def main():
    #bun01 = "Time flies like an arrow"  #入力する文章
    corpus_read()


if __name__ == '__main__':
    main()
