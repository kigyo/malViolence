label dr_danger_1:
  scene bg tutorial2 with dissolve:
    align (0.5,0.5) zoom 0.8
  pause 1
  "(...Well. {w}That was unnerving.)"
  "(It's hard to tell when he's being serious,{w=0.1} but his hatred for \"STOP freaks\" is clearly no joke.)"
  "Almost like he..."
  show bg tutorial2:
    ease 0.5 xalign 0.4
    ease 0.3 xalign 0.5
    ease 0.3 xalign 0.4
    ease 0.5 xalign 0.5
  pause 2
  "(No.)"
  "(Remember your training. {w}Now's not the time to overthink things.)"
  "(You need to get out of here. {w}Detective work can come later.)"

  show bg tutorial2:
    yalign 0.5 xalign 0.5 zoom 0.8
    ease 2 zoom 1.0 xalign 0.5 yalign 0.5
  pause 2
  scene black with fade
  pause 1
  show bg corridor1 with placeintro:
    zoom 0.8 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0


  pause 1
  "(No side corridors,{w=0.5} no secret doors...{w=0.5} not even a crack in the wall.)"

  pause 1

  show bg corridor1 with dissolve:
    align (0.5,0.5) zoom 0.5


  "(No choice but to move forward.)"
  pause 1

  show bg corridor1:
    align (0.5,0.5) zoom 0.5
    ease 2.7 zoom 0.6

  "(You take another cautious step ahead and-){p=0.3}{nw}"
  #"{b}[the {/b}{b}dr.{/b}{b} danger screens go {/b}{b}on ]{/b}"
  "???" "Welcome.{w=0.5} I see you've arrived safely?"

  show bg corridor1:
    align (0.5,0.5) zoom 0.6

  "(What the-?!)" with small_shake
  "({i}Another {/i}voice? {w}And all the screens in the room lit up, too...)"
  scene bg corridor1:
    zoom 0.6 yalign 0.5 xalign 0.5
    ease 4 zoom 1 xalign 0.0 yalign 0.45

  pause 4

  show drdanger stare at crt
  show crt
  show drdangerframe:
    zoom 0.5
  with dissolve 

  pause 1


  #"{b}[pause as the player goes over to one screen, which has {/b}{b}dr.{/b}{b} danger in the room. {/b}{b}it's{/b}{b} {/b}{b}similar to{/b}{b} {/b}{b}cautionne's{/b}{b} tv screen, but the room is less messy.]{/b}"
  "(Huh?)"
  "(You know that woman on the screen.)"
  "({i}Everyone{/i} at STOP knows that face.)"
  "(They've seen her photos in newspaper articles.{w} Broadcasts.{w} Social media.)"
  "(For years,{w=0.1} this mysterious woman was the scourge of STOP.)"
  "(A saboteur who terrorized the public with bombs and cryptic threats.{w} A supervillain,{w=0.1} through and through.)"
  "(A supervillain by the name of...)"
  drx "From the top,{w=0.1} then. {w=0.5}I am Dr. Danger."
  drs "You are here because you're under my temporary employment."
  "(Uh... {w}no?)"
  "(Last time you checked,{w=0.1} you were a STOP agent.{w} By default, Dr. Danger's a sworn enemy.)"
  "(...{i}Was{/i} a sworn enemy.{w} She died {i}weeks{/i} ago,{w=0.1} caught in her own explosion while trying to wipe another STOP facility off the map.)"
  "(Wait.{w} Does this mean she survi-){p=0.3}{nw}"
  drs "Before you begin your task,{w=0.1} please listen carefully."
  drs "Due to my circumstances,{w=0.1} I cannot repeat my instructions."
  "(...No -{w=0.5} thinking back,{w=0.1} her death was {i}very thoroughly{/i} confirmed.{w} Which means-){p=0.3}{nw}" 
  drs "Nor will I be able to answer any of your questions."
  "(...This is just a recording.{w} A cheesy one,{w=0.1} at that.)" 
  "(Turns out even supervillains make the newbies watch employee training videos.)"
  "(Better tune her out.)"

  scene bg corridor1:
    align(0.5,0.5) zoom 0.5
  hide drdanger
  hide crt
  hide drdangerframe
  with dissolve
  pause 1
  "(Besides,{w=0.1} you're no mere hired hand.)"
  "(You're a proud agent of STOP –{w=0.5} trained to fight villains like her.)"
  "(So what if there are more puzzles to solve and locked rooms to explore? {w}To someone like you,{w=0.1} they should be child's play.)"
  pause 1
  "({i}...Should{/i} be.)"
  scene bg corridor1:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 4 zoom 1.0
  pause 2
  scene black with fade
  pause 1
  show bg room1 with placeintro:
    zoom 0.6 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0

  pause 5

  show bg room1 with dissolve:
    zoom 0.4 yalign 0.7

  pause 1
  #"{b}[the camera mimics the player moving towards the door in the middle of the room. they enter the first puzzle room]{/b}"
  ##"{b}[pause. A sound plays as the doors close behind the player when they enter the room]{/b}"
  "(Huh.{w} Seems like a typical evil lab,{w=0.1} straight out of a comic book.)"

  "(Let's see here... {w}Massive computers,{w=0.5} hi-tech gizmos,{w=0.5} and a \"Primary Source Extractor?\")"
  "({i}...Eugh.{/i} {w}Looking at that thing gives you goosebumps.)"
  "(Do you {i}have{/i} to go through here?)"
  "(Maybe there's something you missed in the corridor...)"
  "(Yeah,{w=0.1} you'll turn around and-)"
  pause 1
  "(-it's not opening.)"
  pause 1
  "(No,{w=0.1} there\'s still the door on the other side."
  show bg room1:
    zoom 0.4 yalign 0.7
    ease 4 zoom 0.8 xalign 0.15 yalign 0.65

  extend "You'll just walk over,{w=0.1} and it'll automatically...){p=1.5}{nw}"
  #"{b}[pause as the camera moves to the door in the middle{/b}{b}]{/b}"
  "(...aaaaaaaaand it's shut too.)"
  "(Great.{w} Off to a {i}fantastic{/i} start already.)"
  pause 1
  "(...Wait.{w} There's something else here.)"

  pause 2
  ### show meta puzzle image
  "(A lock with a strange puzzle. {w}Kinda like the one you found in your cell.)"
  pause 1
  "(...Maybe you\'ll find the answer in this room?)"
show bg room1:
  zoom 0.8 
  ease 5 zoom 0.34 xalign 0.0 yalign 0.0

pause 5
call screen room1 with dissolve