import os
import xml.dom.minidom


def main():
    predef_classes = []

    with open("predefined_classes.txt") as file:
        predef_classes = file.readlines()

    g0_files = sorted(os.listdir("Group 0 (XML)"), key=lambda s: int(s.split('_')[0]))
    g1_files = sorted(os.listdir("Group 1 (XML)"), key=lambda s: int(s.split('_')[0]))
    g2_files = sorted(os.listdir("Group 2 (XML)"), key=lambda s: int(s.split('_')[0]))

    keyboard = "Keyboard (Gaming)"
    mouse = "Mouse (Gaming)"
    mousepad = "Mousepad (Gaming)"
    chair = "Chair (Gaming)"

    keyboard_amount = 0
    mouse_amount = 0
    mousepad_amount = 0
    chair_amount = 0

    full_setup = 0
    keyboard_mouse_mousepad = 0
    keyboard_mouse = 0
    mouse_mousepad = 0

    for f in g0_files:
        doc = xml.dom.minidom.parse("Group 0 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {keyboard: 0, mouse: 0, mousepad: 0, chair: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == keyboard:
                dc[keyboard] += 1
                keyboard_amount += 1

            if objname == mouse:
                dc[mouse] += 1
                mouse_amount += 1

            if objname == mousepad:
                dc[mousepad] += 1
                mousepad_amount += 1

            if objname == chair:
                dc[chair] += 1
                chair_amount += 1

        # Full Setup
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) > 0 and dc.get(chair) > 0:
            full_setup += 1

        # Keyboard, Mouse and Mousepad
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) > 0:
            keyboard_mouse_mousepad += 1

        # Keyboard, Mouse
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0:
            keyboard_mouse += 1

        # Mouse, Mousepad
        if dc.get(mouse) > 0 and dc.get(mousepad) > 0:
            mouse_mousepad += 1

    for f in g1_files:
        doc = xml.dom.minidom.parse("Group 1 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {keyboard: 0, mouse: 0, mousepad: 0, chair: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == keyboard:
                dc[keyboard] += 1
                keyboard_amount += 1

            if objname == mouse:
                dc[mouse] += 1
                mouse_amount += 1

            if objname == mousepad:
                dc[mousepad] += 1
                mousepad_amount += 1

            if objname == chair:
                dc[chair] += 1
                chair_amount += 1

        # Full Setup
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) > 0 and dc.get(chair) > 0:
            full_setup += 1

        # Keyboard, Mouse and Mousepad
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) > 0:
            keyboard_mouse_mousepad += 1

        # Keyboard, Mouse
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0:
            keyboard_mouse += 1

        # Mouse, Mousepad
        if dc.get(mouse) > 0 and dc.get(mousepad) > 0:
            mouse_mousepad += 1

    for f in g2_files:
        doc = xml.dom.minidom.parse("Group 2 (XML)/" + f)
        objects = doc.getElementsByTagName("object")

        dc = {keyboard: 0, mouse: 0, mousepad: 0, chair: 0}

        for obj in objects:
            objname = obj.getElementsByTagName("name")[0].firstChild.data

            if objname == keyboard:
                dc[keyboard] += 1
                keyboard_amount += 1

            if objname == mouse:
                dc[mouse] += 1
                mouse_amount += 1

            if objname == mousepad:
                dc[mousepad] += 1
                mousepad_amount += 1

            if objname == chair:
                dc[chair] += 1
                chair_amount += 1

        # Full Setup
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) > 0 and dc.get(chair) > 0:
            full_setup += 1

        # Keyboard, Mouse and Mousepad
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) > 0 and dc.get(chair) == 0:
            keyboard_mouse_mousepad += 1

        # Keyboard, Mouse
        if dc.get(keyboard) > 0 and dc.get(mouse) > 0 and dc.get(mousepad) == 0 and dc.get(chair) == 0:
            keyboard_mouse += 1

        # Mouse, Mousepad
        if dc.get(mouse) > 0 and dc.get(mousepad) > 0 and dc.get(keyboard) == 0 and dc.get(mousepad) == 0 and dc.get(chair) == 0:
            mouse_mousepad += 1

    print("Full Setup: %d" % full_setup)
    print("Keyboard Mouse Mousepad: %d" % keyboard_mouse_mousepad)
    print("Keyboard Mouse: %d" % keyboard_mouse)
    print("Mouse Mousepad: %d" % mouse_mousepad)


if __name__ == "__main__":
    main()
