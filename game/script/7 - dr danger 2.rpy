label dr_danger_2:

  scene black with fade
  pause 1
  show bg corridor2 with placeintro:
    zoom 0.8 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0
  #"{b}[pause as {/b}{b}Cautionne's{/b}{b} screen shuts off, and walking sounds are heard – showing the player move to the next corridor]{/b}"
  "(...)"
  "(This self-styled supervillain has got world-class bad manners.{w} Where could he have picked up such a nasty personality, anyway?)"
  "(You know it's pointless to speculate, but you can't help it..."
  pause 1

  show bg corridor2 with dissolve:
    align (0.5,0.5) zoom 0.5

  "...because your current surroundings are...{w=0.5} unusually ordinary.)"
  pause 1
  "(The last corridor looked straight out of a sci-fi movie.{w} This one's practically mundane.)"
  "(It's got more in common with a basic STOP research building.)"
  "(It brings back memories of your days as low-level agent,{w=0.1} trudging through monochromatic halls,{w=0.1} delivering low-level intel to low-level research assistants.)"
  "(Your supervisor loved emphasizing the \"low-level\" part.)"
  "(Pressing your keycard to the reader,{w=0.1} hearing that little \"beep\" of approval,{w=0.1} seeing the doors click open...)"
  "(...Waking up in a mad scientist's research facility has a way of making you long for the simple life.)"
  pause 1
  #"{b}[pause – maybe a camera movement panning across the doors?]{/b}"
  "(Speaking of doors...{w=0.5} this corridor's got five to choose from.)"
  "(You pause.{w} Once again, your fate is in your own hands.)"
  "(Is this {i}another{/i} one of his puzzles?)"
  pause 0.5
  dr "Good. {w=0.5}You made it through the experiment room."
  "(?!)" with small_shake
  "(Dr. Danger's on again!{w} What did you-)"
  "(No,{w=0.1} no{w=0.1} - calm down.{w} It's probably motion-activated.)"
  "(You should've listened to the last recording,{w=0.1} since it seemed pretty helpful.{w} This time, you'll stay still and pay attention!)"

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
  drs "I apologize for any distress that the previous room may have caused you. "
  drs "For whatever it's worth, please know that I do not take pleasure in hurting others."
  drs "The sight of blood makes me quite ill."
  show drdanger sidestare
  drs "It always has."
  show drdanger stare
  drs "No, {i}that{/i} room belongs to my apprentice."
  drs "Currently, he is running an experiment -{p=0.1}{nw}"
  show drdanger sidestare
  drs "even if he seems more interested in the process than the results."
  drs "Honestly,{w=0.1} I'm in no position to lecture him."
  drs "He's not cruel,{w=0.1}  he's just..."
  show drdanger sidestare silent
  pause 1
  show drdanger stare speaking
  drs "...I suppose I can say this."
  drs "All his test subjects have a certain {i}unfortunate commonality.{/i}"
  drs" A {i}terminal {/i}condition, as he sees it..."
  drs "...that makes it very difficult for him to...{w=0.5} {i}remain impartial.{/i}"
  drs "I apologize for being vague here."
  drs "But this is a subject that has,{w=0.1} and will continue to,{w=0.1} remain between me and him. "
  show drdanger sidestare
  drs "It's not your responsibility.{w=0.5} It's mine."
  "(What's that supposed to mean?)"
  show drdanger sidestare silent
  pause 1
  show drdanger stare speaking
  drs "If you're looking for where to go next,{w=0.1} please take the door directly in front of you."
  show drdanger sidestare
  drs "The other doors are very much best left shut."
  show drdanger stare
  drs "Take care, now. {w=0.5}I'll see you in a week."
  #"{b}[{/b}{b}dr.{/b}{b} danger shuts off her recording]{/b}"

  show drdanger stare silent
  pause 0.1
  hide drdanger stare silent
  hide crt
  with screenoff
  pause 1
  scene bg corridor2 with fade:
    zoom 0.5 align (0.5,0.5)
  pause 1

  "(That recording {i}definitely{/i} wasn't for you.)"
  "(Whoever the intended recipient was,{w=0.1} Dr. Danger clearly trusted them.)"
  "(Better take the door she recommended.)"
  #"{b}[the door in front has an opening sound, and the {/b}{b}bg{/b}{b} changes to room 2]{/b}"
  scene bg corridor2:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 4 zoom 1.0
  pause 2
  scene black with fade
  pause 1
  show bg room2 with placeintro:
    zoom 0.6 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0

  pause 5

  show bg room2 with dissolve:
    zoom 0.4 yalign 0.7

  "(An office...)"
  "(There's shelves everywhere.{w} Loads of files, too.)"
  "(Like the hall before it,{w=0.1} it's...{w=0.5} oddly ordinary.)"
  show bg room2:
    zoom 0.4 yalign 0.7
    ease 4 zoom 0.8 xalign 0.8 yalign 0.65
  "(Just to double check,{w=0.1} though...)"
  pause 1
  #"{b}[pause - a locked door handle sound {/b}{b}plays{/b}{b}]{/b}"
  "(...Yup.{w} This is the next puzzle room.)"
  "(Alright, then.{w} Let's get searching.)"
show bg room2:
  zoom 0.8 
  ease 5 zoom 0.34 xalign 0.0 yalign 0.0

pause 5
call screen room2 with dissolve