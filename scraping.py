from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# -----PR TIMEZ-----
# ヘルステック
with urlopen("https://prtimes.jp/main/action.php?run=html&page=searchkey&search_word=%E3%83%98%E3%83%AB%E3%82%B9%E3%83%86%E3%83%83%E3%82%AF") as res:
    html_PRTIMEZ_1 = res.read().decode("utf-8")

soup_PRTIMEZ_1 = BeautifulSoup(html_PRTIMEZ_1, "html.parser") # BeautifulSoupに渡す
news_PRTIMEZ_1 = soup_PRTIMEZ_1.findAll('article', class_='list-article') # 指定クラスだけを抽出

for i in news_PRTIMEZ_1:
    link_PRTIMEZ_1 = i.find('a') # 記事へのリンクを取ってくる
    print(link_PRTIMEZ_1.text.strip())# a要素のtextを取得
    print("https://prtimes.jp" + link_PRTIMEZ_1['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得

# ヘルスケア
with urlopen("https://prtimes.jp/main/action.php?run=html&page=searchkey&search_word=%E3%83%98%E3%83%AB%E3%82%B9%E3%82%B1%E3%82%A2") as res:
    html_PRTIMEZ_2 = res.read().decode("utf-8")

soup_PRTIMEZ_2 = BeautifulSoup(html_PRTIMEZ_2, "html.parser") # BeautifulSoupに渡す
news_PRTIMEZ_2 = soup_PRTIMEZ_2.findAll('article', class_='list-article') # 指定クラスだけを抽出

for i in news_PRTIMEZ_2:
    link_PRTIMEZ_2 = i.find('a') # 記事へのリンクを取ってくる
    print(link_PRTIMEZ_2.text.strip())# a要素のtextを取得
    print("https://prtimes.jp" + link_PRTIMEZ_2['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得

# 訪問看護
with urlopen("https://prtimes.jp/main/action.php?run=html&page=searchkey&search_word=%E8%A8%AA%E5%95%8F%E7%9C%8B%E8%AD%B7") as res:
    html_PRTIMEZ_3 = res.read().decode("utf-8")

soup_PRTIMEZ_3 = BeautifulSoup(html_PRTIMEZ_3, "html.parser") # BeautifulSoupに渡す
news_PRTIMEZ_3 = soup_PRTIMEZ_3.findAll('article', class_='list-article') # 指定クラスだけを抽出

for i in news_PRTIMEZ_3:
    link_PRTIMEZ_3 = i.find('a') # 記事へのリンクを取ってくる
    print(link_PRTIMEZ_3.text.strip())# a要素のtextを取得
    print("https://prtimes.jp" + link_PRTIMEZ_3['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得



# -----BRIDGE-----
# ヘルステック
with urlopen("https://thebridge.jp/?s=%E3%83%98%E3%83%AB%E3%82%B9%E3%83%86%E3%83%83%E3%82%AF&post_type=post") as res:
    html_BRIDGE_1 = res.read().decode("utf-8")

soup_BRIDGE_1 = BeautifulSoup(html_BRIDGE_1, "html.parser") # BeautifulSoupに渡す
news_BRIDGE_1 = soup_BRIDGE_1.findAll('h1', class_='entry-title') # 指定クラスだけを抽出

for i in news_BRIDGE_1:
    link_BRIDGE_1 = i.find('a') # 記事へのリンクを取ってくる
    print(link_BRIDGE_1.text.strip())# a要素のtextを取得
    print(link_BRIDGE_1['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得
    print('')

# ヘルスケア
with urlopen("https://thebridge.jp/?s=%E3%83%98%E3%83%AB%E3%82%B9%E3%82%B1%E3%82%A2&post_type=post") as res:
    html_BRIDGE_2 = res.read().decode("utf-8")

soup_BRIDGE_2 = BeautifulSoup(html_BRIDGE_2, "html.parser") # BeautifulSoupに渡す
news_BRIDGE_2 = soup_BRIDGE_2.findAll('h1', class_='entry-title') # 指定クラスだけを抽出

for i in news_BRIDGE_2:
    link_BRIDGE_2 = i.find('a') # 記事へのリンクを取ってくる
    print(link_BRIDGE_2.text.strip())# a要素のtextを取得
    print(link_BRIDGE_2['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得
    print('')

# 訪問看護
with urlopen("https://thebridge.jp/?s=%E8%A8%AA%E5%95%8F%E7%9C%8B%E8%AD%B7&post_type=post") as res:
    html_BRIDGE_3 = res.read().decode("utf-8")

soup_BRIDGE_3 = BeautifulSoup(html_BRIDGE_3, "html.parser") # BeautifulSoupに渡す
news_BRIDGE_3 = soup_BRIDGE_3.findAll('h1', class_='entry-title') # 指定クラスだけを抽出

for i in news_BRIDGE_3:
    link_BRIDGE_3 = i.find('a') # 記事へのリンクを取ってくる
    print(link_BRIDGE_3.text.strip())# a要素のtextを取得
    print(link_BRIDGE_3['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得
    print('')



# -----tech crunch-----
# Health tech
with urlopen("https://search.techcrunch.com/search;_ylc=X3IDMgRncHJpZANKSU5JekkzOFJ5S3dvcUYzcDhEOFpBBG5fc3VnZwM5BHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMxMQRxdWVyeQNIZWFsdGglMjB0ZWNoBHRfc3RtcAMxNjczMDE1Njk2?p=Health+tech&fr=techcrunch") as res:
    html_techcrunch_1 = res.read().decode("utf-8")

soup_techcrunch_1 = BeautifulSoup(html_techcrunch_1, "html.parser") # BeautifulSoupに渡す
news_techcrunch_1 = soup_techcrunch_1.findAll('h4', class_='pb-10') # 指定クラスだけを抽出

for i in news_techcrunch_1:
    link_techcrunch_1 = i.find('a') # 記事へのリンクを取ってくる
    print(link_techcrunch_1.text.strip())# a要素のtextを取得
    print(link_techcrunch_1['href']) # 記事のURLを取得
    # print(i.find('time').text) # 記事の日付を取得
    print('')

# # Health care
# with urlopen("https://search.techcrunch.com/search;_ylt=Awr98BaQMbhjyZMHBAinBWVH;_ylc=X1MDMTE5NzgwMjkxOQRfcgMyBGZyA3RlY2hjcnVuY2gEZ3ByaWQDR0tieW4yN29UN3lJTlcxSWpyQkFFQQRuX3JzbHQDMARuX3N1Z2cDOQRvcmlnaW4Dc2VhcmNoLnRlY2hjcnVuY2guY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMxMQRxdWVyeQNIZWFsdGglMjBjYXJlBHRfc3RtcAMxNjczMDIwNjI2?p=Health+care&fr2=sb-top&fr=techcrunch") as res:
#     html_techcrunch_2 = res.read().decode("utf-8")

# soup_techcrunch_2 = BeautifulSoup(html_techcrunch_2, "html.parser") # BeautifulSoupに渡す
# news_techcrunch_2 = soup_techcrunch_2.findAll('h4', class_='pb-10') # 指定クラスだけを抽出

# for i in news_techcrunch_2:
#     link_techcrunch_2 = i.find('a') # 記事へのリンクを取ってくる
#     print(link_techcrunch_2.text.strip())# a要素のtextを取得
#     print(link_techcrunch_2['href']) # 記事のURLを取得
#     # print(i.find('time').text) # 記事の日付を取得
#     print('')

# # nurse
# with urlopen("https://search.techcrunch.com/search;_ylt=AwrOp9HRRLhjC9EGiNKnBWVH;_ylc=X1MDMTE5NzgwMjkxOQRfcgMyBGZyA3RlY2hjcnVuY2gEZ3ByaWQDaVVTN2Z3OHBROWlyd0Y3UnVGd19uQQRuX3JzbHQDMARuX3N1Z2cDNwRvcmlnaW4Dc2VhcmNoLnRlY2hjcnVuY2guY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM1BHF1ZXJ5A251cnNlBHRfc3RtcAMxNjczMDIwNzQz?p=nurse&fr2=sb-top&fr=techcrunch") as res:
#     html_techcrunch_3 = res.read().decode("utf-8")

# soup_techcrunch_3 = BeautifulSoup(html_techcrunch_3, "html.parser") # BeautifulSoupに渡す
# news_techcrunch_3 = soup_techcrunch_3.findAll('h4', class_='pb-10') # 指定クラスだけを抽出

# for i in news_techcrunch_3:
#     link_techcrunch_3 = i.find('a') # 記事へのリンクを取ってくる
#     print(link_techcrunch_3.text.strip())# a要素のtextを取得
#     print(link_techcrunch_3['href']) # 記事のURLを取得
#     # print(i.find('time').text) # 記事の日付を取得
#     print('')

