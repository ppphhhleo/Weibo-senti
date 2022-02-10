# -*- coding: utf-8 -*-
import wordcloud
import jieba
import csv
import jieba.analyse
import jieba.posseg
from imageio import imread
import jiagu
from aip import AipNlp
import json
from collections import defaultdict, OrderedDict
import time
import re


# 使用百度aip 需要自行注册，创建应用，即可获取
""" 你的 APPID AK SK """
APP_ID = '' # 填入AppID
API_KEY = '' # 填入API_Key
SECRET_KEY = '' # 填入Secret_Key

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)  # 访问远端

# 读取微博正文
def get_tweets(datafile, tweetfile):
    num = 0
    csvfile = open(datafile ,'rt', encoding='utf-8')
    tweets = open(tweetfile, "w", encoding='utf-8')
    reader = csv.reader(csvfile)
    column = [row[4] for row in reader]
    # print (column)
    # 将所有微博正文 逐行写入tweets.txt文件
    # content = " "
    for item in column:
        num = num + 1
        print(num, item)
        tweets.write(item + '\n')
        # content = content + ' ' + str(item)
    # print (content)
    csvfile.close()
    tweets.close()

def cut_tweet(tweetfile, tokenfile):
    # 将所有微博正文 逐行读取，并逐行分词，并逐行写入分词后的文件
    num = 0
    tweet = open(tweetfile, "rt", encoding='utf-8')
    tweet_token = open(tokenfile, "w", encoding='utf-8')
    tweet_lines = tweet.readlines()
    for tweet_line in tweet_lines:
        tweet_con = tweet_line.strip('\n')
        tweet_tokens = jieba.cut(tweet_con)
        tweet_token.write(' '.join(tweet_tokens) + '\n')
        num = num + 1
        print(num)
    tweet.close()
    tweet_token.close()

def all_tweet(tokenfile, allfile):
    # 读取所有微博正文已经分词后的文件，所有博文统一写入list文件
    result = open(allfile,'w',encoding='utf-8')
    tweet_token_l = open(tokenfile, "rt", encoding="utf-8")
    tweet_token_ls = tweet_token_l.readlines()
    num = 0
    for l in tweet_token_ls:
        lc = l.strip('\n')
        num = num + 1
        print(num)
        result.write(lc + ' ')
    # result.write(" ".join(content_list))
    result.close()
    tweet_token_l.close()
    # print(" ".join(content_list))

# 获取停用词列表
def get_stopword_list(stopword):
    # stopword = "stop.txt"
    stop = open(stopword, 'r',encoding='utf-8')
    lines = stop.readlines()
    stop_list = []
    for line in lines:
        line = str(line.strip())
    # print(line)
        stop_list.append(line)
    stop.close()
    return stop_list
    # print(stop_list)

def wordcloud_get(str, stopword, cloudfile):
    # 生成词云
    # cloudfile = "test.png"
    # mask = imread("chinamap.jpg")
    w = wordcloud.WordCloud(width=1000,
                            font_path='./msyh.ttc',
                            background_color='white',
                            height=700, stopwords=stopword)
                            # mask = mask)
    w.generate(str.strip())
    w.to_file(cloudfile)

# 单条
def get_all_content(file):
    content_a = " "
    c = open(file, 'rt', encoding='utf-8')
    c_lines = c.readlines()
    for c_l in c_lines:
        c_l = c_l.strip()
        content_a = content_a + " " + str(c_l)
    return content_a

# 读取所有整合在一起的博文
def read_all(allfile):
    c = open(allfile, 'r', encoding='utf-8')
    con = str(c.read())
    c.close()
    return con

def extract_key(content, file):
    # 默认选取TOP 20，topK = 20
    print('-' * 40)
    print(" TF-IDF")
    # tfidf = open("Tf-IDF.txt", '')
    kf = open(file, 'w', encoding='utf-8')
    kf.write("-"*40 + '\n')
    kf.write('TF-IDF' + '\n')
    for x, w in jieba.analyse.extract_tags(content, withWeight=True):
        # print('%s %s' % (x, w))
        kf.write(str(x) + " " + str(w) + '\n')


    print('-' * 40)
    print(" TextRank")
    kf.write("-" * 40+ '\n')
    kf.write('TF-IDF'+ '\n')
    for x, w in jieba.analyse.textrank(content, withWeight=True):
        kf.write(str(x) + " " + str(w) + '\n')
        # print('%s %s' % (x, w))
    kf.close()

