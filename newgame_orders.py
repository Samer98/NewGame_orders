from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import json
import os
from _datetime import datetime
import time
import PySimpleGUI as sg

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
login_url='https://newgame.fun/admin/?key=Game_Admn_Url'
payload = {
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
        result = session.post(login_url,data=payload, headers=headers)
        print(result.headers)
        orders = BeautifulSoup(result.text, "html.parser")
        # print(orders.prettify())
        orders_link = []
        for link in orders.find_all(href=True):
            if "order_id" in link['href']:
                orders_link.append(str(link['href']))

        # print(orders_link)
        first_order = orders_link[order_number-1]
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
        prodcuts =[]
        for details in first_order_result_data.find_all("td",class_='text-left'):
            try:
                prodcuts.append(details.contents[0].getText())
            except:
                continue
        print(prodcuts)


        total_price=[]
        for details in first_order_result_data.find_all("td",class_='text-right'):
            total_price.extend(details.contents)

        total_price= total_price[-1]
        # print(total_price)

    client_details=[]
    client_details.extend([name,telephone,address,district,total_price[:-3],prodcuts])
    return client_details
def order_number(order_number):
    # try:
    #     order_num = int(input('which order do you want to get ? '))
    #
    # except:
    #     order_num = 0
    with requests.Session() as session:
        result = session.post(login_url,data=payload, headers=headers)
        print(result.headers)
        orders = BeautifulSoup(result.text, "html.parser")
        # print(orders.prettify())
        orders_link = []
        for link in orders.find_all(href=True):
            if "order_id" in link['href']:
                orders_link.append(str(link['href']))

        # print(orders_link)
        first_order = orders_link[order_number-1]
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
        prodcuts =[]
        for details in first_order_result_data.find_all("td",class_='text-left'):
            try:
                prodcuts.append(details.contents[0].getText())
            except:
                continue
        print(prodcuts)


        total_price=[]
        for details in first_order_result_data.find_all("td",class_='text-right'):
            total_price.extend(details.contents)

        total_price= total_price[-1]
        # print(total_price)

    client_details=[]
    client_details.extend([name,telephone,address,district,total_price[:-3],prodcuts])
    sg.popup_scrolled(client_details,title="order details")
###############################
def order_number(order_range):

    with requests.Session() as session:
        result = session.post(login_url,data=payload, headers=headers)
        print(result.headers)
        orders = BeautifulSoup(result.text, "html.parser")
        orders_link =[]
        client_details=[]
        for link in orders.find_all(href=True):
            if "order_id" in link['href']:
                orders_link.append(str(link['href']))

        for orders in range(order_range):
            order = orders_link[orders]
            print(order)
            order_result = session.post(order,headers=headers)
            order_result_data = BeautifulSoup(order_result.text, "html.parser")

            for details in order_result_data.find_all(class_="fa fa-phone fa-fw"):
                telephone = (details.parent.parent.parent.contents[3].getText())
            page_contents=[]
            for details in order_result_data.find_all("td",class_='text-left'):
                page_contents.append(details.contents)
            print(page_contents[2])
            name = page_contents[2][0]
            address = page_contents[2][2]
            district = page_contents[2][4]

            prodcuts =[]
            for details in order_result_data.find_all("td",class_='text-left'):
                try:
                    prodcuts.append(details.contents[0].getText())
                except:
                    continue
            print(prodcuts)


            total_price=[]
            for details in order_result_data.find_all("td",class_='text-right'):
                total_price.extend(details.contents)

            total_price= total_price[-1]
            # print(total_price)

            if order_range ==1:
                client_details.extend([name,telephone,address,district,total_price[:-3],prodcuts])
            else:
                client_details.append([name,telephone,address,district,total_price[:-3],prodcuts])
    print(client_details)
    sg.popup_scrolled(client_details,title="order details")


# order_number(3)
##############################
def order_num_layout():
    layout = [[sg.Text("order num settings")],
              [sg.Text("Write the order number"),sg.Input(s=5,key="-orderNumber-")],
              [sg.Button("Done")]
    ]
    window = sg.Window("order number", layout)

    while True:
        event,values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Done":
            order_number(int(values["-orderNumber-"]))
            break
    window.close()

######################
def order_range_layout():
    layout = [[sg.Text("orders range number settings")],
              [sg.Text("Write the how many orders you want"),sg.Input(s=5,key="-orderRange-")],
              [sg.Button("Done")]
    ]
    window = sg.Window("order Range", layout)

    while True:
        event,values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Done":
            order_number(int(values["-orderRange-"]))
            break
    window.close()
######################


layout = [
    [sg.Button("order number"),sg.Button("order range")],
    [sg.Exit(),sg.Button("Get newest order details")]
]

window = sg.Window("NewGame orders details", layout)

while True:
    event, values = window.read()
    print(event,values)
    if event in (sg.WINDOW_CLOSED,"Exit"):
        break
    if event == "Get newest order details":
        order_number(1)
    if event == "order number":
        order_num_layout()
    if event == "order range":
        order_range_layout()
window.close()
