define word_description = _("")

init python:
    def word_submit():
        pass

screen room2_meta():
    sensitive not inspect
    modal True
    tag puzzle
    layer "master"

    frame padding 50,40 xfill True yfill True:
        fixed xsize 700 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5:
                    text word_description style "puzzle_description_text"
                    
            hbox xfill True yalign 1.0 ysize 100:
                frame xalign 0.5 yalign 0.5:
                    textbutton "SUBMIT" style "main_menu_button" action Function(word_submit)
                frame xalign 1.0 yalign 0.5:
                    textbutton "RETURN" style "main_menu_button" action Return()
                    
        fixed xsize 1920-700:
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

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room3, "word", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("word_game_over")] style "main_menu_button"


default word_answer = []
