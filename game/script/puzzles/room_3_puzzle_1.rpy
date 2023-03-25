init python:
    def quilt_checker():
        quilts = quilt_presets.copy()
        quilts.update(quilt_input)

        for i in range(6*11):
            if i not in quilts:
                print("failed because not all fields are full")
                return False
        
        for col in range(6):
            for row in range(11):
                if row < 10 and not quilt_shared(quilts[col*11 + row], quilts[col*11 + row + 6]):
                    print("failed because " + str(col*11 + row) + " did not match vertically")
                    return False
                if row%2 == 0 and (col*11 + row)%2 == 0 and not quilt_shared(quilts[col*11 + row], quilts[(col*11 + row)+1]):
                    print("failed because " + str(col*11 + row) + " did not match horizontally")
                    return False
                if row%2 == 1 and (col*11 + row)%2 == 1 and not quilt_shared(quilts[col*11 + row], quilts[(col*11 + row)+1]):
                    print("failed because " + str(col*11 + row) + " did not match horizontally 2")
                    return False
        return True
    
    def quilt_current_move_valid(idx):
        return False

    def quilt_shared(a,b):
        shared = 0
        for i in range(3):
            if a[i] == b[i]:
                shared += 1
        return shared == 2

    def quilt_set(idx):
        global quilt_input
        if idx not in quilt_presets:
            quilt_input[idx] = [quilt_color, quilt_shape, quilt_fill]
        
        if not quilt_current_move_valid(idx) and not (achievement_dead11 in persistent.my_achievements and not preferences.hard_mode):
            renpy.jump("quilt_game_over")
        
        if quilt_checker():
            store.room3["sewing book"] = "solved"
            renpy.jump("room_3")
    
        store.quilt_moves += 1
        return


define quilt_presets = {0:[1,2,2], 2:[2,1,1], 4:[1,2,0], 7:[1,1,1], 11:[1,1,1], 12:[2,1,2], 15:[0,0,0], 16:[2,2,1], 20:[1,0,1], 23:[0,2,1], 24:[2,0,2], 34:[2,1,1], 
    35:[0,0,2], 36:[2,1,1], 41:[2,0,2], 42:[1,1,1], 44:[0,2,2], 45:[0,3,2], 54:[1,0,1], 57:[0,3,2], 59:[1,1,2], 61:[2,0,0], 62:[1,3,0], 64:[0,1,1]}
define quilt_input = {}

default quilt_color = 0
default quilt_shape = 0
default quilt_fill = 0

default quilt_moves = 0

define quilt_colors = ["blue", "red", "yellow"]
define quilt_shapes = ["bolt", "pill", "swirl", "x"]
define quilt_fills = ["empty", "full", "striped"]

