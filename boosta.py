from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import clipboard
# from newgame_orders import order_number_no_gui


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
login_url='https://newgame.fun/admin/?key=Game_Admn_Url'
payload_newgame = {
    'username':'Super_User',
    'password':'987654321'
}
def order_number_no_gui(order_number):
    # try:
    #     order_num = int(input('which order do you want to get ? '))
    #
    # except:
    #     order_num = 0
    with requests.Session() as session:
        result = session.post(login_url,data=payload_newgame, headers=headers)
        # print(result.headers)
        orders = BeautifulSoup(result.text, "html.parser")
        # print(orders.prettify())
        orders_link = []
        for link in orders.find_all(href=True):
            if "order_id" in link['href']:
                orders_link.append(str(link['href']))

        # print(orders_link)
        first_order = orders_link[order_number-1]
        # print(first_order)
        first_order_result = session.post(first_order,headers=headers)
        first_order_result_data = BeautifulSoup(first_order_result.text, "html.parser")
        # print(first_order_result_data)



        for details in first_order_result_data.find_all(class_="fa fa-phone fa-fw"):
            telephone = (details.parent.parent.parent.contents[3].getText())
        page_contents=[]
        for details in first_order_result_data.find_all("td",class_='text-left'):
            page_contents.append(details.contents)
        # print(page_contents)
        name = page_contents[2][0]
        address = page_contents[2][2]
        district = page_contents[2][4]

        prodcuts =[]
        for details in first_order_result_data.find_all("td",class_='text-left'):
            # print(details)
            try:
                prodcuts.append(details.contents[0].getText())
            except:
                continue

        quanitiy=[]
        for details in first_order_result_data.find_all("td",class_='text-right'):
            # print(details.contents)
            quanitiy.append(details.contents)
            # try:
            #     prodcuts.append(details.contents[0].getText())
            # except:
            #     continue
        print(quanitiy)


        total_price=[]
        for details in first_order_result_data.find_all("td",class_='text-right'):
            total_price.extend(details.contents)

        total_price= total_price[-1]
        # print(total_price)

    client_details=[]
    client_details.extend([name,telephone,address,district,total_price[:-3],prodcuts])
    return client_details
bosta_login_url='https://business.bosta.co/overview'
payload = {
    'Email':'newgame.help@gmail.com',
    'Password':'Newgame_bosta_4'
}
# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(options=options)
# driver.get("https://business.bosta.co/overview")
# username = driver.find_element_by_id("email")
# password = driver.find_element_by_id("password")
# username.send_keys("newgame.help@gmail.com")
# password.send_keys("Newgame_bosta_4")
# # This is the button for creating new order "متابعة"
# driver.find_element(By.XPATH, '//button[normalize-space()="متابعة"]').click()
# time.sleep(5)
# driver.get("https://business.bosta.co/create-order")
# page_loaded = False

client_details = order_number_no_gui(1)
print(client_details)

# client_name = driver.find_element_by_id("create-edit-order-form_receiver_fullName")
# telephone = driver.find_element_by_id("create-edit-order-form_receiver_phone")
# address = driver.find_element_by_id("create-edit-order-form_address_firstLine")
# district = driver.find_element_by_id("create-edit-order-form_address_city")
# total_price = driver.find_element_by_id("create-edit-order-form_cod")
# product=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/textarea') #Prodcut detials text area
# time.sleep(5)

# print(' '.join(client_details[5]))
# clipboard.copy(client_details[1])
# telephone.send_keys(Keys.CONTROL + 'v')
# client_name.send_keys(client_details[0])
# address.send_keys(client_details[2])
# district.send_keys(client_details[3])
# district.send_keys(Keys.ENTER)
# total_price.send_keys(client_details[4])
# product.send_keys(' , '.join(client_details[5]))
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div/span[2]/button[2]').click() #Click on order confimarion button "تاكيد الاوردر"
