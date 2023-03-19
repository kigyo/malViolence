default tutorial = {"vent":0, }

screen tutorial_room():
    sensitive not inspect
    layer "master"
    viewport:
        xinitial roomval[0] yinitial roomval[1] xadjustment roomadjustmentx yadjustment roomadjustmenty
        child_size (3840, 2160) arrowkeys True #edgescroll (300, 700)
        imagebutton idle Null(1410, 395) action [SetVariable("inspect", "bed"), Jump("tutorial_room")] pos (560, 1760)
        imagebutton idle Null(700, 280) action [SetVariable("inspect", "desk"), Jump("tutorial_room")] pos (2315, 1370)
        imagebutton idle Null(380, 800) action [SetVariable("inspect", "handle"), Jump("tutorial_room")] pos (1750, 680)
        imagebutton idle Null(880, 610) action [SetVariable("inspect", "tap"), Jump("tutorial_room")] align (1.0, 1.0)
        if tutorial["vent"] == 0:
            add "bg tutorial1"
            imagebutton idle Null(340, 560) action [SetVariable("inspect", "painting"), Jump("tutorial_room")] pos (840, 715)
        else:
            add "bg tutorial2"
            imagebutton idle Null(270, 450) action [SetVariable("inspect", "bowl"), Jump("tutorial_room")] pos (880, 780)
            imagebutton idle Null(730, 225) action [SetVariable("inspect", "vent"), Jump("tutorial_room")] pos (1075, 1715)
    use arrow_controls

label tutorial_room:
    show screen tutorial_room
    if inspect == "painting":
        "(There's a weird stock photo on the cover, but otherwise it's your average vent. Cautionne won't be winning any awards for home decor anytime soon.)"
        $ tutorial["vent"] = 1
        #[the vent opens with a creak]
        "(Guess he wasn't kidding about the LabScrip. It's right there, neatly served in a metal bowl.)"
        pause 1
        "(...)"
        "(To be honest, you could use something to fill your empty stomach. You made the smart decision to skip lunch on your way here.)"
        "(You pick up the bowl and shove a fistful of pellets into your mouth. They taste like...)"
        "(...well, you don't know what you expected. They're grainy, if nothing else.)"
        "(You try not to think about Cautionne laughing at you from the other side of the screen.)"
        pause 1
        "(...Huh? What's this?)"
        "(There's something at the bottom of the bowl. Something colorful.)"
        "(To get a better look, you dump the rest of the pellets on the floor.)"
        #[sound of pellets falling]
        show tutorial_bowl with dissolve:
            yalign 0.2 xalign 0.5
        pause 1
        "(It's... a Venn diagram. One with weird shapes?)"
        "(Wonder if it means anything...)"
        hide tutorial_bowl with dissolve
    elif inspect == "bowl":
        show tutorial_bowl with dissolve:
            yalign 0.5 xalign 0.5
        pause
        hide tutorial_bowl with dissolve
    elif inspect == "vent":
        if tutorial["vent"] < 2:
            $ tutorial["vent"] = 2
            "(Again, it's just your average vent-)"
            "(-wait. Something's on the back side of that cover.)"
            show tutorial_painting with dissolve:
                yalign 0.2 xalign 0.5
            pause 1
            "(Again with those weird shapes!)"
            "(Yeah, they definitely mean something.)"
            "(Maybe... it's a way out?)"
            hide tutorial_painting with dissolve
        else:
            show tutorial_painting with dissolve:
                yalign 0.5 xalign 0.5
            pause
            hide tutorial_painting with dissolve
    elif inspect == "pellets":
        "(Rat pellets! Now on the floor.)"
        "(...To be honest, you're still pretty hungry.)"
        "(It wouldn't hurt to eat a little more, right? You could see yourself getting used to the crunchy texture.)"
        menu:
            "(Sure!)":
                "(You scoop up another fistful of pellets and eat it without a second thought.)"
                #[crunching sounds]
                "(...Why did you do that?)"
                "(Those pellets still don't taste great.)"
                "(In fact, the more you chew on them, the bitterer they- )"
                "(-HURK!)"
                #[screen shakes and camera moves down to the floor] 
                pause 1
                "(...Aw, crap.)"
                #[screen begins to distort]
                "(Of course there was something in the food.)"
                "(Whatever it was... it's making everything throb like crazy. Your chest, your head, your eyes...)"
                "(But your throat's clammed up. You can't scream, or cry, or moan. And breathing's getting harder and harder...)"
                "(Soon..."
                #[screen cuts black]
                extend " your vision goes black.)"
                "Lab Report 310: Subject expired shortly after ingesting higher than recommended daily serving of cyanide-laced rodent feed."           
                "Contributing factors to death: Their stomach was bigger than their brain, evidently. May need to re-avaluate STOP agents' dietary preferences."
                #[DEAD END 01: Cheers! It's Cyanide.]
            "(Nah.)":
                "(Nah, you're good.)"
                "(Actually, you get drowsy when you eat too much.)"
                "(You hate to admit it, but in the situation you're in, it's probably better to be alert and hungry.)"
    elif inspect == "desk":
        "(It's a desk. For desk things.)"
        "(What an evocative desk-ription!)"
    elif inspect == "bed":
        "(It's a bed!)"
        "(You're surprised you slept at all on something that lumpy.)"
        "(...Yeah, right. Back at home, you worshipped your crappy mattress.)"
    elif inspect == "tap":
        "(Your throat's dry and sore, but you can't find a cup anywhere.)"
        "(Does he expect you to drink out of the faucet?)"
        #[sound of dry squeaking]
        "(...Great. It doesn't even work.)"
        "(So much for quenching my thirst. Asshole.)"
    elif inspect == "handle":
        if tutorial["vent"] == 0:
            "(A door handle.)"
            show tutorial_lock with dissolve:
                yalign 0.2 xalign 0.5
            "(But what's with the lock? You've never seen anything like it.)"
        elif tutorial["vent"] == 2:
            show tutorial_lock with dissolve:
                yalign 0.2 xalign 0.5
            "(Oh, this is your ticket out of here.)"
            "(The wheel's just like the wheels on the vent cover!)"
            "(With a little time and effort... you think you can crack it.)"
            #TODO: Puzzle
            #[If puzzle is solved, play a solving/unlocking sound and then go to the post-tutorial cautionne scene]
        else:
            "(A door handle.)"
            show tutorial_lock with dissolve:
                yalign 0.2 xalign 0.5
            "(For some reason, you want to look around the room again...)"
        hide tutorial_lock with dissolve
    $ inspect = None
    call screen tutorial_room