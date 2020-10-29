import os
import xml.dom.minidom
import shutil


def main():
    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    musc_inst_1 = "Musical Instrument (Electric Guitar)"
    musc_inst_2 = "Musical Instrument (Generic)"
    musc_inst_3 = "Musical Instrument (Guitar)"
    musc_inst_4 = "Musical Instrument (Keyboard/Piano)"

    ext_woofers = "External Speakers (Subwoofers)"

    os.makedirs(os.path.dirname("E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Instruments/"),
                exist_ok=True)

    os.makedirs(os.path.dirname("E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Subwoofers/"),
                exist_ok=True)

    print("Group 0:")

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == musc_inst_1 or objname == musc_inst_2 or objname == musc_inst_3 or objname == musc_inst_4:
                print("Instrument: %s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/Group 0/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Instruments/")
                break

            if objname == ext_woofers:
                print("Subwoofer: %s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/Group 0/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Subwoofers/")
                break

    print("Group 1:")

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == musc_inst_1 or objname == musc_inst_2 or objname == musc_inst_3 or objname == musc_inst_4:
                print("Instrument: %s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/Group 1/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Instruments/")

            if objname == ext_woofers:
                print("Subwoofer: %s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/Group 1/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Subwoofers/")
                break

    print("Group 2:")

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == musc_inst_1 or objname == musc_inst_2 or objname == musc_inst_3 or objname == musc_inst_4:
                print("Instrument: %s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/Group 2/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Instruments/")

            if objname == ext_woofers:
                print("Subwoofer: %s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/Group 2/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Musicians/Subwoofers/")
                break


if __name__ == "__main__":
    main()
