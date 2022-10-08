from facebook_informations import (
        Facebook_Information,
        Dump_public,
        dprint,
        Information,
        Dump_follower,
    )
from facebook_informations import Find_ID_Facebook,Ceck_Aplication,TypeTable
import os,sys
import re 
import requests
from bs4 import BeautifulSoup


find_d = Find_ID_Facebook()

cookies = {
        "cookie":" masukan cookies anda di sini ..."
        }


#with requests.Session() as requ:
#    req = requ.get(
#            "https://mbasic.facebook.com/profile.php?v=friends",
#            cookies=cookies,
#            )
#so = BeautifulSoup(req.content,'html.parser')
#    td_ = so.find_all('td',attrs={"style":"vertical-align: middle"})
#    tabm = so.find_all('h3')
#    for dc in td_:
#        pass


#// testing number 1

information = Information()
lsd = information.information(
        idz_="me",
        async_with_cookies=True,
        async_with_token=True,
)


# // testing basic number 2
sys.exit(1)

url_like = "https://mbasic.facebook.com/ufi/reaction/profile/browser/?limit=5000&ft_ent_identifier="

with requests.Session() as requ:
    req = requ.get(
        url_like,cookies=cookies
        )
    so = BeautifulSoup(req.content, 'html.parser')
    c = so.find_all('h3')
    for d in c:
        for z in d.find_all('a'):
            nama = z.text
            user = z["href"].replace("profile.php?id=", "").split('=')[0].replace('/','').replace('&eav','').replace('?eav','')
            print(user)
    led = so.find('a',string="Lihat Selengkapnya")['href']
    req = requ.get(
            "https://mbasic.facebook.com"+led,cookies=cookies,
            )
    so = BeautifulSoup(req.content,'html.parser')
    
    led_a = so.find_all('a',href=True)
    for d in led_a:
        print(d['href'].split('=')[1])

# // testing number 3
sys.exit(1)

apps = Ceck_Aplication()
lsd = apps.ceck_apps(
        cookies_=cookies,
        view_href_total=True,
        url_aplication_type="inactive",
        )


