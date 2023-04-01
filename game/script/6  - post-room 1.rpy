label post_room_1:
  $renpy.block_rollback()
  $ inspect = "post room"
  #"{b}[pause as the microphone turns on and {/b}{b}cautionne{/b}{b} appears on the screen]{/b}"

#### confirmation sound - yay, you won room 1!

  stop music fadeout 1.0

  $ play_sound(roomsuccess)
  pause 2
  $ play_sound(doorunlock)
  pause 2

  scene black
  show cautionne_frame_noglow:
    zoom 0.5
  with fade
  pause 1
  
  $ queue_sound([staticshort, tvon])
  pause 0.4

  show cautionne hairtwirl at crt
  show crt
  show cautionne_frame_glow at bg
  with screenon
  $ play_music(cautionnetheme)
  voice "audio/voice/cautionne/postroom/Cautionne_Post Room 1-01.ogg"
  c "Well, well, well.{w=0.036} If it isn't the {i}lab rat{/i}."
  c "For someone with chronic resting-{i}blah{/i}-face,{w=0.1} you look {i}real{/i} proud of yourself."
  show cautionne lean speaking
  c "And you know what?{w=0.5} You should be. "
  c "By getting {i}this {/i}far,{w=0.1} you're statistically proven to have more brains than 96\% of STOP employees."
  show cautionne lean eyeclosed
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
  c "So congrats!"
  show cautionne leaneyeclosed pause
  pause 1
  show cautionne think
  c "...That said,{w=0.1} I actually expected you to die by now."
  c "I'm not sure how to reward you for your success..."
  show cautionne lean speaking
  stop music fadeout 1.0
  c "Ooh —{w=0.1} wait,{w=0.1} wait.{w=0.5} I have an idea!"
  show cautionne lean eyeclosed
  c "How about a sticker?"
  c "If you get out of here,{w=0.1} I'll give you a fruit-scented one!"
  if len(room1_investigated) == 3:
    show cautionne lean speaking
    c "At the rate you're going,{w=0.1} you might even get one of my {cps=20}suuuuuuuper{/cps} special grape stickers."
    show cautionne lean eyeclosed
    c "And I {i}never{/i} give those out."
    show cautionne leaneyeclosed pause
    pause 1
    show cautionne think
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    c "Huh.{w=0.5} I don't see you jumping for joy."
    c "Not a grape fan?"
  elif len(room1_investigated) == 0:
    show cautionne lean frown
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    c "But at the rate you're going...{w=0.5} Oof."
    c "You might not even deserve the {i}durian-scented{/i} one. "
    show cautionne lean speaking
    c "Hey,{w=0.1} maybe you're just terminally un-curious and a lifelong sticker-hater."
    show cautionne lean eyeclosed
    c "No shame in being a hater, though.\n{w=0.5}I hate things 24/7!"
    show cautionne leaneyeclosed pause
    pause 1
    show cautionne serious
    c "{size=-13}...Not even gonna deny that, huh?{/size}"
  else:
    show cautionne lean speaking
    c "Though if you were expecting a grape-scented sticker,{w=0.1} you're outta luck."
    show cautionne lean eyeclosed
    c "I slap the best ones all over my tech!"
    show cautionne leaneyeclosed pause
    pause 1
    show cautionne think
    voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
    c "Huh.{w=0.5} You're not smiling or anything."
    c "Not a sticker superfan?"
  show cautionne lean eyeclosed
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Well Then.ogg"
  $ play_music(cautionnetheme, fadein=1.0, fadeout=0.1)
  c "Oh well.{w=0.5} More for me! "
  show cautionne leaneyeclosed pause
  if len(room1_investigated) == 0:
    show cautionne lean frown
    c "{size=-13}Even the durian-scented ones.{/size}"
    show cautionne leanfrown pause

  pause 1
  show cautionne hairtwirl
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hey Lab Rat.ogg"
  c "So,{w=0.1} what did you think of our—{p=0.5}{nw}"
  c "{i}—my{/i} Research Lab?"
  show cautionne lean speaking
  c "It's awesome,{w=0.1} isn't it?"
  show cautionne think
  c "A little \"derivative\", maybe..."
  show cautionne lean speaking
  c "...but any scientist worth their salt \nneeds a room filled with{p=0.5}{nw}"
  c "hi-tech computers and big fat source libraries."
  show cautionne lean eyeclosed
  c "Though,{w=0.1} there is {i}one{/i} thing that makes my lab better than the others."
  show cautionne hairtwirl
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
  c "My {i}Primary Source Extractor!{/i}"
  show cautionne think
  c "It's kinda loud once it revs up,{w=0.1} and it's a pain to clean afterwards."
  show cautionne lean speaking
  c "But the results are...\n"
  show cautionne lean eyeclosed
  extend "{i}mwah!{/i} {w=0.5}{i}Ah-{w=0.1}mazing!{/i}"
  show cautionne think
  c "I {i}had {/i}planned on giving you a first-hand demonstration..."
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmm.ogg"
  show cautionne oops
  c "...but the last experiment got so messy that I'm still cleaning the rafters."
  show cautionne lean eyeclosed
  c "Disappointing,{w=0.1} I know. "
  c "But never fear!"
  show cautionne hairtwirl
  c "The Great Cautionne,{w=0.1} Emperor of MalViolence,{p=0.5}{nw}" 
  c "used his aptitude for adaptation to his advantage."
  show cautionne lean speaking
  c "And so,{w=0.1} he constructed these quasi-deadly puzzle rooms,{p=0.5}{nw}"
  c "sure to satisfy even the least imaginative of STOP agents."
  show cautionne lean eyeclosed
  c "Aren't I thoughtful,{w=0.1} lab rat?"
  show cautionne leaneyeclosed pause
  pause 1
  show cautionne lean frown
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
  c "{size=-13}{i}...Yeesh,{/i}{w=0.1} tough crowd.{/size}"
  c "{size=-13}You must be fun at parties.{/size}"
  show cautionne hairtwirl
  c "Anyway,{w=0.1} enough dilly-dallying! "
  c "{i}Vamoose{/i} to the next room already.{w=0.5} There's more games for you to play!"
  c "Or {i}hell{/i},{w=0.1} take your sweet time."
  show cautionne laugh
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hehehehehe.ogg"
  c "I've {i}always{/i} wanted to see how motivating electrified floors can be!"
  "(He's clearly joking again.)"
  pause 1
  "(Probably.)"
  pause 1
  "(...Maybe.)"
  pause 1
  "(...No.{w} Better not tempt fate.)"

  stop music 

  $ play_sound(tvoff)
  hide cautionne laugh
  hide cautionne_frame_glow
  hide crt
  show cautionne_frame_noglow:
    zoom 0.5
  with screenoff
  pause 2

  show bg room1 with fade:
    zoom 0.4 yalign 0.7

  pause 1

  $ play_sound(footsteps4)

  show bg room1:
    zoom 0.4 yalign 0.7
    ease 4 zoom 0.8 xalign 0.15 yalign 0.65

  pause 4

  jump dr_danger_2