init python:
    def marble_init(txt=None):
        store.marble_killed = []
        store.marble_used = []
        store.marble_killed_shown = [0,0,0]
        store.marble_selected = 0
        if txt:
            renpy.notify(txt)

    def marble_dragged(drags, drop):
        drag = drags[0]
        store.marble_selected = 0
        drag.snap(marble_positions[drag.drag_name-1], 0, 0.5)
        renpy.retain_after_load()
        renpy.restart_interaction()
    
    def marble_dropped(drop, drags):
        drag = drags[0]

        if drop.drag_name not in marble_killed:
            store.marble_killed.append(drop.drag_name)
            store.marble_used.append(drag.drag_name)
            
            store.marble_selected = drop.drag_name

            renpy.sound.play(bodycrush)

            for i in range(len(marble_killed_shown)):
                if marble_killed_shown[i] == 0:
                    store.marble_killed_shown[i] = marble_selected
                    break

            if len(marble_killed) == 3:
                if [marble_solution[room1["solved"][0]],marble_solution[room1["solved"][1]],marble_solution[room1["solved"][2]]] == marble_killed:
                    store.room1["marble"] = "solved"
                    return True
                elif ("dead2" in persistent.dead_ends and not preferences.hard_mode):
                    marble_init(_("Invalid. Restarting..."))
                    renpy.retain_after_load()
                    renpy.restart_interaction()
                else:
                    renpy.jump("marble_game_over")

        renpy.retain_after_load()
        renpy.restart_interaction()

define marble_positions = [250,600,950]
define marble_solution = {"hacking":1, "decanting":2, "bomb":3}

default marble_killed = []
default marble_used = []
default marble_killed_shown = [0,0,0]
default marble_selected = 0

screen room1_marble():
    sensitive (not inspect and not _menu)
    modal True
    tag puzzle
    layer "puzzles"
    
    frame style "puzzle_frame":
        fixed align (0.1,0.3):
            add "puzzles/room_1_meta/base_marble_maze.png"

            showif marble_selected != 0:
                add "puzzles/room_1_meta/marble_maze_highlight_" + str(marble_selected) + ".png" at alphashow(1)

            for i in range(3):
                if i+1 in marble_killed:
                    add "puzzles/room_1_meta/marble_maze_effigy_" + str(i+1) + "_dead.png"
                else:
                    add "puzzles/room_1_meta/marble_maze_effigy_" + str(i+1) + ".png"


        fixed xsize 475 xalign 1.0:
            fixed ysize 880:
                vbox spacing 30 yalign 0.5:
                    style_prefix "puzzle_description"
                    label _("Instructions") yoffset -20
                    text marble_description
                    if "bomb" in room1["solved"]:
                        text _("- \"Colby Padilla\" (Bomb)")
                    if "hacking" in room1["solved"]:
                        text _("- \"Asiya Bishop\" (Hacking)")
                    if "decanting" in room1["solved"]:
                        text _("- \"Brooke Yang\" (Poison)")
                    if len(room1["solved"]) == 0:
                        text _("- Nobody :(")

        draggroup:
            if "bomb" in room1["solved"] and 1 not in marble_used:
                drag:
                    xpos 250
                    droppable False drag_name 1 dragged marble_dragged
                    add "puzzles/room_1_meta/marble1.png" zoom 0.25
            if "hacking" in room1["solved"] and 2 not in marble_used:
                drag:
                    xpos 600
                    droppable False drag_name 2 dragged marble_dragged
                    add "puzzles/room_1_meta/marble2.png" zoom 0.25
            if "decanting" in room1["solved"] and 3 not in marble_used:
                drag:
                    xpos 950
                    droppable False drag_name 3 dragged marble_dragged
                    add "puzzles/room_1_meta/marble3.png" zoom 0.25
            
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
        
        text _("Colby Padilla") xalign 0.12 yalign 0.95 style "marble_name_text"
        text _("Asiya Bishop") xalign 0.37 yalign 0.91 style "marble_name_text"
        text _("Brooke Yang") xalign 0.68 yalign 0.98 style "marble_name_text"

        if config.developer:
            vbox  xalign 0.5:
                text str(tuple(marble_killed)) xalign 0.5
                text str(tuple(marble_killed_shown)) xalign 0.5
                for i in room1["solved"]:
                    text i xalign 0.5
        
        hbox spacing 30 yalign 1.0 ysize 100 xalign 1.0:
            if not preferences.hard_mode:
                textbutton "RESET" style "confirm_button" action Function(marble_init, _("Restarting...")) text_color "#fff" sensitive not inspect yalign 0.5 at zoomed(0.75)
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] yalign 0.5

        if len(room1["solved"]) == 3 and ("room1_meta" in persistent.solved_puzzles or ("dead2" in persistent.dead_ends and not preferences.hard_mode) or not preferences.hard_mode):
            textbutton "SKIP" style "confirm_button" action [SetDict(room1, "marble", "solved"), Return()]

    if config.developer:
        vbox:
            frame:
                textbutton _("Skip Puzzle") action [SetDict(room1, "marble", "solved"), Return()] style "main_menu_button"
            frame:
                textbutton _("Game Over") action [Jump("marble_game_over")] style "main_menu_button"

style marble_name_text is puzzle_description_text:
    color "#fff"