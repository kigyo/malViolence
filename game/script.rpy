image splash_anim_1:

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

define eyeopen = ImageDissolve("images/open.png", 0.5, 0)

init python:
    def roomchangedx(i):
        global roomval
        roomval[0] = i/(3840-1920)
        return
    def roomchangedy(i):
        global roomval
        roomval[1] = i/(2160-1080)
        return

default roomval = [0.5, 0.5]
define roomadjustmentx = ui.adjustment(range=1.0, changed=roomchangedx)
define roomadjustmenty = ui.adjustment(range=1.0, changed=roomchangedy)