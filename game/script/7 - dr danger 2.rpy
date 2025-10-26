label dr_danger_2:

  scene black with fade
  $ play_sound(creakyvent)
  pause 2
  show bg corridor2 tvoff with placeintro:
    zoom 0.8 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0
  $ Achievement.add(achievement_room1)
  $ play_sound(metaldoorclose)
  #"{b}[pause as {/b}{b}Cautionne's{/b}{b} screen shuts off, and walking sounds are heard – showing the player move to the next corridor]{/b}"
  "(...)"
  "(This self-styled supervillain has got {i}world-class{/i} bad manners.)"
  "(Where could he have picked up such a nasty personality,{w=0.1} anyway?)"
  "(You know it's pointless to speculate,{w=0.1} but you can't help it..."
  pause 0.5

  show bg corridor2 tvoff with dissolve:
    align (0.5,0.5) zoom 0.5

  "...because your current surroundings are...{w=0.5} unusually ordinary.)"
  pause 0.5
  "(The last corridor looked straight out of a sci-fi movie.{w} This one's practically mundane.)"
  "(It's got more in common with a basic STOP research building.)"
  "(It brings back memories of your days as a low-level agent,{w=0.1} trudging through halls,{w=0.1} delivering low-level intel to low-level researchers.)"
  "(Your supervisor loved emphasizing the \"low-level\" part.)"
  "(Pressing your keycard to the reader,{w=0.1} hearing that little \"beep\" of approval,{w=0.1} seeing the doors click open...)"
  pause 0.5
  "(...Waking up in a mad scientist's research facility has a way of making you long for the simple life.)"
  pause 1
  #"{b}[pause – maybe a camera movement panning across the doors?]{/b}"
  "(Speaking of doors...{w=0.5} this corridor's got five to choose from.)"
  "(You pause.{w} Once again,{w=0.1} your fate is in your own hands.)"
  "(Is this {i}another{/i} one of his puzzles?)"
  $ play_sound(staticshort)
  show bg corridor2
  pause 0.5
  voice "audio/voice/dr.danger/Danger_Corridor2-01.ogg"
  dr "Good. {w=0.559}You made it through the experiment room."
  "(?!)" with small_shake
  "(Dr. Danger's on again!{w} What did you—){w=1}{nw}"
  "(No,{w=0.1} no{w=0.1} — calm down.{w} It's probably motion-activated.)"
  "(You should've listened to the last recording,{w=0.1} since it seemed pretty helpful.{w} This time,{w=0.1} you'll stay still and pay attention!)"

  $ play_sound(footsteps2)

  show bg corridor2:
    zoom 0.5 yalign 0.5 xalign 0.5
    ease 4 zoom 1.5 xalign 0.1 yalign 0.4

  pause 4
  hide bg corridor2
  show drdanger stare at crt
  show crt
  show drdangerframe at bg
  with dissolve 

  pause 1
  voice "audio/voice/dr.danger/Danger_Corridor2-02.ogg"
  drs "I apologize for any distress that the previous room may have caused you. "
  voice "audio/voice/dr.danger/Danger_Corridor2-03.ogg"
  drs "For whatever it's worth,{w=0.359} please know that I do not take pleasure in hurting others.{w=3}{nw}"
  voice sustain
  drs "The sight of blood makes me quite ill."
  show drdanger sidestare
  voice "audio/voice/dr.danger/Danger_Corridor2-04.ogg"
  drs "{size=-13}It...{w=0.503} always has.{/size}"
  pause 0.5
  show drdanger stare
  $ play_music(backstorytheme, fadein=1.0, fadeout=1.0)
  voice "audio/voice/dr.danger/Danger_SB-Allow Me To Explain.ogg"
  drs "No,{w=0.1} {i}that{/i} room belongs to my apprentice."
  drs "Currently,{w=0.1} he is running an experiment —{w=1.25}{nw}"
  show drdanger sidestare
  drs "even if he seems more interested in the process than the results."
  voice "audio/voice/dr.danger/Danger_SB-Sigh.ogg"
  drs "Honestly,{w=0.1} I'm in no position to lecture him."
  drs "He's not cruel,{w=0.1}  he's just..."
  show drdanger sidestare silent
  pause 1
  show drdanger stare speaking
  voice "audio/voice/dr.danger/Danger_SB Please Listen Carefully.ogg"
  drs "...I suppose I can say this."
  drs "All his test subjects have a certain {i}unfortunate commonality.{/i}"
  drs" A {i}terminal {/i}condition, as he sees it...{w=1.25}{nw}"
  drs "...that makes it very difficult for him to...{w=0.5} {i}remain impartial.{/i}"
  voice "audio/voice/dr.danger/Danger_SB-I Apologize.ogg"
  drs "I apologize for being vague here."
  drs "But the nature of this work has always been a...{w=0.5} private matter."
  show drdanger sidestare
  drs "It's not your responsibility.{w=0.5} It's mine."
  "(What's that supposed to mean?)"
  show drdanger sidestare silent

  stop music fadeout 1.0
  pause 1
  show drdanger stare speaking
  voice "audio/voice/dr.danger/Danger_Corridor2-05.ogg"
  drs "If you're looking for where to go next,{w=0.065} please take the door directly in front of you.{w=3}{nw}"
  show drdanger sidestare
  voice sustain
  drs "The other doors are very much {i}best left shut.{/i}"
  show drdanger stare
  voice "audio/voice/dr.danger/Danger_Corridor2-06.ogg"
  drs "Take care, now.{w=0.389} I'll see you in a week."
  #"{b}[{/b}{b}dr.{/b}{b} danger shuts off her recording]{/b}"

  show drdanger stare silent
  pause 1
  $ play_sound(tvoff)
  hide drdanger stare silent
  hide crt
  show drdangerframe off
  with screenoff
  pause 2
  scene bg corridor2 tvoff with fade:
    zoom 0.5 align (0.5,0.5)
  pause 2

  "(That recording {i}definitely{/i} wasn't for you.)"
  "(Whoever the intended recipient was,{w=0.1} Dr. Danger clearly trusted them.)"
  "(Better take the door she recommended.)"
  #"{b}[the door in front has an opening sound, and the {/b}{b}bg{/b}{b} changes to room 2]{/b}"
  $ play_sound(footsteps2)
  scene bg corridor2 tvoff:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 4 zoom 1.5 yalign 0.55
  pause 4
  scene black with fade
  $ play_sound(dooropen)
  pause 3
  show bg room2 with placeintro:
    zoom 0.6 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0

  pause 5
  show bg room2 with dissolve:
    zoom 0.4 yalign 0.7
  $ play_sound(doorclose)
  pause 1
  "(An office...)"
  "(There's shelves everywhere.{w} Loads of files,{w=0.1} too.)"
  "(Like the hall before it,{w=0.1} it's...{w=0.5} oddly ordinary.)"
  "(Just to double check,{w=0.1} though...)"
  $ play_sound(footsteps2)
  show bg room2:
    zoom 0.4 yalign 0.7
    ease 4 zoom 0.8 xalign 0.8 yalign 0.65
  pause 4
  $ play_sound(doorlock)
  pause 1
  #"{b}[pause - a locked door handle sound {/b}{b}plays{/b}{b}]{/b}"
  "(...Yup.{w} Pretty sure this is another puzzle room.)"
  "(Alright,{w=0.1} then.{w} Let's get searching.)"
  show bg room2:
    zoom 0.8 
    ease 5 zoom 0.335 xalign 0.0 yalign 0.0

  pause 5
  $ play_music(room2theme, fadein=1.0, fadeout=0.1)
  $ inspect = None
  call screen room2 with dissolve