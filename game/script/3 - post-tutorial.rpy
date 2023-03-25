label post_tutorial:
  #[If puzzle is solved, play a solving/unlocking sound]
  $Achievement.add(achievement_tfng)
  scene black 
  show cautionne_frame_glow at bg
  with dissolve
  show cautionne annoyed behind cautionne_frame_glow at crt
  show crt behind cautionne_frame_glow
  with screenon
  #"{b}[static as {/b}{b}Cautionne{/b}{b} gets back on screen. {/b}{b}Maybe an{/b}{b} ATL animation that makes it look like his CRT screen's turning on again?]{/b}
  c "{size=+35}{i}WHAT?!?{/i}{/size}" with small_shake
  c "How the {i}hell{/i} did you break the lock? "
  c nohands "There's no way you could've-"
  c "...gotten out on..."
  c oops "...your own."
  c "..."
  c "..."
  c "..."
  c serious "Oi. Lab-rat."
  c "I can {i}see {/i}you, y'know. "
  c "You're just like the rest of those STOP freaks."
  c "So textbook authoritarian they could use you for their recruitment posters."
  c "That blank stare, that bland uniform, that world-class poker-face... "
  c "...makes me wanna peel your brain like an orange."
  c"{size=-15}God knows what sick and twisted thoughts lurk beneath.{/size}"
  "(Is he telling you to smile more?)"
  "(He is, {w=0.5}isn't he? {w}Guess you'll give him the ol' \"passport photo.\")"
  #"{b}[pause as {/b}{b}Cautionne{/b}{b} looks surprised, before going back to his smug look]{/b}"
  c "...Heh. "
  c "You're cute."

  show cautionne lean eyeclosed

  extend " {i}Real{/i} cute."
  c "I'll forgive you for that."
  c "After all, I'm the {i}Great Cautionne, Emperor of MalViolence{/i}."
  c " I'm not the type of man to go-all out on a scrub like yourself."
  c serious "But alas, even my {i}limitless{/i} generosity has an expiration date."
  c "And you're creeping up fast on the \"Sell-By.\""

  show cautionne serious pause
  pause 1

  c lean "...Anyhoo, you {i}do{/i} want to escape, don't you?"
  c "Well, then."
  c lean eyeclosed "Allow me to give you a final pearl of wisdom..."

  show cautionne leaneyeclosed pause

  pause 1

  c lean frown "Stop making mistakes."
  c "Because the next time you screw up, {w=0.5}{i}you're not gonna like what happens next.{/i}"

  show cautionne leanfrown pause
  pause 0.1
  hide cautionne leanfrown pause
  hide cautionne_frame_glow
  show cautionne_frame_noglow:
    zoom 0.5
  with screenoff


  pause 1
  jump dr_danger_1