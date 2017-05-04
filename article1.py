#encoding=utf-8
import jieba
import io

jieba.set_dictionary('./extra_dict/dict.txt.big')

with io.open('./data/article1.txt', 'r' ,encoding='utf8') as f:
   content=f.read()

print( type(content))
print "Input：", content

words = jieba.tokenize(content)

print "Output in Full Mode："
for tk in words:
    print "word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2])


# exit()
#=======
import jieba.analyse
tags = jieba.analyse.extract_tags(content, 10)

print "Output："
print ",".join(tags)
# 程式中的 jieba.analyse.extract_tags(content, 10)，就是告訴 jieba 我們
# 要從這個文章中取出前 10 個 tf-idf 值最大的關鍵詞。

#=============
import jieba.posseg as pseg
words = pseg.cut(content)
for w in words:
   print('%s %s' % (w.word, w.flag))
