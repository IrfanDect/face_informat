#!/usr/bin/env python3

# //+-------------+------------------------------------------------------------------------------+
# //| info        | infor                                                                        |
# //+=============+==============================================================================+
# //| craeted     | irfanDect                                                                    |
# //| version     | percobaan                                                                    |
# //| typed       | basic code (supaya gampang di pahami untuk pemula)                           |
# //| next_update | likers, dump-group , bot_reac, search_name ,bot_comment, bot_share , etc ... |
# //+-------------+------------------------------------------------------------------------------+

import requests
import json
from rich.panel import Panel
from rich import print as dpr
from rich import box
from rich.tree import Tree
from rich.table import Table
from bs4 import BeautifulSoup
from typing import (
        Optional,
        Callable,
        Union,
        Dict,
        Tuple,
        List,
        )
import re
from rich.tree import Tree   
import os,sys,time
import shutil
from file_login import *

# // remove sampah
class __removed__:
    sampah = [
            "__pycache__",
            "__style__/__pycache__",
        ]

    @classmethod
    def run(cls):
        try:
            [shutil.rmtree(parser) for parser in cls.sampah]
        except:
            pass

# // save_daftar aplikasi
save_aplikasi = open(".aplikasi.log",'w')

class Facebook_Information:
    def __init__(self):
        self.graph_url = "https://graph.facebook.com/"
        self.graph_access = "&access_token="
        self.graph_access_info = "?access_token="
        self.graph_friends = "?fields=friends.fields(name,id)"
        self.graph_follower = "/subscribers?limit="
        self.url_mbasic = "https://mbasic.facebook.com/"
        self.req_ses = requests.Session() 

class dprint:
    """
    args :
    +-------------+------------------------+
    | value1      | value2                 |
    +=============+========================+
    | use_tree    | bool -> False          |
    | use_panel   | bool -> False          |
    | style_panel | str -> colors -> [red] |
    +-------------+------------------------+
    """ 
    def __init__(self, text : str , 
                 use_panel : bool = False,
                 use_tree : bool = False,
                 style_panel : Optional[str] = "blue") -> Optional[Panel]:

        self.text = text
        self.use_panel = use_panel
        self.style_panel = style_panel
        self.use_tree = Tree

        if self.use_panel == True:
            dpr(Panel(self.text,
                    highlight=True,
                    border_style="%s"%(
                        self.style_panel
                        )
                    )
                ) 
        else:
            dpr(self.text)
            

class Information(
        Facebook_Information
        ):
    def information(self,
                    idz_ : Optional[str] = None,
                    async_with_token : bool = False,
                    async_with_cookies : bool = False,
                    ) -> None:
        self.idz_ = idz_
        self.async_with_token = async_with_token
        self.async_with_cookies = async_with_cookies

        if self.async_with_token and self.async_with_cookies == True:
            req = self.req_ses.get(
                    "%s%s%s%s"%(
                        self.graph_url,
                        self.idz_,
                        self.graph_access_info,
                        token_log,
                        ),cookies=cookies_log,
                    )
            self.js = json.loads(
                    req.text
                    )
            return self.js

class Dump_follower(
        Facebook_Information
        ):
    def dump_follower(
            self, idz_ : Optional[str] = None,
            async_with_token : bool = False,
            async_with_cookies : bool = False,
            limit : int = 0,
            ):
        self.idz_ = idz_
        self.async_with_token = async_with_token
        self.async_with_cookies = async_with_cookies
        self.limit = limit

        if self.async_with_token and async_with_cookies == True:
            req = self.req_ses.get(
                    "%s%s%s%s%s%s"%(
                    self.graph_url,
                    self.idz_,
                    self.graph_follower,
                    self.limit,
                    self.graph_access,
                    token_log,
                    ),cookies=cookies_log
                )
            self.js = json.loads(
                    req.text
                    )
            return self.js

class Dump_public(
        Facebook_Information
        ):
    def dump_me(
            self
            ):
        req = self.req_ses.get(
                "%sme%s%s%s"%(
                    self.graph_url,
                    self.graph_friends,
                    graph_access,
                    token_log,
                    ),cookies=cookies_log
                )
        self.js = json.loads(
                req.text
                )
        return self.js

    def dump_public(self,
                    async_with_token : bool = False,
                    async_with_cookies : bool = False,
                    token_ : str = "EAAAG",
                    cookies_ : Optional[Dict[str , str]] = None, 
                    idz_ : Optional[str] = None,
                    limit : Optional[int] = 0,
                    ) -> None:
        self.async_with_token = async_with_token
        self.async_with_cookies = async_with_cookies
        self.idz_ = idz_
        self.limit = limit
        self.token_ = token_
        self.cookies_ = cookies_
        
        if self.async_with_token and self.async_with_cookies == True:
            with requests.Session() as requ:
                req = requ.get(
                        "%s%s%s%s%s"%(
                            self.graph_url,
                            self.idz_,
                            self.graph_friends,
                            self.graph_access,
                            token_log
                            ),cookies=cookies_log
                        )
                self.js = json.loads(
                        req.text
                        )
                return self.js
        else:
            with requests.Session() as requ:
                req = requ.get(
                        "%s%s%s%s%s"%(
                            self.graph_url,
                            self.idz_,
                            self.graph_friends,
                            self.graph_access,
                            self.token_
                            ),cookies=self.cookies_
                        )
                self.js = json.loads(
                        req.text
                        )
                return self.js

