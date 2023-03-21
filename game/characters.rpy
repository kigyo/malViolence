screen debugging():
    if config.developer:
        vbox:
            null
            #text testvar
            #text str(speaking)

default testvar = "0"

init python:
    config.overlay_screens.append("debugging")

default speaking = None
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

define x = Character(_("???"), color="#00e7ff", image="cautionne", callback=speaker("cautionne"), ctc="ctc")
define c = Character(_("Cautionne"), color="#00e7ff", image="cautionne", callback=speaker("cautionne"), ctc="ctc")
define dr = Character(_("Dr. Danger"), color="#ffffff", image="danger", callback=speaker("danger"), ctc="ctc")
define narrator = Character(color="#ffffff", callback=speaker("protagonist"), ctc="ctc")

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

layeredimage cautionne hairtwirl:
    zoom 0.5
    always "cautionne_hairtwirl"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_hairtwirl_speaking", "cautionne_hairtwirl_mouth_closed")
image cautionne_hairtwirl_speaking:
    "cautionne_hairtwirl_mouth_open"
    pause 0.12
    "cautionne_hairtwirl_mouth_closed"
    pause 0.12
    repeat
image cautionne_hairtwirl:
    "cautionne_hairtwirl_base_0001"
    pause 0.1
    "cautionne_hairtwirl_base_0002"
    pause 0.1
    "cautionne_hairtwirl_base_0003"
    pause 0.1
    "cautionne_hairtwirl_base_0004"
    pause 0.1
    repeat

layeredimage cautionne laugh:
    zoom 0.5
    always "cautionne_laugh_1"
    group mouth:
        attribute idle "cautionne_laugh_1"
        attribute animate default "cautionne_laughing"
image cautionne_laughing:
    "cautionne_laugh_2"
    pause 0.2
    "cautionne_laugh_1"
    pause 0.2
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
    group mouth:
        attribute angry default WhileSpeaking("cautionne", "cautionne_shoot_angry", "cautionne_shoot_angry_closed")
        attribute cry WhileSpeaking("cautionne", "cautionne_shoot_cry", "cautionne_shoot_cry_closed")
        attribute grin WhileSpeaking("cautionne", "cautionne_shoot_grin", "cautionne_shoot_grin_closed")
image cautionne_shoot_angry:
    "cautionne_shoot_angry_open"
    pause 0.12
    "cautionne_shoot_angry_closed"
    pause 0.12
    repeat
image cautionne_shoot_cry:
    "cautionne_shoot_cry_open"
    pause 0.12
    "cautionne_shoot_cry_closed"
    pause 0.12
    repeat
image cautionne_shoot_grin:
    "cautionne_shoot_grin_open"
    pause 0.12
    "cautionne_shoot_grin_closed"
    pause 0.12
    repeat

layeredimage cautionne shot:
    zoom 0.5
    always "cautionne_shot"

layeredimage cautionne sit_far:
    zoom 0.5
    always "cautionne_sit_faraway"

layeredimage cautionne stunned:
    zoom 0.5
    group mouth:
        attribute hope default WhileSpeaking("cautionne", "cautionne_sit_hope", "cautionne_sit_hope_closed")
        attribute stunned WhileSpeaking("cautionne", "cautionne_sit_stunned", "cautionne_sit_stunned_closed")
        attribute smug WhileSpeaking("cautionne", "cautionne_sit_smug", "cautionne_sit_smug_closed")
image cautionne_sit_hope:
    "cautionne_sit_hope_open"
    pause 0.12
    "cautionne_sit_hope_closed"
    pause 0.12
    repeat
image cautionne_sit_stunned:
    "cautionne_sit_stunned_open"
    pause 0.12
    "cautionne_sit_stunned_closed"
    pause 0.12
    repeat
image cautionne_sit_smug:
    "cautionne_sit_smug_open"
    pause 0.12
    "cautionne_sit_smug_closed"
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