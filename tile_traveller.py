import math
# tökum kommuna út úr tile´unum þ.a. td. 3,2 er 32..
# ..Ef farið er í norður/suður þá +/- 1 því tile fyrir ofan/neðan eru 1 meira eða minna...
# ..Ef farið er í vestur/austur þá +/- 10 því tile fyrir hliðin á eru 10 meira eða minna...
def direction_(direction_inp,tile):
    if direction_inp=="e":
        tile=tile+10
    if direction_inp=="w":
        tile=tile-10
    if direction_inp=="n":
        tile=tile+1
    if direction_inp=="s":
        tile=tile-1
    return tile
borderW="valid"
borderN="valid"
borderE="valid"
borderS="valid"
# Þurfum að skilgreina í hvaða stefnu má ekki fara í ef maður er staðsettur á X tile´i..
# Ef borderX = "not_valid" þá má ekki fara í þá átt í völundarhúsinu..
def border_e(tile):
    borderE="valid"
    if tile==11:
        borderE="not_valid"
    if tile==22:
        borderE="not_valid"
    if tile==21:
        borderE="not_valid"
    if tile==33 or tile==32:
        borderE="not_valid"
    return borderE
def border_n(tile):
    borderN="valid"
    if tile==22:
        borderN="not_valid"
    if tile==13 or tile==23 or tile==33:
        borderN="not_valid"
    return borderN
def border_w(tile):
    borderW="valid"
    if tile==21:
        borderW="not_valid"
    if tile==32:
        borderW="not_valid"
    if tile==13 or tile==12 or tile==11:
        borderW="not_valid"
    return borderW
def border_s(tile):
    borderS="valid"
    if tile==23:
        borderS="not_valid"
    if tile==11 or tile==21:
        borderS="not_valid"
    return borderS
tile=11
#Búum til while setningu til þess að koma í veg fyrir að "or" komi fremst fram í you can travel: "    " ...
while tile!=31:
    out=""
    count=0
    borderS=border_s(tile)
    borderN=border_n(tile)
    borderW=border_w(tile)
    borderE=border_e(tile)
    if borderN=="valid":
        out =out+"(N)orth"
        count+=1
    if borderE=="valid":
        if count>0:
            out=out+" or "
        out=out+"(E)ast"
        count+=1
    if borderS=="valid":
        if count>0:
            out=out+" or "
        out=out+"(S)outh"
        count+=1
    if borderW=="valid":
        if count>0:
            out=out+" or "
        out=out+"(W)est"
        count+=1

    print("You can travel: "+out+".")
    direction_inp=input("Direction: ")
    direction=str.lower(direction_inp)
    if direction=="w"and borderW=="not_valid":
        print("Not a valid direction!")
    elif direction=="s"and borderS=="not_valid":
        print("Not a valid direction!")
    elif direction=="n"and borderN=="not_valid":
        print("Not a valid direction!")
    elif direction=="e"and borderE=="not_valid":
        print("Not a valid direction!")
    else:
        tile=direction_(direction,tile)

print("Victory!")

