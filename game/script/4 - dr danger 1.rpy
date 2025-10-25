label dr_danger_1:
  scene bg tutorial2 with dissolve:
    align (0.5,0.5) zoom 0.8
  pause 1
  "(...Well. {w}That was unnerving.)"
  "(It's hard to tell when he's being serious,{w=0.1} but his hatred for \"STOP freaks\" is clearly no joke.)"
  "Almost like he..."
  show bg tutorial2:
    ease 0.5 xalign 0.4
    ease 0.5 xalign 0.6
    ease 0.5 xalign 0.45
    ease 0.5 xalign 0.55
    ease 0.5 xalign 0.5
  pause 3
  "(No.)"
  "(Remember your training. {w}Now's not the time to overthink things.)"
  "(You need to get out of here. {w}Detective work can come later.)"

  $ play_sound(footsteps1)

  show bg tutorial2:
    yalign 0.5 xalign 0.5 zoom 0.8
    ease 2 zoom 1.0 xalign 0.5 yalign 0.5
  pause 2
  $ play_sound(dooropen)
  scene black with fade
  pause 2
  show bg corridor1 tvoff with placeintro:
    zoom 0.8 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0
  $ Achievement.add(achievement_tfng)
  $ achievement.grant("tfng")

  $ play_sound(doorclose)
  pause 2
  "(No side corridors,{w=0.5} no secret doors...{w=0.5} not even a crack in the wall.)"

  pause 1

  show bg corridor1 tvoff with dissolve:
    align (0.5,0.5) zoom 0.5


  "(No choice but to move forward.)"
  pause 1


  show bg corridor1 tvoff:
    align (0.5,0.5) zoom 0.5
    ease 2.7 zoom 0.6

  $ play_sound(singlefootstep)


  "(You take another cautious step ahead and—){w=1}{nw}"
  $ play_sound(staticshort)
  show bg corridor1
  pause 0.5
  voice "audio/voice/dr.danger/Danger_Corridor1-01.ogg"
  #"{b}[the {/b}{b}dr.{/b}{b} danger screens go {/b}{b}on ]{/b}"
  "???" "Welcome.{w=0.52} I see you've arrived safely?"

  show bg corridor1:
    align (0.5,0.5) zoom 0.6

  "(What the—?!)" with small_shake
  "({i}Another {/i}voice? {w}And all the screens in the room lit up, too...)"

  $ play_sound(footsteps1)
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
  "(A saboteur who terrorized the public with bombs and cryptic threats.)"
  "(A supervillain,{w=0.1} through and through.)"
  "(A supervillain by the name of...)"
  voice "audio/voice/dr.danger/Danger_Corridor1-02.ogg"
  drx "From the top,{w=0.622} then. {w=1}I am Dr. Danger."
  voice "audio/voice/dr.danger/Danger_Corridor1-03.ogg"
  drs "You are here because you're under my temporary employment."
  "(Uh... {w}no?)"
  "(Last time you checked,{w=0.1} you were a STOP agent.{w} By default, Dr. Danger's a sworn enemy.)"
  "(...{i}Was{/i} a sworn enemy.{w} She died {i}weeks{/i} ago,{w=0.1} caught in her own explosion while trying to wipe another STOP facility off the map.)"
  "(Wait.{w} Does this mean she survi—){w=1}{nw}"
  voice "audio/voice/dr.danger/Danger_Corridor1-04.ogg"
  drs "Before you begin your task,{w=0.14} please listen carefully.{w=1.75}{nw}"
  voice sustain
  drs "Due to my circumstances, I cannot repeat my instructions.{w=2}{nw}"
  voice sustain
  drs "Nor will I be able to answer any of your questions."
  "(...No.{w} Her death was {i}very thoroughly{/i} confirmed.{w} Which means...)" 
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
  "(You're a proud agent of STOP —{w=0.5} trained to fight villains like her.)"
  "(So what if there are more puzzles to solve and locked rooms to explore? {w}To someone like you,{w=0.1} they should be child's play.)"
  pause 1
  "({i}...Should{/i} be.)"
  $ play_sound(footsteps1)
  scene bg corridor1:
    xalign 0.5 yalign 0.5 zoom 0.5
    ease 4 zoom 1.0
  pause 2
  scene black with fade
  $ play_sound(creakyvent)
  pause 3
  show bg room1 with placeintro:
    zoom 0.6 xalign 0.0 yalign 0.5
    linear 20 xalign 1.0

  pause 5

  show bg room1 with dissolve:
    zoom 0.4 yalign 0.7

  $ play_sound(metaldoorclose)
  pause 1
######### metal door shut plays here

  "(Huh.{w} Seems like a typical evil lab,{w=0.1} straight out of a comic book.)"

  "(Let's see here... {w}Massive computers,{w=0.5} hi-tech gizmos,{w=0.5} and a...{w=0.5} \"Primary Source Extractor?\")"
  "({i}...Eugh.{/i} {w}Looking at that thing gives you goosebumps.)"
  "(Do you {i}have{/i} to go through here?)"
  "(Maybe there's something you missed in the corridor...)"
  "(Yeah,{w=0.1} you'll turn around and—){w=1}{nw}"
  $ play_sound(metaldoorlock)
  pause 2
  "(—it's not opening.)"
  pause 1
  "(No,{w=0.1} there\'s still the door on the other side."

  show bg room1:
    zoom 0.4 yalign 0.7
    ease 4 zoom 0.8 xalign 0.15 yalign 0.65

  $ play_sound(footsteps4)

  "(You'll just walk over,{w=0.1} and it'll automatically-{w=2}{nw}"


  #"{b}[pause as the camera moves to the door in the middle{/b}{b}]{/b}"
  extend "...aaaaaaaaand it's shut too.)"
  "(Great.{w} Off to a {i}fantastic{/i} start already.)"
  pause 1
  "(...Wait.{w} There's something else here.)"

  ####quickly defining a transition bg for this scene. this is where the tutorial room has the vent open but no pellets on the floor
  layeredimage marblemeta:
    always "images/puzzles/room_1_meta/base_marble_maze.png"
    always "images/puzzles/room_1_meta/marble_maze_effigy_1.png"
    always "images/puzzles/room_1_meta/marble_maze_effigy_2.png"
    always "images/puzzles/room_1_meta/marble_maze_effigy_3.png"

  show marblemeta with dissolve:
    xpos 200 yoffset -100

  pause 2
  ### show meta puzzle image
  "(A lock with a strange puzzle. {w}Kinda like the one you found in your cell.)"

  hide marblemeta with dissolve
  pause 1
  "(...Maybe you\'ll find the answer in this room?)"
  show bg room1:
    zoom 0.8 
    ease 5 zoom 0.335 xalign 0.0 yalign 0.0

  pause 5
  $ inspect = None
  $ play_music(room1theme, fadein=1.0, fadeout=0.1)
  call screen room1 with dissolve
