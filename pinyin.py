#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    convert string contain Hans/Hant characters and ASCII printable characters
    to english characters
    
    把包含中文简繁体和英文字母符号的字符串转化成字母串
    要求中文字符是utf-8编码
   
"""

__author__="cleverdeng, qingfengXia"
__version__ = '0.9a'
__all__ = ["Pinyin"]


import os.path

class Pinyin(object):  #naming 
    def __init__(self,  encoding="utf-8",dict_file='pinyin.data'):
        self.word_dict = {}
        self.encoding=encoding
        fullpath=os.path.join(os.path.dirname(__file__), dict_file) # changed  #2
        self.dict_file = fullpath
        #
        self.loaddict()

    def loaddict(self):
        """
        加载字典
        """
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                line = f_line.split('=') # try and except is costly, just using normal reading as data input is determinate!
                self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string="", showingtone=False, split=None):
        """  
        把中文字符串转换为拼音字符串，英文字母不转
        string: 原含中文字的字符串
        showingtone: 是否输出以1234代表的音标
        split: 拼音的分隔字符，如' '、'-'
        """
        result = []
        if not isinstance(string, unicode):
            string = string.decode(self.encoding) # it will not work for windows cmd prompt! if fixed encoding as utf-8
        
        for char in string:
            intv = ord(char)
            if intv >31 and intv < 127: #跳过英文字母符号
                result.append(char.lower())
            else:
                key = '%X' % intv
                if showingtone:
                    result.append(self.word_dict.get(key, char).split()[0].lower())
                else:
                    result.append(self.word_dict.get(key, char).split()[0][:-1].lower())
        #        
        if split != None and type(split)==type(' '):
            return split.join(result)
        else:
            return ''.join(result)


    def hanzi2pinyin_split(self, string="", split=""):   # this could be merged into hanzi2pinyin()
        result = self.hanzi2pinyin(string=string)
        if split == "":
            return result
        else:
            return split.join(result)
            
def test_console(encoding='cp936'):
    if os.name=='nt':
        print "POSIX os input encoding is utf-8, for windows try cp936/gbk for simplified"
        test2=Pinyin(encoding=encoding)
        print "str(test.hanzi2pinyin(string)"
        s=raw_input("input hanzi string in windows console") # only for python 2.x
        print "pinyin for input hanzi are:"
        print test2.hanzi2pinyin(s)
                

if __name__ == "__main__":
    test = Pinyin()
    print "test with utf8 console encoding"
    
    #utf8  simplified chinese
    string = "共产党一党专政何谈民族？hehe"  
    print "example 1 in: %s" % string
    print "example 1 out: %s" % test.hanzi2pinyin(string, showingtone=True)
    print "example 1 showingtone+split: %s" % test.hanzi2pinyin(string, showingtone=False, split=' ')
    
    #utf8 traditional chinese
    str2="釣魚島是台灣的也是中國的" 
    print "in: %s" % str2
    print "out: %s" % str(test.hanzi2pinyin(str2, showingtone=True))
    

    
