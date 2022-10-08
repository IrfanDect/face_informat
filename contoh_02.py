from __style__.__style__ import (
        Base_Styled,
        get_colors,
    )
import locale
from facebook_informations import (
        Information,
        Dump_public,
        TypeTable,
        dprint,
        __removed__,
        Ceck_Aplication,
    )
from time import sleep as sleep
import os,sys

__removed__.run()

cek = Ceck_Aplication()

ingfo = Information()

message_get = """
{}Username :{} {}
{}Id    :{} {}
{}Brithday :{} {}
{}Email :{} {}
{}name  :{} {}
{}Firstname :{} {}
{}Gender :{} {} 
{}Lastname :{} {}
{}Locale :{} {}
{}Link :{} {}
"""

# // example 1
def Scripter(_):
    cli = Base_Styled(_,shadow=True,no_mouse=True)

    coded , userid = cli.INPUT_(
            ".",
            height = 8,
            width  = 50,
        ) 
    if coded == cli.button_y:
        informat = ingfo.information(
                idz_=userid,
                async_with_token=True,
                async_with_cookies=True,
            )
        try:
            message = cli.MESSAGE_(
                    message_get.format(
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['username'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['id'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['birthday'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['email'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['name'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['first_name'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['gender'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['last_name'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['locale'],
                        get_colors['biru'],
                        get_colors['reset'],
                        informat['link'],
                        ),
                    height = 17,
                    width  = 60,
                    style_all=True,
                    title  = " %sInformasi "%(get_colors['hejo']),
                )
        except KeyError :
            message = cli.MESSAGE_(
                    "Id : %s\nName : %s"%(informat['id'],informat['name'])
                ) 
    if coded == cli.button_x:
        coded , choicer = cli.MENU_(
                " .",
                choices=[
                    ('1','aplikasi kadaluarsa'),
                    ('2','aplikasi aktive'),
                    ('3','lihat aplikasi'),
                    ],
                style_all=True,
            )
        if coded == cli.button_y:
            if '1' == choicer:
                app = cek.ceck_apps(
                        view_href_total=True,
                        url_aplication_type="inactive",
                        cookies_={
                            "cookie":" masukan cookies anda .."
                            },
                        )
            else:
                raise SystemExit(1)

if __name__ == "__main__":
    Scripter(" Aplication ")

    



