#author : kawasaki
import sys
import re

def corpus_read():
    word_dic = {}
    wordpos_list = [] #単語/品詞のリスト
    word_list = []  #単語のリスト
    pos_list = []  #品詞のリスト

    word_index = [] #単語の索引（重複なし）
    pos_index = []  #品詞の索引（重複なし）


    #訓練データを文字列データに格納
    f = open('data/sample.train')
    corpus = f.readline()  # ファイル一行読んだデータを返す
    #corpus = f.read()
    f.close()

    #空白とスラッシュを区切りにして偶数番目に語句、奇数番目に品詞にする
    wordpos_list = re.split('[/ ]', corpus)


    for i in range(len(wordpos_list)) :
        if wordpos_list[i] == "\n" :
            wordpos_list.pop(i)

    for k in range(len(wordpos_list)):
        if wordpos_list[k] == "\n" or wordpos_list[k] == "":
            del wordpos_list[k]
    #print(wordpos_list)

    k = 0
    for k in range(len(wordpos_list)):
        if k % 2 == 0 :
            #if wordpos_list[k] == "\n"
            word_list.append(wordpos_list[k])
        elif k % 2 == 1 :
            pos_list.append(wordpos_list[k])
        else :
            break
    #print(word_list)

    #重複無しの単語のリストを作成
    for word in word_list :
        if  word not in word_index :
            word_index.append(word) #単語インデックスに追加する

    #重複無しの品詞のリストを作成
    for pos in pos_list :
        if pos not in pos_index :
            pos_index.append(pos)
    print(pos_index)


    #辞書のValueを各品詞の回数を数える
    c_dict = {}
    word_dict = {}

    #品詞とその出現数の辞書を作成

    for p in pos_index :
        c_dict[p] = 0   #最初は全て出現数は０にする
    #二重辞書の作成
    """
    for w in word_index :
        word_dict[w] = word_dict.get(w,c_dict.copy())
    """
    for w in word_index :
        #for p in pos_index :
        if w not in word_dict.keys():
            word_dict[w] = c_dict.copy()
    #print(word_dict)


    dict_firstkeys = list(word_dict.keys())
    dict_secondkeys = list(c_dict.keys())
    #print("これは単語辞書の最初のキー", dict_firstkeys)
    #print("辞書の中の辞書のキー", dict_secondkeys)
    """
    (word_dict['Fujitsu'])['NNP'] = 1
    #print(list(word_dict.keys()))
    for w in list(word_dict.keys()):
        for p in pos_index:
            print(w,word_dict[w])
    """
    i=0
    j=0
    #二重辞書へ出現数を登録する
    for i in range(len(word_index)) :
        w = word_index[i]
        for j in range(len(pos_index)) :
            p = pos_index[j]
            if  
                word_dict[w][p] += 1


    print(word_dict)


def main():
    #bun01 = "Time flies like an arrow"  #入力する文章
    corpus_read()


if __name__ == '__main__':
    main()
