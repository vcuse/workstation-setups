import os
import xml.dom.minidom


def main():
    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    win = "Windows"
    osx = "OSX"
    lin = "Linux"

    tWin = "Tablet (Windows)"
    dWin = "Desktop (Windows)"
    lWin = "Laptop (Windows)"

    tOSX = "Tablet (iPad)"
    dOSX = "Desktop (OSX)"
    lOSX = "Laptop (OSX)"
    mOSX = "Monitor (iMac)"

    lLinux = "Laptop (Linux)"
    dLinux = "Desktop (Linux)"

    apple = 0
    windows = 0
    linux = 0

    appleAndWindows = 0
    appleAndLinux = 0
    windowsAndLinux = 0

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {win: 0, osx: 0, lin: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == tWin or objname == dWin or objname == lWin:
                windows += 1
                dc[win] += 1

            if objname == tOSX or objname == dOSX or objname == lOSX or objname == mOSX:
                apple += 1
                dc[osx] += 1

            if objname == lLinux or objname == dLinux:
                linux += 1
                dc[lin] += 1

        if dc.get(osx) > 0 and dc.get(win) > 0:
            appleAndWindows += 1

        if dc.get(osx) > 0 and dc.get(lin) > 0:
            appleAndLinux += 1

        if dc.get(win) > 0 and dc.get(lin) > 0:
            windowsAndLinux += 1

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {win: 0, osx: 0, lin: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == tWin or objname == dWin or objname == lWin:
                windows += 1
                dc[win] += 1

            if objname == tOSX or objname == dOSX or objname == lOSX or objname == mOSX:
                apple += 1
                dc[osx] += 1

            if objname == lLinux or objname == dLinux:
                linux += 1
                dc[lin] += 1

        if dc.get(osx) > 0 and dc.get(win) > 0:
            appleAndWindows += 1

        if dc.get(osx) > 0 and dc.get(lin) > 0:
            appleAndLinux += 1

        if dc.get(win) > 0 and dc.get(lin) > 0:
            windowsAndLinux += 1

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {win: 0, osx: 0, lin: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == tWin or objname == dWin or objname == lWin:
                windows += 1
                dc[win] += 1

            if objname == tOSX or objname == dOSX or objname == lOSX or objname == mOSX:
                apple += 1
                dc[osx] += 1

            if objname == lLinux or objname == dLinux:
                linux += 1
                dc[lin] += 1

        if dc.get(osx) > 0 and dc.get(win) > 0:
            appleAndWindows += 1

        if dc.get(osx) > 0 and dc.get(lin) > 0:
            appleAndLinux += 1

        if dc.get(win) > 0 and dc.get(lin) > 0:
            windowsAndLinux += 1

    print("Apple Users: %d" % apple)
    print("Windows Users: %d" % windows)
    print("Linux Users: %d" % linux)
    print("Apple and Windows: %d" % appleAndWindows)
    print("Apple and Linux: %d" % appleAndLinux)
    print("Windows and Linux: %d" % windowsAndLinux)


if __name__ == "__main__":
    main()
