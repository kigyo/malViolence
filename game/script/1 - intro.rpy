
label start:
    # Uncomment to test puzzles.
    stop music
    # jump test_puzzles

    #starts with the first track, then continues looping the second one
    #play music ending_intro
    #queue music ending_kill
    scene black
    with dissolve
    #[static plays as the game begins. the screen is black, since the protagonist is recovering from being knocked out]
    pause 2
    voice "audio/voice/cautionne/intro/Cautionne_Intro-01.ogg"
    x "...llo?"
    pause 2
    voice "audio/voice/cautionne/intro/Cautionne_Intro-02.ogg"
    x "{bt}Hello?{/bt}"
    pause 2
    voice "audio/voice/cautionne/intro/Cautionne_Intro-03.ogg"
    x "{sc}{size=+35}{i}HEY!{w=0.1} WAKE THE HELL UP!!!{/i}{/size}{/sc}" with small_shake

    $ play_sound(bedsitup)

    scene bg tutorial1 with eyeopen:
        zoom 1.2 yalign 1.2 xalign 0.5
        ease 0.4 zoom 1 yalign 0.5
    $Achievement.add(achievement_start)
    "(GAH! {w}What the-)"
    "(...Huh? {w}Where {i}are{/i} you?)"
    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 1.5 yalign 0.3
        ease 1.5 xalign 0.3 yalign 0.4
        ease 1.5 xalign 0.5 yalign 0.7
        ease 1.5 xalign 0.7 yalign 0.4
        ease 1.5 xalign 0.5 yalign 0.5
    "(Some sort of... cell? {w}But everything's so... woozy, so you can't...)"
    pause 0.5
    "(No, no - what were you doing {i}before{/i} you got here?)"
    "(You wanted a bonus, and your boss told you to go here and get info.{w} So, you did, and then...)"
    "(...and then something hit your back, and... {w}you, {w=0.5}uh...) "
    "(You...)"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-04.ogg"
    x "Oh dear, looks like the anaesthesia hasn't worn off, has it? {w=0.5}{size=-8}Must've given them the wrong dose of ketamine.{/size}"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-05.ogg"
    x "Just give it a couple more minutes.{w=0.5} Soon, you'll be right as rain!"
    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 0.5 yalign 0.5 xalign 0.3
        ease 0.7 yalign 0.5 xalign 0.7
        ease 0.5 yalign 0.5 xalign 0.5
    "(Where... {w=0.5}where's that voice coming from?)"
    "(It's giving you a migraine. {w}You just wanna shut it-){w=0.5}{nw}"

    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 1 xalign 0.25 yalign 0.1
    pause 0.75
    "(Oh, over {i}there!{/i}"
    extend " That monitor, in the corner...)"
    "(You'll just push yourself up and make your way over to it.)"

    $ play_sound(bedgetoff)

    scene bg tutorial1:
        yalign 0.1 xalign 0.25
        ease 1 yalign 0.05
        ease 0.5 yalign 0.1

    pause 2

    $ play_sound(footsteps1)


    scene bg tutorial1:
        yalign 0.1 xalign 0.25
        ease 2 zoom 1.5 xalign 0.3 yalign 0.2

    pause 2

    scene black
    show cautionne_frame_noglow:
        zoom 0.5

    with dissolve

    pause 2
    #[Cautionne's monitor cg shows, but the screen is black]
    "(...What? {w}There's no volume button on the front panel.)"
    pause 0.5
    "(Maybe it's to the side,{w=0.5} or...)"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-06.ogg"
    x "{i}Too bad,{/i} lab rat!{w=0.5} You won't find any volume buttons here."
    "({i}\"Lab rat?\"{/i} {w}What's with that-)"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-07.ogg"
    x "You're {i}awfully{/i} confused by all of this,{w=0.25} aren't you?"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-08.ogg"
    x "Well, then - {w=0.25} allow me to introduce myself."
