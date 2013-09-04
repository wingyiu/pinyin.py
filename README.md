
                  
### 使用: 
拷贝`pinyin.py`, `pinyin.data` 到你的project下或者到$PYTHONPATH路径下
                  
### 测试
	python -m pinyin.py
                                    
### 示例
utf8 简体中文

    test = Pinyin()
    print "test with utf8 console encoding"
    
    string = "共产党一党专政何谈民族？hehe"  
    print "example 1 in: %s" % string
    print "example 1 out: %s" % test.hanzi2pinyin(string, showingtone=True)
    print "example 1 showingtone+split: %s" % test.hanzi2pinyin(string, showingtone=False, split=' ')
    

输出
	
	test with utf8 console encoding
	example 1 in: 共产党一党专政何谈民族？hehe
	example 1 out: gong4chan3dang3yi1dang3zhuan1zheng4he2tan2min2zu2？hehe
	example 1 showingtone+split: gong chan dang yi dang zhuan zheng he tan min zu  h e h e
	
    
utf8繁体中文

    str2="釣魚島是台灣的也是中國的" 
    print "in: %s" % str2
    print "out: %s" % str(test.hanzi2pinyin(str2, showingtone=True))
    
输出

	in: 釣魚島是台灣的也是中國的
	out: diao4yu2dao3shi4tai2wan1de5ye3shi4zhong1guo2de5
	
	
### 拓展阅读 
(1) ruby    "Ruby module:  hanzi_to_pinyin" 

(2）java  pinyin4j:   supports  6 pinyin resprensation styles:  Yale, Wade-Giles, etc

(3) ibus-pinyin: phrase 

(4) oopinyinguide: openoffice 3.x extension

(5) Unicode for  greater Chinese charset: CJKV:  4E00-9FFF,  
     this pinyin.data (0x3400-9F2D) and (0x20000-0x2B6F8)

    