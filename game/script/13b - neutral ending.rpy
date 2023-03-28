label neutral_ending:
    #"{b}[pause – walking sounds play as the exit BG appears]{/b}"
    show bg corridor_exit:
        align (0.5,0.5) zoom 0.5
        ease 4 zoom 1.0 align(0.5,0.6)

    pause 4

    scene black with fade

    pause 1


    show bg garage with placeintro:
        zoom 0.8 xalign 0.0 yalign 0.5
        linear 30 xalign 1.0

    pause 1
    "(There's the exit,{w=0.1} right up ahead.)"
    #"{b}[pan across {/b}{b}bg{/b}{b} to show {/b}{b}all of{/b}{b} the items there]{/b}"
    "(It's in the middle of a big,{w=0.1} garage space;{w=0.5} one filled with boxes of all shapes and sizes.{w} Maybe it's for storing tools or materials.)"
    "(You don't really want to find out.{w} Like the hallway before it,{w=0.1} this room's completely unremarkable.)"

    "(And besides,{w=0.1} you've had enough of exploring.)"
    #"{b}[pause]{/b}"
    pause 1
    show bg garage with dissolve:
        zoom 0.5 align(0.5,0.5)
    "(...All that said,{w=0.1} you weren't expecting your escape to be so...{w=0.5} {i}straightforward.{/i})"
    "(The exit's wide open.{w} If you walked through right now,{w=0.1} you'll-){p=0.3}{nw}"
    #"{b}[quick footsteps sound out]{/b}"
    pause 1
    "(Aw,{w=0.1} crap.{w} You jinxed yourself.)"
    "H-hello?{w} Who's there?"
    x "So,{w=0.1} you {i}finally {/i}made it.{w=0.5} Did you like my games,{w=0.1} lab rat?"

    scene bg garage:
        zoom 0.5 align (0.5,0.5)
        ease 4 zoom 1.0 yalign 0.6

    pause 3

    scene cautionne gun far silent with fade

    pause 2

    pause 1
    #"{b}[show {/b}{b}Cautionne{/b}{b} shooting CG]{/b}"
    "(A...{w=0.5} a {i}gun?{/i})"
    scene cautionne gun cu with dissolve
    "(Why does he have a gun?{w} Someone his age shouldn't-){p=0.5}{nw}"
    "(No,{w=0.1} it's a fake,{w=0.1} isn't it?{w} Of course –{w=0.5} it's just a practical joke of his!)"
    pause 1
    "Um...{w=0.5} I'm glad you're having fun and all,{w=0.1} but I really should get going."
    "See,{w=0.1} adults have these things called “jobs”,{w=0.1} and-{p=0.3}{nw}"
    scene black
    pause 2
    #"{b}[Pause – sound of {/b}{b}Cautionne{/b}{b} firing a bullet into your kneecap. Screen turns black for a pause. ]{/b}"
    "(Oh.{w} My knee.)"
    pause 0.5
    "(Aah?)"
    pause 0.5
    "{si}(Aaaaaaah?!){/si}"
    pause 0.5
    "{sc}(AaaaaAAAAaaAaAAAAaaAAAAH?!?!?!?){/sc}"

    #"{b}[the player collapses on the floor]{/b}"

    pause 3
    "{si}(Shit.{w} Shit,{w=0.1} shit,{w=0.1} shit.){/si}"
    "{si}(I can't believe –{w} I made such a {i}rookie {/i}mistake!){/si}"
    "{si}(And I can't...{w} Haa...{w} I can't...{w} {i}stand{/i} any more!){/si}"
    "{si}(Wha...{w} what am I gonna do?{w} How am I gonna get out of here {i}now?{/i}){/si}"
    #"{b}[footsteps sounds as{/b}{b} Cautionn{/b}{b}e walks over.]{/b}"
    pause 3
    cr "Patronize me at your own risk."
    cr "...Is what I should've said before firing,{w=0.1} but I'm still new at this part."
    cr "Only a little newer than you,{w=0.1} {i}lab rat.{/i}"
    cr "It's why you don't scare me.{w=0.5} You're just a {i}low-level nobody{/i} with a hand-to-mouth life."
    cr "That's why you did this mission,{w=0.1} right?{w=0.5} ‘Cause you wanted that sweet,{w=0.1} fat,{w=0.1} paycheck?"
    "{si}(...I...{w} I want...{w} to say something...){/si}"
    "{si}(But,{w=0.1} haah...{w} I'm shaking...{w} and sweating...{w} everywhere...){/si}"
    "{si}(All I can do...{w} is open my eyes...){/si}"

    scene cautionne shoot with eyeopen:
        align(0.0,1.0)
        easein 45 align(0.0,0.0)

    pause 3
    #"{b}[Show the bottom of his shooting CG]{/b}"
    cr "Struggling just to open your mouth?{w=0.5} That's almost cute,{w=0.1} in a gross kind of way."
    cr "You've never experienced this much pain before,{w=0.1} have you?"
    if most_explored == 1:

        cr "In fact,{w=0.1} it seems like you haven't experienced much of {i}anything.{/i}"
        cr "If I let you go,{w=0.1} would your bosses even care?"
        cr "After all,{w=0.1} you're not much of an investigator."
        cr "So, how ‘bout I save you all the exit interviews and put things to an end here."
        "{si}(N-no...{w} I can still get up!){/si}"
        "{si}(If I...{w} crawl all the way back...{w} they'll...{w} definitely forgive me...){/si}"
        #"{b}[pan up to his face]{/b}"
        scene cautionne shoot grin with dissolve:
            align(0.0,0.0)
        pause 1
        cr "Hm...{w=0.5} I'll admit,{w=0.1} I'm curious."
        cr "When you're gone,{w=0.1} will STOP eulogize you?{w=0.5} Or will they just write you off as another wasted asset?"
        cr "...Hee hee.{w=0.5} I'm undecided."
        #"{b}[the trigger clicks]{/b}"
        scene cautionne shoot grinsilent:
            align(0.0,0.0)
        pause 0.1
        scene cautionne shoot grinsilent with dissolve:
            zoom 2 align(0.0,0.07)
        pause 0.1
        scene cautionne shoot grin:
            zoom 2 align(0.0,0.07)
        cr "But I wouldn't be much of a scientist if I didn't test my hypotheses."

        scene black
        pause 3

        show text "{size=200}{color=#00e7ff}MALVIOLENCE{/color}{/size}":
                xalign 0.5 yalign 0.5

        pause 5

        hide text

        pause 3

        show text "{size=90}{color=#ffffff}neutral end (a){/color}{/size}":
                xalign 0.5 yalign 0.5

        pause 5

        hide text

        pause 3

        return

    elif most_explored == 2:
        cr "But as much as I sympathize...{w=0.5} I just can't let you go."
        cr "You got your muddy paws on some {i}confidential {/i}information.{w=0.5} Stuff {i}way{/i} above your paygrade."
        cr "So,{w=0.1} I'm afraid I'll have to end things here."
        #"{b}[pan up to his face]{/b}"
        scene cautionne shoot grin with dissolve:
            align(0.0,0.0)
        pause 2
        cr "No hard feelings.{w=0.5} I know you were just doing your job."
        cr "But see,{w=0.1} there's a little {i}conflict of interest{/i} between you and me."
        scene cautionne shoot angry:
            align(0.0,0.0)
        cr "Besides,{w=0.1} I've got to finish what Dr. Danger started.{w=0.5} That's {i}my {/i}{i}job{/i},{w=0.1} now that she's gone."
        #"{b}[the trigger clicks]{/b}"
        scene cautionne shoot angrysilent:
            align(0.0,0.0)
        pause 0.1
        scene cautionne shoot angrysilent with dissolve:
            zoom 2 align(0.0,0.07)
        pause 0.1
        scene cautionne shoot angry:
            zoom 2 align(0.0,0.07)
        cr "And by the time I'm finished,{w=0.1} they'll be {i}begging{/i} for her to come back."
        #"{b}[the gun fires]{/b}"
        scene black
        pause 3

        show text "{size=200}{color=#00e7ff}MALVIOLENCE{/color}{/size}":
                xalign 0.5 yalign 0.5

        pause 5

        hide text

        pause 3

        show text "{size=90}{color=#ffffff}neutral end (b){/color}{/size}":
                xalign 0.5 yalign 0.5

        pause 5

        hide text

        pause 3

        return
        #"{b}[NEUTRAL END – ROOM 2 VARIANT]{/b}"
        #"{b}[{/b}{b}Cautionne{/b}{b} laughing more menacingly as the {/b}{b}endin{/b}{b} text pops up]{/b}"
        #"{b}[credits roll]{/b}"
    else:
        cr "Want a fun fact?{w=0.5} You'll {i}definitely {/i}find it interesting."
        cr "The pain you're feeling right now...{w=0.5} is only a thousandth of the pain I went through."
        cr "I {i}wish{/i} I was exaggerating,{w=0.1} but they came up with very accurate,{w=0.1} scientific measurements for this kind of thing.{w=0.5} {i}Only one thousandth.{/i}"
        cr "You read Dr. Danger's diary,{w=0.1} right?{w=0.5} You {i}know{/i} what STOP did to me."
        cr "Getting up from my bed took weeks.{w=0.5} Walking with my new legs took months.{w=0.5} I still twitch and faint 'cause of the shit they put in my brain."
        cr "You'll never know what that's like.{w=0.5} Being a {i}real {/i}lab rat."
        scene cautionne shoot angrysilent with dissolve:
            align(0.0,0.0)
        pause 1
        scene cautionne shoot angry:
            align(0.0,0.0)
        cr "I {i}won't{/i} let anyone else live through what I did."
        cr "You weren't there.{w=0.5} You weren't in charge. "
        scene cautionne shoot cry:
            align(0.0,0.0)
        cr "But after everything you people did to me...{w=0.5} No,{w=0.1} to {i}us...{/i}"

        scene cautionne shoot crysilent:
            align(0.0,0.0)
        pause 0.1
        scene cautionne shoot crysilent with dissolve:
            zoom 2 align(0.0,0.07)
        pause 0.1
        scene cautionne shoot cry:
            zoom 2 align(0.0,0.07)
        #"{b}[{/b}{b}cautione{/b}{b} is on the verge of tears]{/b}"
        cr "I...{w=0.5} I..."
        scene cautionne shoot crysilent:
            zoom 2 align(0.0,0.07)
        pause 1
        scene cautionne shoot cry:
            zoom 2 align(0.0,0.07)
        #"{b}[the trigger clicks]{/b}"
        cr "...I just can't forgive someone who'd brush that aside."
    

        scene black
        pause 2

        show text "{size=200}{color=#00e7ff}MALVIOLENCE{/color}{/size}":
                xalign 0.5 yalign 0.5

        pause 5

        hide text

        pause 3

        show text "{size=90}{color=#ffffff}neutral end (c){/color}{/size}":
                xalign 0.5 yalign 0.5

        pause 5

        hide text

        pause 3

        return
        #"{b}[the gun fires]{/b}"
        #"{b}[{/b}{b}Cautionne{/b}{b} is heard crying softly as the ending text pops up]{/b}"
        #"{b}[NEUTRAL END – ROOM 3 VARIANT]{/b}"