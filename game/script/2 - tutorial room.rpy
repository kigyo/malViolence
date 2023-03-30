default tutorial = {"vent":0, "investigated":[], "lock": [0,0,0,0,0,0,0,0]}

screen tutorial_room():
    sensitive not inspect
    layer "master"
    tag room

    fixed at zoomed:
        imagebutton idle Null(700, 280) action [SetVariable("inspect", "desk"), Jump("tutorial_room")] pos (2315, 1370) mouse "inspect"
        imagebutton idle Null(380, 800) action [SetVariable("inspect", "handle"), Jump("tutorial_room")] pos (1750, 680) mouse "inspect":
            if tutorial["vent"] == 2:
                mouse "puzzle"
        imagebutton idle Null(880, 610) action [SetVariable("inspect", "tap"), Jump("tutorial_room")] pos (2960, 1550) mouse "inspect"

        if tutorial["vent"] == 0:
            add "bg tutorial1"
            imagebutton idle Null(340, 560) action [SetVariable("inspect", "painting"), Jump("tutorial_room")] pos (840, 715) mouse "inspect"
        else:
            add "bg tutorial2"
            imagebutton idle Null(540, 348) action [SetVariable("inspect", "vent"), Jump("tutorial_room")] pos (1776, 1629) mouse "inspect"
            imagebutton idle Null(270, 450) action [SetVariable("inspect", "painting"), Jump("tutorial_room")] pos (880, 780) mouse "inspect"
            imagebutton idle Null(192,144) action [SetVariable("inspect", "pellets"), Jump("tutorial_room")] pos (1254, 1782) mouse "inspect"
        imagebutton idle Null() action [SetVariable("inspect", "bed"), Jump("tutorial_room")] pos (561, 1753) mouse "inspect" focus_mask Image("rooms/tutorial_bed_mask.png")

    if config.developer:
        frame:
            textbutton _("Skip Room") action [Jump("post_tutorial")] style "main_menu_button"


init python:
    def tutorial_set_lock(idx):
        store.tutorial["lock"][idx] += 1
        if tutorial["lock"][idx] == 6:
            store.tutorial["lock"][idx] = 0
        if tutorial_valid_solution():
            renpy.jump("post_tutorial")
            
    def tutorial_valid_solution():
        result = False
        for i in range(8):
            if tutorial["lock"][i%8] == 0 and tutorial["lock"][(i+1)%8] == 0 and tutorial["lock"][(i+2)%8] == 4 and tutorial["lock"][(i+3)%8] == 3 and tutorial["lock"][(i+4)%8] == 4 and tutorial["lock"][(i+5)%8] == 3 and tutorial["lock"][(i+6)%8] == 5 and tutorial["lock"][(i+7)%8] == 2:
                return True
        return result

screen tutorial_lock():
    sensitive not inspect
    modal True
    layer "master"
    zorder 5
    tag puzzle

    if config.developer:
        hbox yalign 0.1 xalign 0.5:
            for i in range(8):
                text str(tutorial["lock"][i]) + " "
        frame:
            textbutton _("Skip Puzzle") action [Hide(), Jump("post_tutorial")] style "main_menu_button"
    add "puzzles/tutorial_circle.png" align (0.5,0.5)
    for i in range(8):
        imagebutton idle "puzzles/tutorial_"+ str(tutorial["lock"][i]) +".png" action Function(tutorial_set_lock, i) focus_mask True align (0.5,0.5) at rotated(i*45)
        
    if not inspect:
        textbutton "Return" action [Return()] style "confirm_button" xalign 0.8 yalign 0.5

