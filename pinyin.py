#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    based on pinyin.py V0.9         Author:  cleverdeng     E-mail:clverdeng@gmail.com
    #https://github.com/pinyin.py.git
   
"""

__author__="Qingfeng Xia"
__version__ = '0.9a'
__all__ = ["Pinyin"]
#https://github.com/qingfengxia/pinyin.py.git

import os.path

"""
def convert_dict(input ):
    with file(dict_file) as f_obj:
        for f_line in f_obj.readlines():
            line = f_line.split('=') # try and except is costly, just using normal reading as data input is determinate!
            self.word_dict[line[0]] = line[1]
"""

class Pinyin(object):  #naming 
    def __init__(self,  encoding="utf-8",dict_file='pinyin.data'):
        self.word_dict = {}
        self.encoding=encoding
        fullpath=os.path.join(os.path.dirname(__file__), dict_file) # changed  #2
        self.dict_file = fullpath
        #
        self.loaddict()

    def loaddict(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                line = f_line.split('=') # try and except is costly, just using normal reading as data input is determinate!
                self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string="", showingtone=True, split=None):
        """  add a switch to show tone number: showingtone
        repr:   
        split :  controlled by switch now
        """
        result = []
        if not isinstance(string, unicode):
            string = string.decode(self.encoding) # it will not work for windows cmd prompt! if fixed encoding as utf-8
        
        for char in string:
            key = '%X' % ord(char)
            if showingtone:
                result.append(self.word_dict.get(key, char).split()[0].lower())
            else:
                result.append(self.word_dict.get(key, char).split()[0][:-1].lower())
        #        
        if split!=None and type(split)==type(' '):
            return split.join(result)
        else:
            return result


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
    #test.load_word()  # it shuld be done in ctor()
    import os
    #
    print "test with utf8 console encoding"
    string = "钓鱼岛是中国的"  #utf8  simplified chinese
    print "in: %s" % string
    print "out: %s" % str(test.hanzi2pinyin(string, showingtone=True))
    print "out: %s" % test.hanzi2pinyin_split(string, split="-")
    #
    str2="釣魚島是台灣的也是中國的" #utf8 traditional chinese
    print "in: %s" % str2
    print "out: %s" % str(test.hanzi2pinyin(str2, showingtone=True))
    

    
