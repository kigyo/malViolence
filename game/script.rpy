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
    show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0
    if not persistent.seen_splash:
        $ renpy.pause(5)
        $ persistent.seen_splash = True
    else:
        if renpy.pause(5):
            jump skip_splash
    scene black
    with fade

    label skip_splash:
        pass
    return

default inspect = None
default minigame = False

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

style puzzle_description_text:
    size 28 justify True color gui.accent_color 



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