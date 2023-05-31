## Splashscreen Settings##################################
##
## A custom screen that allows players to set their accessibility settings the first
## time they launch the game. Borrows elements from the Preferences screen in
## screens.rpy, and will need to be manually adjusted.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

screen splash_settings():

    modal True

    zorder 200

    style_prefix "confirm"

    frame at alphashow(0.5):

        xpadding 100
        ypadding 50
        xmargin 200

        vbox:

            yalign .5
            xalign 0.5
            spacing 50

            label _("Accessibility Settings") xalign 0.5
            label _("These options can be adjusted at any time in the menu.") xalign 0.5 text_color "#fff" text_font "gui/font/TitilliumWeb-Regular.ttf" text_size 35

            hbox xfill True:
                xalign 0.8
                #vbox:
                #    style_prefix "radio"
                #    label _("Typeface")
                #    textbutton _("{font=gui/font/TitilliumWeb-Regular.ttf}{size=32}TitilliumWeb{/size}{/font}") action [gui.SetPreference("font", "gui/font/TitilliumWeb-Regular.ttf"), gui.SetPreference("size", 39), SetVariable("persistent.typeface", "TitilliumWeb")] alt "Change font to TitilliumWeb"
                #    textbutton _("{font=gui/font/Atkinson-Hyperlegible-Regular-102.ttf}{size=32}Hyperlegible{/size}{/font}") action [gui.SetPreference("font", "gui/font/Atkinson-Hyperlegible-Regular-102.ttf"), gui.SetPreference("size", 42), SetVariable("persistent.typeface", "Hyperlegible")] alt "Change font to HyperLegible"

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
                    style_prefix "check"
                    label _("Toggles") 
                    #textbutton _("Image Descriptions") action ToggleVariable("persistent.image_captions") alt "Toggle Image Descriptions"
                    textbutton _("Audio Titles") action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions"
                    if renpy.variant("pc"):
                        ## Self-voicing does not work on smartphone devices, so this
                        ## option only shows if the user is playing on a PC.
                        textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing"
                    textbutton "Screenshake" action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screen Shake"
                    textbutton "Graphic Icons" action ToggleField(persistent,"skullicon",true_value=True,false_value=False) alt "Toggle Screen Shake"

                vbox:
                    style_prefix "radio"
                    label _("Puzzle Difficulty")
                    textbutton _("Easy") action SetField(persistent, "difficulty", 1)
                    textbutton _("Medium") action SetField(persistent, "difficulty", 2)
                    textbutton _("Hard") action SetField(persistent, "difficulty", 3)

                vbox:
                    style_prefix "check"
                    label _("Puzzle Tools")
                    textbutton _("Skip Button"):
                        action ToggleField(preferences, "hard_mode", true_value=False, false_value=True) alt "Puzzle Skipper"
                        tooltip "{size=30}Adds a skip button to all puzzles.{/size}"
                    textbutton _("Failsafes"):
                        action ToggleField(preferences, "puzzle_resets") alt "Puzzle Failsafes"
                        tooltip "{size=30}Prevents game overs and adds \na reset button to most puzzles.{/size}"

            textbutton _("Confirm") action Return() xalign 0.5

    $ tooltip = GetTooltip()
    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame padding 15,5,15,5:
                xalign 0.3
                text tooltip
style presplash_label:
    top_margin gui.pref_spacing
    bottom_margin 3
    text_align 0.5

style presplash_label_text:
    yalign 1.0


## Extras screens ###########################################
##
## Screens that includes Image Galleries, Music Room, Replay Room, and Dev Notes.
## https://www.renpy.org/doc/html/rooms.html

## We let Ren'Py resize our images so we don't have to make buttons in another
## program.

## These background buttons are 384x216
#image room_button = im.FactorScale("bg/room.jpg", 0.2)
#image office_button = im.FactorScale("bg/future_office.jpg", 0.2)
#image beach_button = im.FactorScale("bg/sort_of_beautiful_beach_day.jpg", 0.2)
#image bglock_button = "gui/button/cg_locked.jpg"