######### edit voices from here
    pause 0.5
    voice "audio/voice/cautionne/intro/Cautionne_Intro-09.ogg"
    x "Some call me a simple sidekick.{w=0.5} Others call me the \"Disciple of Danger.\""
    pause 0.5
    voice "audio/voice/cautionne/intro/Cautionne_Intro-10.ogg"
    x "But if you asked me, I prefer..."
    play audio "audio/sfx/TV On 1.ogg"
    show cautionne hairtwirl at crt
    show crt
    show cautionne_frame_glow at bg
    with screenon
    pause 0.2
    $ play_music(cautionnetheme)
    voice "audio/voice/cautionne/intro/Cautionne_Intro-11.ogg"
    c "{i}\"...The Great Cautionne,{w=0.1} Emperor of MalViolence!\"{/i}"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-12.ogg"
    c "Or \"Cautionne\", for your convenience."
    show cautionne hairtwirl silent
    pause 0.5
    "(...Seriously? {w}A kid?)"
    "(You got locked up by a {i}kid?{/i})"
    show cautionne lean eyeclosed
    voice "audio/voice/cautionne/intro/Cautionne_Intro-13.ogg"
    c "Oh, lab rat, that look on your face is {i}priceless.{/i}{p=2.2}{nw}"
    voice sustain
    c "I wanna take a commemorative photo and tack it to my bedroom wall!"
    "(Ugh, please don't.{w} Everyone tells you that you have a resting bitch face.)"
    show cautionne lean speaking
    voice "audio/voice/cautionne/intro/Cautionne_Intro-14.ogg"
    c "Sadly, my camera isn't with me right now...{p=2.1}{nw}"
    voice sustain
    c "So, you'll have to make-do with me telling you why you're here."
    show cautionne hairtwirl at crt
    voice "audio/voice/cautionne/intro/Cautionne_Intro-15.ogg"
    c "That's another thing you're wondering about,{w=0.1} isn't it?{p=1.5}{nw}"
    c "Why {i}are{/i} you here?"
    "(...You think?)"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-16.ogg"
    c "Alright, then!{w=0.1} Let's make this quick."
    show cautionne lean 
    voice "audio/voice/cautionne/intro/Cautionne_Intro-17.ogg"
    c "{i}You{/i} want something from {i}me.{/i}"
    voice "audio/voice/cautionne/intro/Cautionne_Intro-18.ogg"
    c "That's why you came here, right?{p=0.5}{nw}"
    voice sustain
    c "Your boss told you to come here and get something."
    voice "audio/voice/cautionne/intro/Cautionne_Intro-19.ogg"
    c "But I can't let that happen. {w=1}No-siree!"
    show cautionne lean eyeclosed
    voice "audio/voice/cautionne/intro/Cautionne_Intro-20.ogg"
    c "So, I'm gonna have fun with you instead.{p=1.2}{nw}"
    voice sustain
    c " I'll learn what you're after,{w=0.1} and you won't be bored!"
    show cautionne lean speaking
    voice "audio/voice/cautionne/intro/Cautionne_Intro-21.ogg"
    c "Great deal, right?"
    "(No.{w} No, it's not.)"
    show cautionne laugh
    voice "audio/voice/cautionne/intro/Cautionne_Intro-22.ogg"
    c "Ha ha ha!{p=1.1}{nw}"
    show cautionne lean eyeclosed
    c"You're a funny one, lab rat.{w=0.5} I like you already!"
    voice sustain
    voice "audio/voice/cautionne/intro/Cautionne_Intro-23.ogg"
    c "So much so, that I've let you keep your gun.{p=1.2}{nw}"
    voice sustain
    c "Feel free to shoot my screen anytime.{p=1.2}{nw}"
    voice sustain
    c "I promise I won't care!"
    "(The temptation's there,{w=0.1} but no thanks.)"
    "(You'd prefer to have some form of self-defense on-hand.)"
    show cautionne think
    voice "audio/voice/cautionne/intro/Cautionne_Intro-24.ogg"
    c "Now, I'm still tidying up a couple of things on my end.{p=1}{nw}"
    voice sustain
    c "So,{w=0.1} before I get back to work..."

    show cautionne thinkpause

    scene bg tutorial1 at bg with fade
    pause 0.2
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Well Then.ogg"
    cr "...welcome to your new home!"
    cr "Cozy,{w=0.1} isn't it?{w=0.5} It's got everything you need to live a normal human life."
    cr "A comfy bed...{w=0.5} Well, not comfy, but...{w=0.1} a {i}bed.{/i}"
    cr "A tap with running water,{w=0.1} a desk for...{w=0.1} {i}desk things.{/i}"
    cr "Quintessential five-star living,{w=0.1} just like the famous Milton Hotels."
    cr "Oh,{w=0.1} and if you get hungry,{w=0.1} just lift {color=#00e7ff}the painting in the middle of the room.{/color}"
    cr "The vent dispenses LabScrip 4053."
    cr "Reviewers say its \"safe for human consumption,\"{w=0.1} so don't be shy. {w}It's got all the nutrients you need to live a good life!"
    pause 1
    cr "...Well, what's the holdup?{w=0.5} Have a look around,{w=0.1} beg for mercy,{w=0.1} or make yourself comfortable."
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
    cr "After all...{w=0.5} you'll be here for a while!"
    $ play_sound(staticshort)
    stop music
    pause 2
    $ play_music(tutroom, fadein=1.0, fadeout=0.1)
    call screen tutorial_room with dissolve
