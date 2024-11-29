capitulo = 0

def titulo(_tit):
    global capitulo
    capitulo += 1
    print()
    print("#####################################")
    print("##", capitulo, "##  " + _tit)
    print("#####################################")

def parte(_tit):
    print()
    print("--  " + _tit + "  --")
    print("-------------------------------------")