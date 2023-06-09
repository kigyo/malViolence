default quilt_x = 6
default quilt_y = 11
default quilt_bg = "puzzles/room_3_puzzle_1/quilt.png"

image quilt_idle_button:
    Null(104,61)
    # "puzzles/room_3_puzzle_1/tile.png"

init python:
    def quilt_reset():
        store.quilt_input = {}
        store.quilt_error = None
        store.quilt_color = 0
        store.quilt_shape = 0
        store.quilt_fill = 0
        store.quilt_eraser = False
        store.quilt_moves = 0

        if difficulty_level == 1:
            store.quilt_bg = "puzzles/room_3_puzzle_1/quilt_1.png"
            store.quilt_y = 5
        elif difficulty_level == 2:
            store.quilt_bg = "puzzles/room_3_puzzle_1/quilt_2.png"
            store.quilt_y = 7
        elif difficulty_level == 3:
            store.quilt_bg = "puzzles/room_3_puzzle_1/quilt.png"
            store.quilt_y = 11
        
        store.quilt_level = difficulty_level

    def quilt_valid():
        quilts = quilt_presets.copy()
        quilts.update(quilt_input)

        for i in range(quilt_x*quilt_y):
            if i not in quilts:
                store.quilt_error = i
                return False

        for row in range(quilt_y):
            for col in range(quilt_x):
                i = row*quilt_x + col
                if i in quilts:
                    if row < quilt_y-1 and ((row+1)*quilt_x + col) in quilts and not quilt_shared(quilts[i], quilts[(row+1)*quilt_x + col]):
                        store.quilt_error = i
                        return False
                    if col < quilt_x-1 and row%2 == 0 and i%2 == 0 and i+1 in quilts and not quilt_shared(quilts[i], quilts[i+1]):
                        store.quilt_error = i
                        return False
                    if col < quilt_x-1 and row%2 == 1 and i%2 == 1 and i+1 in quilts and not quilt_shared(quilts[i], quilts[i+1]):
                        store.quilt_error = i
                        return False
        return True

    def quilt_shared(a,b):
        shared = 0
        for i in range(3):
            if a[i] == b[i]:
                shared += 1
        return shared == 2

    def quilt_set(idx):
        global quilt_input
        store.quilt_error = None
        if idx not in quilt_presets:
            quilt_input[idx] = [quilt_color, quilt_shape, quilt_fill]
        renpy.retain_after_load()

    def quilt_erase(idx):
        global quilt_input
        if idx not in quilt_presets:
            del quilt_input[idx]
        renpy.retain_after_load()

    def quilt_submit():
        if not quilt_valid() and not preferences.puzzle_resets:
            renpy.jump("quilt_game_over")
        elif not quilt_valid():
            renpy.notify(_("Not a valid solution."))
        else:
            store.room3["quilt"] = "solved"
            clear_puzzle("room3_1")
            return True


define quilt_presets = {0:[1,2,2], 2:[2,1,1], 4:[1,2,0], 7:[1,1,1], 11:[1,1,1], 12:[2,1,2], 15:[0,0,0], 16:[2,2,1], 20:[1,0,1], 23:[0,2,1], 24:[2,0,2], 34:[2,1,1],
    35:[0,0,2], 36:[2,1,1], 41:[2,0,2], 42:[1,1,1], 44:[0,2,2], 45:[0,3,2], 54:[1,0,1], 57:[0,3,2], 59:[1,1,2], 61:[2,0,0], 62:[1,3,0], 64:[0,1,1]}
default quilt_input = {}

default quilt_color = 0
default quilt_shape = 0
default quilt_fill = 0

default quilt_error = None

default quilt_eraser = False

default quilt_moves = 0

define quilt_colors = ["blue", "red", "yellow"]
define quilt_shapes = ["bolt", "pill", "swirl", "x"]
define quilt_fills = ["empty", "full", "striped"]

define quilt_description = _("""This quilt's unfinished, and {color=#fff}you need to make it complete!{/color}\n\nEach tile has {color=#fff}three traits (color, shape, and fill).\n\n{/color}In order to finish the intended pattern, each adjacent tile must share {color=#fff}exactly 2 out of 3 traits with the next tile.{/color}

Below, {color=#fff}construct the next motif{/color} you want to place by{color=#fff} adjusting the color, shape, and fill with the arrows:{/color}""")

