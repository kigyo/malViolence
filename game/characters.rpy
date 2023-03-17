screen debugging():
    vbox:
        text testvar
        text str(speaking)

default testvar = "0"

init python:
    config.overlay_screens.append("debugging")

default speaking =None
init python:

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        global speaking
        if speaking == name and not _menu:
            return speak_d, 0.1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        speaking = name
        if event == "slow_done":
            speaking = None
            renpy.restart_interaction()

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

define x = Character(_("???"), color="#00e7ff", image="cautionne", callback=speaker("cautionne"))
define c = Character(_("Cautionne"), color="#00e7ff", image="cautionne", callback=speaker("cautionne"))
define p = Character(_("Protagonist"), color="#ffffff", image="protagonist", callback=speaker("protagonist"))

image bg cautionne_screen = "cautionne_screen_background.png"

layeredimage cautionne annoyed:
    zoom 0.5
    always "cautionne_annoyed_closed_face"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_annoyed_speaking", "cautionne_annoyed_closed_face")
    group hands:
        attribute hands default WhileSpeaking("cautionne", "cautionne_annoyed_hands_speaking", "cautionne_annoyed_closed_hands")
        attribute nohands Null()
image cautionne_annoyed_speaking:
    "cautionne_annoyed_open_face"
    pause 0.12
    "cautionne_annoyed_closed_face"
    pause 0.12
    repeat
image cautionne_annoyed_hands_speaking:
    "cautionne_annoyed_open_hands"
    pause 0.12
    "cautionne_annoyed_closed_hands"
    pause 0.12
    repeat

layeredimage cautionne block:
    zoom 0.5
    always "cautionne_block_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_block_speaking", "cautionne_block_closed")
image cautionne_block_speaking:
    "cautionne_block_open"
    pause 0.12
    "cautionne_block_closed"
    pause 0.12
    repeat

image cautionne dead = "cautionne_dead.png"

layeredimage cautionne gun:
    zoom 0.5
    always "cautionne_gun_ECU_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_gun_speaking", "cautionne_gun_ECU_closed")
image cautionne_gun_speaking:
    "cautionne_gun_ECU_open"
    pause 0.12
    "cautionne_gun_ECU_closed"
    pause 0.12
    repeat

layeredimage cautionne laugh:
    zoom 0.5
    always "cautionne_laugh_1"
    group mouth:
        attribute idle default "cautionne_laugh_1"
        attribute animate "cautionne_laughing"
image cautionne_laughing:
    "cautionne_laugh_2"
    pause 0.12
    "cautionne_laugh_1"
    pause 0.12
    repeat

layeredimage cautionne lean:
    zoom 0.5
    always "cautionne_lean_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_lean_speaking", "cautionne_lean_closed")
image cautionne_lean_speaking:
    "cautionne_lean_open"
    pause 0.12
    "cautionne_lean_closed"
    pause 0.12
    repeat

layeredimage cautionne oops:
    zoom 0.5
    always "cautionne_oopsie"

layeredimage cautionne pencil:
    zoom 0.5
    always "cautionne_pencil_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_pencil_speaking", "cautionne_pencil_closed")
image cautionne_pencil_speaking:
    "cautionne_pencil_open"
    pause 0.12
    "cautionne_pencil_closed"
    pause 0.12
    repeat

layeredimage cautionne serious:
    zoom 0.5
    always "cautionne_serious_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_serious_speaking", "cautionne_serious_closed")
image cautionne_serious_speaking:
    "cautionne_serious_open"
    pause 0.12
    "cautionne_serious_closed"
    pause 0.12
    repeat

layeredimage cautionne shoot:
    zoom 0.5
    always "cautionne_shoot_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_shoot_speaking", "cautionne_shoot_closed")
image cautionne_shoot_speaking:
    "cautionne_shoot_open"
    pause 0.12
    "cautionne_shoot_closed"
    pause 0.12
    repeat

layeredimage cautionne shot:
    zoom 0.5
    always "cautionne_shot"

layeredimage cautionne stunned:
    zoom 0.5
    always "cautionne_shoot_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_stunned_speaking", "cautionne_shoot_closed")
image cautionne_stunned_speaking:
    "cautionne_stunned_open"
    pause 0.12
    "cautionne_shoot_closed"
    pause 0.12
    repeat

layeredimage cautionne think:
    zoom 0.5
    always "cautionne_think_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_think_speaking", "cautionne_think_closed")
image cautionne_think_speaking:
    "cautionne_think_open"
    pause 0.12
    "cautionne_think_closed"
    pause 0.12
    repeat