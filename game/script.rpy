

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

default persistent.firstlaunch = False
default persistent.seen_splash = False

label splashscreen:

    scene black

    ## The first time the game is launched, players can set their accessibility settings.
    if not persistent.firstlaunch:

        ## This screen is at the top of extras.rpy

        call screen splash_settings

        ## This screen will not appear in subsequent launches of the game when
        ## the following variable becomes true.
        $ persistent.firstlaunch = True

    ## Here begins our splashscreen animation.
    show splash_anim_1
    show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
        xalign 0.5 yalign 0.8 alpha 0.0
        pause 6.0
        linear 1.0 alpha 1.0
    
    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:
        
        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(8.5, hard=True)
 
        $ persistent.seen_splash = True
    
    ## Players can skip the animation in subsequent launches of the game.
    else:
 
        if renpy.pause(8.5):
 
            jump skip_splash

    scene black
    with fade
 
    label skip_splash:
 
        pass
 
    return

## The game starts here.

label start:
    scene bedroom
    show cautionne annoyed
    with fade
    c "I am Cautionne, and this is some test dialogue. Can you see my mouth moving?"
    c nohands "I put my hands down. They're gone now. Amazing. Time for a new pose..."

    # This unlocks the the achievement with the corresponding name
    $ achievement.grant("Beginning")

    # This adds an integer value to a point-based achievement.
    # To track how much of it has been earned, use a regular variable for now.
    # $ achievement.progress("Point_Collector", 10)
    # $ persistent.points =+ 10

    # These display lines of dialogue.

    c lean "You've created a new Ren'Py game."

    c "Once you add a story, pictures, and music, you can release it to the world!"

    c "Haha, sorry. Had to get that out of the way first."

    c "Thanks for downloading this All-In-One GUI Template! After you play through this script, be sure to open up the files and adjust the {color=#32CD32}options.rpy{/color}, {color=#32CD32}gui.rpy{/color}, and {color=#32CD32}screens.rpy{/color} to fit your own project's needs!"

    c "You can even make a copy of the entire {color=#32CD32}game{/color} folder and start your project from there."
    scene black
    $match3_start()

    c "So now, let's demonstrate some of the custom Accessibility Options."

    c "When you run this project for the first time, you should have been able to adjust the Audio and Image Caption options."

    c "I'll make some sounds now. If Audio Captions are on, you'll see a notification in the top-left corner describing the sound."

    c "Let's close this so the breeze doesn't mess up my hair..."

    c "Found it!"

    c "If you had your Audio Captions on, you should have seen something appear in the notification tab."

    c "Neat, right?"

    c "Now let's test Image Captions."

    show eileen at right with move

    ic "Eileen walks to the right of the room."

    c "Over here..."

    show eileen at left with move

    ic "Eileen walks to the left of the room."

    c "Now here..."

    show eileen at center with move

    ic "Eileen walks to the center of the room."

    c "And there we go!"

    c "If you had your Image Captions on, then you should have seen some extra narration describing my movements."

    c "This is done with the special {color=#32CD32}{i}ic{/i}{/color} speaker tag we defined in {color=#32CD32}{i}accessibility.rpy{/i}{/color}."

    c "Now, let's test the Screen Shake settings."

    $ shake()

    show eileen surprised with dissolve

    ic "The room shakes."

    e upset "If you had it on, did you notice how robust that Screen Shake was? That wasn't the classic {color=#32CD32}{i}hpunch{/i}{/color}."

    e"This time around, we added in a custom Shake function that is randomized each time, with varying levels of intensity you can choose from."

    c "You can turn the screen shaking effect off in Preferences, just in case the motion makes you or your players sick. One more time."

    $ shake()

    ic "The room shakes again."

    e happy "Now let's try NVL Mode."

    nar_nvl "NVL Mode is a different way of displaying text on the screen."

    e_nvl "Unlike ADV, past lines of dialogue are still displayed until it is cleared off."

    nar_nvl "Usually NVL will cover the entire screen, but you can adjust the size of the window to only cover a certain part if need be."

    nvl clear

    e_nvl "Not all games may need to use both ADV and NVL, but it's nice to have options as a developer."

    e_nvl "With that said, let's go somewhere else."

    nar_nvl "Eileen wonders where she should travel to."

    stop music fadeout 1.0

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

    menu (nvl=True):

        "Office":

            ## This empty label is solely for replay mode purposes.

            label office:

                pass

            c "To the office? Okay...?"

            $ achievement.grant("Office")

            $ play_music(business,fadein=2.0,fadeout=2.0)

            scene future_office
            show eileen angry at center:
                yoffset 250
            with fade

            c "Ugh, you know that saying about \"all work and no play,\" right?"

            "Eileen seems bothered by something."

        "Beach":

            label beach:

                pass

            c "The beach sounds fun!"

            $ achievement.grant("Beach")

            $ play_music(summer,fadein=2.0,fadeout=2.0)

            hide eileen with dissolve
            $ casual = False

            scene sort_of_beautiful_beach_day
            show eileen summer happy at center:
                yoffset 230
            with fade

            c "Hehe, I have a swimsuit now!"

            "Eileen seems pleased with herself."

    "Remember to check the History screen if you have not done so yet."

    ## This ends the replay mode segment. Doesn't affect normal gameplay.
    $ renpy.end_replay()

## End Credits
label credits:

    ## We hide the quickmenu for the last part of the game so they don't
    ## appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits(15.0)

    $ persistent.credits_seen = True

    scene black
    with fade
    
    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:
 
        pass

    ## Makes [result] work. This needs to be near the end of the game
    ## for it to work properly.
    $ percent()

    ## We display a screen that shows how much the player has seen and played of the game.
    show screen results
    
    centered "Fin"

    hide screen results

    if persistent.game_clear:

        pass

    ## Do you want to leave some author's notes or a hidden message for your dedicated fans?
    ## This will check if they've seen all that the game has to offer.
    else:

        if readtotal == 100:

            $ achievement.grant("Completionist")

            ## Due to the way that $ percent() works, we need to make this a text displayable
            ## or else it'll try to count it too.
            show text "{size=60}{color=#ffffff}You've unlocked a special message.\nAccess it through the Extras Menu.{/color}{/s}":
                xalign 0.5 yalign 0.5 alpha 0.0
                linear 1.0 alpha 1.0

            $ persistent.game_clear = True

            ## The game will show our text displayable so the player can read it
            ## And only continue when there is input
            pause

    ## We re-enable the quickscreen as the credits are over.
    $ quick_menu = True

    # This ends the game.
    return