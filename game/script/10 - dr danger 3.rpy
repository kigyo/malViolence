label dr_danger_3:

  "(...Again with the temper tantrum,{w=0.1} huh.)"
  "(Seriously,{w=0.1} why's he so pissed off at you?)"
  "(He and Dr. Danger have fought against STOP field agents in the past,{w=0.1} but that's not your department.)"
  "(What right does he have to act all high and mighty towards {i}you?{/i})"
  pause 1
  "(...)"
  "(Right - {i}supervillain.{/i})"
  "(Big ego,{w=0.1} no self-awareness.{w} Don't overthink it.)"

  show bg room2:
    zoom 0.8 align (0.8,0.5)
    ease 2 zoom 1.0
  pause 2
  scene black with fade
  pause 1
  show bg corridor3 with placeintro:
    zoom 0.8 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0
  $Achievement.add(achievement_room2)
  pause 4
  show bg corridor3 with dissolve:
    zoom 0.5
  "(...The dim corridor stretches before you,{w=0.1} with no answers to offer.)"
  "(Yes,{w=0.1} it's darker here -{w=0.5} but not in an unpleasant way.{w} It's warmer than the previous rooms,{w=0.1} literally and figuratively.)"
  "(The wooden floorboards and the decorated wallpaper feel...{w=0.5} welcoming.{w} {i}Nostalgic,{/i} even.)"
  "(If you viewed this hall alone,{w=0.1} you'd assume it'd belong to a family household.\n{w}Not to a scheming terrorist and her kooky sidekick.)"
  "(It's been a very long...{w=0.5} day?{w} Hard to tell how much time has passed.)"
  "(The gentle heat tempts you to sit down on the floor.{w} Or maybe lie down.)"
  pause 1
  "(Um...{w} Would Cautionne allow you to take a quick breather?)"
  #"{b}[animate camera movements to simulate the protagonist slowly crouching down to the floor] {/b}"
  "(If he meant what he said about not harming a hair on your head,"
  show bg corridor3:
    zoom 0.5 xalign 0.5 yalign 0.5
    ease 3 yalign 1.0 zoom 0.6
  extend "{cps=20} then maybe the smart thing to do would be to-){p=0.5}{nw}"
  dr "Very tempting for a wooden floor,{w=0.1} isn't it?"
  show bg corridor3:
    zoom 0.6 xalign 0.5 yalign 1.0
    easein 0.2 yalign 0.5 zoom 0.6
  "(Gah!{w} A {i}third{/i} time?!)" with small_shake
  dr "{i}Heated flooring.{/i} My job has always been stressful,{w=0.5} so I've always strived to maximize comfort wherever I could."

  show bg corridor3:
    zoom 0.6 yalign 0.5 xalign 0.5
    ease 4 zoom 1.7 xalign 0.3 yalign 0.5

  pause 4
  hide bg corridor3
  show drdanger smirk at crt
  show crt
  show drdangerframe at bg
  with dissolve 

  drs "When your work is done,{w=0.1} you can sleep here all you like."
  drs "But before then,{w=0.1} you've got dishes to clean,{w=0.1} washes to run,{w=0.1} bedrooms to vacuum..."
  show drdanger sidestare
  drs "...and of course,{w=0.1} Cautionne to take care of."
  drs "He represents a unique challenge,{w=0.1} I know."
  show drdanger smirk
  drs "But you wouldn't have gotten this far if you and I didn't believe you could do it."
  show drdanger stare
  drs "While I'm away on business,{w=0.1} it's important that you keep him on his daily routine."
  drs "7am to 9pm –{w=0.5} regularity is key."
  drs "Remember that all his dietary habits,{w=0.1} health regimens{w=0.1} and study exercises{p=0.5}{nw}"
  drs "are detailed in the files that we went over together."
  show drdanger sidestare
  drs "I apologize if you'll have to decrypt them again,{w=0.1} but..."
  drs "...Cautionne and I have made a habit of hiding our tracks for good reason."
  show drdanger smirk
  drs "And when the day is over,{w=0.1} feel free to play games, watch movies or read comics together. "
  drs "If you need a suggestion..."
  drs "...Cautionne told me that he loves the \"Cantaloupe Mall\" course on \"Marco Kart\"."
  show drdanger sidestare
  drs "...I might be pronouncing that wrong,{w=0.1}  but he'll know what you mean."
  show drdanger stare
  drs "So, take care."
  drs "If things go smoothly,{w=0.1} I'll be back for him in a week."
  show drdanger sidestare
  drs "And if things {i}don't{/i}{i} {/i}go smoothly..."
  show drdanger sidestare silent
  pause 1
  show drdanger stare speaking
  drs "Well,{w=0.1} there are systems in place that will guide you on what to do."
  drs "That's all for now.{w=0.5} Goodbye."
  show drdanger tender
  drs "And thank you for taking care of my..."
  show drdanger tender silent
  pause 1
  #"{b}[{/b}{b}Dr.{/b}{b} Danger pauses, and her expression changes – showing {/b}{b}she's{/b}{b} {/b}{b}hold{/b}{b}ing something back]{/b}"
  show drdanger sidestare speaking
  drs "{size=-13}Note to self,{w=0.1} re-record instructions at earliest convenience.{/size}"
  drs "{size=-13}Try not to be so ominous next time.{/size}"
  show drdanger sidestare silent
  pause 0.5
  hide drdanger sidestare silent
  hide crt
  with screenoff
  pause 1
  scene bg corridor3 with fade:
    zoom 0.5 align (0.5,0.5)
  pause 1

  pause 1
  "(That message wasn't for you,{w=0.1} and it wasn't for one of Dr. Danger's goons either.)"
  "(But a {i}babysitter?{/i}{w} {i}Really?{/i})"
  "(Who in the world would be qualified to babysit {i}him?{/i})"
  "(...)"
  pause 1
  "(...C'mon.{w} Just focus on the task at hand.)"

  scene bg corridor3:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 4 zoom 1.0
  pause 2
  scene black with fade
  pause 1
  show bg room3_downstairs with placeintro:
    zoom 0.6 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0

  pause 5

  show bg room3_downstairs with dissolve:
    zoom 0.4 yalign 0.7
  #"{b}[pause, walking sounds play as the player goes to room 3]{/b}"
  "(It's...{w=0.5} a normal apartment?)"
  "(There's a kitchenette,{w=0.5} a dining table,{w=0.5} a small sitting area...)"
  "(...and stairs.{w} Probably a bedroom up there.)"
  pause 0.5
  "(Are you {i}supposed{/i} to be here?)"
  #"[pause – the locked door handle sound is heard]"
  pause 1
  "(Guess you are.)"

  show bg room3_downstairs:
    zoom 0.4 
    ease 5 zoom 0.34 xalign 0.0 yalign 0.0

  pause 5
  call screen room3 with dissolve