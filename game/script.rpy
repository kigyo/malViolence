image splash_anim_1:

    "gui/team_logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0 zoom 0.2
    easein 2 alpha 1.0 zoom 0.4 rotate -5
    easein 0.05 rotate 5
    easein 0.05 rotate 0

default persistent.firstlaunch = False
default persistent.seen_splash = False
default persistent.extras_unlocked = False

label splashscreen:
    scene black
    if not persistent.firstlaunch:
        call screen splash_settings
        $ persistent.firstlaunch = True
    show splash_anim_1
    $ renpy.pause(3)
    scene black
    with Dissolve(0.5)
    return

default inspect = None

### custom transitions

define eyeopen = ImageDissolve("images/open.png", 0.5, 0)
define eyeclose = ImageDissolve("images/open.png", 0.5, 0, reverse=True)
define screenon = ImageDissolve("images/open.png", 0.15, 0)
define screenoff = ImageDissolve("images/open.png", 0.15, 0, reverse=True)
define placeintro = ImageDissolve("images/open.png", 3, 0)
define placeexit = ImageDissolve("images/open.png", 3, 0, reverse=True)

transform crt:
    parallel:
        function WaveShader(amp=0.05, period=17.219, speed=4, direction="horizontal", damp=(0.999,0.043))

transform dizzy:
    parallel:
        function WaveShader(amp=(1,1), period=(1,2), speed=(1.5,1.5), direction="horizontal", damp=(1,0), double="horizontal")

transform crt_effects:
    parallel:
        blend "multiply" alpha 0.5
    parallel:
        function WaveShader(amp=0.05, period=17.219, speed=4, direction="vertical", damp=(0.043,1.0))

image crt = At("crt.png", crt_effects)

image ctc:
    "gui/ctc1.png"
    alpha 0.0 yalign 1.0 yoffset 9 xoffset 10 subpixel True
    block:
        ease 0.5 alpha 1.0 rotate 0
        ease 0.5 alpha 1.0 rotate 90
        ease 0.5 alpha 1.0 rotate 180
        ease 0.5 alpha 0.5 rotate 270
        rotate 0
        repeat
    #block:
    #    ease 0.5 alpha 1.0 rotate 180
    #    ease 0.5 alpha 1.0 rotate 90
    #    ease 0.5 alpha 1.0 rotate 0
    #    ease 0.5 alpha 0.5 rotate 270
    #    
    #    repeat

################### puzzle styles ################

style puzzle_description_label is gui_label:
    xalign 0.5

style puzzle_description_label_text is gui_label_text:
    color "#fff" underline True

style puzzle_description_text:
    size 28 justify True color gui.accent_color outlines [(1.5, "#000000", 1, 1)]

style puzzle_frame is gui_frame:
    background "gui/puzzle.png"
    padding (50,40) xfill True yfill True

################### for defining mini cgs in the game ################
image tutorial_pellets = "images/tutorial_pellets.png"
image room1_electricchair = "images/room1_electricchair.png"
image room1_megaphones = "images/room1_megaphones.png"
image room1_oil = "images/room1_oil.png"
image room2_blueprintcollection = "images/room2_blueprintcollection.png"
image room2_evidenceboard = "images/room2_evidenceboard.png"
image room2_limbsdesigns = "images/room2_limbsdesigns.png"
image room2_news = "images/room2_news.png"
image room2_postitnotes = "images/room2_postitnotes.png"
image room3_lockedbox = "images/room3_lockedbox.png"
image room3_notebook = "images/room3_notebook.png"
image room3_report = "images/room3_report.png"
image room3_scrapbookcg = "images/room3_scrapbookcg.png"
image room3_sewingsetup = "images/room3_sewingsetup.png"
image room3_wig = "images/room3_wig.png"



################ reset some puzzles after loading a save (drags reset their positions)
init python:
    def clear_puzzle(name):
        if name not in persistent.solved_puzzles:
            persistent.solved_puzzles.append(name)
            
    def reset_puzzles_after_load():
        #room1

        #room2
        word_init()

        #room3
        scrapbook_init()
        pass

    config.after_load_callbacks.append(reset_puzzles_after_load)

default persistent.solved_puzzles = []