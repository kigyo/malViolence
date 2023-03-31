init python:
    def evidence_init():
        store.evidence_connections = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}

    def evidence_dropped(drop, drags):
        global evidence_connections
        drag = drags[0]
        drag.snap(evidence_positions[drag.drag_name][0], evidence_positions[drag.drag_name][1], 0.5)
        if drop.drag_name not in evidence_connections[drag.drag_name] and drag.drag_name not in evidence_connections[drop.drag_name]:
            evidence_connections[drag.drag_name].append(drop.drag_name)


define evidence_notes = {
    0: _("During our last operation, we only managed to save three test subjects. We also found some incomplete records and a box of their personal belongings from the subjects on site. \n\nUsing what information we have, {u}figure out which item belongs to who, and who grew up where{/u}.")
}
define evidence_positions = [(0.05,0.05),(0.25,0.2),(0.2,0.65),(0.0,0.5),(0.45,0.7),(0.65,0.1),(0.7,0.65),(0.8,0.0),(0.88,0.25)]
#room2["notes"] = []

default evidence_connections = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}

screen room2_evidence:
    sensitive not inspect
    modal True
    layer "master"
    frame style "puzzle_frame":
        use evidence_note(0)

        for i in range(len(evidence_positions)):
            use evidence_photo(i)

        draggroup:
            for id in range(len(evidence_positions)):
                drag pos (evidence_positions[id][0], evidence_positions[id][1]):
                    drag_name id dropped evidence_dropped
                    frame background Null() xysize 200,300 pos (evidence_positions[id][0], evidence_positions[id][1]):
                        add "puzzles/room_2_puzzle_1/"+ str(id) +".jpg"
                        fixed xpos 0.35:
                            add "puzzles/room_2_puzzle_1/pin_shadow.png"
                            add "puzzles/room_2_puzzle_1/pin_lower.png"
                            add "puzzles/room_2_puzzle_1/pin_upper.png"
                
        vbox xfill True yalign 1.0 ysize 100 spacing 30:
            textbutton "SUBMIT" style "confirm_button" action Return() xalign 1.0 yalign 0.5
            textbutton "RETURN" style "confirm_button" action Return() xalign 1.0 yalign 0.5


screen evidence_note(id, x=0.5, y=0.5):
    add Solid("#0000004a") xysize 500,500 align (x,y) xoffset 20 yoffset 20
    frame background Solid("#ffafee") xysize 500,500 padding 50,50 align (x,y):
        text evidence_notes[id] align (0.5,0.5) style "evidence_note_text"

screen evidence_photo(id):
    zorder -5
    frame background Solid("#0000004a") xysize 200,300 xoffset 20 yoffset 20 pos (evidence_positions[id][0], evidence_positions[id][1]):
        fixed xoffset -20 yoffset -20:
            add "puzzles/room_2_puzzle_1/"+ str(id) +".jpg"
            fixed xpos 0.35:
                add "puzzles/room_2_puzzle_1/pin_shadow.png"
                add "puzzles/room_2_puzzle_1/pin_lower.png"
                add "puzzles/room_2_puzzle_1/pin_upper.png"

style evidence_note_text:
    color "#fff" font "gui/font/TitilliumWeb-Regular.ttf" size 29 line_spacing -10 justify True outlines [(1.5, "#790e0e", 1, 1)]