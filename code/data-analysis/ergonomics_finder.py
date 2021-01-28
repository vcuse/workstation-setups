import os
import xml.dom.minidom
import shutil


def main():
    equal_threshold = False
    less_equal_threshold = False
    threshold = 3

    ei1 = "Mouse (Ergonomic)"
    ei2 = "Monitor Arm"
    ei3 = "External Microphone(with Boom Arm)"
    ei4 = "Laptop Stand"
    ei5 = "Chair (Gaming)"
    ei6 = "Desk (Standing)"
    ei7 = "Keyboard (Ergonomic)"
    ei8 = "Footrest"
    ei9 = "Acoustic Foam"

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    if not equal_threshold:
        os.makedirs(os.path.dirname("E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                    str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/"),
                    exist_ok=True)
    else:
        os.makedirs(os.path.dirname("E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                    str(threshold) + "/"),
                    exist_ok=True)

    print("Group 0:")

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0
        dc = {ei1: 0, ei2: 0, ei3: 0, ei4: 0, ei5: 0, ei6: 0, ei7: 0, ei8: 0, ei9: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == ei1:
                dc[ei1] += 1

            if objname.split(" (")[0] == ei2:
                dc[ei2] += 1

            if objname.split(" (")[0] == ei3:
                dc[ei3] += 1

            if objname.split(" (")[0] == ei4:
                dc[ei4] += 1

            if objname.split(" (")[0] == ei5:
                dc[ei5] += 1

            if objname.split(" (")[0] == ei6:
                dc[ei6] += 1

            if objname.split(" (")[0] == ei7:
                dc[ei7] += 1

            if objname.split(" (")[0] == ei8:
                dc[ei8] += 1

            if objname.split(" (")[0] == ei9:
                dc[ei9] += 1

        if dc[ei1] > 0:
            counter += 1

        if dc[ei2] > 0:
            counter += 1

        if dc[ei3] > 0:
            counter += 1

        if dc[ei4] > 0:
            counter += 1

        if dc[ei5] > 0:
            counter += 1

        if dc[ei6] > 0:
            counter += 1

        if dc[ei7] > 0:
            counter += 1

        if dc[ei8] > 0:
            counter += 1

        if dc[ei9] > 0:
            counter += 1

        if not equal_threshold:
            if less_equal_threshold:
                if counter <= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-zero-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/Monitor/Threshold " +
                                 str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/")
            else:
                if counter >= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-zero-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                 str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/")
        else:
            if counter == threshold:
                print("%s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-zero-images/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                             str(threshold) + "/")

    print("Group 1:")

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0
        dc = {ei1: 0, ei2: 0, ei3: 0, ei4: 0, ei5: 0, ei6: 0, ei7: 0, ei8: 0, ei9: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == ei1:
                dc[ei1] += 1

            if objname.split(" (")[0] == ei2:
                dc[ei2] += 1

            if objname.split(" (")[0] == ei3:
                dc[ei3] += 1

            if objname.split(" (")[0] == ei4:
                dc[ei4] += 1

            if objname.split(" (")[0] == ei5:
                dc[ei5] += 1

            if objname.split(" (")[0] == ei6:
                dc[ei6] += 1

            if objname.split(" (")[0] == ei7:
                dc[ei7] += 1

            if objname.split(" (")[0] == ei8:
                dc[ei8] += 1

            if objname.split(" (")[0] == ei9:
                dc[ei9] += 1

        if dc[ei1] > 0:
            counter += 1

        if dc[ei2] > 0:
            counter += 1

        if dc[ei3] > 0:
            counter += 1

        if dc[ei4] > 0:
            counter += 1

        if dc[ei5] > 0:
            counter += 1

        if dc[ei6] > 0:
            counter += 1

        if dc[ei7] > 0:
            counter += 1

        if dc[ei8] > 0:
            counter += 1

        if dc[ei9] > 0:
            counter += 1

        if not equal_threshold:
            if less_equal_threshold:
                if counter <= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-one-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                 str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/")
            else:
                if counter >= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-one-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                 str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/")
        else:
            if counter == threshold:
                print("%s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-one-images/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                             str(threshold) + "/")

    print("Group 2:")

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        counter = 0
        dc = {ei1: 0, ei2: 0, ei3: 0, ei4: 0, ei5: 0, ei6: 0, ei7: 0, ei8: 0, ei9: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname.split(" (")[0] == ei1:
                dc[ei1] += 1

            if objname.split(" (")[0] == ei2:
                dc[ei2] += 1

            if objname.split(" (")[0] == ei3:
                dc[ei3] += 1

            if objname.split(" (")[0] == ei4:
                dc[ei4] += 1

            if objname.split(" (")[0] == ei5:
                dc[ei5] += 1

            if objname.split(" (")[0] == ei6:
                dc[ei6] += 1

            if objname.split(" (")[0] == ei7:
                dc[ei7] += 1

            if objname.split(" (")[0] == ei8:
                dc[ei8] += 1

            if objname.split(" (")[0] == ei9:
                dc[ei9] += 1

        if dc[ei1] > 0:
            counter += 1

        if dc[ei2] > 0:
            counter += 1

        if dc[ei3] > 0:
            counter += 1

        if dc[ei4] > 0:
            counter += 1

        if dc[ei5] > 0:
            counter += 1

        if dc[ei6] > 0:
            counter += 1

        if dc[ei7] > 0:
            counter += 1

        if dc[ei8] > 0:
            counter += 1

        if dc[ei9] > 0:
            counter += 1

        if not equal_threshold:
            if less_equal_threshold:
                if counter <= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-two-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                 str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/")
            else:
                if counter >= threshold:
                    print("%s" % f)
                    shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-two-images/" + f.replace("xml", "jpg"),
                                 "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                                 str(threshold) + ("_or_more" if not less_equal_threshold else "_or_less") + "/")
        else:
            if counter == threshold:
                print("%s" % f)
                shutil.copy2("E:/Github/Research VCU/workstations/data/images/group-two-images/" + f.replace("xml", "jpg"),
                             "E:/Github/Research VCU/workstations/data/images/analysed/ergonomics/threshold_" +
                             str(threshold) + "/")


if __name__ == "__main__":
    main()
