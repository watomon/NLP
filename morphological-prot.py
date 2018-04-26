#author : kawasaki


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
    #print(corpus) # 文字列データ


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
    print(word_list)
    print(pos_list)

    for word in word_list :
        if  word not in word_index :
            word_index.append(word) #単語インデックスに追加する
    #print(word_index)

    for pos in pos_list :
        if  pos not in pos_index :
            pos_index.append(pos)
    #print(pos_index)

    #辞書のValueを各品詞と回数にする
    c_dict = {}
    word_dict = {}

    for w in word_list :   # wordpos_listとword_indexを見比べて、
        num = 0
        for p in pos_index :
            c_dict.setdefault(p, num) #全ての品詞の出現回数を初期化する
        for pl in pos_list :
            if pl in c_dict :
                num+=1
                c_dict.setdefault(p, num)
        #for w in word_index
        word_dict.setdefault(w, c_dict) #辞書の中に辞書を入れる
        #print(w,word_dict[w])


    i = 0
    for w in word_list :
        num=0
        #print(w  == word_dic.keys()[i])
        #c_dict.setdefault(pos_index[i], 0)
        if pos_list[i] in c_dict :    #品詞辞書の中に該当すれば、
            num+=1
            #print(num)
            #print(c_dict.keys())
            c_dict[pos_list[i]] += num
        word_dict.setdefault(w, c_dict)
        c_dict.setdefault(p, 0)
        i += 1
    print(word_dict)
"""
    i = 0
    for i in range(len(pos_list)) :
        num=0
        #c_dict.setdefault(pos_index[i], 0)
        if pos_list[i] in c_dict :    #品詞辞書の中に該当すれば、
            num+=1
            #print(num)
            #print(c_dict.keys())
            c_dict[pos_list[i]] += num
        word_dict.setdefault(w, c_dict)
        c_dict.setdefault(p, 0)
    print(word_dict)
"""

"""
    for w in word_index :
        word_dict.setdefault(w, c_dict)
"""

"""
    #print(word_dict)
    i = 0
    j = 0
    for i in range(len(word_index)) : #
        for j in range(len(pos_index)) : #品詞の数だけ調べる
            #print(wordpos_list[i] in enumerate(word_dict))
            #nest = word_dict.keys()[i]
            #print(wordpos_list[i])
            #print(wordpos_list[i] in word_dict)
            if wordpos_list[i] in word_dict: #単語と辞書内の単語が一致すれば、
                #print(wordpos_list[i] in word_dict)

                if wordpos_list[i+1] in word_dict.keys()[j] :
                    word_dict[word_dict.keys()[i]][word_dict[word_dict.keys()[i].keys()[j]]] += 1
                    print("Hello")
"""




def main():
    #bun01 = "Time flies like an arrow"  #入力する文章
    corpus_read()


if __name__ == '__main__':
    main()
