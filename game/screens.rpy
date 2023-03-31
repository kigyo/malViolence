﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style slider:
    ysize gui.slider_size
    right_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    left_bar Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:

        background Transform(style.window.background, alpha=persistent.say_window_alpha)
        ### IMPORTANT: The Transform() is holding the window background, and the alpha variable ties to our say window alpha

        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text "> " + who.upper() id "who"

        text what id "what" outlines [(1.5, "#000000", 1, 1)]

    use quick_menu

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen subtitle(who, what):
    style_prefix "say"

    window:
        background Null()
        id "window"
        text what id "what" outlines [(7, "#fff", 0, 0),(5, "#000", 0, 0)] xalign 0.5 layout "subtitle" size 56 text_align 0.5 yalign 0.5

    #use quick_menu()

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

default persistent.say_window_alpha = 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False
    line_spacing gui.preference("dialogue_spacing", 2)

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu(yoff=0):

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox yoffset yoff:
            style_prefix "quick"
            spacing -32

            xpos 812
            ypos 723
            button at quick_hover:
                text _("HISTORY")
                action ShowMenu('history')
            button at quick_hover:
                text _("SAVE")
                action ShowMenu('save')
            button at quick_hover:
                text _("OPTIONS")
                action ShowMenu('preferences')
            button at quick_hover:
                text _("AUTO")
                action Preference("auto-forward", "toggle")
            button at quick_hover:
                text _("SKIP")
                action Skip() alternate Skip(fast=True, confirm=True)

transform quick_hover:
    on hover:
        ease 0.1 yoffset -3
    on idle:
        ease 0.1 yoffset 0
## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
#     config.overlay_screens.append("quick_menu")

## We'll set this to False by default so we can show and hide the quick_menu during
## choices and such

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    background "gui/button/quick_menu_idle.png"

style quick_text is button_text:
    properties gui.button_text_properties("quick_button")
    xpos 0.5 ypos 0.5 
    selected_color "#ffffff"
style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    on "show" action Stop("sound", fadeout=0.5)

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        ypos gui.navigation_ypos

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("START") action Start() at navigation_move

        else:

            ## We're using the Separated History Screen, so we'll comment this out
            # textbutton _("History") action ShowMenu("history")

            textbutton _("SAVE") action ShowMenu("save") at navigation_move

        textbutton _("LOAD") action ShowMenu("load") at navigation_move

        textbutton _("OPTIONS") action ShowMenu("preferences") at navigation_move

        textbutton _("ABOUT") action ShowMenu("about") at navigation_move

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("HELP") action ShowMenu("help") at navigation_move

        if main_menu:

            textbutton _("EXTRAS") action ShowMenu("achievement_menu") alt "Extras" at navigation_move

        if _in_replay:

            textbutton _("END REPLAY") action EndReplay(confirm=True) at navigation_move

        elif not main_menu:

            textbutton _("MAIN MENU") action MainMenu() at navigation_move

    textbutton _("RETURN") + "                             " action Return() xpos gui.navigation_xpos ypos 0.75 text_size 40 at navigation_move
        


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    size 45 xalign 0.0

transform navigation_move:
    on hover:
        ease 0.15 xoffset 5
    on idle:
        ease 0.15 xoffset 0


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    add gui.main_menu_background at bg(0.5)
    add AlphaMask(At("gui/scroller.png",scroll_skew), "gui/grid_opacity.png")
    
    add "gui/logo.png" xalign 0.5 yalign 0.15

    hbox pos (50,50) spacing 30:
        imagebutton idle "gui/Twitter.png" action OpenURL("https://twitter.com/madocactus") at quick_hover
        imagebutton idle "gui/Itch.png" action OpenURL("https://madocallie.itch.io/malviolence") at quick_hover

    vbox xalign 0.5 yalign 0.6 spacing 15:
        style_prefix "main_menu"
        textbutton _("START") action Start()
        textbutton _("LOAD") action ShowMenu("load")
        textbutton _("OPTIONS") action ShowMenu("preferences")
        textbutton _("ABOUT") action ShowMenu("about")
        if main_menu and persistent.extras_unlocked:
            textbutton _("EXTRAS") action ShowMenu("achievements") alt "Extras"
        if renpy.variant("pc"):
            textbutton _("QUIT") action Quit(confirm=not main_menu)

    add "gui/main_menu_accent.png" xalign 0.5 yalign 0.85

    text "[config.version]" xalign 0.99 yalign 0.99:
        style "main_menu_version"

