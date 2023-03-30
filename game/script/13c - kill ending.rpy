label kill_ending:
    show bg corridor_exit:
        align (0.5,0.5) zoom 0.5
        ease 4 zoom 1.0 align(0.5,0.6)

    pause 4

    play sound "audio/sfx/Opening Door.ogg"
    scene black with fade

    pause 2
    play sound "audio/sfx/Closing Door2.ogg"

    #"{b}[pause – walking sounds play as the exit BG appears]{/b}"
    scene bg garage with fade:
        zoom 0.5 align (0.5,0.5)
    "({i}There it is.{/i}{w} There's the exit.)"
    "(And the path is clear -{w=0.5} no guards,{w=0.1} no traps.{w} Just a big garage,{w=0.1} littered with cardboard boxes.)"
    "(Huh.{w} You weren't expecting your escape to be so...{w=0.5} simple.)"
    play sound "audio/sfx/Quick Footsteps 1.ogg"
    pause 1
    "(Scratch that.{w} You spoke too soon.)"
    pause 0.2
    "Identify yourself!"
    #### cautionne's voices go here
    x "How many guesses will you need {i}this{/i} time?"

    scene bg garage:
        zoom 0.5 align (0.5,0.5)
        ease 4 zoom 1.0 yalign 0.6

    pause 3

    scene cautionne gun far silent with fade

    pause 2
    #"{b}[show {/b}{b}Cautionne{/b}{b} shooting CG{/b}{b}]{/b}"
    "No more TV screens,{w=0.1} huh?"

    scene cautionne gun cu with dissolve
    voice "audio/voice/cautionne/soundbites/Normal/Cautionne_SBN-Hmph!.ogg"
    cr "Don't need them.{w=0.5} Not if {i}I'm{/i} going to finish what Dr. Danger started."
    "Using{i} that?{/i}{w} Kid,{w=0.1} you shouldn't be wielding-{p=0.5}{nw}"
    scene cautionne gun ecu with dissolve
    voice "audio/voice/cautionne/soundbites/Normal/Cautionne_SBN-Shut Up 1.ogg"
    cr "Shut up and {i}let me improvise,{/i}{w=0.1} lab rat."
    cr "I didn't {i}actually {/i}think you'd make it this far."
    cr "But alas,{w=0.1} as it turns out...{w=0.5} your puzzle-solving skills are...{w=0.6} decent."
    cr "In another life,{w=0.1} you'd make {i}quite {/i}the sidekick."
    "...Well,{w=0.1} maybe if you'd free me-{p=0.5}{nw}"
    cr "No more hypotheticals."
    cr "You're {i}dangerous,{/i}{w=0.1} lab rat,{w=0.1} and I just can't let you go."
    scene cautionne gun ecu silent
    "(The brat's got bravado -{w=0.5} you'll give him that.{w} He's keeping that revolver remarkably steady,{w=0.1} even though he's shaking all over.)"
    "(But he's still just a kid.{w} Might never have even wielded a weapon before,{w=0.1} for all his big talk.)"
    "(On the other hand...{w=0.5} {i}you're{/i} a STOP agent.)"
    "(You can draw and fire a gun faster than someone can say \"knife\".{w} It's the first thing they teach you as a trainee.)"
    "(He’s scared,{w=0.1} but he’s not going to hesitate any longer.)"
    "(You exhale,{w=0.1} and before his finger can snake itself over the trigger-)"
    "(-you raise your gun towards his torso.)"
    scene black
    pause 3
    #"{b}[bang – with a cut to black]{/b}"
    "(You half expected that freak to go down cackling,{w=0.1} like something out of a movie.)"
    "(A villain shrieking with laughter,{w=0.1} even as they're plugged with thousands of rounds.)"
    #"{b}[show bleeding {/b}{b}cautionne{/b}{b} cg with a slow fade]{/b}"
    scene cautionne gun ecu dead with fade:
        zoom 2.0 align(0.5,0.5)
        parallel:
            ease 20 zoom 1.0 
        parallel:
            ease 20 yalign 0.5
    pause 3
    "(...But Cautionne's final moments are surprisingly quiet.)"
    pause 1
    "(He stutters out a pained gasp.)"
    pause 1
    scene cautionne gun cu dead with dissolve
    play sound "audio/sfx/Single Footstep 1.ogg"
    "(He reaches forward.{w} He struggles to grab something you can't see.)"
    scene black
    play sound "audio/sfx/Body Fall 1.ogg"
    pause 1
    "(He falls.)"
    scene black
    pause 1
    "(His gun clatters on the floor.)"
    pause 1
    "(He doesn't move again.)"
    pause 3
    scene cautionne dead with fade:
        zoom 1.0 align (0.5,0.6)
        ease 40 zoom 0.5 
    pause 2
    #"{b}[pause for a few seconds]{/b}"
    #"{b}[show dead {/b}{b}Cautionne{/b}{b} CG with a slow fade.]{/b}"
    play sound "audio/sfx/Walking Footsteps 4.ogg"
    "(As you walk from the garage,{w=0.1} you do your best to ignore Cautionne's lifeless body.)"
    "(From the corner of your eye,{w=0.1} you watch his blood ooze onto the floor.{w} Once a better agent comes here to gather evidence,{w=0.1} they'll mop the stains and burn the body.)"
    "(The sight of his blood at the edge of your vision fills you with exhaustion.{w} You just want to get out of here and let someone higher up sort this shit out.)"
    "(But as you leave,{w=0.1} you can't help but think to yourself...)"
    "(\"That was easy.\")"
    #"{b}[pause]{/b}"
    "(Easier than it should've been,{w=0.1} maybe.)"
    #"{b}[pause]{/b}"
    "(Or maybe not.)"
    pause 1
    "(...But one thing's for sure.{w} There's one less villain out there now.)"
    "(One less threat.)"
    "(One less thorn in STOP's side.)"

    scene cautionne dead with dissolve:
        zoom 0.5 align(0.0,0.0)
    pause 2
    #"{b}[pause]{/b}"
    "(When you go to write up your report, that's all you'll be able to say.)"
    pause 3

    scene black with fade
    pause 3

    show text "{size=200}{color=#00e7ff}MALVIOLENCE{/color}{/size}":
            xalign 0.5 yalign 0.5

    pause 5

    hide text
    $Achievement.add(achievement_end2)

    pause 3

    show text "{size=90}{color=#ffffff}kill end{/color}{/size}":
            xalign 0.5 yalign 0.5

    pause 5

    hide text

    pause 3
    #"{b}[pause and last cg fades to black]{/b}"
    #"{b}[KILL END]{/b}"
    #"{b}[credits roll]{/b}"
    return