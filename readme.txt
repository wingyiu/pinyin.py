    Pinyin python module
    
    Origin:      Author:cleverdeng      E-mail:clverdeng@gmail.com (not reachable)
    
    forked by QingfengXia based on v0.9:  
                   (1)renamed class name from PinYin to Pinyin 
                   (2) for easy deployment, just copy pinyin.py and word.data into a folder/site-packages
                   (3) add encoding support, or it will not work for windows cmd prompt! 
                   (4) move load_word() (renamed as loaddict() ) into __init__(), to make API concise
                   (5) word.data  "ord(UNICODE)= list of pinyin", for quick loading and human readable check
                      why some unicode has multiple pinyin units??? 
                   (6) word.data  is  renamed  as "pinyin.data"
                   
    installation: 
                   copy the two files:  pinyin.py, pinyin.data , into your project folder, or under $PYTHONPATH
                   
    test:   testing code is under __main__ secion
                   python -m pinyin.py
                   
    suggested new features: 
                      (1)  traditional chinese support:    add new pairs into data file, using pinyin4j 's pinyindb
                      (2)  repr()   print the tones, print in two lines,  first line using ASCII char as tone -- / \ V
                      (3)  other  pinyin romanization resprensation styles:  Yale, Wade-Giles, etc
                      (4) consider python 3.x support: by replace print with print_function  for test()
                      (5) performance improvement, using better container than dict
                      
    see also: 
        (1) ruby    "Rubyºº×Ö×ªÆ´Òô hanzi_to_pinyin" 
              java  pinyin4j:   supports  6 pinyin resprensation styles:  Yale, Wade-Giles, etc
        (2) ibus-pinyin: phrase 
        (3) oopinyinguide: openoffice 3.x extension
        (4) Unicode for  greater Chinese charset: CJKV:  4E00-9FFF,  
              this pinyin.data (0x3400-9F2D) and (0x20000-0x2B6F8)
                   