transform scroll_skew:
    perspective True subpixel True
    matrixtransform RotateMatrix(30, 0, 0)* OffsetMatrix(-1500, -300, 400)#OffsetMatrix(-500, 0, 1000)
    block:
        linear 3 yoffset 250
        yoffset 0
        repeat

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style main_menu_button:
    xalign 0.5 xysize (242, 64)
    hover_background "gui/button/main_menu_hover.png"
    idle_background Null()
style main_menu_button_text:
    idle_color "#ffffff" hover_color gui.accent_color# bold True
    size 60 yalign 0.5


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 200
    top_padding 200

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 590
    yfill True

style game_menu_content_frame:
    left_margin 90
    right_margin 150
    top_margin 15

style game_menu_viewport:
    xsize 1050

style game_menu_vscrollbar:
    unscrollable gui.unscrollable xoffset 80

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 140
    ypos 90
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox spacing 30:
            add "gui/logo.png" at zoomed(0.4) xalign 0.5

            ## gui.about is usually set in options.rpy.
            text "This game was crafted with love within 31 days for NaNoRenO 2023, by:" size gui.label_text_size-10 font gui.text_font
            grid 2 6:
                xspacing 0 yspacing 10 xoffset 50
                hbox spacing 15:
                    label _("Director & CG Artist:")
                    text _("{a=https://madocallie.carrd.co/}Mado{/a}") 
                hbox spacing 15:
                    label _("Scenario:")
                    text _("{a=https://madocallie.carrd.co/}Mado{/a}, {a=https://ofthedevilgame.itch.io/}Brian Mulholland{/a}, {a=https://itch.io/profile/luoxyz}Z{/a}") 
                hbox spacing 15:
                    label _("Programmer:")
                    text _("{a=https://kigyodev.com/}KigyoDev{/a}") 
                hbox spacing 15:
                    label _("Puzzle Designer:")
                    text _("{a=https://omelette.itch.io/}speck{/a}") 
                hbox spacing 15:
                    label _("UI & Logo:")
                    text _("{a=https://spicaze.itch.io/}spicaze{/a}") 
                hbox spacing 15:
                    label _("Backgrounds:")
                    text _("{a=https://twitter.com/ReinaTensei}Reina{/a}") 
                hbox spacing 15:
                    label _("Cautionne VA:")
                    text _("{a=https://www.carrickinabnett.com/}Carrick Inabnett{/a}") 
                hbox spacing 15:
                    label _("Dr. Danger VA:")
                    text _("{a=https://vynvox.com/}Vyn Vox{/a}") 
                hbox spacing 15:
                    label _("Voice Direction:")
                    text _("{a=https://twitter.com/pheberryfab}Phebe Fabacher{/a}") 
                hbox spacing 15:
                    label _("Audio Mastering & SFX:")
                    text _("{a=https://twitter.com/DrayReedOFC}D.ray{/a}") 
                hbox spacing 15:
                    label _("Music:")
                    text _("{a=https://melo-dii.carrd.co/}Melo-dii{/a}, {a=https://twitter.com/doranthedoran}Doran{/a}") 
                hbox spacing 15:
                    label _("Trailer:")
                    text _("{a=https://twitter.com/HarborSealDev}Jennymhulla{/a}") 

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a}.") size 25 font gui.text_font


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
    color gui.idle_color

style about_text:
    size gui.label_text_size

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            vbox:
                xalign 0.4
                yalign 0.5
                hbox xalign 1.0:
                    style_prefix "page"
                    #label _("SAVE YOUR FILE") xalign 0.0

                    spacing gui.page_spacing

                    #textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    #textbutton _(">") action FilePageNext()

                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"


                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot, empty="gui/button/save_empty.png") xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%d/%m/%Y, %H:%M"), empty=""):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key ["save_delete"] action FileDelete(slot)

