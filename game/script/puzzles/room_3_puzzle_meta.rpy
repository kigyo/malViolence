screen room3_meta:
    sensitive not inspect
    modal True
    tag puzzle
    layer "puzzles"
    frame style "puzzle_frame":
        default scrapbook_page = 1

        if scrapbook_page == 1:
            add "puzzles/room_3_meta/scrapbook2.png" xalign 0.5
            imagebutton idle Null(175,140) action SetScreenVariable("scrapbook_page",2) xpos 1402 mouse "inspect"

        else:
            add "puzzles/room_3_meta/scrapbook1.png" xalign 0.5
            imagebutton idle Null(145,135) action SetScreenVariable("scrapbook_page",1) xpos 203 ypos 75 mouse "inspect"

        draggroup ypos 0 xpos 0:
            if "quilt" in room3["solved"]:
                drag: 
                    xpos 0
                    add "room3_meta1" at rotated(5)
            if "cooking" in room3["solved"]:
                drag: 
                    xpos 300
                    add "room3_meta2" at rotated(-10)
            if "toys" in room3["solved"]:
                drag: 
                    xpos 600
                    add "room3_meta3" at rotated(-5)
        
        #if len(room3["solved"]) >= 3 and room3["scrapbook_new"] < 2:
        #    timer 0.1 action Jump("room3_meta_cutscene") 
        #if room3["scrapbook_new"] == 2:
        #    use jigsaw 

        textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 1.0
