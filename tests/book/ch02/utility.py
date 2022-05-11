# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-05-24 22:11
# 《自然语言处理入门》2.2.2 词典的加载
# 配套书籍：http://nlp.hankcs.com/book.php
# 讨论答疑：https://bbs.hankcs.com/
from pyhanlp import *


def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')  
    #JClass函數是連通Java和Python的橋樑，他根據Java路徑名稱得到一個Python類別
    #利用JClass取得HanLP的IOUtil工具類別
    
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt') 
    #取得HanLP的組態項目Config的詞典路徑。寫到設定檔的條目，最終會讀入這個結構
    #例如設定檔為CoreDictionaryPath=data/dictionary/CoreNatureDictionary.txt，該組態將讀入HanLP.Config.CoreDictionaryPath。要載入mini詞典就改路徑
    
    dic = IOUtil.loadDictionary([path])
    #像對待Python工具類別一般的呼叫IOUtil的靜態方式loadDictionary。
    
    #該方法支援讀取多個檔案到同一詞典，因此只須傳入一個list。他返回java Map物件。
    
    return set(dic.keySet())


if __name__ == '__main__':
    dic = load_dictionary()
    print(len(dic))
    print(list(dic)[0])
