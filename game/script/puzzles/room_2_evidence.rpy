init python:
    def evidence_init():
        pass

screen room2_evidence:
    sensitive not inspect
    modal True
    layer "master"
    frame style "puzzle_frame":


                
        hbox xfill True yalign 1.0 ysize 100:
            textbutton "RETURN" style "confirm_button" action Return() xalign 1.0 yalign 0.5