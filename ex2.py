#encoding=utf-8
import jieba

jieba.set_dictionary('./extra_dict/dict.txt.big')
jieba.load_userdict("userdict.txt")

content = open('lyric2.txt', 'rb').read()

print "Input：", content

words = jieba.cut(content, cut_all=False)

print "Output 精確模式 Full Mode："
for word in words:
    print word
