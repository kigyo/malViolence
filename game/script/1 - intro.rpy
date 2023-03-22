
label start:
    #starts with the first track, then continues looping the second one
    #play music ending_intro
    #queue music ending_kill
    scene black
    #[static plays as the game begins. the screen is black, since the protagonist is recovering from being knocked out] 
    pause 1
    x "...llo?"
    pause 1
    x "Hello?"
    pause 1
    x "{size=+35}{i}HEY! WAKE THE HELL UP!!!{/i}{/size}" with small_shake
    scene bg tutorial1 with eyeopen:
        zoom 1.2 yalign 0.8 xalign 0.5
        ease 0.8 zoom 1 yalign 0.5
    "(GAH! What the-)"
    "(...Huh? Where are you?)"
    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        linear 1 yalign 0.3
        linear 1 xalign 0.3 yalign 0.4
        linear 1 xalign 0.5 yalign 0.7
        linear 1 xalign 0.7 yalign 0.4
        linear 1 xalign 0.5 yalign 0.5
    "(Some sort of... cell? But everything's so... woozy, so you can't...)"
    "(No, no - what were you doing before you got here?)"
    "(You wanted a bonus, and your boss told you to go here and get info. So, you did, and then...)"
    "(...and then something hit your back, and... you, uh...) "
    "(You...)"
    x "Oh dear, looks like the anaesthesia hasn't worn off, has it?"
    x "{size=-3}Must've given them the wrong dose of ketamine...{/size}"
    x "Just give it a couple more minutes. Soon, you'll be right as rain!"
    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 0.5 yalign 0.5 xalign 0.3
        ease 1 yalign 0.5 xalign 0.7
        ease 0.5 yalign 0.5 xalign 0.5
    "(Where... where's that voice coming from?)"
    "(It's giving you a migraine. You just wanna shut it-)"
    "(Oh, over there! "
    scene bg tutorial1:
        yalign 0.5 xalign 0.5
        ease 1 xalign 0.25 yalign 0.1
    extend "That monitor, in the corner...)"
    "(I'll just push myself up and make my way over to it.)"
    #[Cautionne's monitor cg shows, but the screen is black] 
    "(...What? There's no volume button on the front panel.)"
    "(Maybe it's to the side, or...)"
    x "Too bad, lab rat! You won't find any volume buttons here."
    "(\"Lab rat?\" What's with that-)"
    x "You're awfully confused by all of this, aren't you?"
    x "Well, then - allow me to introduce myself."
    x "Some call me a simple sidekick."
    x "Others call me the \"Disciple of Danger.\""
    x "But if you asked me, I prefer..."
    show cautionne hairtwirl at crt
    show crt
    with dissolve
    x "\"...The Great Cautionne, Emperor of MalViolence!\"" 
    c "Or \"Cautionne\", for your convenience."
    "(...Seriously? A kid?)"
    "(You got locked up by a kid?)"
    c "Oh, lab rat, that look on your face is priceless. I wanna take a commemorative photo and tack it to my bedroom wall!"
    "(Ugh, please don't. Everyone tells you that you have a resting bitch face.)"
    c "Sadly, my camera isn't with me right now... So, you'll have to make-do with me telling you why you're here."
    c "That's another thing you're wondering about, isn't it? Why are you here?"
    "(...You think?)"
    c "Alright, then. Let's make this quick."
    c "You want something from me."
    c "That's why you came here, right? Your boss told you to come here and get something."
    c "But I can't let that happen. No-siree!"
    c "So, I'm gonna have fun with you instead. I'll learn what you're after, and you won't be bored!"
    c "Great deal, right?"
    "(No. No, it's not.)"
    c "Ha ha ha! You're a funny one, lab rat. I like you already!"
    c "So much so, that I've let you keep your gun."
    c "Feel free to shoot my screen anytime. I promise I won't care!"
    "(The temptation's there, but no thanks.)"
    "(You'd prefer to have some form of self-defense on-hand.)"
    c "Now, I'm still tidying up a couple of things on my end."
    c "So, before I get back to work..."
    
    scene bg tutorial1 at bg with fade
    c "...welcome to your new home, lab rat!"
    c "Cozy, isn't it? It's got everything you need to live a normal human life."
    c "A comfy bed... Well, not comfy, but... a bed. A tap with running water, a desk for... desk things."
    c "Quintessential five-star living, just like the famous Milton Hotels."
    c "Oh, and if you get hungry, just lift the painting in the middle of the room."
    c "The vent dispenses LabScrip 4053. Reviewers say its \"safe for human consumption,\" so don't be shy. It's got all the nutrients you need to live a good life!"
    pause 1
    c "...Well, what's the holdup? Get up, look around, beg for mercy, or make yourself comfortable."
    c "After all... you'll be here for a while."
    #[mic mute sound]
    call screen tutorial_room with dissolve