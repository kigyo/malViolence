label neutral_ending:
    #"{b}[pause – walking sounds play as the exit BG appears]{/b}"
    show bg corridor_exit:
        align (0.5,0.5) zoom 0.5
        ease 4 zoom 1.0 align(0.5,0.6)

    pause 4

    $ play_sound(dooropen)
    scene black with fade

    pause 2

    $ play_sound(doorclose)


    show bg garage with placeintro:
        zoom 0.8 xalign 0.0 yalign 0.5
        linear 30 xalign 1.0

    pause 1
    "(There's the exit,{w=0.1} right up ahead.)"
    #"{b}[pan across {/b}{b}bg{/b}{b} to show {/b}{b}all of{/b}{b} the items there]{/b}"
    "(It's in the middle of a big,{w=0.1} garage-like space;{w=0.5} one filled with boxes of all shapes and sizes.{w} Maybe it's for storing tools or materials.)"
    "(You don't really want to find out.{w} Like the hallway before it,{w=0.1} this room's completely unremarkable.)"

    "(And besides,{w=0.1} you've had enough of exploring.)"
    #"{b}[pause]{/b}"
    pause 1
    show bg garage with dissolve:
        zoom 0.5 align(0.5,0.5)
    "(...All that said,{w=0.1} you weren't expecting your escape to be so...{w=0.5} {i}straightforward.{/i})"
    "(The exit's wide open.{w} If you walked through right now,{w=0.1} you'll—){w=1}{nw}"

    $ play_sound(quickfootsteps)
    #"{b}[quick footsteps sound out]{/b}"
    pause 1
    "(Crap.{w} You jinxed yourself.)"
    "H-hello?{w} Who's there?"
    voice "audio/voice/cautionne/Endings/Neutral Endings/NE 1/Cautionne_NeutralEnding1-01.ogg"
    xc "So,{w=0.142} you {i}finally {/i}made it.{w=0.5} Did you like my games, lab rat?"

    scene bg garage:
        zoom 0.5 align (0.5,0.5)
        ease 4 zoom 1.0 yalign 0.6

    pause 3

    scene cautionne gun far silent with fade

    $ play_music(endingintro, loop=False)
    $ queue_music(neutralending)

    pause 2

    pause 1
    #"{b}[show {/b}{b}Cautionne{/b}{b} shooting CG]{/b}"
    "(A...{w=0.5} a {i}gun?{/i})"
    scene cautionne gun cu with dissolve
    "(Why does he have a gun?{w} Someone his age shouldn't—){w=1}{nw}"
    "(No,{w=0.1} it's a fake,{w=0.1} isn't it?{w} Of course —{w=0.5} it's just a practical joke of his!)"
    pause 1
    "Um...{w=0.5} I'm glad you're having fun and all,{w=0.1} but I really should get going."
    "See,{w=0.1} adults have these things called “jobs”,{w=0.1} and—{w=1}{nw}"
    $ play_sound(gunblast1)
    $ queue_sound(bulletimpact)
    scene black
    stop music
    pause 3
    #"{b}[Pause – sound of {/b}{b}Cautionne{/b}{b} firing a bullet into your kneecap. Screen turns black for a pause. ]{/b}"

    scene cautionne gun far silent with fade
    "(Oh.{w} It just hit your knee.)"
    pause 0.5
    "(Aah?)"
    pause 0.5
    "{si}(Aaaaaaah?!){/si}"
    pause 0.5
    "{sc}(AaaaaAAAAaaAaAAAAaaAAAAH?!?!?!?){/sc}"

    $ play_sound(bodyfall)

    scene cautionne gun far silent with small_shake:
        zoom 1 xalign 0.5 yalign 0.5
        linear 0.05 yalign 1.0 xalign 0.5 zoom 3

    scene black

    #"{b}[the player collapses on the floor]{/b}"

    pause 3
    "{si}(Shit.{w} Shit,{w=0.1} shit,{w=0.1} shit.){/si}"
    "{si}(You can't believe —{w} you made such a {i}rookie {/i}mistake!){/si}"
    "{si}(And you can't...{w} Haa...{w} you can't...{w} {i}stand{/i} any more!){/si}"
    "{si}(Wha...{w} what are you gonna do?){/si}"
    "{si}(How are you gonna get out of here {i}now?{/i}){/si}"

    $ play_sound(footsteps4)
    #"{b}[footsteps sounds as{/b}{b} Cautionn{/b}{b}e walks over.]{/b}"
    pause 3
    voice "audio/voice/cautionne/soundbites/Normal/Cautionne_SBN-Shut Up 1.ogg"
    cr "Patronize me at your own risk."
    cr "...Is what I should've said before firing,{w=0.1} but I'm still new to this."
    cr "Kind of like you and your job,{w=0.1} {i}lab rat.{/i}"
    voice "audio/voice/cautionne/soundbites/Normal/Cautionne_SBN-Hmph!.ogg"
    $ play_music(neutralending, fadein=1.0, fadeout=1.0)
    cr "It's why you don't scare me.{w=0.5} You're just a {i}low-level nobody{/i} living a hand-to-mouth life."
    cr "That's why you did this mission,{w=0.1} right?{w=0.5} 'Cause you wanted a sweet,{w=0.1} fat,{w=0.1} paycheck?"
    "{si}(...You...{w} you want...{w} to say something...){/si}"
    "{si}(But,{w=0.1} haah...{w} you're shaking...{w} and sweating...{w} everywhere...){/si}"
    "{si}(All you can do...{w} is open your eyes...){/si}"

    scene cautionne shoot with eyeopen:
        align(0.0,1.0) subpixel True
        easein 45 align(0.0,0.0)

    pause 3
    #"{b}[Show the bottom of his shooting CG]{/b}"
    cr "Struggling just to open your mouth?{w=0.5} That'd earn you plenty of pity points...{w=0.5} if you weren't so gross about it."
    cr "You've never experienced this much pain before,{w=0.1} have you?"
    if most_explored == 1:

        cr "In fact,{w=0.1} it seems like you haven't experienced much of {i}anything.{/i}"
        pause 0.5
        cr "If I let you go,{w=0.1} would your bosses even care?"
        cr "After all,{w=0.1} you're not much of an investigator."
        cr "So, how 'bout I save you all the exit interviews and put things to an end here."
        "{si}(N-no...{w} you can still get up!){/si}"
        "{si}(If you...{w} crawl all the way back...{w} they'll...{w} definitely forgive you...){/si}"
        #"{b}[pan up to his face]{/b}"
        scene cautionne shoot grin with dissolve:
            align(0.0,0.0)
        pause 1
        voice "audio/voice/cautionne/Endings/Neutral Endings/NE 1/Cautionne_NeutralEnding1-02.ogg"
        cr "Hm...{w=0.514} I'll admit,{w=0.16} I'm curious."
        voice "audio/voice/cautionne/Endings/Neutral Endings/NE 1/Cautionne_NeutralEnding1-03.ogg"
        cr "When you're gone,{w=0.107} will STOP eulogize you?{w=0.27} Or will they just write you off as another wasted asset?"
        voice "audio/voice/cautionne/Endings/Neutral Endings/NE 1/Cautionne_NeutralEnding1-04.ogg"
        cr "...Hee hee.{w=0.025} I'm undecided."
        #"{b}[the trigger clicks]{/b}"
        scene cautionne shoot grinsilent:
            align(0.0,0.0)
        pause 0.1
        scene cautionne shoot grinsilent with dissolve:
            zoom 2 align(0.0,0.07)
        pause 0.1
        scene cautionne shoot grin:
            zoom 2 align(0.0,0.07)
        voice "audio/voice/cautionne/Endings/Neutral Endings/NE 1/Cautionne_NeutralEnding1-05.ogg"
        cr "But I wouldn't be much of a scientist if I didn't test my hypotheses."

    elif most_explored == 2:
        label neutral2:
            cr "But as much as I sympathize...{w=0.5} I just can't let you go."
            cr "You got your muddy paws on some {i}confidential {/i}information.{w=0.5} Stuff {i}way{/i} above your paygrade."
            cr "So,{w=0.1} I'm afraid I'll have to end things here."
            #"{b}[pan up to his face]{/b}"
            scene cautionne shoot grinsilent with dissolve:
                align(0.0,0.0)
            pause 2
            scene cautionne shoot grin:
                align(0.0,0.0)
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 2/Cautionne_NeutralEnding2-01.ogg"
            cr "No hard feelings.{w=0.111} I know you were just doing your job."
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 2/Cautionne_NeutralEnding2-02.ogg"
            cr "But see,{w=0.272} there's a little {i}conflict of interest{/i} between you and me."
            scene cautionne shoot angry:
                align(0.0,0.0)
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 2/Cautionne_NeutralEnding2-03.ogg"
            cr "Besides,{w=0.14} I've got to finish what Dr. Danger started.{w=0.5} That's {i}my {/i}{i}job{/i},{w=0.1} now that she's gone."
            #"{b}[the trigger clicks]{/b}"
            scene cautionne shoot angrysilent:
                align(0.0,0.0)
            pause 0.1
            scene cautionne shoot grinsilent with dissolve:
                zoom 2 align(0.0,0.07)
            pause 0.1
            scene cautionne shoot grin:
                zoom 2 align(0.0,0.07)
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 2/Cautionne_NeutralEnding2-04.ogg"
            cr "And by the time I'm finished,{w=0.339} they'll be {i}begging{/i} for her to come back."
            #"{b}[the gun fires]{/b}"

            #"{b}[NEUTRAL END – ROOM 2 VARIANT]{/b}"
            #"{b}[{/b}{b}Cautionne{/b}{b} laughing more menacingly as the {/b}{b}endin{/b}{b} text pops up]{/b}"
            #"{b}[credits roll]{/b}"
    else:
        label neutral3:
            cr "Want a fun fact?{w=0.5} You'll {i}definitely {/i}find it interesting."
            cr "The pain you're feeling right now...{w=0.5} is only a thousandth of the pain I went through."
            cr "I {i}wish{/i} I was exaggerating,{w=0.1} but they came up with very accurate,{w=0.1} scientific measurements for this kind of thing."
            cr "Only {i}one thousandth.{/i}"
            cr "You read Dr. Danger's diary,{w=0.1} right?{w=0.5} You {i}know{/i} what STOP did to me."
            cr "Getting up from my bed took weeks.{w=0.5} Walking with my new legs took months.{w=0.5} I still twitch and faint 'cause of the shit they put in my brain."
            cr "You'll never know what that's like.{w=0.5} Being a {i}real {/i}lab rat."
            scene cautionne shoot angrysilent with dissolve:
                align(0.0,0.0)
            pause 1
            scene cautionne shoot angry:
                align(0.0,0.0)
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 3/Cautionne_NeutralEnding3-05.ogg"
            cr "I won't let anyone else live through what I did."
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 3/Cautionne_NeutralEnding3-01.ogg"
            cr "You weren't there.{w=0.928} You weren't in charge. "
            scene cautionne shoot cry:
                align(0.0,0.0)
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 3/Cautionne_NeutralEnding3-02.ogg"
            cr "But after everything you people did to me...{w=0.717} No,{w=0.507} to {i}us...{/i}"

            scene cautionne shoot crysilent:
                align(0.0,0.0)
            pause 0.1
            scene cautionne shoot crysilent with dissolve:
                zoom 2 align(0.0,0.07)
            pause 0.1
            scene cautionne shoot cry:
                zoom 2 align(0.0,0.07)
            #"{b}[{/b}{b}cautione{/b}{b} is on the verge of tears]{/b}"
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 3/Cautionne_NeutralEnding3-03.ogg"
            cr "I...{w=1.265} I..."
            scene cautionne shoot crysilent:
                zoom 2 align(0.0,0.07)
            pause 1
            scene cautionne shoot cry:
                zoom 2 align(0.0,0.07)
            #"{b}[the trigger clicks]{/b}"
            voice "audio/voice/cautionne/Endings/Neutral Endings/NE 3/Cautionne_NeutralEnding3-04.ogg"
            cr "...I just can't forgive someone who'd brush that aside."
            #"{b}[the gun fires]{/b}"



            #"{b}[{/b}{b}Cautionne{/b}{b} is heard crying softly as the ending text pops up]{/b}"
            #"{b}[NEUTRAL END – ROOM 3 VARIANT]{/b}"

    $ play_sound(gunblast1)

    scene black

    pause 5
    call screen credits(60) with Dissolve(2)
    hide text
    pause 3
    $persistent.credits_seen = True
    $ Achievement.add(achievement_end3)

    show text "{size=90}{color=#ffffff}END{/color}{/size}" with dissolve:
            xalign 0.5 yalign 0.5

    pause 5

    hide text with dissolve

    stop music fadeout 2.0

    pause 3

    return