import os
import xml.dom.minidom
import collections


def main():
    threshold = 7

    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    dct = {}

    for predef_class in predef_classes:
        dct[predef_class.replace('\n', '')] = 0

    print("Group 0:")

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counted = {}
        for predef_class in predef_classes:
            counted[predef_class.replace('\n', '')] = False

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data
            if not counted[objname]:
                dct[objname] = dct.get(objname) + 1
                counted[objname] = True
                counter += 1

        if counter <= threshold:
            print("%s" % f)

    print("Group 1:")

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counted = {}
        for predef_class in predef_classes:
            counted[predef_class.replace('\n', '')] = False

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data
            if not counted[objname]:
                dct[objname] = dct.get(objname) + 1
                counted[objname] = True
                counter += 1

        if counter <= threshold:
            print("%s" % f)

    print("Group 2:")

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counted = {}
        for predef_class in predef_classes:
            counted[predef_class.replace('\n', '')] = False

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data
            if not counted[objname]:
                dct[objname] = dct.get(objname) + 1
                counted[objname] = True
                counter += 1

        if counter <= threshold:
            print("%s" % f)


if __name__ == "__main__":
    main()