init python:

    g_bg = Gallery()

    # Backgrounds for the BG Gallery
    #g_bg.button("room")
    #g_bg.unlock_image("room") 

    #g_bg.button("office")
    #g_bg.image("future_office")
    #g_bg.unlock("future_office")

    #g_bg.button("beach")
    #g_bg.image("sort_of_beautiful_beach_day")
    #g_bg.unlock("sort_of_beautiful_beach_day")

    # Sprites for the Sprite Gallery
    # We put a background in the first spot so Eileen isn't floating in a void.

    #g_sprite = Gallery()

    #g_sprite.button("eileen happy")
    #g_sprite.unlock_image("room", "eileen happy")

    #g_sprite.button("eileen neutral")
    #g_sprite.unlock_image("room", "eileen neutral")

    #g_sprite.button("eileen surprised")
    #g_sprite.unlock_image("room", "eileen surprised")

    #g_sprite.button("eileen upset")
    #g_sprite.image("room", "eileen upset")
    #g_sprite.unlock("room", "eileen upset")

    #g_sprite.button("eileen angry")
    #g_sprite.image("room", "eileen angry")
    #g_sprite.unlock("room", "eileen angry")

    ## The button used for locked images
    #g_bg.locked_button = "bglock_button"
    #g_sprite.locked_button = "spritelock_button"

    ## The transition used when switching images.
    #g_bg.transition = dissolve
    #g_sprite.transition = dissolve

    ## MusicRoom instance.
    #mr = MusicRoom(fadeout=1.0)

    ## Add music files.
    #mr.add("audio/music/Careless-Summer_Looping.mp3", always_unlocked=True)
    #mr.add("audio/music/Future-Business_v001.mp3")
    #mr.add("audio/music/Sculpture-Garden_Looping.mp3")
    #mr.add("audio/music/The-Concrete-Bakes_Looping.mp3")

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.
default persistent.game_clear = False

screen extras_navigation():

    key "game_menu" action ShowMenu("about")

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        ypos gui.navigation_ypos

        spacing gui.navigation_spacing

        textbutton _("ACHIEVEMENTS") action ShowMenu("achievement_menu") alt "Achievements" at navigation_move
        textbutton _("FAILURES") action ShowMenu("failchievement_menu") alt "Failures" at navigation_move

        #textbutton _("SPRITE GALLERY") action ShowMenu("sprite_gallery") alt "Sprite Gallery"

        #textbutton _("CG GALLERY") action ShowMenu("bg_gallery") alt "Background Gallery" at navigation_move

        #textbutton _("MUSIC ROOM") action ShowMenu("music_gallery") alt "Music Room" at navigation_move

        #textbutton _("REPLAY ROOM") action ShowMenu("replay_gallery") alt "Replay Room" at navigation_move

        if persistent.game_clear or config.developer:

            textbutton _("DEVELOPER NOTES") action ShowMenu("dev_notes") alt "Developer Notes" at navigation_move

        else:

            textbutton _("???") action None alt "Locked Option" at navigation_move

    textbutton _("RETURN") + "                             " action ShowMenu("about") alt "Return" xpos gui.navigation_xpos ypos 0.75 text_size 40 at navigation_move

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

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

    label title

    use extras_navigation

## Sprite Gallery screen ######################################
##
## This is a simple screen that shows buttons that display a sprite imposed on a
## background.

screen sprite_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu(_("Sprite Gallery")):

        grid 5 1:

            xfill True
            yfill True

            ## Call make_button to show a particular button.
            # add g_sprite.make_button("sprite", "sprite_button")

            add g_sprite.make_button("eileen happy", "ehappy_button")
            add g_sprite.make_button("eileen neutral", "eneutral_button")
            add g_sprite.make_button("eileen surprised", "esurprised_button")
            add g_sprite.make_button("eileen upset", "eupset_button")
            add g_sprite.make_button("eileen angry", "eangry_button")

## Background Gallery screen ############################################################
##
## This is a simple screen that shows buttons that display a background.
## You can easily adapt this screen to make a CG or concept art screen.

screen bg_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu(_("CG Gallery")):

        grid 2 2:

            xfill True
            yfill True

            ## Call make_button to show a particular button.
            # add g_bg.make_button("background", "bg_button")

            #add g_bg.make_button("room", "room_button", xalign=0.5, yalign=0.5)
            #add g_bg.make_button("office", "office_button", xalign=0.5, yalign=0.5)
            #add g_bg.make_button("beach", "beach_button", xalign=0.5, yalign=0.5)

