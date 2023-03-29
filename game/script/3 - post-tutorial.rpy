label post_tutorial:
  #[If puzzle is solved, play a solving/unlocking sound]
  play sound "audio/sfx/Door Unlock 1.ogg"
  pause 1
  play sound "audio/sfx/staticshort.ogg"
  scene black 
  show cautionne_frame_glow at bg
  with dissolve
  show cautionne annoyed behind cautionne_frame_glow at crt
  show crt behind cautionne_frame_glow
  with screenon
  voice "audio/voice/cautionne/posttutorial/Cautionne_Post Tutorial-01.ogg"
  #"{b}[static as {/b}{b}Cautionne{/b}{b} gets back on screen. {/b}{b}Maybe an{/b}{b} ATL animation that makes it look like his CRT screen's turning on again?]{/b}
  c "{size=+35}{i}WHAT?!?{/i}{/size}" with small_shake
  voice "audio/voice/cautionne/posttutorial/Cautionne_Post Tutorial-02.ogg"
  c "How the {i}hell{/i} did you break the lock? "
  c nohands "There's no way you could've-"
  c "...gotten out on..."
  c oops "...your own."
  c "..."
  c "..."
  c "..."
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
  c serious "Oi.{w=0.5} Lab-rat."
  c "I can {i}see {/i}you,{w=0.1} y'know. "
  c "You're just like the rest of those STOP freaks."
  c "So textbook authoritarian they could use you for their recruitment posters."
  c "That blank stare,{w=0.1} that bland uniform,{w=0.1} that world-class poker face... "
  c "...makes me wanna peel your brain like an orange."
  c"{size=-15}God knows what sick and twisted thoughts lurk beneath.{/size}"
  "(Is he telling you to smile more?)"
  "(He is, {w=0.1}isn't he? {w}Guess you'll give him the ol' \"passport photo.\")"
  #"{b}[pause as {/b}{b}Cautionne{/b}{b} looks surprised, before going back to his smug look]{/b}"
  c "...Heh. "
  c "You're cute."

  show cautionne lean eyeclosed

  extend " {i}Real{/i} cute."

  c "I'll forgive you for that."
  c "After all,{w=0.1} I'm the {i}Great Cautionne, Emperor of MalViolence{/i}."
  c "I'm not the type of man to go all-out on a scrub like yourself."
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Hmph!.ogg"
  c serious "But alas,{w=0.1} even my {i}limitless{/i} generosity has an expiration date."
  c "And you're creeping up fast on the \"Sell-By.\""

  show cautionne serious pause
  pause 1

  c lean "...Anyhoo,{w=0.1} you {i}do{/i} want to escape, don't you?"
  voice "audio/voice/cautionne/soundbites/Effected/Cautionne_SBE-Well Then.ogg"
  c "Well, then."
  c lean eyeclosed "Allow me to give you a final pearl of wisdom..."

  show cautionne leaneyeclosed pause

  pause 1
  voice "audio/voice/cautionne/posttutorial/Cautionne_Post Tutorial-03.ogg"
  c lean frown "Stop making mistakes."
  voice "audio/voice/cautionne/posttutorial/Cautionne_Post Tutorial-04.ogg"
  c "Because the next time you screw up,{w=0.5} {i}you're not gonna like what happens next.{/i}"

  show cautionne leanfrown pause
  pause 0.1
  play sound "audio/sfx/TV Off 1.ogg"
  hide cautionne leanfrown pause
  hide cautionne_frame_glow
  hide crt
  show cautionne_frame_noglow:
    zoom 0.5
  with screenoff


  pause 1
  jump dr_danger_1