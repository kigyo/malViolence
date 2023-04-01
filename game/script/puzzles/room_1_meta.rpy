init python:
    def marble_init():
        store.marble_killed = [False, False, False]
    
    def marble_dragged():
        drag = drags[0]
        drag.snap(marble_positions[drag.drag_name][0], 0, 0.5)
    
    def marble_dropped():
        pass



default marble_killed = [False, False, False]
default marble_used = [0,0,0]
default marble_positions = [200,400,600]
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
                if marble_killed[i] == False:
                    add "puzzles/room_1_meta/marble_maze_effigy_" + str(i+1) + ".png"
                else:
                    add "puzzles/room_1_meta/marble_maze_effigy_" + str(i+1) + "_dead.png"

        fixed xsize 475 xalign 1.0:
            fixed ysize 880:
                vbox spacing 50 yalign 0.5:
                    style_prefix "puzzle_description"
                    label _("Instructions")
                    text marble_description

        draggroup:
            if "bomb" in room1["solved"] and 1 not in marble_used:
                drag:
                    droppable False drag_name 1
                    add "puzzles/room_1_meta/marble.png"
            if "hacking" in room1["solved"] and 2 not in marble_used:
                drag:
                    droppable False drag_name 2
                    add "puzzles/room_1_meta/marble.png"
            if "decanting" in room1["solved"] and 3 not in marble_used:
                drag:
                    droppable False drag_name 3
                    add "puzzles/room_1_meta/marble.png"
            
            drag:
                draggable False dropped marble_dropped
                pos (230,210)
                add Solid("#000") xysize 150,150 alpha 0.5
            drag:
                draggable False dropped marble_dropped
                pos (565,190)
                add Solid("#000") xysize 150,150 alpha 0.5
            drag:
                draggable False dropped marble_dropped
                pos (1035,160)
                add Solid("#000") xysize 150,150 alpha 0.5#Null(150,150)
        
        
        hbox xfill True yalign 1.0 ysize 100:
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5