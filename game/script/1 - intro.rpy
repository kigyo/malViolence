
label start:

    # Uncomment to test puzzles.
    # jump test_puzzles

    #starts with the first track, then continues looping the second one
    #play music ending_intro
    #queue music ending_kill
    scene black
    #[static plays as the game begins. the screen is black, since the protagonist is recovering from being knocked out]
    pause 2
    x "...llo?"
    pause 2
    x "{bt}Hello?{/bt}"
    pause 2
    x "{sc}{size=+35}{i}HEY! WAKE THE HELL UP!!!{/i}{/size}{/sc}" with small_shake
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
    x "Oh dear, looks like the anaesthesia hasn't worn off, has it?"
    x "{size=-8}Must've given them the wrong dose of ketamine.{/size}"
    x "Just give it a couple more minutes. Soon, you'll be right as rain!"
    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 0.5 yalign 0.5 xalign 0.3
        ease 0.7 yalign 0.5 xalign 0.7
        ease 0.5 yalign 0.5 xalign 0.5
    "(Where... {w=0.5}where's that voice coming from?)"
    "(It's giving you a migraine. {w}You just wanna shut it-{nw})"

    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 1 xalign 0.25 yalign 0.1
    pause 0.75
    "(Oh, over {i}there!{/i} "
    extend "That monitor, in the corner...)"
    "(You'll just push yourself up and make your way over to it.)"

    scene bg tutorial1:
        yalign 0.1 xalign 0.25
        ease 2 zoom 1.5 xalign 0.3 yalign 0.2

    pause 2

    scene black
    show cautionne_frame_noglow:
        zoom 0.5

    with dissolve

    pause 1
    #[Cautionne's monitor cg shows, but the screen is black]
    "(...What? {w}There's no volume button on the front panel.)"
    pause 0.5
    "(Maybe it's to the side,{w=0.5} or...)"
    x "{i}Too bad,{/i} lab rat! {w}You won't find any volume buttons here."
    "({i}\"Lab rat?\"{/i} {w}What's with that-)"
    x "You're {i}awfully{/i} confused by all of this,{w=0.25} aren't you?"
    x "Well, then - {w=0.25} allow me to introduce myself."
    pause 0.5
    x "Some call me a simple sidekick."
    pause 0.5
    x "Others call me the \"Disciple of Danger.\""
    pause 0.5
    x "But if you asked me, I prefer..."
    show cautionne hairtwirl at crt
    show crt
    show cautionne_frame_glow at bg
    with screenon
    pause 0.2
    c "{i}\"...The Great Cautionne, {w=0.1}Emperor of MalViolence!\"{/i}"
    c "Or \"Cautionne\", for your convenience."
    pause 0.5
    "(...Seriously? {w}A kid?)"
    "(You got locked up by a {i}kid?{/i})"
    show cautionne lean eyeclosed
    c "Oh, lab rat, that look on your face is {i}priceless.{/i}"
    c "I wanna take a commemorative photo and tack it to my bedroom wall!"
    "(Ugh, please don't. Everyone tells you that you have a resting bitch face.)"
    show cautionne lean speaking
    c "Sadly, my camera isn't with me right now..."
    c "So, you'll have to make-do with me telling you why you're here."
    show cautionne hairtwirl at crt
    c "That's another thing you're wondering about, isn't it?"
    c "{i}Why{/i}  are you here?"
    "(...You think?)"
    c "Alright, then!{w=0.1} Let's make this quick."
    show cautionne lean 
    c "{i}You{/i} want something from {i}me.{/i}"
    c "That's why you came here, right?"
    c "Your boss told you to come here and get something."
    c "But I can't let that happen. {w=0.5}No-siree!"
    show cautionne lean eyeclosed
    c "So, I'm gonna have fun with you instead."
    c " I'll learn what you're after, {w=0.1}and you won't be bored!"
    show cautionne lean speaking
    c "Great deal, right?"
    "(No.{w} No, it's not.)"
    show cautionne laugh
    c "Ha ha ha!"
    show cautionne lean eyeclosed
    c"You're a funny one, lab rat.{w=0.5} I like you already!"
    c "So much so, that I've let you keep your gun."
    show cautionne lean speaking
    c "Feel free to shoot my screen anytime."
    c "I promise I won't care!"
    "(The temptation's there, but no thanks.)"
    "(You'd prefer to have some form of self-defense on-hand.)"
    show cautionne think
    c "Now, I'm still tidying up a couple of things on my end."
    c "So, before I get back to work..."

    show cautionne thinkpause

    scene bg tutorial1 at bg with fade
    pause 0.5
    cr "...welcome to your new home!"
    cr "Cozy, isn't it? {w}It's got everything you need to live a normal human life."
    cr "A comfy bed... {w}Well, not comfy, but...{w=0.1} a bed."
    cr "A tap with running water,{w} a desk for...{w=0.1} desk things."
    cr "Quintessential five-star living, just like the famous Milton Hotels."
    cr "Oh, and if you get hungry, just lift the painting in the middle of the room."
    cr "The vent dispenses LabScrip 4053."
    cr "Reviewers say its \"safe for human consumption,\" so don't be shy. {w}It's got all the nutrients you need to live a good life!"
    pause 1
    cr "...Well, what's the holdup? {w}Get up, look around, beg for mercy, or make yourself comfortable."
    cr "After all... {w=1}you'll be here for a while."
    #[mic mute sound]
    call screen tutorial_room with dissolve