def senti(tweetfile):
    tw = open(tweetfile, 'rt', encoding='utf-8')
    tw_lines = tw.readlines()
    for tw_line in tw_lines:
        tw_line = tw_line.strip()
        print(tw_line, jiagu.sentiment(tw_line))


def clean(str):
    # print(str)
    # comp = re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5^#^，^。^“^”^.^【^】^：^:]')
    comp = re.compile('[^0-9^\u4e00-\u9fa5^#^，^。^“^”^.^【^】^：^:^+^-^！^!^？^?^、^《^》^<^>^%]')
    str = comp.sub('',str)
    # print(str)
    return str

def clean2(str):
    comp = re.compile('[^\u4e00-\u9fa5]') # 仅保留中文
    str = comp.sub('', str)
    return str

def pre1(tweetfile, newtweetfile):
    tweets = open(tweetfile, 'r', encoding='utf-8')
    ntweets = open(newtweetfile, 'a', encoding='utf-8')
    tweet_lines = tweets.readlines()
    num = 0
    for tweet in tweet_lines:
        tweet = tweet.strip('\n')
        tweet = clean(tweet)
        num = num + 1
        print(num, tweet)
        ntweets.write(tweet + '\n')
    tweets.close()
    ntweets.close()

def pre2(tweetfile, newtweetfile):
    tweets = open(tweetfile, 'r', encoding='utf-8')
    ntweets = open(newtweetfile, 'a', encoding='utf-8')
    tweet_lines = tweets.readlines()
    num = 0
    for tweet in tweet_lines:
        tweet = tweet.strip('\n')
        tweet = clean2(tweet)
        num = num + 1
        print(num, tweet)
        ntweets.write(tweet + '\n')
    tweets.close()
    ntweets.close()

def senti_baidu(tweetfile, sentijson, senticsv):
    tweets = open(tweetfile, 'r', encoding='utf-8')
    tweets_lines = tweets.readlines()
    tmp_list = []
    tmp_count = 0
    count_num = 0 # 如果与远端断开了，可以根据已完成情况，修改此变量，即可继续分析
    empty = ''
    connect_num = 0
    for tweet_line in tweets_lines[count_num:]:
        # 计算情感倾向
        # 如果是追加，先获取json中的列表
        if count_num != 0:
            tmp_json = open(sentijson, 'r', encoding='utf-8')
            tmp_list = json.load(tmp_json)
            tmp_json.close()

        # 避免发出请求过多被中断，每隔一段时间，暂停一下
        if connect_num <= 1500:
            connect_num = connect_num + 1
        else:
            connect_num = 0
            time.sleep(15)
        # 请求远端
        tweet_line = str(tweet_line.strip())
        re = client.sentimentClassify(tweet_line)

        # 如果是error 则跳过，error是因为博文长度过长，跳过
        if re.get('error_code', "Not Available") != "Not Available" :
            continue

        # 写入json 文件
        count_num = count_num + 1
        print(count_num, re)
        sjw = open(sentijson,'w',encoding='utf-8')
        tmp_list.append(re)
        json.dump(tmp_list, sjw, indent = 4,ensure_ascii=False)
        sjw.close()

        # 写入csv文件
        sc = open(senticsv, 'a', encoding='utf-8-sig',newline='')
        senti_writer = csv.writer(sc)
        # print(re['items'][0]['sentiment'], re['items'][0]['positive_prob'], re['items'][0]['negative_prob'], re['text'])
        senti_writer.writerow([re['items'][0]['sentiment'], empty, re['items'][0]['positive_prob'], re['items'][0]['negative_prob'], re['text']])
        sc.close()

        # 更新写入json文件的列表
        """
        sjr = open(sentijson, 'r', encoding='utf-8')
        tmp_list = json.load(sjr)
        sjr.close()
        """
        # 控制QPS
        tmp_count += 1
        if tmp_count == 2 :
            time.sleep(1)
            tmp_count = 0