## Music Gallery screen ############################################################
##
## This is a simple screen that shows buttons that play a music track.

screen music_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu(_("Music Room")):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.
            #textbutton "The Concrete Brakes" action mr.Play("audio/music/The-Concrete-Bakes_Looping.mp3")
            #textbutton "Sculpture Garden" action mr.Play("audio/music/Sculpture-Garden_Looping.mp3")
            #textbutton "Future Business" action mr.Play("audio/music/Future-Business_v001.mp3")
            #textbutton "Careless Summer" action mr.Play("audio/music/Careless-Summer_Looping.mp3")

            null height 20

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous() alt "Previous Song"
                textbutton "Next" action mr.Next() alt "Next Song"

            null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        ## Restore the main menu music upon leaving.
        ## You can actually comment this out if you want to let players enjoy the music
        ## while looking at the other screens.
        #on "replaced" action Play("music", "audio/The-Concrete-Bakes_Looping.mp3")


## Dev Notes screen ########################################
##
## This screen contains a message for players after they beat the entire game.
## We borrowed the base of this screen from the About screen.

screen dev_notes():

    tag menu

    ## This use statement includes the extras_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the extras_menu
    ## screen.
    use extras_menu(_("Developer's Notes"), scroll="viewport"):

        vbox spacing 10:
            style_prefix "developer_notes"
            frame:
                has vbox
                text _("There’s so much I want to say about making this project - but ah… all I can muster right now is “Thank you for letting me direct!” and “I really want to eat a cheesy corn dog now…”\n\n“malViolence” is my first work as a director of a visual novel, rather than a solo dev. I was worried about taking on such an important role, and I didn’t know how my vision would be executed when working in a team… but I’m really happy that I ended up working with such talented, kind teammates for this NaNoRenO 2023. Their kindness and incredible work has brought me a lot of confidence. Because of them I’ve found a new love for directing things…\n\nI hope you enjoyed Cautionne’s and Dr. Danger’s story! Let me know what you think in the Itch.io comments or on Twitter - I’d love to see your feelings on my lovely little family of villains… and on the game as a whole.\nBut for now, ciao!")
                add "gui/developer notes/mado.png" xalign 0.5
                label "— " + _("{a=https://madocallie.carrd.co/}Mado{/a}") + " (" + _("Director, CG Artist & Writing") + ")"
            frame:
                has vbox
                text _("Mado's strong vision and the whole team's dedication is what made this project come together. I hope you enjoyed playing as much as we enjoyed working on it. It was a pleasure contributing to the script and story where I could. Thank you for playing!")
                label "— " + _("{a=https://ofthedevilgame.itch.io/}Brian Mulholland{/a}") + " (" + _("Writing") + ")"
            frame:
                has vbox
                text _("Thank you for playing! Thanks to everyone on the team for making everything possible! Learned a lot and had fun!")
                label "— " + _("{a=https://itch.io/profile/luoxyz}Z{/a}") + " (" + _("Writing") + ")"
            frame:
                has vbox
                text _("So grateful to work with such a talented team under such a strong director this Nano! I hope you enjoyed playing the game as much as I enjoyed working on it and I hope the puzzles give you a little trouble, but not too much trouble~")
                label "— " + _("{a=https://omelette.itch.io/}speck{/a}") + " (" + _("Puzzle Designer") + ")"
            frame:
                has vbox
                text _("Putting everyone's work together was a lot of fun, and I'm so happy with how it turned out! Huge thanks to Mado and speck for their coding contributions; they're responsible for the astonishing level of polish, and the cooler puzzles, respectively. \n\nI learned so much this past month, and can't wait to put it to good use in my own games. Also, please view my new son:")
                hbox xfill True:
                    add "gui/developer notes/kigyodev.png"
                    label "— " + _("{a=https://kigyodev.com/}KigyoDev{/a}") + " (" + _("Programmer") + ")"
            frame:
                has vbox
                text _("Thank you for the chance to work in malViolence! It's my first gamejam in a while and I'm really excited to see everything come together!")
                label "— " + _("{a=https://spicaze.itch.io/}spicaze{/a}") + " (" + _("UI & Logo") + ")"
            frame:
                has vbox
                text _("Thank you for playing.")
                label "— " + _("{a=https://twitter.com/ReinaTensei}Reina{/a}") + " (" + _("Backgrounds") + ")"
            frame:
                has vbox
                text _("What an honor it's been to provide the voice of this unhinged yet tragic little scrunkly. Getting to work on a project like this has been an absolute honor, and I couldn't be more thankful to the team for giving me the chance. Who knows what adventures await our little pint sized mad scientist? Whatever that may be for you, don't forget to get out there and approach life just like a real super villain. With PRESENTATION!!!")
                label "— " + _("{a=https://www.carrickinabnett.com/}Carrick Inabnett{/a}") + " (" + _("Cautionne VA") + ")"
            frame:
                has vbox
                text _("What can I say except, 'WOW??? OMG WOW???' I had such an amazing time participating, and I hope everyone enjoys!")
                label "— " + _("{a=https://vynvox.com/}Vyn Vox{/a}") + " (" + _("Dr. Danger VA") + ")"
            frame:
                has vbox
                text _("My team and I at Very Berry Studios are extremely thankful for the opportunity to cast and find the voice actors for Malviolence! I am super happy with the final result and I think the casting is perfect, and Mado chose the perfect actors to represent Cautionne and Dr. Danger. Malviolence is a very unique project when it comes to both the art and the process of playing the game, so I hope everyone who played enjoys it to its full potential, everyone on the team worked super hard!")
                label "— " + _("{a=https://twitter.com/pheberryfab}Phebe Fabacher{/a}") + " (" + _("Voice Direction") + ")"
            frame:
                has vbox
                text _("It was honor to work on this project. Thanks to the voice actors and musician's for letting me present their contributions in the best light. I wanted to achieve the best sounding game audio I could and I hope that comes through. May my sound design startle your earholes as well.\nMalviolence turned out to be a great and unique game. I almost didn't join the project but am glad that I did.  Thanks to everyone on team Malviolence. And thanks to anyone who plays.")
                label "— " + _("{a=https://twitter.com/DrayReedOFC}D.ray{/a}") + " (" + _("Audio Mastering & SFX") + ")"
            frame:
                has vbox
                text _("I consider myself lucky to be part of such a unique team and game as my first experience with game development. malViolence is the first project I ever worked on as a music composer and it was a really exciting experience. Everyone on this team worked very hard to make this an amazing game, and I'm very happy to able to say this was the first team I was part of. It was wonderful to get to see behind the curtains of the development of a visual novel for the very first time. I hope my contribuition has touched you in some way and has made this project even more amazing!")
                label "— " + _("{a=https://twitter.com/doranthedoran}Doran{/a}") + " (" + _("Music") + ")"
            frame:
                has vbox
                text _("I'm more than thankful for mado inviting me on board to compose music for malViolence! As this was my first time composing VGM, I learned quite a lot composing music for malviolence (and games in general), especially in managing the time to make sure stuff gets done as well making sure the music is loopable! I hope you enjoyed what I had brought to this lovely vn! (Between you and me, my favorite track is the jail cell theme d(owx;;) ) \n\nI also cannot get over the coincidence that Cautionne happens to have an X eye like me.")
                add "gui/developer notes/melo-dii.png" fit "contain"
                label "— " + _("{a=https://melo-dii.carrd.co/}Melo-dii{/a}") + " (" + _("Music") + ")"
            frame:
                has vbox
                text _("It's been a blast to work with talented and caring people during the production of this project.")
                label "— " + _("{a=https://twitter.com/HarborSealDev}Jennymhulla{/a}") + " (" + _("Trailer") + ")"
            frame:
                has vbox
                text _("This is the best game ever made I know bc I am a gamer")
                label "— " + _("cluniies") + " (" + _("QA Testing") + ")"
            frame:
                has vbox
                text _("I was here for one day and in that time I gained a crippling fear of panopticons and a crippling attraction to Cautionne. No regrets.")
                label "— " + _("wBrian") + " (" + _("QA Testing") + ")"
            
