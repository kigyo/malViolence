label dr_danger_1:
  scene bg tutorial2 with dissolve:
    align (0.5,0.5) zoom 0.8
  "(...Well. That was unnerving.)"
  "(It's hard to tell when he's being serious, but his hatred for \"STOP freaks\" is clearly no joke.)"
  "Almost like he..."
  show bg tutorial2:
    ease 0.3 xalign 0.3
    ease 0.3 xalign 0.7
    ease 0.3 xalign 0.3
    ease 0.15 xalign 0.5
  "(No. Remember your training. Now's not the time to overthink things.)"
  "(You need to get out of here. Detective work can come later.)"
  scene bg corridor1 at bg with wipeleft
  "(No side corridors, no secret doors... not even a crack in the wall.)"
  "(No choice but to move forward.)"
  "(You take another cautious step ahead and-)"
  #"{b}[the {/b}{b}dr.{/b}{b} danger screens go {/b}{b}on ]{/b}"
  "???" "Welcome. I see you've arrived safely?"
  "(What the-?!)" with small_shake
  "({i}Another {/i}voice? And all the screens in the room lit up, too...)"
  scene bg corridor1:
    zoom 0.5 yalign 0.5 xalign 0.5
    ease 4 zoom 1 xalign 0.0 yalign 0.45
  #"{b}[pause as the player goes over to one screen, which has {/b}{b}dr.{/b}{b} danger in the room. {/b}{b}it's{/b}{b} {/b}{b}similar to{/b}{b} {/b}{b}cautionne's{/b}{b} tv screen, but the room is less messy.]{/b}"
  "(Huh?)"
  "(You know that woman on the screen.)"
  "(Everyone at STOP knows that face. They've seen her photos in newspaper articles. Broadcasts. Social media.)"
  "(For years, this mysterious woman was the scourge of STOP. A saboteur who terrorized the public with bombs and cryptic threats. A supervillain, through and through.)"
  "(A supervillain by the name of...)"
  "???" "From the top, then. I am Dr. Danger."
  dr "You are here because you're under my temporary employment."
  "(Uh... no?)"
  "(Last time you checked, you were a STOP agent. By default, Dr. Danger was your sworn enemy.)"
  "(A sworn enemy who was ki-)"
  dr "Before you begin your task, please listen carefully. Due to my circumstances, I cannot repeat my instructions. Nor will I be able to answer any of your questions."
  "(...Oh, should've caught it earlier. This is all pre-recorded.)"
  "(Turns out even supervillains make the newbies watch employee training videos.)"
  "(Better tune her out. Besides, you're no mere hired hand.)"
  "(You're a proud agent of STOP – trained to fight villains like her.)"
  "(So what if there are more puzzles to solve and locked rooms to explore? To someone like you, they should be child's play.)"
  scene bg corridor1:
    zoom 1 xalign 0.0 yalign 0.45
    ease 1 zoom 0.5 yalign 0.5 xalign 0.5
  pause 1
  "({i}...Should{/i} be.)"
  scene bg corridor1:
    xalign 0.5 yalign 0.5 zoom 0.5
    linear 0.45 yalign 0.35 zoom 0.6
    ease 0.3 yalign 0.5 zoom 0.65
    linear 0.45 yalign 0.38 zoom 0.7
    ease 0.3 yalign 0.5 zoom 0.75
    linear 0.45 yalign 0.4 zoom 0.8
    ease 0.3 yalign 0.5 zoom 0.85
  pause 5
  #"{b}[the camera mimics the player moving towards the door in the middle of the room. they enter the first puzzle room]{/b}"
  scene bg room1 at bg with wipeleft
  ##"{b}[pause. A sound plays as the doors close behind the player when they enter the room]{/b}"
  "(Huh. Seems like a typical evil lab, straight out of a comic book.)"
  "(Let's see here... Massive computers, hi-tech gizmos, and a \"Primary Source Extractor?\")"
  "(...Eugh. Looking at that thing gives you goosebumps. Do you {i}have {/i}to go through here?)"
  "(Maybe there's something you missed in the corridor... Yeah, you'll turn around and-)"
  pause 1
  "(-it's not opening.)"
  "(No, there\'s still the door on the other side. You'll just walk over, and it'll automatically-)"
  #"{b}[pause as the camera moves to the door in the middle{/b}{b}]{/b}"
  "(...aaaaaaaaand it's shut too.)"
  "(Great. Off to a fantastic start already.)"
  pause 1
  "(...Wait. There's something else here.)"
  "(A lock with a strange puzzle. Kinda like the one you found in your cell.)"
  "(...Maybe you\'ll find the answer in this room?)"
  jump post_room_1