import os
import xml.dom.minidom
import collections


def main():
    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    dct = {}

    for predef_class in predef_classes:
        dct[predef_class.replace('\n', '').split(" (")[0]] = 0

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counted = {}
        for predef_class in predef_classes:
            counted[predef_class.replace('\n', '').split(" (")[0]] = False

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data.split(" (")[0]
            if not counted[objname]:
                dct[objname] = dct.get(objname) + 1
                counted[objname] = True

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counted = {}
        for predef_class in predef_classes:
            counted[predef_class.replace('\n', '').split(" (")[0]] = False

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data.split(" (")[0]
            if not counted[objname]:
                dct[objname] = dct.get(objname) + 1
                counted[objname] = True

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counted = {}
        for predef_class in predef_classes:
            counted[predef_class.replace('\n', '').split(" (")[0]] = False

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data.split(" (")[0]
            if not counted[objname]:
                dct[objname] = dct.get(objname) + 1
                counted[objname] = True

    sorted_dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)

    for i in sorted_dct:
        print("%s,%d" % (i[0], i[1]))


if __name__ == "__main__":
    main()
