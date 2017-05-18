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



def count_words(box):
    dict = {}
    for word in box:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict



def tf(file):
    text = mecab("data/"+file)
    ngram = g_ngram(text, 1)
    tf_dict = count_words(ngram)
    for key, value in sorted(tf_dict.items()):
        tf_dict[key] = (float(value)/float(len(tf_dict)))

    return tf_dict



def idf():
    all_list = []
    idf_dict = {}
    files = os.listdir('data')
    for file in files:
        text = mecab('data/'+file)
        ngram = g_ngram(text, 1)
        tf_dict = count_words(ngram)
        all_list += list(tf_dict.keys())

    for word in all_list:
        if word in idf_dict:
            idf_dict[word] += 1
        else:
            idf_dict[word] = 1

    for key, value in sorted(idf_dict.items()):
        idf_dict[key] = math.log2(float(len(files))/float(value))+1

    return idf_dict



def tf_idf(path):
    files = os.listdir('data')
    idf_dict = idf()
    with codecs.open(path, 'w', 'utf-8') as fout:
        for file in files:
            tf_dict = tf(file)
            fout.write(file+"\n")
            for key, value in sorted(tf_dict.items()):
                value = value * idf_dict[key]
                fout.write(key+"\t"+str(value)+"\n")

def index(path):
    idf_dict = {}
    inverted_index = {}

    files = os.listdir('data')
    for file in files:
        text = mecab('data/'+file)
        ngram = g_ngram(text, 1)
        tf_dict = count_words(ngram)
        for word in tf_dict.keys():
            if word in inverted_index:
                inverted_index[word].append(file)
            else:
                inverted_index[word] = [file]

    with codecs.open(path, 'w', 'utf-8') as fout:
        for key, value in sorted(inverted_index.items()):
            fout.write(key+"\t")
            for num in value:
                fout.write(num+"\t")
            fout.write("\n")

# tf_idf("sample.txt")
index("inverted_index.csv")
