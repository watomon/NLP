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

    wordpos_list = re.split('[/ ]', corpus)


    for i in range(len(wordpos_list)) :
        if wordpos_list[i] == "\n" :
            wordpos_list.pop(i)

    for k in range(len(wordpos_list)):
        if wordpos_list[k] == "\n" or wordpos_list[k] == "":
            del wordpos_list[k]
    #print(wordpos_list)

    #wordpos_listから奇数番目を単語のリスト、偶数番目の要素を品詞のリストに格納する。・
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
    #print(pos_list)

    zero = []
    for word in word_list :
        if  word not in word_index :
            word_index.append(word) #単語インデックスに追加する
            zero.append(0)
    #print(word_index)

    #pos_indexにない品詞があれば、品詞インデックスに追加
    for pos in pos_list :
        if pos not in pos_index :
            pos_index.append(pos)
    print(pos_index)

    print(word_index)
    #c_dict={keys:value}
    #辞書のValueを各品詞の回数を数える
    c_dict = {}
    word_dict = {}

    #辞書に出現回数を記録する処理
    i = 0
    j = 0
    #print(pos_count)
    #print(pos_list)
    pos_count = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(word_index)) :   #word_list分、サンプルデータの単語数分回す
        # #ゼロでカウントを初期化
        j = 0
        #if word_list[i] == word_index[j]:
        for j in range(len(pos_index)) :
            pos_count = [0,0,0,0,0,0,0,0,0,0,0]
            #c_dict = dict(zip(pos_index, zero)) #ゼロでカウントを初期化
            num=0
            if pos_list[i] in pos_index[j] :   #品詞インデックスを調べて、該当すれば+1
                num += 1
                pos_count.insert(j, num)
                print(pos_count)
                c_dict = dict(zip(pos_index, pos_count))
            else :
                pos_count.insert(j, num)

            #print(pos_count)
            #辞書に登録できたら、一度pos_countを０で初期化して次の単語のループに入る
            #c_dict.setdefault(pos_index[i], pos_count[i])
        word_dict.setdefault(word_index[i], c_dict)
        #pos_count.clear()
        #print(c_dict)

    print(word_dict)


    #テストで書いてるだけ！
    w_keylist = list(word_dict.keys())

    print("word_dict", word_dict)
    print(word_index)
    print("word_index", word_index)

def main():
    #bun01 = "Time flies like an arrow"  #入力する文章
    corpus_read()


if __name__ == '__main__':
    main()
