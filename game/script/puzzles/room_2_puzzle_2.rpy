
init python:
    def room2_panopticon_set(dir):
        if dir == "r":
            store.panopticon_config[panopticon_selected] += 1
            if panopticon_config[panopticon_selected] == 5:
                store.panopticon_config[panopticon_selected] = 0

            store.panopticon_reverse = panopticon_effects[panopticon_selected]
            for i in panopticon_effects[panopticon_selected]:
                store.panopticon_config[i] -= 1
                if panopticon_config[i] == -1:
                    store.panopticon_config[i] = 4
        else:
            store.panopticon_reverse = [panopticon_selected]
            store.panopticon_config[panopticon_selected] -= 1
            if panopticon_config[panopticon_selected] == -1:
                store.panopticon_config[panopticon_selected] = 4

            for i in panopticon_effects[panopticon_selected]:
                store.panopticon_config[i] += 1
                if panopticon_config[i] == 5:
                    store.panopticon_config[i] = 0
        store.panopticon_selected = None
        if room2_panopticon_valid_solution():
            store.inspect = "panopticon solved"
            renpy.jump("room_2")

        store.panopticon_moves += 1
        return
            
    def room2_panopticon_valid_solution():
        for angle in range(5):
            solution_list = []
            for row in range(5):
                temp = panopticon_values[row][angle-panopticon_config[row]]
                print(str(angle) +", " + str(row) + ": " + str(temp))
                if temp in solution_list:
                    print("uh oh!")
                    return False
                solution_list.append(temp)
        return True

default panopticon_selected = None
default panopticon_config = [0,0,0,0,0]
default panopticon_pos = [0,0,0,0,0]
default panopticon_reverse = []
default panopticon_moves = 0
define panopticon_effects = {0:[1,3], 1:[2], 2:[0,4], 3:[2], 4:[1,3]}
#circle = 1, x = 2, triangle = 3, square = 4. starts at bottom
define panopticon_values = {0:[4,2,3,4,3], 1:[4,3,1,2,0], 2:[0,0,1,3,0], 3:[4,1,2,1,4], 4:[2,1,2,3,0]}

screen room2_panopticon():
    sensitive not inspect
    modal True
    layer "master"
    if config.developer:
        vbox yalign 0.05 xalign 0.5:
            hbox:
                for i in range(len(panopticon_config)):
                    text str(panopticon_config[i]) + " "
            hbox:
                for i in range(len(panopticon_config)):
                    text str(panopticon_pos[i]) + " "

    for i in range(len(panopticon_config)):
        if panopticon_pos[i] == panopticon_config[i] * 72:
            imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at rotated(panopticon_pos[i])
        elif i in panopticon_reverse:
            imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at rotate_reverse(panopticon_pos[i])
            $ panopticon_pos[i] = panopticon_config[i] * 72
        elif i not in panopticon_reverse:
            imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at rotate_anim(panopticon_pos[i])
            $ panopticon_pos[i] = panopticon_config[i] * 72
    add "puzzles/room2_2_base.png" align (0.5,0.5)
    
    if panopticon_selected:
        hbox xalign 0.5 yalign 0.9 spacing 20:
            textbutton "COUNTERCLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "l")]
            textbutton "CLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "r")]

    textbutton "Return" action [Hide(), SetVariable("panopticon_selected", None), Jump("room_2")] style "main_menu_button" xalign 0.8 yalign 0.5


transform rotate_anim(val):
    rotate val
    linear 0.2 rotate val+72
transform rotate_reverse(val):
    rotate val
    linear 0.2 rotate val-72
    