class Find_ID_Facebook(
        Facebook_Information
        ):
    def find_id_facebook(
            self,
            username : str = "https://...",
            cookies_ : Optional[Dict[str, str]] = None,
        ) -> None:

        self.username = username
        self.cookies_ = cookies_

        req = BeautifulSoup(
                self.req_ses.get(
                    "https://mbasic.facebook.com/%s"%(
                        self.username,
                        ),
            cookies=self.cookies_).content, features='html.parser')
        lfind_ = req.find('a',string='Lainnya')['href'].split("=")[1]
        return lfind_.replace(
                "&paipv",""
                )

class Ceck_Aplication(
        Facebook_Information
        ):
    """args : 
    Menggunakan Coding Beruntun(coding basic) Tidak di recomendasikan Codingan kek Gini Karna sangat tidak
    efisien & memperlambat waktu + terlalu mempersulit hidup , kalau udah jago tinggal loop aja beres 

    [#] jika minat saya jual yang open source + simple code + all fiktur crack max_=(3 orang)
    +---------------------+--------+--------------------+
    | value1              | value2 | value3             |
    +=====================+========+====================+
    | view_href_total     | bool   | pengembamgan       |
    | cookies_            | str    | cookies akun       |
    | url_aplication_type | str    | active -> inactive |
    +---------------------+--------+--------------------+
    """
    def ceck_apps(self,
                  view_href_total : bool = False,
                  url_aplication_type : str = "active",
                  cookies_ : Optional[Dict[str, str]] = None,
                  ) -> Optional[None]:
        self.cookies_ = cookies_
        self.url_aplication_type = url_aplication_type
        self.view_href_total = view_href_total


        tree = Tree(
                " 📦 [blue bold]aplikasi %s"%(
                    self.url_aplication_type,
                    ),
                style="green bold")
        if self.view_href_total == True:
            try:
                req = BeautifulSoup(
                        self.req_ses.get(
                            f"https://mbasic.facebook.com/settings/apps/tabbed/?tab=%s"%(
                                url_aplication_type
                                ),
                            cookies=self.cookies_
                                    ).content,"html.parser")
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_d = req.find('a',string='Lihat Lainnya')['href']
                
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_d,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                
                self.parser_c = req.find('a',string='Lihat Lainnya')['href']

                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_c,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_b = req.find('a',string='Lihat Lainnya')['href']

                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_b,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')
                    
                self.parser_a = req.find('a',string='Lihat Lainnya')['href']

                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_a,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_e = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_e,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_f = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_f,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_g = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_g,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')
                    
                self.parser_h = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_h,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_i = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_i,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_j = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_j,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_k = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_k,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_l = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_l,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                self.parser_m = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_m,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')
                
                self.parser_n = req.find('a',string='Lihat Lainnya')['href']
                 
                req = BeautifulSoup(
                        self.req_ses.get(
                            "https://mbasic.facebook.com"+self.parser_n,
                            cookies=self.cookies_
                            ).content,'html.parser'
                        )
                for parser in req.find_all('h3'):
                    tree.add(parser.text)
                    save_aplikasi.write(parser.text + '\n')

                return tree
            except TypeError:

                return tree
                dpr(f"[blue bold] total [white]:[green]href < {self.view_href_total}")

        if self.view_href_total == False:
            req = BeautifulSoup(
                        self.req_ses.get(
                            f"https://mbasic.facebook.com/settings/apps/tabbed/?tab=%s"%(
                             self.url_aplication_type,
                            ),
                        cookies=self.cookies_
                    ).content,'html.parser'
                )
            for parser in req.find_all('h3'):
                tree.add(parser.text)
                save_aplikasi.write(parser.text + '\n')
            return tree

class TypeTable:
    def __init__(self, text : str = "text") -> str:
        self.text = text

        listjson = [
                "id",
                "birthday",
                "education",
                "email",
                "first_name",
                "gender",
                "last_name",
                "link",
                "locale",
                "name",
                "timezone",
                "updated_time",
                "username",
                "excpet_error ",
                "verified",
        ]

        tab = Table(
                highlight=True,
                box=box.SQUARE_DOUBLE_HEAD,
                border_style="gray23 bold"
            )
        
        tab.add_column(
                "info_list",
                style="blue bold",
                header_style="red bold",
                )
        tab.add_column(
                "information",
                header_style="red bold",
                )
        for cpr in listjson:
            try:
                tab.add_row(
                    f"{cpr}","%s"%(self.text[cpr])
                )
            except KeyError:
                tab.add_row(
                        "[red bold]example_error "," ... ",
                        )
        dpr(tab)