## Set these to false if you wish to remove the Auto or Quick file pages
define config.has_autosave = True
define config.has_quicksave = True

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    yoffset 12


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):

        vbox xoffset 30:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Custom Preferences here

                vbox:
                    style_prefix "check"
                    label _("Toggles")
                    #textbutton _("Image Descriptions") action ToggleVariable("persistent.image_captions") alt "Toggle Image Descriptions"
                    textbutton _("Audio Titles") action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions"
                    if renpy.variant("pc"):
                        ## Self-voicing does not work on smartphone devices, so this
                        ## option only shows if the user is playing on a PC.
                        textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing"
                    textbutton "Screenshake" action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screen Shake"

                vbox:
                    style_prefix "radio"
                    label _("Typeface")
                    textbutton _("{font=gui/font/TitilliumWeb-Regular.ttf}{size=32}TitilliumWeb{/size}{/font}") action [gui.SetPreference("font", "gui/font/TitilliumWeb-Regular.ttf"), gui.SetPreference("size", 39), SetVariable("persistent.typeface", "TitilliumWeb")] alt "Change font to TitilliumWeb"
                    textbutton _("{font=gui/font/Atkinson-Hyperlegible-Regular-102.ttf}{size=32}Hyperlegible{/size}{/font}") action [gui.SetPreference("font", "gui/font/Atkinson-Hyperlegible-Regular-102.ttf"), gui.SetPreference("size", 42), SetVariable("persistent.typeface", "Hyperlegible")] alt "Change font to HyperLegible"

                vbox:
                    style_prefix "radio"
                    label _("Font Size")
                    if persistent.typeface == "TitilliumWeb":
                        textbutton _("Large") action gui.SetPreference("size", 44) alt "Change to Large Size Text"
                        textbutton _("Regular") action gui.SetPreference("size", 39) alt "Change to Regular Size Text"
                    elif persistent.typeface == "Hyperlegible":
                        textbutton _("Large") action gui.SetPreference("size", 49) alt "Change to Large Size Text"
                        textbutton _("Regular") action gui.SetPreference("size", 42) alt "Change to Regular Size Text"

                vbox:
                    style_prefix "radio"
                    label _("Game Overs")
                    textbutton _("Infinite") action SetField(preferences, "hard_mode", True) alt "Hard mode: Failing puzzles always results in a game over" 
                    textbutton _("Once per Puzzle") action SetField(preferences, "hard_mode", False) alt "Easy mode: Have at most one game over per puzzle"

                #vbox:
                #    style_prefix "radio"
                #    label _("Text Color")
                #    textbutton _("White") action gui.SetPreference("color", "#ffffff") alt "Change text color to white" 
                #    textbutton _("Cream") action gui.SetPreference("color", "#FFFDD0") alt "Change text color to cream" 

                #vbox:
                #    style_prefix "radio"
                #    label _("Line Spacing")
                #    textbutton _("Taller") action gui.SetPreference("dialogue_spacing", 4) alt "Change the height of the space between lines of dialogue to be taller"
                #    textbutton _("Regular") action gui.SetPreference("dialogue_spacing", 2) alt "Change the height of the space between lines of dialogue to the regular height"


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (2 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                    label _("Textbox Opacity")

                    bar value FieldValue(persistent, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=.2) xmaximum 400 style "slider" alt "Textbox Opacity"


                vbox:

                    if config.has_music:
                        hbox xsize 400:
                            label _("Music Volume")
                            textbutton _("Mute All") action Preference("all mute", "toggle") xalign 1.0 yalign 1.0

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                                
            null height gui.pref_spacing


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 348

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 400

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 520


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

## Note: This is my custom version of the History screen that is not attached
## to the game menu, and will appear in place of the textbox when called up.
## Margins and Padding may need to be adjusted accordingly.

## TODO: If you are not basing your project off this template, please do the following:
## At "style vscrollbar", add the line below:
## unscrollable "hide"
## Copy over the styles for this history screen
## In "gui.rpy", change "gui.history_height" to "None"
## Use CTRL + F to find the terms as you need to.

screen history():

    tag menu

    predict False
    add "gui/history.png" align (0.5,0.5)
    add "gui/history_decor.png" align (0.65,0.15)
    frame:
        background Null()

        style_prefix "history"

        ## If you have a custom image you want to use for the screen, you can set it as
        ## a Frame below.
        # background Frame(["gui/frame.png"], gui.history_frame_borders, tile=True)

        ## Style this as needed in the style definitions
        label _("History")

        ## Using margin properties will allow the screen to automatically adjust should
        ## you choose to use a different resolution than 1080p, and will always be centered. 
        ## You can also resize the screen using "xmaximum", "ymaximum", or "maximum(x,y)"
        ## if desired, but you will need to use "align(x,y)" to manually position it.

        ## xmargin essentially combines the left_margin and right_margin properties
        ## and sets them to the same value
        xmargin 200

        ## ymargin essentially combines the top_margin and bottom_margin properties
        ## and sets them to the same value
        ymargin 50

        ## xpadding essentially combines the left_padding and right_padding properties
        ## and sets them to the same value
        xpadding 50

        ## ypadding essentially combines the top_padding and bottom_padding properties
        ## and sets them to the same value
        top_padding 150
        bottom_padding 100

        vpgrid:

            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:

                for h in _history_list:

                    window:

                        ## This lays things out properly if history_height is None.
                        has fixed:
                            yfit True

                        if h.who:

                            label "> " + h.who.upper():
                                style "history_name"
                                substitute False

                                ## Take the color of the who text from the Character, if
                                ## set.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            line_spacing 5
                            substitute False
                            outlines [(1.5, "#000000", 1, 1)]

                    ## This puts some space between entries so it's easier to read
                    null height 20

                if not _history_list:

                    text "The text log is empty." line_spacing 10
                    ## Adding line_spacing prevents the bottom of the text
                    ## from getting cut off. Adjust when replacing the
                    ## default fonts.

        textbutton "Return":
            style "history_return_button"
            action Return()
            alt _("Return") 

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "size", "i" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_vscrollbar:
    xoffset -120 ysize 575

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font gui.text_font

style history_label:
    xfill True top_margin -70

style history_label_text:
    xalign 0.5 size 60
    ## Note: When altering the size of the label, you may need to increase the
    ## ypadding of the Frame, or separate it again into top_padding and bottom_padding

style history_return_button:
    align(1.0,1.0)
    yoffset 50 xoffset 130


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    add "gui/quit.png" at bg(1)

    frame:
        background Null()

        vbox:
            xalign .5
            yalign .5
            spacing 45
            if message == "Are you sure you want to quit?":
                label _("QUIT GAME?") text_size 80 xalign 0.5

                text _("Any unsaved progress will be lost."):
                    style "confirm_prompt"
                    xalign 0.5 xsize 450 text_align 0.5
            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Yes").upper() action yes_action
                textbutton _("No").upper() action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    background "gui/button/quit_button.png"
    xsize 234

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    color gui.interface_text_color size 55 text_align 0.5 yalign 0.5
    hover_color gui.hover_color


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame at notify_appear:

        hbox yalign 0.5:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos ysize 80
    background Frame("gui/notify.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]" yalign 0.5

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0 xoffset -300
        easein .25 alpha 1.0 xoffset 0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos ysize 80

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

default nvl_heading = ""

screen nvl(dialogue, items=None):

    add "gui/nvl.png" align (0.5, 0.5)
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

    if nvl_heading:
        label ("> " + nvl_heading).upper() pos (372, 90)

    use quick_menu(-639)


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id outlines [(1.5, "#000000", 1, 1)]


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Null()
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

    

screen gameover(lbl):
    
    add gui.main_menu_background at bg(0.5)
    add AlphaMask(At("gui/scroller.png",scroll_skew), "gui/grid_opacity.png")

    add "black" alpha 0.7

    label _("GAME OVER") text_size 200 yalign 0.4 xalign 0.5 text_outlines [(3, "#000", 1, 1)]
    vbox xalign 0.65 ypos 0.55:
        textbutton _("> Restart Room") action Jump(lbl) text_size 65 at navigation_move
        textbutton _("> Main Menu") action Return() text_size 65 at navigation_move

init python:
    def game_over(room = 1):
        room_init(room)
        store.inspect = None
        renpy.scene()
        renpy.scene("screens")
        renpy.scene("puzzles")
        renpy.block_rollback()
        if room == "tutorial":
            renpy.call_screen("gameover", "tutorial_room")
        else:
            renpy.call_screen("gameover", "room_" + str(room))
        renpy.with_statement(eyeopen)

    def room_init(room = 1):
        if room == 1:
            store.room1 = {"investigated":[], "solved":[], "oil":0, "chair":0, "megaphone":0, "marble":0, "hacking":0, "decanting":0, "bomb":0}
        elif room == 2:
            store.room2 = {"solved":[], "investigated":[], "blueprints":0, "post-its":0, "limbs":0, "corkboard":0, "clippings":0, "panopticon":0, "recalibration":0, "evidence":0, "word":0, "notes":[]}
        elif room == 3:
            store.room3 = {"room":"down", "investigated":[], "solved":[], "pages":[], "read_pages":[], "diary":0, "mannequin":0, "scrapbook":0, "health_record":0, "locked_container":0, "confidence_workbook":0, "sewing_book":0, "quilt":0, "cooking":0, "scrapbook_new":0, "toys":0}
        else:
            store.tutorial = {"vent":0, "investigated":[], "lock": [0,0,0,0,0,0,0,0]}