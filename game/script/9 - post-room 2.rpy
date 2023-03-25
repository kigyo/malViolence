label post_room_2:
  #"{b} [The TV {/b}{b}isn't{/b}{b} on yet]{/b}"
  $Achievement.add(achievement_room2)
  "(No message from the kid yet.)"
  "(Maybe if you're stealthy, you could sneak past without being subjected to another one of his-)"
  #"{b}[{/b}{b}pasue{/b}{b} as the TV TURNS ON and cautionne appears]{/b}"
  show cautionne laugh
  show crt
  show cautionne_frame_glow at bg
  with dissolve
  c "{i}Snooping as usual, {/i}I see?"
  "(...You spoke too soon.)"
  c "Yeah, you're right in your element, huh? "
  c "Not that you'd know it from looking at your face, but I've got a good eye for this kind of thing!"
  c "I bet you've got that bubbly feeling buzzing under your skin... Like sweet, sparkling Limonata in your veins?"
  "(What a colorful turn of phrase.)"
  c "I'd give my right arm to feel as excited as you do now, lab rat!"
  c "You must be {i}salivating {/i}at the mountain of evidence beneath your fingertips. "
  c "Weapons, corkboards, secret evil notes... All the classics are here, and {i}we both know{/i} you know you want to rub your grubby paws all over them."
  c "Even if you copied half of one blueprint onto a bar napkin and threw it through the washing machine, you'd still have enough evidence to net you a promotion from HQ."
  c "So, go ahead! Take as much as you like! I won't touch a hair on your head."
  c "After all, The Great Cautionne, Emperor of MalViolence, knows that you only care about the truth. He shall let you indulge."
  pause 1
  c "..."
  c "Hey lab rat. Can I ask you something?"
  c "You {i}are {/i}just getting evidence, right?"
  if len(room2["investigated"]) == 5:
    "(...Does he not approve of your investigation style?)"
    "(You're being thorough, just to be cautio-)"
    "({i}...You're just being thorough.{/i})"
  elif len(room2["investigated"]) == 0:
    "(You're sticking to the mission objective, just as you're trained to do.)"
    "(He's calling the shots right now - but if you stay focused, he'll run out of rooms.)"
    "(Then, you'll have the chance to close this case for good.)"
  else:
    "(First, he holds you prisoner. Now, he complains about how much you look around?)"
    "(Well, screw him. You'll snoop as much or as little as you please.)"
  c "I've watched you with my drones... Tailored these puzzles to your specific, sub-par problem-solving skills... Carried out quasi-legal research..."
  c "So, I know what you are. You're an agent for STOP... nothing more, nothing less."
  c "...Am I right?"
  pause 1
  c "{i}Again{/i} with the silent treatment. I've met vending machines with better social skills than you, you know that?"
  c "...Fine. "
  extend annoyed hands "{i}FINE!{/i}" with small_shake
  c "The next time you escape, I won't talk either! See how YOU like it!!"
  c "Now, MOVE! Or you'll be {i}fatally {/i}late for your next staring contest."
  jump dr_danger_3