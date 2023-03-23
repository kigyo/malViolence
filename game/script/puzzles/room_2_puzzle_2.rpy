
init python:
    def room2_panopticon_set(dir):
        if dir == "r":
            store.room2["panopticon"][panopticon_selected] += 1
            if room2["panopticon"][panopticon_selected] == 5:
                store.room2["panopticon"][panopticon_selected] = 0

            store.room2["panopticon_reverse"] = room2["panopticon_effects"][panopticon_selected]
            for i in room2["panopticon_effects"][panopticon_selected]:
                store.room2["panopticon"][i] -= 1
                if room2["panopticon"][i] == -1:
                    store.room2["panopticon"][i] = 4
        else:
            store.room2["panopticon_reverse"] = [panopticon_selected]
            store.room2["panopticon"][panopticon_selected] -= 1
            if room2["panopticon"][panopticon_selected] == -1:
                store.room2["panopticon"][panopticon_selected] = 4

            for i in room2["panopticon_effects"][panopticon_selected]:
                store.room2["panopticon"][i] += 1
                if room2["panopticon"][i] == 5:
                    store.room2["panopticon"][i] = 0

        if room2_panopticon_valid_solution():
            store.inspect = "panopticon solved"
            renpy.jump("room_2")

        store.room2["panopticon_moves"] += 1
        return
            
    def room2_panopticon_valid_solution():
        result = False
        if room2["panopticon"] == [2,1,2,4,0]:
            result = True
        return result

default panopticon_selected = None

screen room2_panopticon():
    sensitive not inspect
    modal True
    layer "master"
    if config.developer:
        vbox yalign 0.05 xalign 0.5:
            hbox:
                for i in range(len(room2["panopticon"])):
                    text str(room2["panopticon"][i]) + " "
            hbox:
                for i in range(len(room2["panopticon"])):
                    text str(room2["panopticon_pos"][i]) + " "

    for i in range(len(room2["panopticon"])):
        if room2["panopticon_pos"][i] == room2["panopticon"][i] * 72:
            imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i), ShowMenu("room2_panopticon_select")] focus_mask True align (0.5,0.5) at rotated(room2["panopticon_pos"][i])
        elif i in room2["panopticon_reverse"]:
            imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i), ShowMenu("room2_panopticon_select")] focus_mask True align (0.5,0.5) at rotate_reverse(room2["panopticon_pos"][i])
            $ room2["panopticon_pos"][i] = room2["panopticon"][i] * 72
        elif i not in room2["panopticon_reverse"]:
            imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i), ShowMenu("room2_panopticon_select")] focus_mask True align (0.5,0.5) at rotate_anim(room2["panopticon_pos"][i])
            $ room2["panopticon_pos"][i] = room2["panopticon"][i] * 72
    add "puzzles/room2_2_base.png" align (0.5,0.5)
    textbutton "Return" action [Hide(), Call("room_2")] style "main_menu_button" xalign 0.8 yalign 0.5

screen room2_panopticon_select():
    modal True
    hbox xalign 0.5 yalign 0.9 spacing 20:
        textbutton "COUNTERCLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "l"), Hide()]
        textbutton "CLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "r"), Hide()]

transform rotate_anim(val):
    rotate val
    linear 0.2 rotate val+72
transform rotate_reverse(val):
    rotate val
    linear 0.2 rotate val-72
    