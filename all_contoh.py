from facebook_informations import (
        dprint,
        __removed__,
        Dump_public,
        Dump_follower,
        Information,
        Find_ID_Facebook,
        Ceck_Aplication,
        )
from rich.tree import Tree 

tree = Tree('? ')

__removed__.run()

def exa1():
    i = input("id : ")
    dumpf = Dump_follower()
    ca_ = dumpf.dump_follower(
            idz_=i,
            async_with_cookies=True,
            async_with_token=True,
            )
    dprint(ca_)

def exa2():
    i = input("id : ")
    dumpp = Dump_public()
    ce_ = dumpp.dump_public(
            idz_=i,
            async_with_cookies=True,
            async_with_token=True,
            )
    asd = [bgd for bgd in ce_['friends']['data']]
    for fd in asd:
        tree.add(fd['name']
              + " | " 
              + fd['id']
            )
    dprint(tree)

if __name__ == "__main__":
    exa2()