def filter(sentifile, filterfile):
    # 过滤掉含有【的博文，通常是媒体报道的博文
    sentitw = open(sentifile,'r',encoding='utf-8')
    fi = open(filterfile+"filter.csv", 'w', encoding='utf-8',newline='')
    senti_reader = csv.reader(sentitw)
    sen_writer = csv.writer(fi)
    for sen in senti_reader:
        if '【' in sen[4]:
            continue
        else:
            sen_writer.writerow(sen)
    fi.close()
    sentitw.close()


def statistic(filterfile, posfile, negfile, neufile):
    data = open(filterfile, 'rt', encoding='utf-8')
    postw = open(posfile, 'w', encoding='utf-8-sig',newline='')
    negtw = open(negfile, 'w', encoding='utf-8-sig', newline='')
    neutw = open(neufile, 'w', encoding='utf-8-sig',newline='')
    pos_writer = csv.writer(postw)
    neg_writer = csv.writer(negtw)
    neu_writer = csv.writer(neutw)
    data_reader = csv.reader(data)
    positive_count = 0
    negative_count = 0
    positive_value = 0
    negative_value = 0
    netural_count = 0
    for line in data_reader:
        # print(line)
        if line[0] == '0':
            tmp = float(line[3]) # 消极
            print(tmp)
            negative_count = negative_count + 1
            negative_value = negative_value + float(tmp)
            neg_writer.writerow(line)
            # continue
        if line[0] == '2':
            tmp = float(line[2]) # 积极

            positive_count = positive_count + 1
            positive_value = positive_value + float(tmp)
            pos_writer.writerow(line)
            #continue
        if line[0] == '1':
            netural_count = netural_count + 1
            neu_writer.writerow(line)
    print("positive tweets: " + str(positive_count)  + " 条； ", ("%.7f")%(positive_value / positive_count))
    print("negative tweets: " + str(negative_count) + " 条；", ("%.7f")%(negative_value /negative_count))
    print("neutral tweets: " + str(netural_count) + " 条；")



if __name__ == '__main__':

    jieba.load_userdict("useradd.txt")  # 可以添加保留的词汇

    ofile = "课后服务"  # 爬取所得数据的关键词

    print('-'*40)
    print("读取博文")
    get_tweets(ofile + ".csv", ofile + ".txt")  # 将csv文件所有博文读取 写入 txt文件

    print('-'*40)
    print("预处理文本，仅保留中文，用于关键词和词云生成")
    pre2(ofile + ".txt", ofile + "onlyc.txt")  # 词语级别，之后分词，用于关键词提取

    print('-' * 40)
    print("预处理文本，保留标点符号，用于情感分析")
    pre1(ofile + ".txt", ofile + "sentence.txt") # 句子级别，之后情感分析

    print('-' * 40)
    print("博文分词")
    cut_tweet(ofile+"onlyc.txt", ofile+"tokens.txt")  # 将 所有博文 逐条分词 保存

    print('-' * 40)
    print("整合所有博文词语")
    all_tweet(ofile+"tokens.txt", ofile+"all.txt")   # 获取所有分词后的博文 连续的内容 ，为了获取词云和关键词
    content = read_all(ofile+"all.txt")

    print('-' * 40)
    print("对所有博文词语，提取关键词")
    extract_key(content, ofile+"key.txt")   # 关键词提取

    print('-' * 40)
    print("对所有博文词语，生成词云")
    stopwords = get_stopword_list("stop.txt")
    wordcloud_get(content, stopwords, ofile+"pic.png")

    print('-' * 40)
    print("对所有博文，逐条情感分析")
    senti_baidu(ofile+"sentence.txt",ofile+"senti.json",ofile+"senti.csv")

    print('-' * 40)
    print("对所有博文，筛选个体博文")
    filter(ofile + "senti.csv", ofile + "filter.csv")

    print('-' * 40)
    print("对筛选后的博文，进行极性分析")
    statistic(ofile + "filter.csv", ofile + "filterPos.csv", ofile + "filterNeg.csv", ofile + "filterNeu.csv")


