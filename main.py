import td
import torus_48x14x48 as tdmodel
offset = [0,0,1]
td.camera.render(tdmodel.lookup, offset)
while True:
    d = td.screen.getkey()
    if d == "esc":
        break
    elif d == "w":
        offset[2] += 1
    elif d == "s":
        if offset[2] != 1:
            offset[2] -= 1
    elif d == "a":
        offset[0] -= 1
    elif d == "d":
        offset[0] += 1
    elif d == "r":
        offset[1] += 1
    elif d == "f":
        offset[1] -= 1
    td.screen.clrscn()
    td.camera.render(tdmodel.lookup, offset)
