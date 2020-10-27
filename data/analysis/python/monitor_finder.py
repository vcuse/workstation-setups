import os
import xml.dom.minidom
import collections


def main():
    less_equal_threshold = True
    threshold = 2

    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    print("Group 0:")

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == "Monitor":
                counter += 1

        if less_equal_threshold:
            if counter <= threshold:
                print("%s" % f)
        else:
            if counter > threshold:
                print("%s" % f)

    print("Group 1:")

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == "Monitor":
                counter += 1

        if less_equal_threshold:
            if counter <= threshold:
                print("%s" % f)
        else:
            if counter > threshold:
                print("%s" % f)

    print("Group 2:")

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == "Monitor":
                counter += 1

        if less_equal_threshold:
            if counter <= threshold:
                print("%s" % f)
        else:
            if counter > threshold:
                print("%s" % f)


if __name__ == "__main__":
    main()