style developer_notes_frame is gui_frame:
    padding (40,40) xfill True

style developer_notes_vbox:
    xfill True

style developer_notes_text is puzzle_description_text:
    color "#fff"

style developer_notes_label:
    xalign 1.0 yalign 1.0

## Type your special message here.
define gui.dev_notes = _p("""Hello, this is BáiYù of tofurocks here. I want to thank
    you for downloading this All-In-One GUI template to use in your own game, though it's been a while since I last updated this, hasn't it? Thank you all for your patience as I stamped out as many bugs as I could.
    \n
    While the code provided here is almost a straight copy from the official documentation for the most part, I purposely kept it very bare-bones so that you can customize the GUI yourself. I hope that by sharing this with others, the overall quality of all Ren'Py games will improve.
    \n
    Thank you for taking the time to read this, and I wish you the best on your
    development adventures to come.""")

## End Credits Scroll ############################################################
## A new optimized screen for showing rolling credits. This is similar to the
## gui.about string in options.rpy, and you can style it using text tags.
## https://www.renpy.org/doc/html/text.html

define credits_string = _p("""
\n\n
\n\n
\n\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Director:{/color}{/font}{/size}\n
Mado
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Writing:{/color}{/font}{/size}\n
Mado\n
Brian Mulholland\n
Z
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Puzzles & Programming:{/color}{/font}{/size}\n
speck\n
KigyoDev
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Art & UI:{/color}{/font}{/size}\n
Mado\n
Reina\n
spicaze
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Music:{/color}{/font}{/size}\n
Melo-dii\n
Doran
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Voiceover:{/color}{/font}{/size}\n
Cautionne: Carrick Inabnett\n
Dr. Danger: Vyn Vox
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Sound & Voice Direction:{/color}{/font}{/size}\n
D.ray\n
Phebe Fabacher
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Trailer:{/color}{/font}{/size}\n
Mado
Jennymhulla
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Quality Assurance:{/color}{/font}{/size}\n
cluniies\n
wBrian\n
Whatever Productions
\n\n
{size=+15}{font=gui/font/kenyan coffee rg.otf}{color=#00e7ff}Special Thanks:{/color}{/font}{/size}\n
dmochas\n
tofurocks\n
wattson\n
glsuoa\n
npckc
\n\n\n\n\n\n

""")

