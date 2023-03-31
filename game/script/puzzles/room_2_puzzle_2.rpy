
init python:
    def panopticon_init(start=False):
        store.panopticon_moves = 0
        store.panopticon_selected = None
        store.panopticon_config = [0,0,0,0,0]
        store.panopticon_pos = [0,0,0,0,0]
        store.panopticon_reverse = []
        if not start:
            renpy.notify(_("Restarting..."))

    def room2_panopticon_set(dir):

        store.panopticon_moves += 1

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
            store.room2["panopticon"] = "solved"
            return True

        if panopticon_moves >= panopticon_move_limit and not (achievement_dead8 in persistent.dead_ends and not preferences.hard_mode):
            renpy.jump("panopticon_game_over")

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

default panopticon_moves = 0
define panopticon_move_limit = 20

default panopticon_selected = None
default panopticon_config = [0,0,0,0,0]
default panopticon_pos = [0,0,0,0,0]
default panopticon_reverse = []
define panopticon_effects = {0:[1,3], 1:[2], 2:[0,4], 3:[2], 4:[1,3]}
#circle = 1, x = 2, triangle = 3, square = 4. starts at bottom
define panopticon_values = {0:[4,2,3,4,3], 1:[4,3,1,2,0], 2:[0,0,1,3,0], 3:[4,1,2,1,4], 4:[2,1,2,3,0]}

screen room2_panopticon():
    sensitive not inspect
    modal True
    tag puzzle
    layer "puzzles"
    zorder 5

    frame style "puzzle_frame":
        fixed xsize 775 yfill True xalign 1.0:
            vbox spacing 50:
                style_prefix "puzzle_description"
                null height 10
                label _("Instructions")
                text _("In a stealthy campaign, {color=#fff}Cautionne has managed to take control of a STOP holding center,{/color} where several young test subjects are being held in a futuristic panopticon.\n\nTo give them the best chance of survival, Cautionne needs to {color=#fff}rearrange the cells so that each group of escaping testees is balanced.{/color}\n\nThese groups are shown as {color=#fff}a circle, a triangle, a square{/color} and {color=#fff}an X.{/color}\n\nHowever, the bureaucratic systems have left only the bare minimum operating instructions on how to operate the panopticon.\n\n{color=#fff}Help Cautionne properly arrange the cells according to the limitations of the system.{/color}")
            if (achievement_dead8 in persistent.dead_ends and not preferences.hard_mode):
                textbutton "RESTART" action [Function(panopticon_init)] style "confirm_button" xalign 0.0 yalign 1.0 at zoomed(0.75)
            textbutton "RETURN" action [SetVariable("panopticon_selected", None), Return(), With(puzzle_hide)] style "confirm_button" xalign 1.0 yalign 1.0

        fixed xsize 1000:
            for i in range(len(panopticon_config)):
                if panopticon_pos[i] == panopticon_config[i] * 72:
                    imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at hover_brighten, rotated(panopticon_pos[i])
                elif i in panopticon_reverse:
                    imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at hover_brighten, rotate_reverse(panopticon_pos[i])
                    $ panopticon_pos[i] = panopticon_config[i] * 72
                elif i not in panopticon_reverse:
                    imagebutton idle "puzzles/room2_2_color"+ str(i+1) +".png" sensitive (inspect==None) action [SetVariable("panopticon_selected", i)] focus_mask True align (0.5,0.5) at hover_brighten, rotate_anim(panopticon_pos[i])
                    $ panopticon_pos[i] = panopticon_config[i] * 72
            add "puzzles/room2_2_base.png" align (0.5,0.5)
    
            if panopticon_selected != None:
                #add "gui/overlay/confirm.png"
                hbox xalign 0.5 yalign 0.5 spacing 20:
                    frame:
                        textbutton "COUNTERCLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "l")]
                    frame:
                        textbutton "CLOCKWISE" xysize (370, 64) text_size 60 action [Function(room2_panopticon_set, "r")]
        if not (achievement_dead8 in persistent.dead_ends and not preferences.hard_mode):
            frame xalign 1.0:
                text str(panopticon_moves) + "/" + str(panopticon_move_limit) style "main_menu_button"


    if config.developer:
        #vbox yalign 0.05 xalign 0.5:
        #    hbox:
        #        for i in range(len(panopticon_config)):
        #            text str(panopticon_config[i]) + " "
        #    hbox:
        #        for i in range(len(panopticon_config)):
        #            text str(panopticon_pos[i]) + " "
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room2, "panopticon", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("panopticon_game_over")] style "main_menu_button"

transform rotate_anim(val):
    rotate val
    linear 0.2 rotate val+72
transform rotate_reverse(val):
    rotate val
    linear 0.2 rotate val-72
    