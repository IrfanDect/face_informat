from facebook_informations import (
        dprint,
        Ceck_Aplication,
        __removed__,
        )

# // hapus __pycache__

__removed__.run()

# // cookies akun anda yang mau di cek aplikasi

cookies = {
        "cookie":" your cookies"
        }

# // example cek aplikasi 
app = Ceck_Aplication()

def C():
    apl = app.ceck_apps(
            view_href_total=True, # untuk meliat semua aplikasi
            url_aplication_type="inactive", # // active && inactive
            cookies_=cookies, # cookies yang di atas 
            )
    dprint(apl) # or  print jika mau menggunakan panel , dprint(..., use_panel=True, **kwars)

if __name__ == "__main__":
    C()
