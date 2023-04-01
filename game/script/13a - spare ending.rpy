label spare_ending:

    show bg corridor_exit:
        align (0.5,0.5) zoom 0.5
        ease 4 zoom 1.0 align(0.5,0.6)

    pause 4

    $ play_sound(dooropen)
    scene black with fade

    pause 2

    $ play_sound(doorclose)

    #"{b}[pause – walking sounds play as the exit BG appears]{/b}"
    scene bg garage with fade:
        zoom 0.5 align (0.5,0.5)
    "(In a large garage filled to the brim with carboard boxes,{w=0.1} the exit waits for you,{w=0.1} wide open.)"
    "(It's night already.{w} Outside, you hear the quiet rushing of a river.)"
    "(Just a few more steps,{w=0.1} and you're out of here.{w} Even more,{w=0.1} and you'll be on the bus back home.)"
    "(It'll take a couple of hours to get back to HQ.{w} You'll nap on the ride,{w=0.1} probably,{w=0.1} so that by the time you get to your stop,{w=0.1} you'll have enough energy to run up thousands of narrow stairs.)"
    "(And you'll reach your boss's office,{w=0.1} and...)"
    "(...Well,{w=0.1} what'll happen next?)"
    "(You'll {i}definitely {/i}get that bonus.{w} If this isn't going \"above and beyond...\")"
    "(Maybe you'll get a promotion.{w} A better salary.{w} Better benefits.{w} A better home.)"
    "(A better {i}life.{/i}{w} Something you've always wanted.)"
    "(...And...)"
    "(And maybe that'll help you sort out the pit that's been growing in your stomach this whole—){p=0.5}{nw}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-01.ogg"
    xc "Finally going to take responsibility?"
    $ play_sound(quickfootsteps)
    #"{b}[{/b}{b}Cautionne{/b}{b} appears with his gun]{/b}"

    scene bg garage:
        zoom 0.5 align (0.5,0.5)
        ease 4 zoom 1.0 yalign 0.6

    pause 4

    scene cautionne gun far silent with fade

    "(Not {i}now,{/i} kid!{w} The last thing you need is {i}him{/i} showing up and—){p=0.5}{nw}"

    scene cautionne gun cu with dissolve
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-02.ogg"
    cr "I...{w=0.5} I see my escape rooms have worked their magic."
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-03.ogg"
    cr "I didn't think it was possible but...{w=0.5} you're feeling {i}guilty,{/i} aren't you?"
    "(...{i}Guilt?{/i}{w} Is that what it is?)"
    "(Over something you didn't do?)"
    scene cautionne gun ecu with dissolve
    $ play_music(endingintro, loop=False)
    $ queue_music(spareending)
    voice "audio/voice/cautionne/soundbites/Normal/Cautionne_SBN-Hmph!.ogg"
    cr "All those years,{w=0.1} you must've been so proud to wear that uniform!{w=0.5} To be a brave soldier fighting for such a pristine,{w=0.1} justice-seeking{w=0.1} organization like that."
    "(You feel sick.)"
    cr "But it's not enough for you to {i}feel bad{/i}. "
    cr "'Cause if I let you go home,{w=0.1} and get your bonuses,{w=0.1} and sleep in your nice bed..."
    cr "...You'll be stumbling over yourself to forget everything that happened here as fast as possible."
    cr "You...{w=0.5} Or your boss,{w=0.1} or the next agent..."
    cr "You'll storm in here and sweep away everything me and Dr. Danger fought for."
    cr "{si}S-someone better'll catch me and destroy this place.{/si}"
    cr "{si}And STOP...{w=0.5} STOP'll turn me into a nameless drone,{w=0.1} like I was \n{i}supposed{/i} to be.{/si}"
    "(...He's shaking.{w} He's trying to put on a brave face,{w=0.1} but he's shaking.)"
    #"{b}[{/b}{b}cautionne{/b}{b} begins to break down]{/b}"
    scene cautionne gun ecu cry with dissolve
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-04.ogg"
    cr "{si}B-but I don't {i}want {/i}that,{w=0.1} y'know?{/si}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-05.ogg"
    cr "{si}I...{w=0.5} I don't {i}want {/i}to forget my home.{w=0.5} My books,{w=0.5} my bugs,{w=0.5} my bed...{/si}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-06.ogg"
    cr "{si}And I don't {i}want {/i}to forget myself.{/si}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-07.ogg"
    cr "{si}I don't want to forget about collecting stickers,{w=0.5} or eating pudding,{w=0.5}\n or sewing my first pair of mittens.{/si}"
    
    scene cautionne gun ecu crysilent
    pause 1
    #"{b}[{/b}{b}Cautionne{/b}{b} is yelling now]{/b}"
    scene cautionne gun ecu sob 
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-08.ogg"
    cr "{sc}And I don't {i}want{/i} to forget Dr. Danger!{/sc}{p=1.9}{nw}"
    voice sustain
    cr "{sc}She {i}saved {/i}me!{w=0.9} She {i}raised {/i}me!{w=0.9} \nShe {i}stood up for me{/i} when no one else did!{/sc}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-09.ogg"
    cr "{sc}And what did {i}STOP {/i}do?{/sc}{p=0.9}{nw}"
    voice sustain
    cr "{sc}They MADE her a villain!{w=1.2} They took EVERYTHING away from her!{w=2.1}\n They KILLED her!{/sc}"
    scene cautionne gun ecu sobsilent
    pause 1
    scene cautionne gun cu crysilent with dissolve
    pause 0.1
    scene cautionne gun cu cry
    #"{b}[pause as {/b}{b}Cautionne{/b}{b} regains his composure a little]{/b}"
    cr "{si}S-so,{w=0.1} what're you gonna do now, lab rat?{/si}"
    cr "{si}You've still got your weapon,{w=0.1} don't you?{/si}"
    cr "{si}C'mon.{w=0.5} H-hit me with your best shot.{/si}"
    scene cautionne gun cu crysilent
    pause 0.5
    scene cautionne gun cu cry
    cr "{si}...Hit me!{/si}"
    cr "{si}'Cause if you don't,{w=0.1} I'll...{w=0.5}{/si} {sc}I'll...{/sc}"
    scene cautionne gun cu crysilent
    #"{b}[pause with the sound of the player's gun dropping to the floor]{/b}"

    pause 1

    scene black with fade

    pause 1
    "(...You can't deal with this anymore.)"
    "(You...{w=0.5} you don't want to fight him.)"
    scene cautionne gun cu crysilent with dissolve
    pause 1

    scene cautionne gun cu cry
    #"{b}[pause as {/b}{b}Cautionne's{/b}{b} expression changes]{/b}"
    cr "You...{w=0.5} you're {i}not {/i}going to use your gun?"
    cr "...Heh.{w=0.5} Haha.{w=0.5} {si}Hahahaha.{/si}"

    scene cautionne gun cu crysilent 
    stop music fadeout 1.0
    #"{b}[gun clicks]{/b}"
    pause 1
    scene cautionne gun cu speaking 
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-10.ogg"
    cr "{si}T-then, on behalf of STOP...{/si}{w=1} {i}die.{/i}"
    #"{b}[pause. Sound of the gun firing. {/b}{b}Screen goes black]{/b}"
    scene black
    pause 3
    "(The bullet...)"
    pause 1
    "(...it only grazed your cheek.)"
    $ play_sound(bodyfall)
    pause 2
    "(Huh?{w} Cautionne...{w=0.5} fell?)"
    "(What's going...)"
    $ play_music(spareending, fadein=1.0, fadeout=1.0)
    scene cautionne sit stunned with fade:
        align(0.0,1.0)
        ease 7 align(0.0,0.1)
    pause 3
    #"{b}[pause as cautionne spare end cg fades in]{/b}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-11.ogg"
    cr "I...{w=0.5} I missed."
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-12.ogg"
    cr "I had the muzzle aimed at your head.{w=0.5} The bullets loaded."
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-13.ogg"
    cr "And I missed.{w=0.5} First try."
    "(Cautionne's gaze is vacant.)"
    "(It's the same gaze as that boy in the scrapbook.)"
    "(That alone makes the pit in your stomach sink even deeper.)"
    pause 1
    "(So to fill it...{w=0.5} you say something really,{w=0.1} really{w=0.1} stupid.)"
    "You know...{w=0.5} you could've fired again.{w} I'm at contact shot distance."
    scene cautionne sit hope:
        align (0.0,0.1)
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-14.ogg"
    cr "...Pft."
    scene cautionne sit stunned:
        align (0.0,0.1)
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-15.ogg"
    cr "No,{w=0.1} I couldn't have.{p=0.6}{nw}" 
    voice sustain
    cr "Trying to kill you...{w=0.5} was a lot more tiring than I thought it would be."
    "Tiring?"
    scene cautionne sit stunnedsilent:
        align (0.0,0.1)
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-16.ogg"
    cr "..."
    "(...Ah.)"
    scene cautionne sit stunned:
        align (0.0,0.1)
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-17.ogg"
    cr "Go.{w=0.5} This is what you wanted,{w=0.1} right?"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-18.ogg"
    cr "The exit's right there."
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-19.ogg"
    cr "Go back to your home.{w=0.5} Your TV.{w=0.5} Your{i} money.{/i}"
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-20.ogg"
    cr "I was fooling myself,{w=0.1} thinking I could do what Dr. Danger did for me."
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-21.ogg"
    cr "So,{w=0.1} go. "
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-22.ogg"
    cr "I hope the guilt eats at you for the rest of your fucking life."
    scene cautionne sit stunnedsilent:
        align (0.0,0.1)


    pause 1

    scene black with fade

    pause 1

    scene bg garage with fade:
        zoom 0.5 align (0.5,0.5)

    pause 2
    #"{b}[pause when the exit {/b}{b}bg{/b}{b} shows again. Camera shows the player getting up, and leaving for the {/b}{b}exit{/b}{b}]{/b}"
    "(Slowly,"

    $ queue_sound ([footsteps4, footsteps4, footsteps4])

    scene bg garage:
        zoom 0.5 align (0.5,0.5)
        ease 15 zoom 1.4 yalign 0.55

    extend " you make your way towards the exit.)"
    #"{b}[pause]{/b}"
    pause 5
    "(When you finally make it outside,{w=0.1} you turn back.)"

    scene cautionne sit_far with fade

    pause 1
    "(The boy's still sitting there.)"
    "(Legs splayed haphazardly.{w} Arms,{w=0.1} floppy.{w} Still staring at you.)"
    pause 1
    #"{b}[pause]{/b}"
    "(You stare back at him.{w} Give him a curt nod.)"
    pause 1
    "(He doesn't react.)"
    #"{b}[pause]{/b}"
    pause 1

    scene bg garage with fade:
        zoom 1.4 align (0.5,0.55)

    "(So, without another word,{w=0.1} you—){p=0.5}{nw}"
    cr "...Hey lab rat."
    "(You turn back,"

    scene cautionne sit hope with fade:
        align (0.0,0.1)

    extend " and see him forcing an attempt at a villainous grin.)"
    pause 2
    #"{b}[{/b}{b}pause, and{/b}{b} show a variant of {/b}{b}Cautionne's{/b}{b} spare end CG.]{/b}"
    cr "If you really feel that bad about it..."
    cr "I did sneak copies of everything you've seen here onto your device.{w=0.5} I found your address while you were looking around."
    cr "Pretty devious idea,{w=0.1} right?"
    scene cautionne sit smug:
        align (0.0,0.1)
    extend " Downright heinous."
    "(He takes a deep breath.{w=0.5} Then exhales.)"
    cr "Alright.{w=0.5} Here's another world-class criminal scheme for you:"
    cr "{i}\"STOP agent stakes reputation,{w=0.1} credentials,{w=0.1} leaks internal docs{w=0.1} to all four corners of the net.\"{/i}"
    cr "Not a bad headline."

    scene cautionne sit hope:
        align (0.0,0.1)

    extend " Could make for a half-decent start to a villainous career."
    #"{b}[pause]{/b}"
    scene cautionne sit hopesilent:
        align (0.0,0.1)
    pause 0.5

    scene cautionne sit hope:
        align (0.0,0.1)

    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-23.ogg"

    cr "Your choice,{w=0.1} obviously.{p=0.6}{nw}"

    scene cautionne sit smug:
        align (0.0,0.1)
    voice sustain
    extend " But I know what I'm talking about."
    voice "audio/voice/cautionne/Endings/Spare Ending/Cautionne_SpareEnding-24.ogg"

    stop music fadeout 1.0
    cr "After all,{w=0.1} I {i}am{/i}{i} {/i}a supervillain."

    define slowfade = Fade(2, 0.1, 1)

    scene cautionne sit smugsilent:
        align (0.0,0.1)
    pause 2

    scene black with slowfade
    $ play_sound(footsteps4)
    pause 2

    scene hairclip1 with slowfade:
        zoom 0.5

    pause 2

    scene black with slowfade

    pause 1

    scene hairclip2 with slowfade:
        zoom 0.5

    pause 2

    scene black with slowfade

    pause 1

    scene hairclip3 with slowfade:
        zoom 0.5

    pause 4

    define fadehold = Fade(5, 1.0, 0.5)

    scene black with fadehold

    pause 7

    show text "{size=200}{color=#00e7ff}MALVIOLENCE{/color}{/size}":
            xalign 0.5 yalign 0.5

    pause 5

    hide text

    pause 3
    $Achievement.add(achievement_end1)

    show text "{size=90}{color=#ffffff}spare end{/color}{/size}":
            xalign 0.5 yalign 0.5

    pause 5

    hide text

    pause 3


    #"{b}[pause as {/b}{b}Cautionne's{/b}{b} footsteps are heard slowly walking off]{/b}"
    #"{b}(CG of Cautionne's stoplight hairclip shown on the floor.){/b}"
    #"{b}(The player is shown picking it up with their hand.]{/b}"
    #"{b}[Then, the screen goes black]{/b}"
    #"{b}[SPARE END]{/b}"
    #"{b}[credits roll]{/b}""
    return