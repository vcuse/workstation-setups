import os
import xml.dom.minidom
import xlsxwriter


def main():
    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    workbook = xlsxwriter.Workbook("workstations-data.xlsx")
    header_format = workbook.add_format({'bold': True, 'align': 'center'})

    # ===============================================
    # Worksheet for full data
    worksheet_full = workbook.add_worksheet()
    row = 0
    col = 0

    worksheet_full.write(row, col, "ID", header_format)
    worksheet_full.set_column('A:A', 24.29)
    col += 1

    worksheet_full.write(row, col, "Group", header_format)
    worksheet_full.set_column(col, col, 13.86)
    col += 1

    for predef_class in predef_classes:
        worksheet_full.write(row, col, predef_class.replace('\n', ''), header_format)
        worksheet_full.set_column(col, col, 34.29)
        col += 1

    worksheet_full.write(row, col, "Total Items", header_format)
    worksheet_full.set_column(col, col, 34.29)

    row = 1
    col = 0

    dct0 = {}
    dct1 = {}
    dct2 = {}

    for predef_class in predef_classes:
        dct0[predef_class.replace('\n', '')] = 0
        dct1[predef_class.replace('\n', '')] = 0
        dct2[predef_class.replace('\n', '')] = 0

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        worksheet_full.write(row, col, f.replace(".xml", ""))
        col += 1
        worksheet_full.write(row, col, "Group 0")
        col += 1

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data
            dct0[objname] = dct0.get(objname) + 1

        for predef_class in predef_classes:
            worksheet_full.write(row, col, dct0.get(predef_class.replace('\n', '')))
            dct0[predef_class.replace('\n', '')] = 0
            col += 1

        worksheet_full.write(row, col, "=SUM(C%d:CM%d)" % (row + 1, row + 1))

        col = 0
        row += 1

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        worksheet_full.write(row, col, f.replace(".xml", ""))
        col += 1
        worksheet_full.write(row, col, "Group 1")
        col += 1

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data
            dct1[objname] = dct1.get(objname) + 1

        for predef_class in predef_classes:
            worksheet_full.write(row, col, dct1.get(predef_class.replace('\n', '')))
            dct1[predef_class.replace('\n', '')] = 0
            col += 1

        worksheet_full.write(row, col, "=SUM(C%d:CM%d)" % (row + 1, row + 1))

        col = 0
        row += 1

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        worksheet_full.write(row, col, f.replace(".xml", ""))
        col += 1
        worksheet_full.write(row, col, "Group 2")
        col += 1

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data
            dct2[objname] = dct2.get(objname) + 1

        for predef_class in predef_classes:
            worksheet_full.write(row, col, dct2.get(predef_class.replace('\n', '')))
            dct2[predef_class.replace('\n', '')] = 0
            col += 1

        worksheet_full.write(row, col, "=SUM(C%d:CM%d)" % (row + 1, row + 1))

        col = 0
        row += 1

    worksheet_full.merge_range(row, col, row, col + 1, "Total", workbook.add_format({'bold': True}))
    col += 2

    for predef_class in predef_classes:
        worksheet_full.write(row, col, "=SUM(INDEX(A1:CN431, 0, %d))" % (col + 1))
        col += 1

    worksheet_full.write(row, col, "=SUM(INDEX(A1:CN431, 0, %d))" % (col + 1))
    # ===============================================

    # ===============================================
    # Worksheet for collapsed data
    worksheet_collapsed = workbook.add_worksheet()
    row = 0
    col = 0

    worksheet_collapsed.write(row, col, "ID", header_format)
    worksheet_collapsed.set_column('A:A', 24.29)
    col += 1

    worksheet_collapsed.write(row, col, "Group", header_format)
    worksheet_collapsed.set_column(col, col, 13.86)
    col += 1

    stored_classes = []

    for predef_class in predef_classes:
        if predef_class.replace('\n', '').split(" (")[0] not in stored_classes:
            worksheet_collapsed.write(row, col, predef_class.replace('\n', '').split(" (")[0], header_format)
            worksheet_collapsed.set_column(col, col, 34.29)
            col += 1
            stored_classes.append(predef_class.replace('\n', '').split(" (")[0])

    worksheet_collapsed.write(row, col, "Total Items", header_format)
    worksheet_collapsed.set_column(col, col, 34.29)

    row = 1
    col = 0

    dct0 = {}
    dct1 = {}
    dct2 = {}

    stored_classes = []

    for predef_class in predef_classes:
        if predef_class.replace('\n', '').split(" (")[0] not in stored_classes:
            dct0[predef_class.replace('\n', '').split(" (")[0]] = 0
            dct1[predef_class.replace('\n', '').split(" (")[0]] = 0
            dct2[predef_class.replace('\n', '').split(" (")[0]] = 0
            stored_classes.append(predef_class.replace('\n', '').split(" (")[0])

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        worksheet_collapsed.write(row, col, f.replace(".xml", ""))
        col += 1
        worksheet_collapsed.write(row, col, "Group 0")
        col += 1

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data.split(" (")[0]
            dct0[objname] = dct0.get(objname) + 1

        stored_classes = []

        for predef_class in predef_classes:
            if predef_class.replace('\n', '').split(" (")[0] not in stored_classes:
                worksheet_collapsed.write(row, col, dct0.get(predef_class.replace('\n', '').split(" (")[0]))
                dct0[predef_class.replace('\n', '').split(" (")[0]] = 0
                col += 1
                stored_classes.append(predef_class.replace('\n', '').split(" (")[0])

        worksheet_collapsed.write(row, col, "=SUM(C%d:BA%d)" % (row + 1, row + 1))

        col = 0
        row += 1

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        worksheet_collapsed.write(row, col, f.replace(".xml", ""))
        col += 1
        worksheet_collapsed.write(row, col, "Group 1")
        col += 1

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data.split(" (")[0]
            dct1[objname] = dct1.get(objname) + 1

        stored_classes = []

        for predef_class in predef_classes:
            if predef_class.replace('\n', '').split(" (")[0] not in stored_classes:
                worksheet_collapsed.write(row, col, dct1.get(predef_class.replace('\n', '').split(" (")[0]))
                dct1[predef_class.replace('\n', '').split(" (")[0]] = 0
                col += 1
                stored_classes.append(predef_class.replace('\n', '').split(" (")[0])

        worksheet_collapsed.write(row, col, "=SUM(C%d:BA%d)" % (row + 1, row + 1))

        col = 0
        row += 1

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        worksheet_collapsed.write(row, col, f.replace(".xml", ""))
        col += 1
        worksheet_collapsed.write(row, col, "Group 2")
        col += 1

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data.split(" (")[0]
            dct2[objname] = dct2.get(objname) + 1

        stored_classes = []

        for predef_class in predef_classes:
            if predef_class.replace('\n', '').split(" (")[0] not in stored_classes:
                worksheet_collapsed.write(row, col, dct2.get(predef_class.replace('\n', '').split(" (")[0]))
                dct2[predef_class.replace('\n', '').split(" (")[0]] = 0
                col += 1
                stored_classes.append(predef_class.replace('\n', '').split(" (")[0])

        worksheet_collapsed.write(row, col, "=SUM(C%d:BA%d)" % (row + 1, row + 1))

        col = 0
        row += 1

    worksheet_collapsed.merge_range(row, col, row, col + 1, "Total", workbook.add_format({'bold': True}))
    col += 2

    stored_classes = []

    for predef_class in predef_classes:
        if predef_class.replace('\n', '').split(" (")[0] not in stored_classes:
            worksheet_collapsed.write(row, col, "=SUM(INDEX(A1:BB431, 0, %d))" % (col + 1))
            col += 1
            stored_classes.append(predef_class.replace('\n', '').split(" (")[0])

    worksheet_collapsed.write(row, col, "=SUM(INDEX(A1:BB431, 0, %d))" % (col + 1))

    workbook.close()


if __name__ == "__main__":
    main()