label tutorial_room:
    if inspect not in tutorial["investigated"]:
        $tutorial["investigated"].append(inspect)
    show screen tutorial_room
    hide screen tutorial_lock
    $renpy.block_rollback()

    if inspect == "painting":
        if tutorial["vent"] == 0:
            "(There's a weird stock photo on the cover,{w=0.1} but otherwise it's your average vent.)"
            "(Cautionne won't be winning any awards for home decor anytime soon.)"
            $ play_sound(creakyvent)
            $ tutorial["vent"] = 1
            with fade
            pause 0.5
            show tutorial_bowl with dissolve:
                yalign 0.2 xalign 0.5
            "(Guess he wasn't kidding about the LabScrip.{w} It's right there,{w=0.1} neatly served in a metal bowl.)"
            pause 1
            "(...)"
            "(To be honest,{w=0.1} you {i}could{/i} use something to fill your empty stomach.{w} You made the smart decision to skip lunch on your way here.)"
            hide tutorial_bowl with dissolve
            $ play_sound(bowlgrab)
            "(You pick up the bowl and shove a fistful of pellets into your mouth.)"
            $ play_sound(pelletchew)
            "(They taste like...)"
            pause 0.5
            "(...Well,{w=0.1} you don't know what you expected.{w} They're grainy,{w=0.1} if nothing else.)"
            "(You try not to think about Cautionne laughing at you from the other side of the screen.)"
            pause 1
            "(...Huh?{w} What's this?)"
            "(There's something at the bottom of the bowl.{w} ...A pattern?)"
            $ play_sound(pelletfall)
            "(To get a better look,{w=0.1} you dump the rest of the pellets on the floor.)"
            #[sound of pellets falling]
            show tutorial_diagram with dissolve:
                zoom 0.3 yalign 0.2 xalign 0.5
            "(It's...{w=0.5} a Venn diagram.{w} One with weird shapes?)"
            "(Wonder if it means anything...)"
            hide tutorial_diagram with dissolve
        else:
            show tutorial_diagram with dissolve:
                zoom 0.3 yalign 0.2 xalign 0.5
            pause
            hide tutorial_diagram with dissolve

    elif inspect == "vent":
        if tutorial["vent"] < 2:
            $ tutorial["vent"] = 2
            "(Again,{w=0.1} it's just your average vent-){p=0.5}{nw}"
            "(-wait.{w} Something's on the back side of that cover.)"
            $ play_sound(creakyvent)
            show tutorial_painting with dissolve:
                zoom 0.3 yalign 0.2 xalign 0.5
            "(Again with those weird shapes! {w}And this time,{w=0.1} they're {i}colorful!{/i})"
            "(Yeah,{w=0.1} they definitely mean something.)"
            "(Maybe...{w=0.5} it's a way out?)"
            hide tutorial_painting with dissolve
        else:
            show tutorial_painting with dissolve:
                zoom 0.3 yalign 0.2 xalign 0.5
            pause
            hide tutorial_painting with dissolve

    elif inspect == "pellets":
        show tutorial_pellets with dissolve:
            yalign 0.2 xalign 0.5
        "(Rat pellets!{w} Now on the floor.)"
        pause 0.5
        "(...To be honest,{w=0.1} you're still pretty hungry.)"
        "(It wouldn't hurt to eat a little more, right?{w} You could see yourself getting used to the crunchy texture.)"
        menu:
            "(Sure!)":
                $renpy.block_rollback()
                $ play_sound(pelletchew)
                "(You scoop up another fistful of pellets and eat them without a second thought.)"
                hide tutorial_pellets with dissolve
                #[crunching sounds]
                pause 1
                "(...Why did you do that?)"
                "(Those pellets still don't taste great.)"
                "(In fact,{w=0.1} the more you chew on them,{w=0.1} the bitterer they-){p=0.5}{nw}"
                $ play_sound(bodyfall)
                scene bg tutorial2 with small_shake:
                    parallel:
                        zoom 0.5 xalign 0.5 yalign 0.5
                        linear 0.1 yalign 1.0 xalign 0.5 zoom 0.75


                scene bg tutorial2 at dizzy with dissolve:
                    parallel:
                        yalign 1.0 xalign 0.5 zoom 0.75
                "{sc}({i}-HURK!{/i}){/sc}"
                "{si}(...Aw,{w=0.1} crap.){/si}"
                "{si}(Of {i}course{/i} there was something in the food.){/si}"
                "{si}(Whatever it was...{w=0.5} it's making everything throb like crazy.{/si} {si}{w}{p}Your chest,{w=0.5} your head,{w=0.5} your eyes...){/si}"
                "{si}(But your throat's clammed up.{w} You can't scream,{w=0.1} or cry,{w=0.1} or moan.){/si}"
                "{si}(And breathing's getting harder and harder...){/si}"
                "{si}(And soon...{/si}"
                scene black with eyeclose
                pause 1
                extend " your vision goes black.)"
                nvl clear
                pause 3
                $nvl_heading = "Lab Report #310"
                l "Subject expired shortly after ingesting higher than recommended daily serving of cyanide-laced rodent feed."           
                l "{b}Contributing Factors to Death:{/b} Their stomach was bigger than their brain, evidently. \n{w}May need to re-evaluate STOP agents' dietary preferences."
                $deadend(achievement_dead1)
                le "DEAD END 01: Cheers! It's Cyanide."
                nvl hide
                pause 2
                nvl clear
                $game_over("tutorial")
                return
            "(Nah.)":
                "(Nah,{w=0.1} you're good.)"
                hide tutorial_pellets with dissolve
                "(Actually,{w=0.1} you get drowsy when you eat too much.)"
                "(You hate to admit it,{w=0.1} but in the situation you're in,{w=0.1} it's probably better to be alert and hungry.)"

    elif inspect == "desk":
        "(It's a desk.{w} For desk things.)"
        "(What an evocative desk-ription!)"

    elif inspect == "bed":
        $ play_sound(bedsitup)
        "(It's a bed!)"
        "(You're surprised you slept at all on something that lumpy.)"
        "(...Yeah, right.{w} Back at home,{w=0.1} you {i}worshipped{/i} your crappy mattress.)"

    elif inspect == "tap":
        "(Your throat's dry and sore,{w=0.1} but you can't find a cup anywhere.)"
        "(Does he expect you to drink out of the faucet?)"
        $ play_sound(creakyfaucet)
        pause 1
        "(...Great.{w} It doesn't even work.)"
        "(So much for quenching your thirst.{w} Asshole.)"

    elif inspect == "handle":
        if tutorial["vent"] == 0:
            "(A door handle.)"
            show screen tutorial_lock with dissolve
            "(But what's with the lock?{w} You've never seen anything like it.)"
        elif tutorial["vent"] == 2:
            $ tutorial["vent"] = 3
            show screen tutorial_lock with dissolve
            "(Oh,{w=0.1} {i}this{/i} is your ticket out of here.)"
            "(The wheel's just like the wheels on the vent cover!)"
            "(With a little time and effort...{w} you think you can crack it.)"
            $ inspect = None
            call screen tutorial_lock
        elif tutorial["vent"] == 3:
            $ inspect = None
            call screen tutorial_lock
        else:
            "(A door handle.)"
            show screen tutorial_lock with dissolve
            "(For some reason,{w=0.1} you want to look around the room again...)"
        hide screen tutorial_lock with dissolve

    $ inspect = None
    $renpy.block_rollback()
    call screen tutorial_room