screen room3_quilt():
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"

    if difficulty_level != quilt_level:
        timer 0.1 action Function(quilt_reset)

    frame style "puzzle_frame":
        fixed xsize 775 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5:
                    style_prefix "puzzle_description"
                    label _("Instructions")
                    text quilt_description
                    frame yalign 0.3 xalign 0.5 padding 50,30:
                        has vbox spacing 10
                        label _("Currently placing motif") xalign 0.5
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

            hbox xfill True yalign 1.0 ysize 100:
                vbox xalign 0. yalign 0.5 spacing 5:
                    textbutton "ERASER" style "confirm_button" action ToggleVariable("quilt_eraser") text_selected_idle_color gui.accent_color at zoomed(0.5)
                    textbutton "RESET" style "confirm_button" action Function(quilt_reset) at zoomed(0.5)
                textbutton "SUBMIT" style "confirm_button" action Function(quilt_submit) xalign 0.5 yalign 0.5
                textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5

        if puzzle_cleared("room3_1") or not preferences.hard_mode:
            use skip_button(room3, "quilt", "room3_1", xalign=1.0)

    fixed xoffset -400:
        if difficulty_level == 1:
            ypos 250
        elif difficulty_level == 2:
            ypos 170
        add quilt_bg align (0.5, 0.51) at zoomed(1.35)
        default testy = ""

        if config.developer:
            vbox yalign 0.05 xalign 0.5:
                text testy color "#000"
        grid quilt_x quilt_y xalign 0.5 ypos 75 at zoomed(1.35):
            for row in range(quilt_y):
                for col in range(quilt_x):
                    $ i = row*quilt_x + col
                    fixed fit_first True:
                        if i in quilt_presets:
                            add "quilt_idle_button"
                            if not row%2 and i%2 or row%2 and not i%2:
                                add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_presets[i][0]]) + "/" + str(quilt_fills[quilt_presets[i][2]]) + "_" + str(quilt_shapes[quilt_presets[i][1]]) + ".png" align (0.28,0.5) at zoomed(0.4)
                            else:
                                add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_presets[i][0]]) + "/" + str(quilt_fills[quilt_presets[i][2]]) + "_" + str(quilt_shapes[quilt_presets[i][1]]) + ".png" align (0.75,0.5) at zoomed(0.4)
                        elif i in quilt_input:
                            imagebutton idle "quilt_idle_button" hover "puzzles/room_3_puzzle_1/tile.png" action Function(quilt_set, i):
                                if quilt_eraser == True:
                                    action Function(quilt_erase, i) hover "puzzles/room_3_puzzle_1/error.png"
                            if not row%2 and i%2 or row%2 and not i%2:
                                add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_input[i][0]]) + "/" + str(quilt_fills[quilt_input[i][2]]) + "_" + str(quilt_shapes[quilt_input[i][1]]) + ".png" align (0.28,0.5) at zoomed(0.4)
                            else:
                                add "puzzles/room_3_puzzle_1/" + str(quilt_colors[quilt_input[i][0]]) + "/" + str(quilt_fills[quilt_input[i][2]]) + "_" + str(quilt_shapes[quilt_input[i][1]]) + ".png" align (0.75,0.5) at zoomed(0.4)
                        else:
                            imagebutton idle "quilt_idle_button" hover "puzzles/room_3_puzzle_1/tile.png" action Function(quilt_set, i):
                                if quilt_eraser == True:
                                    action NullAction() hover "puzzles/room_3_puzzle_1/error.png"
                        showif quilt_error == i:
                            add "puzzles/room_3_puzzle_1/error.png" at alphashow(alph=0.9)
                            #imagebutton idle "puzzles/room_3_puzzle_1/tile.png" action [Function(quilt_set, i), SetScreenVariable("testy", str(i))]
                        #if config.developer:
                        #    text "(" + str(col) + "," + str(row) + ")" outlines [(1, "#000000", 0, 0)] size 24

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room3, "quilt", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("quilt_game_over")] style "main_menu_button"

style puzzle_nav_button is main_menu_button:
    xysize (64, 64)
    hover_background "gui/button/square_hover.png"

style puzzle_nav_button_text is main_menu_button_text


transform alphashow(t=0.25, alph=1.0):
    on show:
        alpha 0
        linear t alpha alph
    on hide:
        linear t alpha 0.0
    on replace:
        alpha 0
        linear t alpha alph
    on replaced:
        linear t alpha 0.0
