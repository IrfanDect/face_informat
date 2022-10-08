#// mengunakan coding beruntun(coding basic)

from dialog import Dialog
from typing import (
        Optional,
        List,
        Dict,
        Tuple
    )
import subprocess

# // warna -> underline , bold , reverse , italic 
get_colors = {
        "berem"   : "\Zb\Z1",
        "hejo"    : "\Zb\Z2",
        "koneng"  : "\Zb\Z3",
        "biru"    : "\Zb\Z4",
        "ungu"    : "\Zb\Z5",
        "cyan"    : "\Zb\Z6",
        "bodas"   : "\Zb\Z7",
        "hideung" : "\Zb\Z0",
        "reset"   : "\Zn",
    }

# // create ->
class Base_Styled:
    def __init__(self,
                 bg_title : str            = "___name___",
                 shadow   : Optional[bool] = False,
                 no_mouse : Optional[bool] = False,
                 no_lines : Optional[bool] = False,
            ) -> Optional[Dialog]:

        self.bg_title   = bg_title
        self.no_lines   = no_lines
        self.no_mouse   = no_mouse
        self.shadow     = shadow
        self.aplication = Dialog(
                dialog  = "dialog"
                ) 
        self.set_ = self.aplication.set_background_title(
                "%s"%(
                    self.bg_title,
                    )
                )
        self.remove_f = ".aplikasi"
        self.l_oke = " oke "
        self.l_cancel = " cancel "
        self.add_f = ".aplikasi.log"
        self.aplication.add_persistent_args(
                [
                    '--no-nl-expand'
                    ]
                )
        self.message_   = self.aplication.msgbox
        self.info_      = self.aplication.infobox 
        self.input_     = self.aplication.inputbox
        self.menu_      = self.aplication.menu
        self.button_y   = self.aplication.OK
        self.button_x   = self.aplication.CANCEL
        self.button_h   = self.aplication.HELP
        self.button_e   = self.aplication.EXTRA
        self.dceck_list = self.aplication.checklist
        self.text_text  = self.aplication.textbox
        self.edit       = self.aplication.editbox
        self.tailb      = self.aplication.tailbox
        self.scroll     = self.aplication.scrollbox
        self.progressb  = self.aplication.progressbox
        self.program    = self.aplication.programbox
        self.yesno      = self.aplication.yesno

    def INPUT_(self,
               text         : str            = "", 
               height       : int            = 10,
               width        : int            = 40,
               style_all    : bool           = False,
               title        : str            = "", 
               l_oke        : str            = " oke ",
               l_cancel     : str            = " cancel ",
               add_label_E  : Optional[bool] = False,
               add_label_H  : Optional[bool] = False,
               name_label_H : str            = " help ",
               name_label_E : str            = " extra ",
               **kwargs
            )-> Optional[Dialog]:

        self.text         = text
        self.height       = height
        self.width        = width
        self.style_all    = style_all
        self.title        = title
        self.add_label_E  = add_label_E
        self.add_label_H  = add_label_H
        self.name_label_E = name_label_E
        self.name_label_H = name_label_H


        self.startup = self.input_(
                self.text,
                height       = self.height,
                width        = self.width,
                ok_label     = l_oke,
                cancel_label = l_cancel,
                colors       = self.style_all,
                help_button  = self.add_label_H,
                extra_button = self.add_label_E,
                extra_label  = self.name_label_E,
                help_label   = self.name_label_H,
                shadow       = self.shadow,
                no_mouse     = self.no_mouse,
                no_lines     = self.no_lines,
            )
        return self.startup

    def MENU_(self,
              text      : str                   = "",
              choices   : List[Tuple[str, str]] = [],
              height    : int                   = 10,
              width     : int                   = 40,
              style_all : Optional[bool]        = False,
              l_oke     : str                   = " oke ",
              l_cancel  : str                   = " cancel ",
              **kwargs,
            ) -> Optional[Dialog]:

        self.text         = text
        self.choices      = choices
        self.height       = height
        self.width        = width
        self.style_all    = style_all

        self.startup = self.menu_(
                self.text,
                choices      = self.choices,
                colors       = self.style_all,
                height       = self.height,
                width        = self.width,
                ok_label     = l_oke,
                cancel_label = l_cancel,
                shadow       = self.shadow,
                no_mouse     = self.no_mouse,
                no_lines     = self.no_lines,
            )
        return self.startup

    def DCECK_(self,
               text      : str                    = "",
               choices   : List[Tuple[str , str]] = [],
               height    : Optional[int]          = 10,
               width     : Optional[int]          = 50,
               style_all : Optional[bool]         = False,
               l_oke     : str                    = " oke ",
               l_cancel  : str                    = " cancel ",
               **kwargs 
            ) -> Optional[Dialog]:

        self.text      = text
        self.height    = height
        self.width     = width
        self.style_all = style_all
        self.choices   = choices
        self.l_oke     = l_oke
        self.l_cancel  = l_cancel

        self.startup = self.dceck_list(
                self.text,
                choices      = self.choices,
                height       = self.height,
                width        = self.width,
                colors       = self.style_all,
                ok_label     = l_oke,
                cancel_label = l_cancel,
                shadow       = self.shadow,
                no_mouse     = self.no_mouse,
                no_lines     = self.no_lines,
            )
        return self.startup

    def INFO_(self,  
              text      : str            = "",
              height    : Optional[int]  = 10 ,
              width     : Optional[int]  = 40,
              style_all : Optional[bool] = False,
              title     : str            = "", **kwargs,
            ) -> Optional[Dialog]:

        self.text      = text;self.height     = height;self.width = width
        self.style_all = style_all;self.title = title

        self.startup = self.info_(
                self.text,
                colors   = self.style_all,
                height   = self.height,
                width    = self.width,
                title    = self.title,
                shadow   = self.shadow,
                no_mouse = self.no_mouse,
                no_lines = self.no_lines,
        )
        return self.startup

    def TEXT_(self,
              file_path : str           = None,
              title     : str           = "",
              height    : Optional[int] = None,
              width     : Optional[int] = 60,
              **kwargs,
            )-> Optional[Dialog]:

        self.file_path = file_path
        self.title     = title
        self.height    = height
        self.width     = width

        self.startup = self.text_text(
                file_path,
                exit_label = " keluar ",
                title      = self.title,
                height     = self.height,
                width      = self.width,
                colors     = True,
                shadow     = self.shadow,
                no_mouse   = self.no_mouse,
                no_lines   = self.no_lines,
            )
        return self.startup
    
    def MESSAGE_(
            self,
            text      : Optional[str]  = "",
            height    : int            = 0,
            width     : int            = 0,
            style_all : Optional[bool] = False,
            title     : str            = "",
            **kwargs
            ) -> Optional[Dialog] :

        self.text       = text
        self.height     = height
        self.width      = width
        self.style_all  = style_all
        self.title      = title

        self.startup = self.message_(
                self.text,
                height   = self.height,
                width    = self.width,
                colors   = self.style_all,
                title    = self.title,
                shadow   = self.shadow,
                no_mouse = self.no_mouse,
                no_lines = self.no_lines,
                ok_label = self.l_oke,
            )
        return self.startup

if __name__ == "__main__":
    pass
