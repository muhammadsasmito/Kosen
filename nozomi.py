import MeCab
import codecs
import os
import math

def mecab(file):
    m = MeCab.Tagger('-Owakati')
    with codecs.open(file, 'r', 'utf-8') as fin:
        text = fin.read()
    result = m.parse(text)

    separated_text = result.split(" ")

    return separated_text



def g_ngram(text, n):
    box = []
    for i in range(len(text)-1):
        box.append("".join(text[i:i+n]))
    return box



def g_tf(box):
    dict = {}
    for word in box:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict



def tf():
    text = mecab('data/001.txt')
    ngram = g_ngram(text, 1)
    dict = g_tf(ngram)
    with codecs.open('tf.txt', 'w', 'utf-8') as fout:
        for key, value in sorted(dict.items()):
            value = (float(value)/float(len(dict)))
            fout.write(key+"\t"+str(value)+"\n")



def idf():
    all_list = []
    idf_dict = {}
    files = os.listdir('data')
    for file in files:
        text = mecab('data/'+file)
        ngram = g_ngram(text, 1)
        tf_dict = g_tf(ngram)
        all_list += list(tf_dict.keys())

    for word in all_list:
        if word in idf_dict:
            idf_dict[word] += 1
        else:
            idf_dict[word] = 1

    with codecs.open('idf.txt', 'w', 'utf-8') as fout:
        for key, value in sorted(idf_dict.items()):
            value = math.log2(float(len(files))/float(value))+1
            fout.write(key+"\t"+str(value)+"\n")


tf()
idf()
