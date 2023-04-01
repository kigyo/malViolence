init python:
    def marble_init():
        store.marble_killed = [0, 0, 0]
    
    def marble_dragged(drags, drop):
        drag = drags[0]
        drag.snap(marble_positions[drag.drag_name-1], 0, 0.5)
    
    def marble_dropped(drop, drags):
        drag = drags[0]
        if marble_killed[drop.drag_name-1] == 0:
            store.marble_killed[drop.drag_name-1] = drag.drag_name
        renpy.retain_after_load()
        renpy.restart_interaction()


define marble_positions = [250,600,950]

default marble_killed = [0, 0, 0]
default marble_selected = 0

screen room1_marble():
    sensitive not inspect
    modal True
    tag puzzle
    layer "puzzles"
    
    frame style "puzzle_frame":
        fixed align (0.1,0.3) at zoomed(0.6):
            add "puzzles/room_1_meta/base_marble_maze.png"

            for i in range(3):
                if marble_killed[i] == 0:
                    add "puzzles/room_1_meta/marble_maze_effigy_" + str(i+1) + ".png"
                else:
                    add "puzzles/room_1_meta/marble_maze_effigy_" + str(i+1) + "_dead.png"

        fixed xsize 475 xalign 1.0:
            fixed ysize 880:
                vbox spacing 30 yalign 0.5:
                    style_prefix "puzzle_description"
                    label _("Instructions") yoffset -20
                    text marble_description
                    if "bomb" in room1["solved"]:
                        text _("- \"Field Marshall Grad Rufos\" (Bomb)")
                    if "hacking" in room1["solved"]:
                        text _("- \"Attorney General Zark Hundor\" (Hacking)")
                    if "decanting" in room1["solved"]:
                        text _("- \"Imperator Unnfer Progas\" (Poison)")

        draggroup:
            if "bomb" in room1["solved"] and 1 not in marble_killed:
                drag:
                    xpos 250
                    droppable False drag_name 1 dragged marble_dragged
                    add "puzzles/room_1_meta/marble.png"
            if "hacking" in room1["solved"] and 2 not in marble_killed:
                drag:
                    xpos 600
                    droppable False drag_name 2 dragged marble_dragged
                    add "puzzles/room_1_meta/marble.png"
            if "decanting" in room1["solved"] and 3 not in marble_killed:
                drag:
                    xpos 950
                    droppable False drag_name 3 dragged marble_dragged
                    add "puzzles/room_1_meta/marble.png"
            
            drag:
                draggable False dropped marble_dropped
                pos (230,210) drag_name 1
                add Null(150,150) #Solid("#000") xysize 150,150 alpha 0.5
            drag:
                draggable False dropped marble_dropped
                pos (565,190) drag_name 2
                add Null(150,150)
            drag:
                draggable False dropped marble_dropped
                pos (1035,160) drag_name 3
                add Null(150,150)
        
        text str(tuple(marble_killed)) xalign 0.5
        
        hbox xfill True yalign 1.0 ysize 100:
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room1, "marble", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("marble_game_over")] style "main_menu_button"