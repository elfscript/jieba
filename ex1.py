#encoding=utf-8
import jieba

sentence = u"獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
print "Input：", sentence
words = jieba.cut(sentence, cut_all=False)
print u"Output 精確模式 Full Mode："
for word in words:
    print word

sentence = u"独立音乐需要大家一起来推广，欢迎加入我们的行列！"
print "Input：", sentence
words = jieba.cut(sentence, cut_all=False)
print u"Output 精確模式 Full Mode："
for word in words:
    print word
