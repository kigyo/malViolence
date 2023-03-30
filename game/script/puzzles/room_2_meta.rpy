define word_description = _("Can you come up with a word that's almost as good as the above?")
define word_lenient_failure_message = _("(Nope, not good enough!)")

init python:
    def word_dropped(drop, drags):

        drag = drags[0]
        if isinstance(drop.drag_name, str):
            word_swapped(drop, drags)
        elif word_answer[drop.drag_name]:
            drag.snap((drop.drag_name)*110+205,385,0.3)
        else:
            drag.snap((drop.drag_name)*110+205,495,0.3)
            store.word_answer[drop.drag_name] = drag.drag_name
        renpy.retain_after_load()
        renpy.restart_interaction()
    
    def word_moved(drags):
        drag = drags[0]
        for i in range(len(word_answer)):
            if word_answer[i] == drag.drag_name:
                store.word_answer[i] = ""
        renpy.retain_after_load()
        renpy.restart_interaction()

    def word_submit():
        string_answer = ""
        for i in word_answer:
            string_answer += i

        if len(string_answer) < 5 or string_answer not in word_accepted_answers:
            if not (achievement_dead6 in persistent.dead_ends and not preferences.hard_mode):
                renpy.jump("word_game_over")
            else:
                cr(word_lenient_failure_message)
        store.room2["word"] = "solved"
        return True


default word_answer = ["","","","",""]
define word_rival = "TASER"
define word_accepted_answers = ["ASTER", "RATES", "TEARS", "STARE"]

screen room2_word():
    sensitive not inspect
    modal True
    tag puzzle
    layer "master"

    frame padding 50,40 xfill True yfill True:
        fixed xsize 700 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5 xfill True:
                    hbox xalign 0.5:
                        for i in range(len(word_rival)):
                            frame xysize(75,75):
                                text word_rival[i] align (0.5,0.5)
                    text word_description style "puzzle_description_text"
                    
            hbox xfill True yalign 1.0 ysize 100:
                frame xalign 0.5 yalign 0.5:
                    textbutton "SUBMIT" style "main_menu_button" action Function(word_submit)
                frame xalign 1.0 yalign 0.5:
                    textbutton "RETURN" style "main_menu_button" action [SetVariable("word_answer", ["","","","",""]), Return()]
                    
        fixed xsize 1920-700:
            draggroup ysize 600 xsize 990 yalign 0.45 xalign 0.45:
                drag yalign 1.0 xpos 200:
                    drag_name 0 draggable False dropped word_dropped
                    frame xysize(110,110):
                        pass
                drag yalign 1.0 xpos 310:
                    drag_name 1 draggable False dropped word_dropped
                    frame xysize(110,110):
                        pass
                drag yalign 1.0 xpos 420:
                    drag_name 2 draggable False dropped word_dropped
                    frame xysize(110,110):
                        pass
                drag yalign 1.0 xpos 530:
                    drag_name 3 draggable False dropped word_dropped
                    frame xysize(110,110):
                        pass
                drag yalign 1.0 xpos 640:
                    drag_name 4 draggable False dropped word_dropped
                    frame xysize(110,110):
                        pass

                #TODO: make obtaining tiles conditional on having solved other puzzles
                if not inspect or inspect and "A" not in word_answer:
                    drag xalign 0.1 yalign 0.1:
                        drag_name "A" activated word_moved
                        frame background Solid(gui.accent_color) xysize(100,100):
                            text "A" color "#000" align (0.5,0.5)
                if not inspect or inspect and "E" not in word_answer:
                    drag xalign 0.3 yalign 0.4:
                        drag_name "E" activated word_moved
                        frame background Solid(gui.accent_color) xysize(100,100):
                            text "E" color "#000" align (0.5,0.5)
                if not inspect or inspect and "R" not in word_answer:
                    drag xalign 0.5 yalign 0.0:
                        drag_name "R" activated word_moved
                        frame background Solid(gui.accent_color) xysize(100,100):
                            text "R" color "#000" align (0.5,0.5)
                if not inspect or inspect and "S" not in word_answer:
                    drag xalign 0.7 yalign 0.2:
                        drag_name "S" activated word_moved
                        frame background Solid(gui.accent_color) xysize(100,100):
                            text "S" color "#000" align (0.5,0.5)
                if not inspect or inspect and "T" not in word_answer:
                    drag xalign 0.9 yalign 0.3:
                        drag_name "T" activated word_moved
                        frame background Solid(gui.accent_color) xysize(100,100):
                            text "T" color "#000" align (0.5,0.5)

            if inspect:
                fixed ysize 600 xsize 990 yalign 0.45 xalign 0.45:
                    for i in range(len(word_answer)):
                        if word_answer[i] != "":
                            frame background Solid(gui.accent_color) xysize(100,100) pos (i*110+205,495):
                                text word_answer[i] color "#000" align (0.5,0.5)


    if config.developer:
        #hbox xalign 0.5:
        #    for i in word_answer:
        #        text i + " "
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room3, "word", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("word_game_over")] style "main_menu_button"
