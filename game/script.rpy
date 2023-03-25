﻿image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

default persistent.firstlaunch = False
default persistent.seen_splash = False
default persistent.extras_unlocked = False

label splashscreen:
    if not config.developer:
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
<<<<<<< Updated upstream
=======
define screenon = ImageDissolve("images/open.png", 0.15, 0)
define screenoff = ImageDissolve("images/open.png", 0.15, 0, reverse=True)
define placeintro = ImageDissolve("images/open.png", 3, 0)
define placeexit = ImageDissolve("images/open.png", 3, 0, reverse=True)
>>>>>>> Stashed changes

init python:
    def roomchangedx(i):
        global roomval
        roomval[0] = i/(3840-1920)
        return
    def roomchangedy(i):
        global roomval
        roomval[1] = i/(2160-1080)
        return

default roomval = [960,540]
define roomadjustmentx = ui.adjustment(range=1.0, changed=roomchangedx)
define roomadjustmenty = ui.adjustment(range=1.0, changed=roomchangedy)

screen arrow_controls():
    textbutton "RIGHT" action [Function(roomadjustmentx.change, roomval[0]+200),SetVariable("roomval", [roomval[0]+200, roomval[1]])] xalign 1.0 yalign 0.5 text_size 150
    textbutton "LEFT" action [Function(roomadjustmentx.change, roomval[0]-200),SetVariable("roomval", [roomval[0]-200, roomval[1]])] xalign 0.0 yalign 0.5 text_size 150
    textbutton "UP" action [Function(roomadjustmenty.change, roomval[1]-200),SetVariable("roomval", [roomval[0], roomval[1]-200])] xalign 0.5 yalign 0.0 text_size 150
    textbutton "DOWN" action [Function(roomadjustmenty.change, roomval[1]+200),SetVariable("roomval", [roomval[0], roomval[1]+200])] xalign 0.5 yalign 1.0 text_size 150

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
    alpha 0.0 yalign 1.0 yoffset 9 xoffset 10
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
    size 37 justify True color gui.accent_color