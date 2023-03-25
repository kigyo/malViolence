label dr_danger_1:
  scene bg tutorial2 with dissolve:
    align (0.5,0.5) zoom 0.8
  pause 1
  "(...Well. {w}That was unnerving.)"
  "(It's hard to tell when he's being serious, but his hatred for \"STOP freaks\" is clearly no joke.)"
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
  "(No side corridors, {w=0.5} no secret doors... {w=0.5}not even a crack in the wall.)"

  pause 1

  show bg corridor1 with dissolve:
    align (0.5,0.5) zoom 0.5


  "(No choice but to move forward.)"
  pause 1
  "(You take another cautious step ahead and-){nw}"
  #"{b}[the {/b}{b}dr.{/b}{b} danger screens go {/b}{b}on ]{/b}"
  "???" "Welcome. {w=0.5}I see you've arrived safely?"
  "(What the-?!)" with small_shake
  "({i}Another {/i}voice? {w}And all the screens in the room lit up, too...)"
  scene bg corridor1:
    zoom 0.5 yalign 0.5 xalign 0.5
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
  "(Everyone at STOP knows that face.)"
  "(They've seen her photos in newspaper articles. {w}Broadcasts. {w}Social media.)"
  "(For years, this mysterious woman was the scourge of STOP.)"
  "(A saboteur who terrorized the public with bombs and cryptic threats. {w}A supervillain, through and through.)"
  "(A supervillain by the name of...)"
  xd "From the top, then. {w=1}I am Dr. Danger."
  dr "You are here because you're under my temporary employment."
  "(Uh... {w}no?)"
  "(Last time you checked, you were a STOP agent. {w}By default, Dr. Danger was your sworn enemy.)"
  "(A sworn enemy who was ki-{nw})"
  dr "Before you begin your task, please listen carefully."
  dr "Due to my circumstances, I cannot repeat my instructions. {w=0.5}Nor will I be able to answer any of your questions."
  "(...Oh, should've caught it earlier. {w}This is all pre-recorded.)"
  "(Turns out even supervillains make the newbies watch employee training videos.)"
  "(Better tune her out.)"

  scene bg corridor1:
    align(0.5,0.5) zoom 0.5
  hide drdanger
  hide crt
  hide drdangerframe
  with dissolve
  pause 1
  "(Besides, you're no mere hired hand.)"
  "(You're a proud agent of STOP –{w=0.5} trained to fight villains like her.)"
  "(So what if there are more puzzles to solve and locked rooms to explore? {w}To someone like you, they should be child's play.)"
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
  "(Huh. Seems like a typical evil lab, straight out of a comic book.)"

  "(Let's see here... {w}Massive computers, {w=0.5}hi-tech gizmos, {w=0.5}and a \"Primary Source Extractor?\")"
  "(...Eugh. {w}Looking at that thing gives you goosebumps.)"
  "(Do you {i}have{/i} to go through here?)"
  "(Maybe there's something you missed in the corridor...)"
  "(Yeah, you'll turn around and-)"
  pause 1
  "(-it's not opening.)"
  pause 1
  "(No, there\'s still the door on the other side."
  show bg room1:
    zoom 0.4 yalign 0.7
    ease 4 zoom 0.8 xalign 0.15 yalign 0.65

  extend " You'll just walk over, and it'll automatically..."
  #"{b}[pause as the camera moves to the door in the middle{/b}{b}]{/b}"
  "...aaaaaaaaand it's shut too.)"
  "(Great. {w}Off to a fantastic start already.)"
  pause 1
  "(...Wait. {w}There's something else here.)"

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