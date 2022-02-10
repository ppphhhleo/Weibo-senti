# Weibo-senti
微博爬虫（可基于搜索关键词，爬取博文），对博文数据清洗，并利用百度aip情感分析（三分类）  

# 爬虫工具  
参照了以下工作成果： 
> https://github.com/dataabc/weibo-search.git  

具体使用说明，可在weibo-search文件夹README查看。使用时，请注意替换cookie    

# 词语级分析  
jieba关键词分析，TF-IDF、TextRank  

# 句子级情感分析
因需求粒度不大，借助百度aip情感分析，进行三分类。个人开发者测试，可免费调用，限制单日单功能调用次数50万次，限制每秒请求2次。  
> https://ai.baidu.com/tech/nlp_apply/sentiment_classify
在远端创建应用之后，可获取AppID、API Key、Secret Key，对应填入即可使用  

# To Do
* 可对数据标注aspect，构建模型训练分析
