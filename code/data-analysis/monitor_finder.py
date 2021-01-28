import os
import xml.dom.minidom
import shutil


def main():
    equal_threshold = False
    less_equal_threshold = False
    threshold = 3

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    if not equal_threshold:
        os.makedirs(os.path.dirname("E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                    str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/"),
                    exist_ok=True)
    else:
        os.makedirs(os.path.dirname("E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                    str(threshold) + "/"),
                    exist_ok=True)

    print("Group 0:")

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == "Monitor":
                counter += 1
        
        if not equal_threshold:
            if less_equal_threshold:
                if counter <= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-zero-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/")
            else:
                if counter >= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-zero-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/")
        else:
            if counter == threshold:
                print("%s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-zero-images/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                             str(threshold) + "/")

    print("Group 1:")

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == "Monitor":
                counter += 1

        if not equal_threshold:
            if less_equal_threshold:
                if counter <= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-one-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/")
            else:
                if counter >= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-one-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/")
        else:
            if counter == threshold:
                print("%s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-one-images/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                             str(threshold) + "/")

    print("Group 2:")

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == "Monitor":
                counter += 1

        if not equal_threshold:
            if less_equal_threshold:
                if counter <= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-two-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/")
            else:
                if counter >= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-two-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + (" or more" if not less_equal_threshold else " or less") + "/")
        else:
            if counter == threshold:
                print("%s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-two-images/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                             str(threshold) + "/")


if __name__ == "__main__":
    main()
