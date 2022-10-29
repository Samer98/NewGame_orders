from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from _datetime import datetime
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
login_url='https://newgame.fun/admin/?key=Game_Admn_Url'
payload = {
    'username':'Super_User',
    'password':'987654321'
}
with requests.Session() as session:
    result = session.post(login_url,data=payload, headers=headers)
    print(result.headers)
    cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
    orders = BeautifulSoup(result.text, "html.parser")
    # print(orders.prettify())
    orders_link = []
    for link in orders.find_all(href=True):
        if "order_id" in link['href']:
            orders_link.append(str(link['href']))

    # print(orders_link)
    first_order = orders_link[2]
    print(first_order)
    first_order_result = session.post(first_order,headers=headers)
    first_order_result_data = BeautifulSoup(first_order_result.text, "html.parser")
    # print(first_order_result_data)



    for details in first_order_result_data.find_all(class_="fa fa-phone fa-fw"):
        telephone = (details.parent.parent.parent.contents[3].getText())
    page_contents=[]
    for details in first_order_result_data.find_all("td",class_='text-left'):
        page_contents.append(details.contents)
    print(page_contents[2])
    name = page_contents[2][0]
    address = page_contents[2][2]
    district = page_contents[2][4]

    total_price=[]
    for details in first_order_result_data.find_all("td",class_='text-right'):
        total_price.extend(details.contents)

    total_price= total_price[-1]
    # print(total_price)

client_details=[]
client_details.extend([name,telephone,address,district,total_price[:-3]])
print(client_details)
    # try:
#         video = game.find('iframe')
#         video_link= video['src']
#         video_link= video_link.replace('embed/',"watch?v=")
#     except:
#         video_link ="None"
#         pass
#     try:
#         games.append({"game":title.string.strip()[:-12],
#             "url":url,
#             "description":desc.text.strip(),
#             "youtube_link":video_link,
#             "original_price":int(price.string.strip()[3:-3].replace(",", '')),
#             "discount_price":int(discount.string.strip()[3:-3].replace(",", '')),
#             "images":image_links,
#             "is_in_stock": buy_button == "Add to Cart",
#             "language": language,
#             "SEO_EN": SEO_EN,
#             "SEO_AR": SEO_AR,
#         })
#     except:
#             price = game.find(id="ProductPrice-product-template")
#             games.append({"game":title.string.strip()[:-12],
#             "url":url,
#             "description":desc.text.strip(),
#             "youtube_link":video_link,
#             "original_price":int(price.string.strip()[3:-3].replace(",", '')),
#             "discount_price":"None",
#             "images":image_links,
#             "is_in_stock": buy_button == "Add to Cart",
#             "language": language,
#             "SEO_EN": SEO_EN,
#             "SEO_AR": SEO_AR,
#             })
#             # issue_links.append(url)
#
#     print(f"{url} done")
#     # i = i+1
#     # if i == 3:
#     #     break
# # print(games)
# with open("game_information", "w",encoding='utf-8') as fp:
#     json.dump(games,fp)
#
# with open('issue_links.txt', 'w') as f:
#     for issue_link in issue_links:
#      f.write(issue_link)
#      f.write("\n")
#
# now = datetime.now()
# print ("The time is now: = %s:%s:%s" % (now.hour, now.minute, now.second))
