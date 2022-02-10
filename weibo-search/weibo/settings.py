# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 10
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    #'cookie': 'XSRF-TOKEN=4FX2RW8a79gXl4Y65KLNeybw; SUB=_2A25M6IbODeRhGeVM6FoY8SjMyT2IHXVvn_8GrDV8PUNbmtAKLVTskW9NTiBSiyvUBhmEXG3_JlzDxd6QQK_1Xty8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFMi9YeFn-6pQner9kNzP_N5JpX5KzhUgL.FoeEe0n4eKq7eo22dJLoIXnLxKBLBo.L12eLxKqL12zL1h.LxKqL1-BL12-LxKML1K.LB.BLxKqL1-qLBoeLxKqLBo5LBonLxKBLBo.L12eLxKqL12zL1h.t; ALF=1674455581; SSOLoginState=1642919582; WBPSESS=45qgcWJZjsaqO7lGn5FzJk7z3rx0Ja5tUmasPVv2H1ORcr7H2c94r6HXyYgxR_L7DT_fnJp_ABhhzi71PvE6LI30DFW5af1k0DNU_8xnaZPscFjsgIg6sD_c7wcxZqj8jSFXNnNiZ6U6wy9s5GFbTw=='
    'cookie': 'XSRF-TOKEN=4FX2RW8a79gXl4Y65KLNeybw; SSOLoginState=1642919582; _s_tentry=weibo.com; Apache=9957178600976.717.1642920682450; SINAGLOBAL=9957178600976.717.1642920682450; ULV=1642920682481:1:1:1:9957178600976.717.1642920682450:; WBPSESS=45qgcWJZjsaqO7lGn5FzJk7z3rx0Ja5tUmasPVv2H1ORcr7H2c94r6HXyYgxR_L7DT_fnJp_ABhhzi71PvE6LHkbOIplIW7YknCNSYmbfYPr1SDAJDl072jSV59m1hq-OzJt7UkG34xnNG0cboX8nA==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFMi9YeFn-6pQner9kNzP_N5JpX5KMhUgL.FoeEe0n4eKq7eo22dJLoIXnLxKBLBo.L12eLxKqL12zL1h.LxKqL1-BL12-LxKML1K.LB.BLxKqL1-qLBoeLxKqLBo5LBonLxKBLBo.L12eLxKqL12zL1h.t; ALF=1674890756; SCF=Av8FNWZWDajJD1Ld897MJN6CLXttstgAn1qYiofveiaCL3ENSO_-kyYfM_v0b6v5dY8mUKKaB6ndKivAwnyiimE.; SUB=_2A25M9-rXDeRhGeVM6FoY8SjMyT2IHXVvhVsfrDV8PUNbmtB-LU72kW9NTiBSiy59ZhRXdMezL1TVTZYiRGlxIx7f'
    # 'cookie': 'XSRF-TOKEN=4FX2RW8a79gXl4Y65KLNeybw; SSOLoginState=1642919582; _s_tentry=weibo.com; Apache=9957178600976.717.1642920682450; SINAGLOBAL=9957178600976.717.1642920682450; ULV=1642920682481:1:1:1:9957178600976.717.1642920682450:; SCF=Av8FNWZWDajJD1Ld897MJN6CLXttstgAn1qYiofveiaCqfsIA1Sq6BYByTdVowHABY10ALdOCB-PaeRo1ViuqHo.; SUB=_2A25M9ji4DeRhGeVM6FoY8SjMyT2IHXVvgi1wrDV8PUNbmtAfLUfAkW9NTiBSiwBw6ux6K1kSf23mjU5yA_Om4uk-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFMi9YeFn-6pQner9kNzP_N5JpX5KMhUgL.FoeEe0n4eKq7eo22dJLoIXnLxKBLBo.L12eLxKqL12zL1h.LxKqL1-BL12-LxKML1K.LB.BLxKqL1-qLBoeLxKqLBo5LBonLxKBLBo.L12eLxKqL12zL1h.t; ALF=1674804327; WBPSESS=45qgcWJZjsaqO7lGn5FzJk7z3rx0Ja5tUmasPVv2H1ORcr7H2c94r6HXyYgxR_L7DT_fnJp_ABhhzi71PvE6LHkbOIplIW7YknCNSYmbfYPr1SDAJDl072jSV59m1hq-OzJt7UkG34xnNG0cboX8nA=='
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['开端']  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2021-12-4'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2022-01-27'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
# MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'
