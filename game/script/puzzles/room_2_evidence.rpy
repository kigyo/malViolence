init python:
    def evidence_init(start=False):
        store.evidence_connections = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        if not start:
            renpy.notify(_("Invalid. Restarting..."))

    def evidence_dragged(drags, drop):
        drag = drags[0]
        drag.snap(evidence_positions[drag.drag_name][0], evidence_positions[drag.drag_name][1], 0.5)

    def evidence_dropped(drop, drags):
        global evidence_connections
        drag = drags[0]
        if drop.drag_name not in evidence_connections[drag.drag_name] and drag.drag_name not in evidence_connections[drop.drag_name]:
            if drop.drag_name < drag.drag_name:
                evidence_connections[drop.drag_name].append(drag.drag_name)
            else:
                evidence_connections[drag.drag_name].append(drop.drag_name)
        elif drop.drag_name in evidence_connections[drag.drag_name]:
            evidence_connections[drag.drag_name].remove(drop.drag_name)
        elif drag.drag_name in evidence_connections[drop.drag_name]:
            evidence_connections[drop.drag_name].remove(drag.drag_name)
        renpy.retain_after_load()
        renpy.restart_interaction()

    def evidence_valid():
        
        for i in range(len(evidence_solutions)):
            for solution in evidence_solutions[i]:
                for connection in evidence_connections[solution]:
                    if connection not in evidence_solutions[i]:
                        return False
                        
        for i in range(len(evidence_solutions)):
            if sorted(evidence_connections[evidence_solutions[i][0]]) == sorted(evidence_solutions[i][1:]):
                continue
            elif evidence_connections[evidence_solutions[i][0]] == [evidence_solutions[i][1]] and evidence_connections[evidence_solutions[i][1]] == [evidence_solutions[i][2]]:
                continue
            elif evidence_connections[evidence_solutions[i][0]] == [evidence_solutions[i][2]] and evidence_connections[evidence_solutions[i][1]] == [evidence_solutions[i][2]]:
                continue
            else:
                return False
        return True

    def evidence_submit():
        if evidence_valid():
            store.room2["evidence"] = "solved"
            return True
        elif ("dead7" in persistent.dead_ends and not preferences.hard_mode):
            evidence_init()
            renpy.retain_after_load()
            renpy.restart_interaction()
        else:
            renpy.jump("evidence_game_over")

define evidence_notes = {
    0: _("During our last operation, we only managed to save three test subjects.\n\nWe also found some incomplete records and a box of their personal belongings from the subjects on-site. \n\nUsing what information we have, {i}figure out which item belongs to who, and who grew up where{/i}."),
    1: _("The harmonica has traces of wild pollen found only in remote regions that have yet to be extensively developed."),
    2: _("The red headed kid is certain they did not live in the city."),
    3: _("The bracelet is too big for the redhead."),
    4: _("The blonde kid managed to play a tune on the harmonica when asked, but the other two children could not."),
}

default evidence_connections = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
define evidence_solutions = [[2,3,7], [4,5,6], [0,1,8]]
define evidence_positions = [(0.05,0.05),(0.25,0.2),(0.2,0.65),(0.0,0.5),(0.45,0.7),(0.65,0.1),(0.7,0.65),(0.8,0.0),(0.88,0.25)]
define evidence_note_positions = {1:(0.11,0.45), 2:(0.4,0.0), 3:(0.96,0.72), 4:(0.79,0.4)}
define evidence_small = [2,3]

screen room2_evidence():
    sensitive not inspect
    modal True
    tag puzzle
    layer "puzzles"

    frame style "puzzle_frame":

        use evidence_note(0, xs=500, ys=500)

        for i in range(len(evidence_positions)):
            use evidence_photo(i)

        for i in room2["notes"]:
            if i in evidence_small:
                use evidence_note(i, evidence_note_positions[i][0],evidence_note_positions[i][1], 250, 250)
            else:
                use evidence_note(i, evidence_note_positions[i][0],evidence_note_positions[i][1])

        draggroup:
            for id in range(len(evidence_positions)):
                drag pos (evidence_positions[id][0], evidence_positions[id][1]):
                    drag_name id dropped evidence_dropped dragged evidence_dragged
                    frame background Null() xysize 200,300 pos (evidence_positions[id][0], evidence_positions[id][1]):
                        add Solid("#0000004a") xysize 200,300 xoffset 15 yoffset 15
                        add "puzzles/room_2_puzzle_1/"+ str(id) +".jpg"
                        fixed xpos 0.35:
                            add "puzzles/room_2_puzzle_1/pin_shadow.png"
                            add "puzzles/room_2_puzzle_1/pin.png"
        
        for i in evidence_connections:
            for j in evidence_connections[i]:
                add "puzzles/room_2_puzzle_1/"+str(i)+"_"+str(j)+".png" at alphashow

        for i in range(len(evidence_positions)):
            frame background Null() xysize 200,300 xoffset 20 pos (evidence_positions[i][0], evidence_positions[i][1]):
                add "puzzles/room_2_puzzle_1/pin_upper.png" xalign 0.35
                
        vbox xfill True yalign 1.0 ysize 100 spacing 30:
            textbutton "SUBMIT" style "confirm_button" action Function(evidence_submit) xalign 1.0 yalign 0.5
            textbutton "RETURN" style "confirm_button" action [Return(), With(puzzle_hide)] xalign 1.0 yalign 0.5

        if "room2_1" in persistent.solved_puzzles:
            textbutton "SKIP" style "confirm_button" action [SetDict(room2, "evidence", "solved"), Return()]

    if config.developer:
        vbox:
            textbutton _("Skip Puzzle") action [SetDict(room2, "evidence", "solved"), Return()] style "confirm_button"
            textbutton _("Game Over") action [Jump("evidence_game_over")] style "confirm_button"

screen evidence_note(id, x=0.5, y=0.45, xs=350, ys=350):
    add Solid("#0000004a") xysize xs,ys align (x,y) xoffset 20 yoffset 20
    frame background Solid("#ffafee") xysize xs,ys padding int(xs/10),int(ys/10) align (x,y):
        text evidence_notes[id] align (0.5,0.5) style "evidence_note_text"

screen evidence_photo(id):
    zorder -5
    frame background Solid("#0000004a") xysize 200,300 xoffset 20 yoffset 20 pos (evidence_positions[id][0], evidence_positions[id][1]):
        fixed xoffset -20 yoffset -20:
            add "puzzles/room_2_puzzle_1/"+ str(id) +".jpg"
            fixed xpos 0.35:
                add "puzzles/room_2_puzzle_1/pin_shadow.png"
                add "puzzles/room_2_puzzle_1/pin_lower.png"

style evidence_note_text:
    color "#790e0e" font "gui/font/TitilliumWeb-Regular.ttf" size 28 line_spacing -10 justify True outlines[(2, "#e381ba", 0, 0)]