screen room3_quilt():
    sensitive not inspect
    modal True
    layer "master"
    frame padding 50,40 xfill True yfill True:
        fixed xsize 775 yfill True xalign 1.0:
            vbox spacing 50 yalign 0.5:
                text _("Each tile has three qualities (color, shape, and fill). In order to finish the pattern that was intended, each adjacent tile must share exactly 2 out of three qualities with the next tile. The player is given a collection of un-sewn tiles, and is presented with the incomplete quilt and must match already placed tiles."):
                    style "puzzle_description_text"
                frame yalign 0.3 xalign 0.5 padding 50,30:
                    has vbox spacing 20
                    label _("Currently placing piece:") xalign 0.5
                    hbox xalign 0.5 spacing 50:
                        add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_color]) + "/" + str(quilt_fills[quilt_fill]) + "_" + str(quilt_shapes[quilt_shape]) + ".png" yalign 0.5
                        vbox:
                            hbox spacing 5 xalign 0.5:
                                textbutton "<" action If(quilt_color==0, SetVariable("quilt_color",2), SetVariable("quilt_color", quilt_color-1)) style "puzzle_nav_button"
                                fixed ysize 50 xsize 95:
                                    text "color" size 35 xalign 0.5
                                textbutton ">" action If(quilt_color==2, SetVariable("quilt_color",0), SetVariable("quilt_color", quilt_color+1)) style "puzzle_nav_button"
                            hbox spacing 5 xalign 0.5:
                                textbutton "<" action If(quilt_shape==0, SetVariable("quilt_shape",3), SetVariable("quilt_shape", quilt_shape-1)) style "puzzle_nav_button"
                                fixed ysize 50 xsize 95:
                                    text "shape" size 35 xalign 0.5
                                textbutton ">" action If(quilt_shape==3, SetVariable("quilt_shape",0), SetVariable("quilt_shape", quilt_shape+1)) style "puzzle_nav_button"
                            hbox spacing 5 xalign 0.5:
                                textbutton "<" action If(quilt_fill==0, SetVariable("quilt_fill",2), SetVariable("quilt_fill", quilt_fill-1)) style "puzzle_nav_button"
                                fixed ysize 50 xsize 95:
                                    text "fill" size 35 xalign 0.5
                                textbutton ">" action If(quilt_fill==2, SetVariable("quilt_fill",0), SetVariable("quilt_fill", quilt_fill+1)) style "puzzle_nav_button"
                frame xalign 1.0 ypos 0.5:
                    textbutton "RETURN" style "main_menu_button" action Return()

    fixed xoffset -400:
        add "puzzles/room_3_puzzle_1/quilt.png" align (0.5, 0.5) at zoomed(1.35)
        default testy = ""
        
        if config.developer:
            vbox yalign 0.05 xalign 0.5:
                text testy color "#000"
        grid 6 11 align (0.5, 0.5) yoffset -2 at zoomed(1.35):
            for i in range(6*11):
                fixed fit_first True:
                    if i in quilt_presets:
                        add Null(100,57)
                        if (i < 1*6 or i >= 2*6 and i < 3*6 or i >= 4*6 and i < 5*6 or i >= 6*6 and i < 7*6 or i >= 8*6 and i < 9*6 or i >= 10*6) and i%2 or not (i < 1*6 or i >= 2*6 and i < 3*6 or i >= 4*6 and i < 5*6 or i >= 6*6 and i < 7*6 or i >= 8*6 and i < 9*6 or i >= 10*6) and not i%2:
                            add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_presets[i][0]]) + "/" + str(quilt_fills[quilt_presets[i][2]]) + "_" + str(quilt_shapes[quilt_presets[i][1]]) + ".png" align (0.25,0.4) at zoomed(0.4)
                        else:
                            add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_presets[i][0]]) + "/" + str(quilt_fills[quilt_presets[i][2]]) + "_" + str(quilt_shapes[quilt_presets[i][1]]) + ".png" align (0.7,0.4) at zoomed(0.4)
                    else:
                        imagebutton idle Null(100,57) hover "puzzles/room_3_puzzle_1/tile.png" action Function(quilt_set, i)
                        #imagebutton idle "puzzles/room_3_puzzle_1/tile.png" action [Function(quilt_set, i), SetScreenVariable("testy", str(i))]
                        if i in quilt_input:
                            if (i < 1*6 or i >= 2*6 and i < 3*6 or i >= 4*6 and i < 5*6 or i >= 6*6 and i < 7*6 or i >= 8*6 and i < 9*6 or i >= 10*6) and i%2 or not (i < 1*6 or i >= 2*6 and i < 3*6 or i >= 4*6 and i < 5*6 or i >= 6*6 and i < 7*6 or i >= 8*6 and i < 9*6 or i >= 10*6) and not i%2:
                                add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_input[i][0]]) + "/" + str(quilt_fills[quilt_input[i][2]]) + "_" + str(quilt_shapes[quilt_input[i][1]]) + ".png" align (0.25,0.4) at zoomed(0.4)
                            else:
                                add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_input[i][0]]) + "/" + str(quilt_fills[quilt_input[i][2]]) + "_" + str(quilt_shapes[quilt_input[i][1]]) + ".png" align (0.7,0.4) at zoomed(0.4)

style puzzle_nav_button is main_menu_button:
    xysize (64, 64)
    hover_background "gui/button/square_hover.png"

style puzzle_nav_button_text is main_menu_button_text