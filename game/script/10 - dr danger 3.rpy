label dr_danger_3:



  "(...Again with the temper tantrum,{w=0.1} huh.)"
  "(Seriously,{w=0.1} why's he so pissed off at you?)"
  "(He and Dr. Danger have fought against STOP field agents in the past,{w=0.1} but that's not your department.)"
  "(Hell,{w=0.1} {i}before{/i} this,{w=0.1} you've never met either of them face-to-face.)"
  "(What right does he have to act all high-and-mighty at {i}you?{/i})"
  pause 1
  "(...)"
  "(Right —{w=0.5} {i}supervillain.{/i})"
  "(Big ego,{w=0.1} no self-awareness.{w} Don't overthink it.)"

  $ play_sound(footsteps3)

  show bg room2:
    zoom 0.8 align (0.8,0.5)
    ease 2 zoom 1.0
  pause 2
  $ play_sound(dooropen)
  scene black with fade
  pause 2
  show bg corridor3 tvoff with placeintro:
    zoom 0.8 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0
  $ Achievement.add(achievement_room2)
  pause 4
  show bg corridor3 tvoff with dissolve:
    zoom 0.5
  $ play_sound(doorclose)
  pause 0.5
  "(...The dim corridor stretches before you,{w=0.1} with no answers to offer.)"
  "(It's darker here —{w=0.5} but not in an unpleasant way.{w} It's warmer than the previous rooms,{w=0.1} literally and figuratively.)"
  "(The wooden floorboards and the decorated wallpaper feel...{w=0.5} welcoming.{w} {i}Nostalgic,{/i} even.)"
  "(If you viewed this hall alone,{w=0.1} you'd assume it'd belong to a family household.{w} Not to a scheming terrorist and her kooky sidekick.)"
  "(It's been a very long...{w=0.5} day?{w} Hard to tell how much time has passed.)"
  "(But damn,{w=0.1} you are {i}exhausted.{/i})"
  "(The gentle heat tempts you to sit down on the floor.{w} Or maybe lie down.)"
  pause 1
  "(Um...{w} Would Cautionne allow you to take a quick breather?)"
  #"{b}[animate camera movements to simulate the protagonist slowly crouching down to the floor] {/b}"
  "(If he meant what he said about not harming a hair on your head,"
  $ play_sound(singlefootstep2)
  show bg corridor3 tvoff:
    zoom 0.5 xalign 0.5 yalign 0.5
    ease 3 yalign 1.0 zoom 0.6
  extend "{cps=20} then maybe the smart thing to do would be to—){/cps}{w=1}{nw}"
  $ play_sound(staticshort)
  show bg corridor3
  voice "audio/voice/dr.danger/Danger_Corridor3-01.ogg"
  dr "Very tempting for a wooden floor,{w=0.287} isn't it?"
  $ play_sound(bedsitup)
  show bg corridor3:
    zoom 0.6 xalign 0.5 yalign 1.0
    easein 0.2 yalign 0.5 zoom 0.6
  "(Gah!{w} A {i}third{/i} time?!)" with small_shake
  voice "audio/voice/dr.danger/Danger_Corridor3-02.ogg"
  dr "{i}Heated flooring.{/i}{w=0.41} My work has always been stressful, so...{w=0.193} I've always strived to maximize comfort wherever I could."

  $ play_sound(footsteps3)

  show bg corridor3:
    zoom 0.6 yalign 0.5 xalign 0.5
    ease 4 zoom 1.7 xalign 0.3 yalign 0.5

  pause 4
  hide bg corridor3
  show drdanger smirk at crt
  show crt
  show drdangerframe at bg
  with dissolve 
  voice "audio/voice/dr.danger/Danger_SB-Allow Me To Explain.ogg"
  drs "When your work is done,{w=0.1} you can sleep here all you like."
  drs "But before then,{w=0.1} you've got dishes to clean,{w=0.1} washes to run,{w=0.1} bedrooms to vacuum..."
  show drdanger sidestare
  drs "...and of course,{w=0.1} Cautionne to take care of."
  pause 1
  voice "audio/voice/dr.danger/Danger_SB-Sigh.ogg"
  $ play_music(backstorytheme, fadein=1.0, fadeout=1.0)
  drs "He represents a unique challenge,{w=0.1} I know."
  show drdanger smirk
  drs "But you wouldn't have gotten this far if you and I didn't believe you could do it."
  show drdanger stare
  voice "audio/voice/dr.danger/Danger_SB Please Listen Carefully.ogg"
  drs "While I'm away on business,{w=0.1} it's important that you keep him on his daily routine."
  drs "7am to 9pm —{w=0.5} regularity is key."
  drs "Remember that all his dietary habits,{w=0.1} health regimens{w=0.1} and study exercises{w=1.25}{nw}"
  drs "are detailed in the files that we went over together."
  show drdanger sidestare
  voice "audio/voice/dr.danger/Danger_SB-I Apologize.ogg"
  drs "I apologize if you'll have to decrypt them again,{w=0.1} but..."
  drs "...Cautionne and I have made a habit of hiding our tracks for good reason."
  show drdanger smirk
  drs "And when the day is over,{w=0.1} feel free to play games, watch movies, or read comics together."
  drs "If you need a suggestion..."
  drs "...Cautionne told me that he loves the \"Cantaloupe Mall\" course on \"Marco Kart\"."
  show drdanger sidestare
  voice "audio/voice/dr.danger/Danger_SB-Sigh.ogg"
  drs "...I might be pronouncing that wrong.{w=0.5} He'll know what you mean."
  show drdanger stare
  drs "So, take care."
  voice "audio/voice/dr.danger/Danger_SB Please Listen Carefully.ogg"
  drs "If things go smoothly,{w=0.1} I'll be back for him in a week."
  show drdanger sidestare
  drs "And if things {i}don't{/i}{i} {/i}go smoothly..."
  show drdanger sidestare silent
  stop music fadeout 1.0
  pause 1
  show drdanger stare speaking
  drs "Well,{w=0.1} there are systems in place that will guide you on what to do."
  voice "audio/voice/dr.danger/Danger_Corridor3-03.ogg"
  drs "That's all for now.{w=0.458} Goodbye."
  show drdanger tender
  voice "audio/voice/dr.danger/Danger_Corridor3-04.ogg"
  drs "And thank you for taking care of my..."
  show drdanger tender silent
  pause 1
  show drdanger sidestare silent
  pause 1
  $ play_sound(staticshort)
  hide drdanger sidestare silent
  show drdangerframe off
  with screenoff

  voice "audio/voice/dr.danger/Danger_Corridor3-05.ogg"
  #"{b}[{/b}{b}Dr.{/b}{b} Danger pauses, and her expression changes – showing {/b}{b}she's{/b}{b} {/b}{b}hold{/b}{b}ing something back]{/b}"
  drs "{size=-13}Note to self, re-record instructions at earliest convenience.{w=3}{nw}{/size}"
  voice sustain
  drs "{size=-13}Try not to be so...{w=0.5} {i}ominous{/i} next time.{/size}"
  $ play_sound(tvoff)
  pause 2
  scene bg corridor3 tvoff with fade:
    zoom 0.5 align (0.5,0.5)
  pause 2

  "(That message wasn't for you,{w=0.1} and it wasn't for one of Dr. Danger's goons either.)"
  "(But a {i}babysitter?{/i}{w} Really?)"
  "(Who in the world would be qualified to babysit {i}him?{/i})"
  pause 1
  "(...)"
  "(...{i}C'mon.{/i}{w} Just focus on the task at hand.)"

  $ play_sound(footsteps3)

  scene bg corridor3 tvoff:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 4 zoom 1.0
  pause 3
  scene black with fade
  $ play_sound(dooropen)
  pause 2
  show bg room3_downstairs with placeintro:
    zoom 0.6 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0

  pause 5

  show bg room3_downstairs with dissolve:
    zoom 0.4 yalign 0.7
  $ play_sound(doorclose)
  pause 0.5
  #"{b}[pause, walking sounds play as the player goes to room 3]{/b}"
  "(It's...{w=0.5} a normal apartment?)"
  "(There's a kitchenette,{w=0.5} a dining table,{w=0.5} a small sitting area...)"
  "(...And stairs.{w} Probably a bedroom up there.)"
  pause 1
  "(Are you {i}supposed{/i} to be here?)"
  $ play_sound(doorlock)
  pause 2
  "(Guess you are.)"

  show bg room3_downstairs:
    zoom 0.4 
    ease 5 zoom 0.335 xalign 0.0 yalign 0.0

  pause 5
  $ play_music(room3theme, fadein=1.0, fadeout=1.0)
  $ inspect = None
  call screen room3 with dissolve