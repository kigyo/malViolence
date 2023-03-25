screen debugging():
    if config.developer:
        vbox:
            #text "nesting level: " + str(renpy.context_nesting_level())
            #text "call stack depth: " + str(renpy.call_stack_depth())
            #hbox:
            #    text "return stack: "
            #    for i in renpy.get_return_stack():
            #        text str(i) + " "
            null
            text testvar xalign 0.5
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

define x = Character(_("???"), color="#00e7ff", image="cautionne", callback=speaker("cautionne"), ctc="ctc", ctc_position="nestled-close")
define c = Character(_("Cautionne"), voice_tag="cautionne", color="#00e7ff", screen="subtitle", what_color="#A3EC3D", image="cautionne", callback=speaker("cautionne"), ctc="ctc", ctc_position="nestled-close")
#no-subtitle cautionne
define cr = Character(_("Cautionne"), voice_tag="cautionne", color="#00e7ff", image="cautionne", callback=speaker("cautionne"), ctc="ctc", ctc_position="nestled-close")
define dr = Character(_("Dr. Danger"), voice_tag="danger", color="#ffffff", image="danger", callback=speaker("danger"), ctc="ctc", ctc_position="nestled-close")
define narrator = Character(color="#ffffff", callback=speaker("protagonist"), ctc="ctc", ctc_position="nestled-close")
define n = Character(kind=nvl, callback=speaker("danger"), ctc="ctc", ctc_position="nestled-close")
define l = Character(kind=nvl, what_color="#00e7ff", callback=speaker("danger"), ctc="ctc", ctc_position="nestled-close")
define le = Character(kind=nvl, what_color="#00e7ff", what_prefix="{size=+2}{b}> ", what_suffix="{/b}{/size}", what_italic=True, callback=speaker("danger"), ctc="ctc", ctc_position="nestled-close")

image bg cautionne_screen = "cautionne_screen_background.png"

layeredimage cautionne annoyed:
    zoom 0.5
    always "bg cautionne"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_annoyed_speaking", "cautionne_closeup_face_close")
        attribute silent "cautionne_closeup_face_close"
    group hands:
        attribute hands default WhileSpeaking("cautionne", "cautionne_annoyed_hands_speaking", "cautionne_closeup_hands_close")
        attribute nohands Null()
image cautionne_annoyed_speaking:
    "cautionne_closeup_face_open"
    pause 0.12
    "cautionne_closeup_face_close"
    pause 0.12
    repeat
image cautionne_annoyed_hands_speaking:
    "cautionne_closeup_hands_open"
    pause 0.12
    "cautionne_closeup_hands_close"
    pause 0.12
    repeat

layeredimage cautionne block:
    zoom 0.5
    always "bg cautionne"
    always "cautionne_blocks_closed"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_blocks_speaking", "cautionne_blocks_closed")
image cautionne_blocks_speaking:
    "cautionne_blocks_open"
    pause 0.12
    "cautionne_blocks_closed"
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
    always "bg cautionne"
    always "cautionne_hairtwirl"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_hairtwirl_speaking", "cautionne_hairtwirl_lipflap_close")
image cautionne_hairtwirl_speaking:
    "cautionne_hairtwirl_lipflap_open"
    pause 0.12
    "cautionne_hairtwirl_lipflap_close"
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
    always "bg cautionne"
    group mouth:
        attribute idle "cautionne_laugh_0002"
        attribute animate default "cautionne_laughing"
image cautionne_laughing:
    "cautionne_laugh_0003"
    pause 0.12
    "cautionne_laugh_0002"
    pause 0.12
    repeat

layeredimage cautionne lean:
    zoom 0.5
    always "bg cautionne"
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
    always "bg cautionne"
    always "cautionne_oopsie"

layeredimage cautionne pencil:
    zoom 0.5
    always "bg cautionne"
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
    always "bg cautionne"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_serious_speaking", "cautionne_serious_close")
image cautionne_serious_speaking:
    "cautionne_serious_open"
    pause 0.12
    "cautionne_serious_close"
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
    always "bg cautionne"
    always "cautionne_think_close"
    group mouth:
        attribute speaking default WhileSpeaking("cautionne", "cautionne_think_speaking", "cautionne_think_close")
image cautionne_think_speaking:
    "cautionne_think_open"
    pause 0.12
    "cautionne_think_close"
    pause 0.12
    repeat