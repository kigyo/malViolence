init python:
    def decanting_dropped(drop_size, answer, drop, drags):
        drag = drags[0]
        drag.snap((drag.drag_name-1)*345,100,0.3)

        drag_filled = getattr(renpy.store, "decanting_vial%s" % str(drag.drag_name))
        drop_filled = getattr(renpy.store, "decanting_vial%s" % str(drop.drag_name))

        if drag_filled > 0 and drop_filled < drop_size:
            store.decanting_moves += 1

            transfer_amount = drag_filled
            if drag_filled + drop_filled > drop_size:
                transfer_amount = drop_size - drop_filled

            setattr(renpy.store, "decanting_vial%s" % str(drop.drag_name), drop_filled + transfer_amount)
            setattr(renpy.store, "decanting_vial%s" % str(drag.drag_name), drag_filled - transfer_amount)

            renpy.sound.play(liquidpour2)
            renpy.retain_after_load()
            renpy.restart_interaction()

            if decanting_valid(answer):
                store.room1["decanting"] = "solved"
                clear_puzzle("room1_3")
                return True

            if decanting_moves >= decanting_move_limit and not preferences.puzzle_resets:
                renpy.jump("decanting_game_over")

    def decanting_valid(answer):
        args = answer[:]
        found = 0
        args = list(args)
        for i in range(3):
            if getattr(renpy.store, "decanting_vial%s" % str(i+1)) in args:
                args.remove(getattr(renpy.store, "decanting_vial%s" % str(i+1)))
                found += 1
        return found == len(answer)

    def decanting_init():
        store.decanting_moves = 0
        if difficulty_level == 1:
            store.decanting_vial1 = 8
            store.decant_kwargs = {"v1":8, "v2":6, "v3":2, "answer":[4, 4, 0]}
            store.decanting_size_vial1 = 8
            store.decanting_size_vial2 = 6
            store.decanting_size_vial3 = 2
            store.decanting_solution = 4
        if difficulty_level == 2:
            store.decanting_vial1 = 12
            store.decant_kwargs = {"v1":12, "v2":8, "v3":5, "answer":[6, 6, 0]}
            store.decanting_size_vial1 = 12
            store.decanting_size_vial2 = 8
            store.decanting_size_vial3 = 5
            store.decanting_solution = 6
        if difficulty_level == 3:
            store.decanting_vial1 = 18
            store.decant_kwargs = {"v1":18, "v2":10, "v3":7, "answer":[9, 9, 0]}
            store.decanting_size_vial1 = 18
            store.decanting_size_vial2 = 10
            store.decanting_size_vial3 = 7
            store.decanting_solution = 9
        store.decanting_vial2 = 0
        store.decanting_vial3 = 0
        
        store.decanting_level = difficulty_level

default decant_kwargs = {"v1":18, "v2":10, "v3":7, "answer":[9, 9, 0]}
default decanting_moves = 0
define decanting_move_limit = 20

default decanting_size_vial1 = 12
default decanting_size_vial2 = 8
default decanting_size_vial3 = 5
default decanting_solution = 6

default decanting_vial1 = 12
default decanting_vial2 = 0
default decanting_vial3 = 0

screen room1_decanting(v1=12, v2=8, v3=5, answer=[6, 6, 0]):
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"

    style_prefix "decanting"

    if difficulty_level != decanting_level:
        timer 0.1 action Function(decanting_init)

    frame style "puzzle_frame":
        fixed xsize 675 xalign 1.0:
            fixed ysize 880:
               vbox spacing 50 yalign 0.5:
                    style_prefix "puzzle_description"
                    label _("Instructions")
                    text decanting_description

            hbox xfill True yalign 1.0 ysize 100:
                textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5
        fixed xsize 1920-775:
            draggroup ysize 600 xsize 990 yalign 0.35 xalign 0.45:
                drag yalign 1.0:
                    drag_name 1 dropped renpy.curry(decanting_dropped)(decanting_size_vial1, answer[:])
                    bar value AnimatedValue(decanting_vial1,decanting_size_vial1, 0.75) xalign 0.5 style "decanting_bar1"
                drag yalign 1.0 xalign 0.5:
                    drag_name 2 dropped renpy.curry(decanting_dropped)(decanting_size_vial2, answer[:])
                    bar value AnimatedValue(decanting_vial2,decanting_size_vial2, 0.75) xalign 0.5 style "decanting_bar2"
                drag yalign 1.0 xalign 1.0:
                    drag_name 3 dropped renpy.curry(decanting_dropped)(decanting_size_vial3, answer[:])
                    bar value AnimatedValue(decanting_vial3,decanting_size_vial3, 0.75) xalign 0.5 style "decanting_bar3"
            hbox xalign 0.45 yalign 0.8 spacing 200:
                hbox xsize 150:
                    text str(decanting_vial1) + "/" + str(decanting_size_vial1) xalign 0.5
                hbox xsize 150:
                    text str(decanting_vial2) + "/" + str(decanting_size_vial2) xalign 0.5
                hbox xsize 150:
                    text str(decanting_vial3) + "/" + str(decanting_size_vial3) xalign 0.5

            if not preferences.puzzle_resets:
                frame xalign 1.0:
                    text str(decanting_moves) + "/" + str(decanting_move_limit) style "main_menu_button"
        if puzzle_cleared("room1_3") or not preferences.hard_mode:
            use skip_button(room1, "decanting", "room1_3")

    if config.developer:
        vbox:
            textbutton _("Skip Puzzle") action [SetDict(room1, "decanting", "solved"), Return()] style "confirm_button"
            textbutton _("Game Over") action [Jump("decanting_game_over")] style "confirm_button"

style decanting_bar1:
    bar_vertical True xsize 300 ysize 500 bottom_gutter 20 top_gutter 75
    top_bar "puzzles/room_1_puzzle_3/glass1_empty.png"
    bottom_bar "puzzles/room_1_puzzle_3/glass1_full.png"

style decanting_bar2:
    bar_vertical True xsize 300 ysize 500 bottom_gutter 20
    top_bar "puzzles/room_1_puzzle_3/glass2_empty.png"
    bottom_bar "puzzles/room_1_puzzle_3/glass2_full.png"

style decanting_bar3:
    bar_vertical True xsize 300 ysize 500 bottom_gutter 20 top_gutter 80
    top_bar "puzzles/room_1_puzzle_3/glass3_empty.png"
    bottom_bar "puzzles/room_1_puzzle_3/glass3_full.png"