## This controls the position and speed of your end credits.
transform credits_scroll(t):
    xcenter 0.5 yanchor 0.0 ypos 1.0 subpixel True
    linear t yanchor 1.0 ypos 0.0

## The actual end credits screen that we call.
screen credits(t):
    
    style_prefix "credits"

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    add gui.main_menu_background at bg(0.5)
    add AlphaMask(At("gui/scroller.png",scroll_skew), "gui/grid_opacity.png")

    default title_shown = False

    timer 5 action SetScreenVariable("title_shown", True)

    showif title_shown == False:
        add "gui/logo.png" xalign 0.5 yalign 0.5 at alphashow(0.5)
    else:
        timer t-5 action [Return(), With(Dissolve(2))]
        text credits_string text_align 0.5 at credits_scroll(t)
        
    if persistent.credits_seen:

        textbutton _("Skip Credits") action Return() xalign 1.0 yalign 1.0 xoffset -20 yoffset -20 style "confirm_button"

    ## To use in script:
    ### call screen credits(t)
    ## Where t is the number of seconds it takes to scroll

style credits_text:
    size 50 outlines [(1.5, "#000000", 1, 1)]
    color "#ffffff"


## Results Screen ############################################################
## A screen that displays how much of the game the player has seen.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=39859
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.count_dialogue_blocks

# This creates a percentage based on how much of the game the player has seen. 
init python:

    numblocks = renpy.count_dialogue_blocks()

    def percent():

        global readtotal
        readtotal = renpy.count_seen_dialogue_blocks()* 100 / numblocks
        persistent.readtotal = readtotal
        ## This is displayed in our Achievements screen.

default readtotal = 0

screen results():
    
    zorder 200

    vbox:
        xalign .5
        yalign .2
        spacing 45

        text _("Script Seen: [readtotal]%") color "#fff"

## TODO: Figure out how to get total game time working properly
## https://lemmasoft.renai.us/forums/viewtopic.php?t=40407
## Official Documentation of function: https://www.renpy.org/doc/html/other.html#renpy.get_game_runtime

# default playtime = 0

# init 2 python:

#     def total_playtime(d):
#         renpy.store.playtime += renpy.get_game_runtime()
#         #renpy.clear_game_runtime()
#         d["playtime"] = renpy.store.playtime

    # config.save_json_callbacks = [total_playtime]