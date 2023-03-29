label post_room_2:

  screen nodismiss(): #Our screen, while it is visible, no one can dismiss anything at all
      key "dismiss" action NullAction()

  #"{b} [The TV {/b}{b}isn't{/b}{b} on yet]{/b}"
  "(No message from the kid yet.)"
  "(Maybe if you're stealthy,"
  show screen nodismiss
  play sound "audio/sfx/Walking Footsteps 2.ogg"
  queue sound "audio/sfx/Walking Footsteps 2.ogg"

  show bg room2:
    zoom 0.34 align (0.0,0.0)
    ease 8 zoom 0.8 xalign 0.8 yalign 0.5
  extend "{cps=20} you could sneak past{/cps}{cps=10} without being subjected to{/cps} {cps=6}another one of his-){/cps}{nw}"
  #"{b}[{/b}{b}pasue{/b}{b} as the TV TURNS ON and cautionne appears]{/b}"
  play sound "audio/sfx/TV On 1.ogg"
  queue sound "audio/sfx/staticshort.ogg"
  show cautionne hairtwirl
  show crt
  show cautionne_frame_glow at bg
  with vpunch
  hide screen nodismiss
  voice "audio/voice/cautionne/postroom/Cautionne_Post Room 2-01.ogg"
  c "{i}Snooping as usual,{w=0.1} {/i}I see?"
  "(...You spoke too soon.)"
  show cautionne lean eyeclosed
  c "Yeah,{w=0.1} you're right in your element,{w=0.1} huh? "
  show cautionne lean speaking
  c "Not that {i}you'd{/i} know it,{p=0.5}{nw}"
  show cautionne lean eyeclosed
  extend "but I've got a good eye for this kind of thing!"
  c "I bet you've got that bubbly feeling buzzing under your skin..." 
  show cautionne lean speaking
  c "Like sweet,{w=0.1} sparkling limonata in your veins?"
  "(What a colorful turn of phrase.)"
  show cautionne lean eyeclosed
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
  c "I'd give my right arm to feel as excited as you do now,{w=0.1} lab rat!"
  c "You must be {i}salivating {/i}at the mountain of evidence beneath your fingertips. "
  c "Weapons,{w=0.1} corkboards,{w=0.1} secret evil notes..."
  show cautionne hairtwirl
  c "All the classics are here,{p=0.5}{nw}"
  c "and {i}we both know{/i} you know you want to rub your grubby paws all over them."
  show cautionne think
  c "Even if you copied half of one blueprint onto a bar napkin{p=0.5}{nw}"
  c "and threw it through the washing machine,{p=0.5}{nw}"
  c "you'd {i}still{/i} have enough evidence to net you a promotion from HQ."
  show cautionne lean speaking
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Well Then.ogg"
  c "So, go ahead!{w=0.5} Take as much as you like!"
  show cautionne lean eyeclosed
  c "I won't touch a hair on your head."
  show cautionne hairtwirl
  c "After all,{w=0.1} The Great Cautionne,{w=0.05} Emperor of MalViolence,{p=0.5}{nw}"
  c "knows that you only care about the truth."
  show cautionne lean eyeclosed
  c "He shall let you indulge."

  show cautionne leaneyeclosed pause
  pause 1
  c "..."
  show cautionne lean frown
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
  c "Hey lab rat.{w=0.5} Can I ask you something?"
  c "You {i}are {/i}just getting evidence,{w=0.1} right?"
  if len(room2["investigated"]) == 5:
    "(...Does he not approve of your investigation style?)"
    "(You're being thorough,{w=0.1} just to be cautio-){p=0.5}{nw}"
    pause 1
    "({i}...You're just being thorough.{/i})"
  elif len(room2["investigated"]) == 0:
    "(You're sticking to the mission objective,{w=0.1} just as you're trained to do.)"
    "(He's calling the shots right now -{w=0.1}  but if you stay focused,{w=0.1} he'll run out of rooms.)"
    "(Then,{w=0.1} you'll have the chance to close this case for good.)"
  else:
    "(First, he holds you prisoner.{w} Now, he complains about how much you look around?)"
    "(Well, {i}screw him.{/i}{w} You'll snoop as much or as little as you please.)"
  show cautionne serious
  c "I've watched you with my drones..."
  c "Tailored these puzzles to your specific,{w=0.1} sub-par problem-solving skills..."
  c "Carried out quasi-legal research..."
  show cautionne lean frown
  c "So,{w=0.1} I know what you are."
  c "You're an agent for STOP...{w=0.5} nothing more,{w=0.1} nothing less."
  c "...Am I right?"

  show cautionne leanfrown pause
  pause 1
  show cautionne serious
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
  c "{i}Again{/i} with the silent treatment."
  show cautionne lean frown
  c "I've met {i}vending machines{/i} with better social skills than you,{w=0.1} you know that?"
  show cautionne serious
  c "...Fine. "
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Shut Up 2.ogg"
  extend annoyed hands "{i}FINE!{/i}" with small_shake
  c "The next time you escape,{w=0.1} {i}I won't talk either!{/i}"
  c "See how YOU like it!!"
  show cautionne block
  c "Now, MOVE!{w=0.5} Or you'll be {i}fatally {/i}late for your next staring contest."
  show cautionne blockscreen silent
  pause 0.1

  play sound "audio/sfx/TV Off 1.ogg"
  scene black
  hide cautionne blockscreen silent
  hide cautionne_frame_glow
  hide crt
  show cautionne_frame_noglow:
    zoom 0.5
  with screenoff
  pause 1

  show bg room2 with fade:
    zoom 0.8 align (0.8,0.5)
  pause 1



  jump dr_danger_3