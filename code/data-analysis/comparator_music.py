import os
import xml.dom.minidom


def main():
    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    ext = "ExternalMic"
    sub = "Subwoofer"

    externalMic1 = "External Microphone (Generic)"
    externalMic2 = "External Microphone (with Boom Arm)"
    subwoofer = "External Speakers (Subwoofers)"

    externalAmount = 0
    subwooferAmount = 0
    externalAndSubwooferAmount = 0

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {ext: 0, sub: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == externalMic1 or objname == externalMic2:
                dc[ext] += 1
                externalAmount += 1

            if objname == subwoofer:
                dc[sub] += 1
                subwooferAmount += 1

        # Both User
        if dc.get(ext) > 0:
            if dc.get(sub) > 0:
                externalAndSubwooferAmount += 1

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {ext: 0, sub: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == externalMic1 or objname == externalMic2:
                dc[ext] += 1
                externalAmount += 1

            if objname == subwoofer:
                dc[sub] += 1
                subwooferAmount += 1

        # Both User
        if dc.get(ext) > 0:
            if dc.get(sub) > 0:
                externalAndSubwooferAmount += 1

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {ext: 0, sub: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == externalMic1 or objname == externalMic2:
                dc[ext] += 1
                externalAmount += 1

            if objname == subwoofer:
                dc[sub] += 1
                subwooferAmount += 1

        # Both User
        if dc.get(ext) > 0:
            if dc.get(sub) > 0:
                externalAndSubwooferAmount += 1

    print("External Mic: %d" % externalAmount)
    print("Subwoofers: %d" % subwooferAmount)
    print("Both: %d" % externalAndSubwooferAmount)


if __name__ == "__main__":
    main()
