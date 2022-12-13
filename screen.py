scnmem = []
sx = 64
sy = 32
import os
import keyboard
def cls():
    print("\033[H\033[J")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def pushp(x, y, t="\u2588", r=True):
    global scnmem
    popp(x, y)
    scnmem += [[x, y, t]]
    if r:
        updscn()
def clrscn():
    global scnmem
    scnmem = []
def peekp(x, y, pn=False):
    global scnmem
    for i in scnmem:
        if i[0] == x and i[1] == y:
            return i[2]
    if pn:
        return None
    else:
        return " "
def pescnmem(x,y):
    global scnmem
    for i in scnmem:
        if i[0] == x and i[1] == y:
            return True
    return False
def popp(x,y):
    global scnmem
    for i in scnmem:
        if i[0] == x and i[1] == y:
            scnmem.remove(i)
def updscn():
    cls()
    global scnmem
    for y in range(0, sx):
        for x in range(0, sy):
            if pescnmem(x, y):
                d = peekp(x, y)
                print(d, end="")
            else:
                print(" ", end="")
        print()
def pusht(x, y, t, u = True):
    lt = list(t)
    h = 0
    for rt in lt:
        pushp(x+h, y, rt, False)
        h+=1
    if u:
        updscn()
def getkey():
    return keyboard.read_key(True)
def kscnpipe(x, y, l=64):
    apop(x, y, l)
    updscn()
    stop = False
    offset = 0
    while not stop:
        k = getkey()
        if k == "enter":
            stop = True
            break
        elif k == "space":
            pushp(x+offset, y, " ")
            offset += 1
            offset = abs(offset)
        elif k == "backspace":
            offset -= 1
            offset = abs(offset)
            popp(x+offset, y)
            updscn()
        elif len(k) != 1:
            pass
        else:
            pushp(x+offset, y, k)
            offset += 1
            offset = abs(offset)
        if offset >= l:
            return
def apeek(x, y, le):
    out = ""
    for i in range(le):
        out += peekp(x+i, y)
    return out
def apop(x, y, le):
    pusht(x, y, " "*le)
