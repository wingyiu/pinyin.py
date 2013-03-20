    Pinyin python module
    
    Origin:      Author:cleverdeng      E-mail:clverdeng@gmail.com (not reachable)
    
    forked by QingfengXia based on v0.9:  
                   (1)renamed class name from PinYin to Pinyin, 
                   (2)dict file "word.data"  is  renamed  as "pinyin.data" 
                   (3) add encoding support, or it will not work for windows cmd prompt! 
                   (4) move load_word() (renamed as loaddict() ) into __init__(), to make API concise
                   (5) word.data  "ord(UNICODE)= list of pinyin", for quick loading and human readable check
                      why some unicode has multiple pinyin units??? 
                   
    installation: 
                   copy the two files:  pinyin.py, pinyin.data , into your project folder, or under $PYTHONPATH
                   
    test:   testing code is under __main__ secion
                   python -m pinyin.py
                   
    suggested new features: 
                      (1)  traditional chinese support:    done!
                      (2)  repr()   print the tones, print in two lines,  first line using ASCII char as tone -- / \ V
                      (3)  other  pinyin romanization styles:  Yale, Wade-Giles, etc, using pinyin4j 's pinyindb
                      (4) consider python 3.x support: by replace print with print_function  for test()
                      (5) performance improvement, using better container than dict
                      
    see also: 
        (1) ruby    "Ruby module:  hanzi_to_pinyin" 
              java  pinyin4j:   supports  6 pinyin resprensation styles:  Yale, Wade-Giles, etc
        (2) ibus-pinyin: phrase 
        (3) oopinyinguide: openoffice 3.x extension
        (4) Unicode for  greater Chinese charset: CJKV:  4E00-9FFF,  
              this pinyin.data (0x3400-9F2D) and (0x20000-0x2B6F8)
                   
    example:
    from pinyin import Pinyin
    def test_console(encoding='cp936'):
        import os
        if os.name=='nt':
            print "POSIX os input encoding is utf-8, for windows try cp936/gbk for simplified"
            test2=Pinyin(encoding=encoding)
            print "str(test.hanzi2pinyin(string)"
            s=raw_input("input hanzi string in windows console") # only for python 2.x
            print "pinyin for input hanzi are:"
            print test2.hanzi2pinyin(s)
                    
    
    if __name__ == "__main__":
        test = Pinyin()
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
        #test()
