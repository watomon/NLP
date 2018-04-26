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
    for i in range(1):
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
    #print(pos_list)

    zero = []
    for word in word_list :
        if  word not in word_index :
            word_index.append(word) #単語インデックスに追加する
            zero.append(0)
    #print(word_index)

    for pos in pos_list :
        if  pos not in pos_index :
            pos_index.append(pos)
    #print(pos_index)

    #辞書のValueを各品詞の回数を数える
    c_dict = {}
    word_dict = {}


    i = 0
    j = 0
    #print(pos_count)
    print(pos_list)
    pos_count = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(word_index)) :   #word_list分、サンプルデータの単語数分回す
        # #ゼロでカウントを初期化
        j = 0
        for j in range(len(pos_index)) :
            pos_count = [0,0,0,0,0,0,0,0,0,0,0]
            #c_dict = dict(zip(pos_index, zero)) #ゼロでカウントを初期化
            num=0
            if pos_list[i] in pos_index[j] :   #品詞インデックスを調べて、該当すれば
                num += 1
                pos_count.insert(j, num)
                print(pos_count)
            else :
                pos_count.insert(j, num)

            #print(pos_count)
            #辞書に登録できたら、一度pos_countを０で初期化して次の単語のループに入る
            #c_dict.setdefault(pos_index[i], pos_count[i])
            c_dict = dict(zip(pos_index, pos_count))
        word_dict.setdefault(word_index[i], c_dict)
        #pos_count.clear()
        #print(c_dict)

    print(word_dict)

    #print(word_dict)
    #print(word_dict)

    #テストで書いてるだけ！
    w_keylist = list(word_dict.keys())
    #print(w_keylist) #=> []

def main():
    #bun01 = "Time flies like an arrow"  #入力する文章
    corpus_read()


if __name__ == '__main__':
    main()
