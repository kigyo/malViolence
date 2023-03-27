define decanting_description = _("""Cautionne needs your help poisoning a top STOP official, but his toxin of choice is pretty particular!

Using three vials of {color=#fff}18cc, 10cc,{/color}  and {color=#fff}7cc{/color}  - {color=#fff}measure the poison into two equal doses of 9cc.{/color} Note that {color=#fff}the 18cc vial contains the poison itself.{/color}

But be careful! {color=#fff}If the poison's disturbed too much, it'll give off nasty vapors...{/color}
    
Drag the vials in order to pour their contents into each other.""")

init python:
    def decanting_dropped(drop, drags):

        drag = drags[0]
        drag.snap((drag.drag_name-1)*345,100,0.3)

        drag_filled = getattr(renpy.store, "decanting_vial%s" % str(drag.drag_name))
        
        if drag_filled > 0:
            store.decanting_moves += 1
            
            drop_filled = getattr(renpy.store, "decanting_vial%s" % str(drop.drag_name))
            drop_size = getattr(renpy.store, "decanting_size_vial%s" % str(drop.drag_name))

            transfer_amount = drag_filled
            if drag_filled + drop_filled > drop_size:
                transfer_amount = drop_size - drop_filled

            setattr(renpy.store, "decanting_vial%s" % str(drop.drag_name), drop_filled + transfer_amount)
            setattr(renpy.store, "decanting_vial%s" % str(drag.drag_name), drag_filled - transfer_amount)

            renpy.retain_after_load()
            renpy.restart_interaction()

            if decanting_valid():
                renpy.jump("decanting_solved")
            
            if decanting_moves >= decanting_move_limit and not (achievement_dead5 in persistent.my_achievements and not preferences.hard_mode):
                renpy.jump("decanting_game_over")

    def decanting_valid():
        nines = 0
        for i in range(3):
            if getattr(renpy.store, "decanting_vial%s" % str(i+1)) == 9:
                nines += 1
        return nines == 2
    

default decanting_moves = 0
define decanting_move_limit = 20

define decanting_size_vial1 = 18
define decanting_size_vial2 = 10
define decanting_size_vial3 = 7

default decanting_vial1 = 18
default decanting_vial2 = 0
default decanting_vial3 = 0

screen room1_decanting():
    sensitive not inspect
    modal True
    tag puzzle
    layer "master"

    style_prefix "decanting"
    
    frame padding 50,40 xfill True yfill True:

        fixed xsize 725 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5:
                    style_prefix "puzzle_description"
                    text decanting_description
                
            hbox xfill True yalign 1.0 ysize 100:
                frame xalign 1.0 yalign 0.5:
                    textbutton "RETURN" style "main_menu_button" action Return()

        fixed xsize 1920-775:
            draggroup ysize 600 xsize 990 yalign 0.45 xalign 0.45:
                drag yalign 1.0:
                    drag_name 1 dropped decanting_dropped
                    bar value AnimatedValue(decanting_vial1,18, 0.75) xalign 0.5 style "decanting_bar1"
                drag yalign 1.0 xalign 0.5:
                    drag_name 2 dropped decanting_dropped
                    bar value AnimatedValue(decanting_vial2,10, 0.75) xalign 0.5 style "decanting_bar2"
                drag yalign 1.0 xalign 1.0:
                    drag_name 3 dropped decanting_dropped
                    bar value AnimatedValue(decanting_vial3,7, 0.75) xalign 0.5 style "decanting_bar3"
            hbox xalign 0.45 yalign 0.85 spacing 200:
                hbox xsize 150:
                    text str(decanting_vial1) + "/" + str(decanting_size_vial1) xalign 0.5
                hbox xsize 150:
                    text str(decanting_vial2) + "/" + str(decanting_size_vial2) xalign 0.5
                hbox xsize 150:
                    text str(decanting_vial3) + "/" + str(decanting_size_vial3) xalign 0.5

        if not (achievement_dead5 in persistent.my_achievements and not preferences.hard_mode):
            frame xalign 1.0:
                text str(decanting_moves) + "/" + str(decanting_move_limit) style "main_menu_button"
    
    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [Jump("decanting_solved")] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("decanting_game_over")] style "main_menu_button"

style decanting_bar1:
    bar_vertical True xsize 300 ysize 500 bottom_gutter 20
    top_bar "puzzles/room_1_puzzle_3/glass1_empty.png"
    bottom_bar "puzzles/room_1_puzzle_3/glass1_full.png"

style decanting_bar2:
    bar_vertical True xsize 300 ysize 500 bottom_gutter 20
    top_bar "puzzles/room_1_puzzle_3/glass2_empty.png"
    bottom_bar "puzzles/room_1_puzzle_3/glass2_full.png"

style decanting_bar3:
    bar_vertical True xsize 300 ysize 500 bottom_gutter 20
    top_bar "puzzles/room_1_puzzle_3/glass3_empty.png"
    bottom_bar "puzzles/room_1_puzzle_3/glass3_full.png"