#2018/09/17
#author : kawasaki
#coding:utf-8
import sys
import re
import copy

def read_dict(a):
    f = open(a,'r')
    corpus1 = f.read()
    f.close()
    return corpus1

def main():

    pos_list = [0, 1, 2, 3, 4]  # F Det N V P
    cost_of_pos = []

    input_sentence = "an arrow like flies"  #入力する文章
     = read_dict('bigram_prob.dict')

    print(read_dict('bigram_prob.dict'))
    print(read_dict('lex_prob.dict'))






if __name__ == '__main__':
    main()
