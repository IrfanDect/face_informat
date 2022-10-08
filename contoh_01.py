from __style__.__style__ import (
        Base_Styled,
        get_colors,
        )

from facebook_informations import (
        Dump_public,
        Information,
        )

info = Information()

try:
    view_apk = open('.aplikasi.log','r').read()
except :
    print(' silahkan get_cek aplikasi terlebih dahulu .. ')

# style Text
def view_aplikasi():
    view = Base_Styled(" viewers ...",shadow=True)
    view.TEXT_(
            ".aplikasi.log",
            )
view_aplikasi()

# Style Message
def Type_Message():
    typer = Base_Styled(" viewers type ",shadow=True)
    typer.MESSAGE_(
            "\n\n%s"%(
                view_apk
                ),
            height=60,
            width=60,
            style_all=True,
            title= " %sAplikasi kadaluarsa "%(get_colors['hejo'])
        )
Type_Message()

# // face informasi

def informat():
    std = Base_Styled(' informasi ')
    coded , ued = std.INPUT_(
            "enter your id facebook ...",
            height=9,
            width=60,
        )
    if coded == std.button_y:
        me = info.information(
                idz_=ued,
                async_with_cookies=True,
                async_with_token=True,
            )
        pass

informat()
