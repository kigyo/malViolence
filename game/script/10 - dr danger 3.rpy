label dr_danger_3:
  scene bg room2 at bg with eyeclose
  "(...Again with the temper tantrum, huh.)"
  "(Seriously, why's he so pissed off at you?)"
  "(He and Dr. Danger have fought against STOP field agents in the past, but that's not your department.)"
  "(What right does he have to act all high and mighty towards {i}you?{/i})"
  "(...)"
  "(Right - {i}supervillain.{/i} Big ego, no self-awareness. Don't overthink it)"
  scene bg corridor3 at bg(0.6) with wipeleft
  "(...The dim corridor stretches before you, with no answers to offer.)"
  "(Yes, it's darker here - but not in an unpleasant way. It's warmer than the previous rooms, literally and figuratively.)"
  "(The wooden floorboards and the decorated wallpaper feel... welcoming. Nostalgic, even.)"
  "(If you viewed this hall alone, you'd assume it'd belong to a family household. Not to a scheming terrorist and her kooky sidekick.)"
  "(It's been a very long... day? Hard to tell how much time has passed.)"
  "(The gentle heat tempts you to sit down on the floor. Or maybe lie down.)"
  pause 1
  "(Um... Would Cautionne allow you to take a quick breather?)"
  scene bg corridor3:
    zoom 0.6 xalign 0.5 yalign 0.5
    easeout 1 yalign 1.0 zoom 0.6
  #"{b}[animate camera movements to simulate the protagonist slowly crouching down to the floor] {/b}"
  "(If he meant what he said about not harming a hair on your head, then maybe the smart thing to do would be to-)"
  dr "Very tempting for a wooden floor, isn't it?"
  scene bg corridor3:
    zoom 0.6 xalign 0.5 yalign 1.0
    easein 0.3 yalign 0.5 zoom 0.6
  "(Gah! A third time?!)" with small_shake
  dr "{i}Heated flooring.{/i} My work has always been stressful, so I've always strived to maximize comfort wherever I could."
  dr "Of course, when your work is done, you can sleep here all you like. But before then, you've got dishes to clean, washes to run, bedrooms to vacuum..."
  dr "...and of course, Cautionne to take care of."
  dr "He represents a unique challenge, I know. But you wouldn't have gotten this far if you and I didn't believe you could do it."
  dr "While I'm away on business, it's important that you keep him on his daily routine. 7am to 9pm – regularity is key."
  dr "Remember that all his dietary habits, health regimens and study exercises are detailed in the files that we went over together."
  dr " I apologize if you'll have to decrypt them again, but... Cautionne and I have made a habit of hiding our tracks for good reason."
  dr "And when the day is over, feel free to play games, watch movies or read comics together. "
  dr "If you need a suggestion, Cautionne told me that he loves the \"Cantaloupe Mall\" course on \"Marco Kart\"."
  dr "...I might be pronouncing that wrong, but he'll know what you mean."
  dr "So, take care. If things go smoothly, I'll be back for him in a week."
  dr "And if things {i}don't{/i}{i} {/i}go smoothly... Well, there are systems in place that will guide you on what to do."
  dr "That's all for now. Goodbye."
  dr "And thank you for taking care of my..."
  pause 1
  #"{b}[{/b}{b}Dr.{/b}{b} Danger pauses, and her expression changes – showing {/b}{b}she's{/b}{b} {/b}{b}hold{/b}{b}ing something back]{/b}"
  dr "{size=-3}Note to self, re-record instructions at earliest convenience. Try not to be so ominous, next time.{/size}"
  scene bg corridor3 at bg with eyeclose
  "(That message wasn't for you, and it wasn't for one of Dr. Danger's goons either.)"
  "(But a babysitter? {i}Really?){/i}"
  "(Who in the world would be qualified to babysit {i}him?{/i})"
  "(...)"
  "(No one, apparently.)"
  "(...C'mon. Just focus on the task at hand.)"
  #"{b}[pause, walking sounds play as the player goes to room 3]{/b}"
  scene bg room3_downstairs at bg(0.35) with wipeleft
  "(It's... a normal apartment?)"
  "(There's a kitchenette, a dining table, a small sitting area...)"
  "(...and stairs. Probably a bedroom up there.)"
  "(Are you supposed to be here?)"
  #"[pause – the locked door handle sound is heard]"
  pause 1
  "(Guess you are.)"
  call screen room3 with dissolve