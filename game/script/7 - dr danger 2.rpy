label dr_danger_2:
  #"{b}[pause as {/b}{b}Cautionne's{/b}{b} screen shuts off, and walking sounds are heard – showing the player move to the next corridor]{/b}"
  scene bg corridor2 at bg with wipeleft
  "(...)"
  "(This self-styled supervillain has got world-class bad manners. Where could he have picked up such a nasty personality, anyway?)"
  "(You know it's pointless to speculate, but you can't help it. Your current surroundings are... unusually ordinary.)"
  pause 1
  "(The last corridor looked straight out of a sci-fi movie. This one's practically mundane. It's got more in common with a basic STOP research building.)"
  "(It brings back memories of your days as low-level agent, trudging through monochromatic halls, delivering low-level intel to low-level research assistants.)"
  "(Your supervisor loved emphasizing the \"low-level\" part.)"
  "(Pressing your keycard to the reader, hearing that little \"beep\" of approval, seeing the doors click open...)"
  "(...Waking up in a mad scientist's research facility has a way of making you long for the simple life.)"
  pause 1
  #"{b}[pause – maybe a camera movement panning across the doors?]{/b}"
  "(Speaking of doors... this corridor's got five to choose from.)"
  "(You pause. Once again, your fate is in your own hands.)"
  "(Is this {i}another {/i}one of his puzzles?)"
  "???" "Good. You made it through the experiment room."
  "(?!)" with small_shake
  "(Dr. Danger's on again! What did you-)"
  "(No, no - calm down. It's probably motion-activated.)"
  "(You should've listened to the last recording, since it seemed pretty helpful. This time, you'll stay still and pay attention!)"
  dr "I apologize for any distress that the previous room may have caused you. "
  dr "For whatever it's worth, please know that I do not take pleasure in hurting others. The sight of blood makes me quite ill."
  dr "It always has."
  dr "No, that room belongs to my apprentice."
  dr "Currently, he is running an experiment - even if he seems more interested in the process than the results."
  dr "Honestly, I'm in no position to lecture him. He's not cruel, he's just..."
  pause 1
  dr "...I suppose I can say this."
  dr "All his test subjects have a certain unfortunate commonality. A {i}terminal {/i}condition, as he sees it, that makes it very difficult for him to... remain impartial."
  dr "I apologize for being vague here, but this is a subject that has, and will continue to, remain between me and him. "
  dr "It's not your responsibility. It's mine."
  "(What's that supposed to mean?)"
  dr "If you're looking for where to go next, please take the door directly in front of you.  The other doors are very much best left shut."
  dr "Take care, now. I'll see you in a week."
  #"{b}[{/b}{b}dr.{/b}{b} danger shuts off her recording]{/b}"
  pause 1
  "(That recording {i}definitely{/i} wasn't for you.)"
  "(Whoever the intended recipient was, Dr. Danger clearly trusted them.)"
  "(Better take the door she recommended.)"
  #"{b}[the door in front has an opening sound, and the {/b}{b}bg{/b}{b} changes to room 2]{/b}"
  scene bg room2 at bg with wipeleft:
    xalign 1.0
    linear 5 xalign 0.0
  "(An office...)"
  "(There's shelves everywhere. Loads of files, too.)"
  "(Like the hall before it, it's... oddly ordinary.)"
  scene bg room2 at bg:
    xalign 0.0
    ease 3 xalign 1.0
  "(Just to double check, though...)"
  pause 1
  #"{b}[pause - a locked door handle sound {/b}{b}plays{/b}{b}]{/b}"
  scene bg room2 at bg:
    xalign 1.0
    ease 2 xalign 0.5
  "(...Yup. This is the next puzzle room.)"
  "(Alright, then. Let's get searching.)"
  scene bg room2:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 2 zoom 0.35 yalign 0.0 xalign 0.0
  pause 2
  call screen room2 with dissolve